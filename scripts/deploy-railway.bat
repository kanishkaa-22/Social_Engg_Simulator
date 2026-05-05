@echo off
REM Social Engineering Simulator - Railway Deployment Script

echo.
echo ========================================
echo  Railway Deployment Setup
echo ========================================
echo.

echo Step 1: Logging in to Railway...
echo Please authenticate in the browser window that opens.
railway login

if %errorlevel% neq 0 (
    echo Error: Railway login failed
    pause
    exit /b 1
)

echo.
echo Step 2: Initializing Railway project...
railway init --name Social-Engg-Simulator

if %errorlevel% neq 0 (
    echo Error: Railway init failed
    pause
    exit /b 1
)

echo.
echo Step 3: Deploying to Railway...
railway up

if %errorlevel% neq 0 (
    echo Error: Deployment failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Deployment Complete!
echo ========================================
echo.
echo Your app is now live on Railway!
echo Check the deployment logs above for your URL.
echo.
pause
