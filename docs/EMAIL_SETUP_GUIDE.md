# 🚀 EMAIL LINK SETUP - Multi-Device Access

## 📋 What's New?

The email system now **automatically detects** and includes the **ngrok public URL** in emails. This means:
- ✅ Recipients can access from **any device, anywhere**
- ✅ Works on **different networks** and **different countries**
- ✅ All access automatically **logged with IP & device info**
- ✅ **No manual URL copying** needed

---

## ⚡ Quick Start (5 Minutes)

### Step 1: Prepare Recipients List
Edit `receivers.txt` - add email addresses (one per line):
```
friend@gmail.com
random.user@yahoo.com
another.person@example.com
```

### Step 2: Download ngrok (One-time)
1. Go to: https://ngrok.com/download
2. Download for Windows
3. Extract `ngrok.exe` 
4. Place in `d:\Hackathon\socialeng_simulator\`

### Step 3: Run Email Blast
Double-click: `send_email_blast.bat`

The script will:
- ✅ Start Flask app
- ✅ Start ngrok tunnel
- ✅ Get the public URL automatically
- ✅ Send emails with the link
- ✅ Show live event logs

**That's it!** Recipients will receive emails with a clickable link.

---

## 🔍 What Each Script Does

### `share_with_ngrok.bat`
- Starts Flask + ngrok
- Shows you the public URL manually
- Useful for testing or sharing URL with friends

### `send_email_blast.bat` (NEW!)
- Starts Flask + ngrok
- Automatically gets public URL
- Sends emails to all addresses in `receivers.txt`
- Emails include the **live public URL**
- Recipients click → get logged

---

## 📊 How It Works Behind the Scenes

### Without Email (Manual):
```
You:     Run share_with_ngrok.bat
You:     Get URL: https://abc123.ngrok-free.dev
You:     Copy & send manually to friends
Friend:  Receives URL
Friend:  Clicks link → Logged
```

### With Email (Automated):
```
You:     Create receivers.txt
You:     Run send_email_blast.bat
Script:  Starts Flask + ngrok
Script:  Queries ngrok API for public URL
Script:  Sends emails with URL included
Friend:  Receives email with "Verify Account" button
Friend:  Clicks button → Logged (any device/location)
```

---

## 🔐 How the URL is Retrieved

The `mail_sender.py` script queries the **ngrok local API** (`http://127.0.0.1:4040/api/tunnels`) to get the public URL in real-time.

**Why this works:**
- ngrok always runs on `localhost:4040`
- The local API provides current tunnel information
- We extract the HTTPS URL and include it in emails

---

## 📱 What Recipients See

**Email Subject:**
```
Instagram Account Verification Required
```

**Email Body:**
```
We detected unusual activity in your account.
Please verify your account immediately to avoid restrictions.

[Verify Account Button] ← Links to ngrok public URL
```

---

## 📊 Data Logged

When recipient clicks the link:
```
====== LOGIN EVENT ======
Time       : 2026-05-01 14:23:45.123456
Action     : Email Link Clicked
IP Address : 203.45.67.89           ← Their real public IP
Device     : Chrome / Windows 10      ← Browser/OS from their device
Username   : 
Password   : 
Status     : 
=========================
```

---

## ✅ Requirements

### Already Installed:
- Flask 2.3.0
- Werkzeug 2.3.0
- user-agents 2.2.0

### Newly Added:
- **requests** 2.31.0 (for querying ngrok API)

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Troubleshooting

### Problem: "ngrok.exe not found"
**Solution:** Download ngrok from https://ngrok.com/download and extract to project folder

### Problem: "Error getting ngrok URL"
**Cause:** ngrok not running or still initializing
**Solution:** Wait a few seconds, ngrok needs time to create tunnel

### Problem: "Failed to send email"
**Causes:**
- Gmail account doesn't have app password
- Email/password incorrect in mail_sender.py
- Gmail security blocking the access
**Solution:** 
- Use Gmail app password (if 2FA enabled)
- Allow less secure apps in Gmail settings
- Check email/password in mail_sender.py line 16-17

### Problem: Emails not received
**Solution:** Check spam folder, recipients might be blocking

---

## 🔄 Full Example Workflow

```
1. Create receivers.txt:
   alice@example.com
   bob@example.com

2. Download ngrok.exe (if not done)

3. Double-click: send_email_blast.bat
   - Opens Flask window
   - Opens ngrok window
   - Sends emails automatically

4. Check login_events.txt as recipients click link

5. Keep running to receive more clicks

6. View complete logs in login_events.txt
```

---

## 📝 File Locations

- Main app: `app.py`
- Email sender: `mail_sender.py`
- Recipients list: `receivers.txt`
- Email script: `send_email_blast.bat`
- Event logs: `login_events.txt`
- Manual ngrok script: `share_with_ngrok.bat`

---

## ⚙️ Advanced: Manual Setup

If you prefer manual control:

**Terminal 1 - Start Flask:**
```bash
python app.py
```

**Terminal 2 - Start ngrok:**
```bash
ngrok http 5000
```

**Terminal 3 - Send emails:**
```bash
python mail_sender.py
```

---

## 🎯 Next Steps

1. ✅ Add emails to `receivers.txt`
2. ✅ Download ngrok
3. ✅ Run `send_email_blast.bat`
4. ✅ Monitor `login_events.txt` for activity
5. ✅ Track who clicks, from where, on what device
