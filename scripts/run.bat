@echo off
REM Social Engineering Simulator - Quick Start Script for Windows

echo.
echo ==========================================
echo Social Engineering Simulator
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [✓] Python found

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Flask not found. Installing dependencies...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
    echo [✓] Dependencies installed
) else (
    echo [✓] Flask already installed
)

echo.
echo ==========================================
echo Starting Application...
echo ==========================================
echo.
echo Open your browser and go to:
echo http://127.0.0.1:5000/
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
