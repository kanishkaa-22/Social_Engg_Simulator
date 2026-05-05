# Quick Start Guide - Social Engineering Simulator

## Windows Users (Easiest Method)

### Step 1: Double-click run.bat
Navigate to `d:\socialeng_simulator\socialeng_simulator\` and double-click `run.bat`

The batch script will:
- Check if Python is installed
- Install Flask if needed
- Start the application automatically

### Step 2: Open Browser
Once you see "Starting Application..." message, open your browser:
- http://127.0.0.1:5000/

### Step 3: Test Login
Use any of these credentials:
- Username: `po` → Password: `po`
- Username: `asd` → Password: `asd`
- Username: `asdf` → Password: `asdf`
- Username: `qwdf` → Password: `qwef`
- Username: `sesha` → Password: `sesha`

### Step 4: Check Login Events
After each login attempt, view the log:
- Open `login_events.txt` to see all recorded events

---

## Manual Method (Windows Command Prompt)

```bash
# Navigate to the app directory
cd d:\socialeng_simulator\socialeng_simulator

# Install dependencies (if not already installed)
pip install -r requirements.txt

# Start the application
python app.py
```

Then open http://127.0.0.1:5000/ in your browser.

---

## What Happens When You Login?

1. **You enter username & password** → fills the form
2. **You click Login button** → form submitted to backend
3. **Backend receives data** → validates against users.txt
4. **Event is logged** → recorded in login_events.txt
5. **Response shown** → success dashboard or error message

### Login Events Are Logged Including:
✅ Successful login attempts
✅ Failed login attempts (wrong password)
✅ Invalid usernames
✅ Exact timestamp
✅ Username and password entered

---

## View Login Events

### Option 1: Open the File
Navigate to `login_events.txt` and open with any text editor

### Option 2: Command Line (Windows PowerShell)
```powershell
# View all events
Get-Content login_events.txt

# Watch events in real-time (Ctrl+C to stop)
Get-Content -Path login_events.txt -Wait
```

---

## Stopping the Application

Press `Ctrl + C` in the command prompt/PowerShell where the app is running.

---

## Application Map

```
HOME PAGE (/)
    ↓
[Go to Login] link
    ↓
LOGIN PAGE (/login)
    ├→ Enter username & password
    ├→ Click Login
    ├→ [EVENT LOGGED TO login_events.txt] ← Backend stores event here
    ↓
    ├→ If credentials correct → DASHBOARD (/dashboard) ✓
    └→ If credentials wrong → LOGIN PAGE (show error) ✗
```

---

## File Purposes

| File | Purpose |
|------|---------|
| app.py | Flask backend that handles login and logging |
| login.html | Login form UI |
| index.html | Home page |
| users.txt | List of valid usernames & passwords |
| login_events.txt | **Log file - stores all login events** |
| requirements.txt | Python dependencies |
| run.bat | Quick start script for Windows |
| README.md | Full documentation |

---

## Troubleshooting

**Q: Port 5000 already in use?**
- Another instance is running. Stop it or restart your computer.

**Q: Flask not found?**
- Run: `pip install flask`

**Q: Can't see login_events.txt?**
- It's created after the first login attempt. Try logging in first.

**Q: Need to monitor events live?**
- Use: `Get-Content -Path login_events.txt -Wait` (PowerShell)

---

**Ready to run? Double-click `run.bat` and start testing!** 🚀
