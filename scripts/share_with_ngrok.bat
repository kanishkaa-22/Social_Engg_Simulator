@echo off
REM Social Engineering Simulator - Share with ngrok

echo.
echo ==========================================
echo Social Engineering Simulator
echo Sharing with ngrok (Random Users Access)
echo ==========================================
echo.

REM Check if ngrok exists
if not exist "ngrok.exe" (
    echo ERROR: ngrok.exe not found!
    echo.
    echo Please download ngrok from: https://ngrok.com/download
    echo Extract ngrok.exe to this folder
    echo.
    pause
    exit /b 1
)

REM Start Flask app in background
echo [1/2] Starting Flask Application...
start "Flask App" /B python app.py
timeout /t 3 >nul

REM Start ngrok tunnel
echo [2/2] Starting ngrok tunnel...
echo.
echo ==========================================
echo SHARE THIS PUBLIC LINK WITH YOUR FRIEND:
echo ==========================================
echo.

ngrok http 5000

pause
