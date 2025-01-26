@echo off
:: Check for admin privileges
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c runas /user:Administrator \"cmd /c python \"C:\Users\xlkay\OneDrive\Desktop\Cursor Code Editor - Trial Generator\Dark Mode - Notepad\darkmode-notepad.py\"' -Verb RunAs"
    exit /b
)

:: Run the Python script
python "C:\Users\xlkay\OneDrive\Desktop\Cursor Code Editor - Trial Generator\Dark Mode - Notepad\darkmode-notepad.py"
pause