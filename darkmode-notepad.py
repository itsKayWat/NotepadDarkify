import winreg as reg

def enable_notepad_dark_mode():
    try:
        # Open the registry key for Notepad
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Notepad", 0, reg.KEY_SET_VALUE)

        # Set the color scheme for dark mode
        # 0x000000 is black (background), 0xFFFFFF is white (text)
        reg.SetValueEx(key, "Color1", 0, reg.REG_DWORD, 0x000000)  # Background color (black)
        reg.SetValueEx(key, "Color2", 0, reg.REG_DWORD, 0xFFFFFF)  # Text color (white)

        # Close the registry key
        reg.CloseKey(key)

        print("Notepad dark mode enabled successfully!")
    except Exception as e:
        print(f"Failed to enable dark mode: {e}")

if __name__ == "__main__":
    enable_notepad_dark_mode()