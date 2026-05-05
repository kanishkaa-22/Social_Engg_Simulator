# 📱 Social Engineering Simulator (Instagram Phishing Awareness System)

## � Deployment Status

[![Railway Deployment](https://img.shields.io/badge/Railway-Online-brightgreen?style=flat-square&logo=railway)](https://social-engg-simulator-production.up.railway.app)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Active-blue?style=flat-square&logo=github)](https://github.com/kanishkaa-22/Social_Engg_Simulator)
[![Flask Application](https://img.shields.io/badge/Flask-Running-red?style=flat-square&logo=flask)](https://social-engg-simulator-production.up.railway.app)
[![GitHub Actions](https://github.com/kanishkaa-22/Social_Engg_Simulator/actions/workflows/deploy.yml/badge.svg)](https://github.com/kanishkaa-22/Social_Engg_Simulator/actions)

**Live Application:** 🔗 https://social-engg-simulator-production.up.railway.app

**GitHub Actions CI/CD:** ✅ Automatic deployment enabled on push to main

---

## �📌 Overview
This project is a Flask-based social engineering simulator that demonstrates phishing attacks using a realistic Instagram-like interface.

It simulates real-world attack scenarios where users receive a phishing email, interact with a fake login page, and their actions are recorded for awareness and analysis.

---

## 🎯 Objectives
- Simulate real-world phishing attacks
- Provide a realistic Instagram verification experience
- Capture and analyze user behavior
- Improve phishing awareness
- Promote safe social media practices

---

## ⚙️ Features
- Instagram-like verification/login page  
- Phishing email simulation with clickable button  
- User interaction tracking (clicks + login attempts)  
- IP address and device detection  
- Event logging to login_events.txt  
- Dashboard after login  
- Ngrok public access support  

---

## 🏗️ Project Structure
socialeng_simulator/
│
├── app.py                 # Main Flask application  
├── mail_sender.py         # Email sending script  
├── receivers.txt          # List of email receivers  
├── login_events.txt       # Event log (auto-created)  
├── README.md              # Project documentation  
│
├── templates/  
│   ├── index.html         # Home page  
│   ├── login.html         # Instagram-like login page  
│   ├── dashboard.html     # Success page  
│   ├── details.html       # Project info page  
│   └── awareness.html     # Awareness page  
│
└── static/  
    └── images/            # Images used in UI  

---

## 🚀 SYSTEM WORKFLOW

Step 1: Start Flask Server  
python app.py  

Step 2: Start ngrok (Public Access)  
ngrok http 5000  

Copy the HTTPS link generated (example):  
https://abcd1234.ngrok-free.app  

Step 3: Update Email Link  
Edit in mail_sender.py:  
LOCAL_URL = "https://abcd1234.ngrok-free.app/"  

Step 4: Send Emails  
python mail_sender.py  

---

## 🔄 EXECUTION FLOW

1. User receives phishing email  
2. Clicks "Verify Account" button  
3. Redirected to Flask application (index page)  
4. Navigates to login page  
5. Enters credentials and clicks verify  
6. System logs:  
   - Username & password  
   - IP address  
   - Device information  
   - Timestamp  
7. User is redirected to dashboard or awareness page  

---

## 🌐 CLOUD DEPLOYMENT (Production)

### Railway.app Deployment
- **Status:** 🟢 Online and Running
- **Platform:** Railway.app (Production Environment)
- **Live URL:** https://social-engg-simulator-production.up.railway.app
- **Build Command:** gunicorn app:app
- **Auto-Deploy:** Enabled on GitHub push

### GitHub Actions CI/CD Pipeline
- **Workflow File:** `.github/workflows/deploy.yml`
- **Trigger:** Automatic on push to `main` branch
- **Action:** Deploys to Railway production environment
- **Status:** ✅ Active and Monitoring
- **View Actions:** https://github.com/kanishkaa-22/Social_Engg_Simulator/actions

### GitHub Integration
- **Repository:** https://github.com/kanishkaa-22/Social_Engg_Simulator
- **Main Branch:** main (Production-ready)
- **Default Branch:** main
- **Auto-Deploy:** Yes (via GitHub Actions)
- **Latest Commit:** Synced to Railway

### Access Methods
| Method | URL |
|--------|-----|
| **Production (Railway)** | https://social-engg-simulator-production.up.railway.app |
| **Local Development** | http://127.0.0.1:5000 |
| **Network Access** | http://192.168.x.x:5000 |
| **Public Tunnel (ngrok)** | https://xxxx-xxxx-xxxx.ngrok-free.app |

### Deployment Flow
```
Push to main → GitHub Actions Triggered → Railway Deployment → Live Production
```

---

## 📊 LOGIN EVENT TRACKING

File: login_events.txt  

Sample Output:
====== LOGIN EVENT ======  
Time       : 2026-05-02 10:30:22  
Action     : Verification Form Submitted  
IP Address : 192.168.1.5  
Device     : Chrome / Windows  
Username   : kani  
Password   : 1234  
Status     : Verification Successful  
=========================  

---

## 📧 EMAIL SYSTEM

- Sends phishing simulation emails  
- Includes HTML "Verify Account" button  
- Redirects user to Flask app using ngrok link  

---

## 🔐 Requirements

Install dependencies:  
pip install flask user-agents requests  

---

## 🧪 Testing

Same Device:  
http://127.0.0.1:5000  

Different Device:  
Use ngrok HTTPS link  

---

## ⚠️ Important Notes

- This project is for educational and awareness purposes only  
- Do not use without proper authorization  
- Credentials are logged in plaintext (simulation purpose only)  

---

## 🎯 Key Benefits
- Real-world phishing simulation  
- Realistic Instagram interface  
- User behavior tracking  
- Awareness generation  
- Practical cybersecurity learning  

---

## 🚀 Future Enhancements
- Risk scoring system  
- Multiple phishing scenarios  
- Admin analytics dashboard  
- Real-time monitoring  
- Email click tracking  

---

## 👨‍💻 Author
Developed as part of a cybersecurity awareness project  

---

## 📌 Version
1.0 – Fully Functional Simulation System