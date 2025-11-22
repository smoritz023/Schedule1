import pyautogui
import time

# Give yourself a few seconds to click on the target application window after running the script
print("Switch to the application window within 5 seconds...")
time.sleep(5)

def press_e_every_five_seconds():
    """
    Continuously presses the 'e' key every 5 seconds.
    The script can be stopped by pressing Ctrl+C in the terminal.
    """
    print("Pressing 'e' every 5 seconds. Press Ctrl+C to stop.")
    try:
        while True:
            pyautogui.press('e')
            print("Pressed 'e'")
            time.sleep(5)  # Wait for 5 seconds
    except KeyboardInterrupt:
        print("\nScript stopped.")

if __name__ == "__main__":
        press_e_every_five_seconds()