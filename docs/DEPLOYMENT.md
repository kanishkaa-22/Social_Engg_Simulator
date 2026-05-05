# 🚀 GitHub Actions Deployment Guide

## Overview
This project uses **GitHub Actions** for continuous integration and automatic deployment to Railway in production.

---

## ✅ Prerequisites

### 1. Railway Account & Token
- Go to [Railway.app](https://railway.app)
- Create an account or login
- Generate an API token from Railway dashboard
- Copy the token (RAILWAY_TOKEN)

### 2. GitHub Repository Secrets
Add the following secret to GitHub:
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add secret:
   - **Name:** `RAILWAY_TOKEN`
   - **Value:** (paste your Railway API token)

---

## 📁 GitHub Actions Setup

### Workflow File Location
```
.github/workflows/deploy.yml
```

### Current Configuration
```yaml
on:
  push:
    branches:
      - main
  workflow_dispatch:
```

**Triggers deployment when:**
- Code is pushed to `main` branch (automatic)
- Manual trigger via "Run workflow" button (manual)

---

## 🔄 Deployment Process

### Step 1: Push Code to GitHub
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

### Step 2: GitHub Actions Automatically:
1. ✅ Checks out code
2. ✅ Runs deploy job
3. ✅ Connects to Railway using token
4. ✅ Deploys to production

### Step 3: Monitor Deployment
1. Go to **Actions** tab on GitHub
2. Click on latest workflow run
3. View logs in real-time

---

## 📊 Deployment Status

### View Actions
- **GitHub Actions:** https://github.com/kanishkaa-22/Social_Engg_Simulator/actions
- **Railway Dashboard:** https://railway.app
- **Live App:** https://social-engg-simulator-production.up.railway.app

### Status Indicators
- 🟢 Green = Deployment successful
- 🟡 Yellow = Deployment in progress
- 🔴 Red = Deployment failed

---

## 🛠️ Manual Deployment

If automatic deployment fails, deploy manually:

### Option 1: GitHub Actions Manual Trigger
1. Go to **Actions** tab
2. Select **Deploy to Production** workflow
3. Click **Run workflow** → **Run workflow**

### Option 2: Railway CLI
```bash
railway up --detach
```

### Option 3: Railway Dashboard
1. Log in to [Railway.app](https://railway.app)
2. Go to project
3. Click **Deploy** button

---

## 🔐 Environment Variables

### Railway Environment Variables
Set these in Railway dashboard for production:

```
PORT=8080
FLASK_ENV=production
```

---

## 📝 Commit & Push Workflow

### Development Cycle
1. Make changes locally
2. Commit: `git commit -m "feat: Add feature"`
3. Push: `git push origin main`
4. GitHub Actions automatically deploys
5. Check live app at: https://social-engg-simulator-production.up.railway.app

---

## 🐛 Troubleshooting

### Deployment Failed?
1. Check GitHub Actions logs
2. Verify RAILWAY_TOKEN secret is set
3. Ensure config/Procfile is correct
4. Check config/requirements.txt has all dependencies

### App Not Updating?
1. Check if push actually triggered workflow
2. Wait 2-3 minutes for deployment to complete
3. Manually trigger workflow in Actions tab
4. Check Railway logs for errors

### Token Issues?
1. Generate new Railway API token
2. Update secret in GitHub
3. Retry deployment

---

## 📚 Resources

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Railway Deployment Docs](https://docs.railway.app)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/2.3.x/deploying/)

---

## ✨ Features Enabled

✅ Automatic deployment on push to main  
✅ Manual trigger via GitHub Actions  
✅ Railway production environment  
✅ Continuous deployment pipeline  
✅ Status monitoring  

**Your project is production-ready!** 🎉
