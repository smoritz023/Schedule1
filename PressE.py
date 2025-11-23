import time
import keyboard

def press_e_every_five_seconds():
    """
    Continuously presses the 'e' key every 5 seconds.
    The script can be stopped by pressing Ctrl+C in the terminal.
    """
    print("Pressing 'e' every 5 seconds. Press Ctrl+C to stop.")
    try:
        while True:
            keyboard.press('e')
            time.sleep(1)
            keyboard.release('e')
            print("Pressed 'e'")
            time.sleep(3)  # Wait for 5 seconds
    except KeyboardInterrupt:
        print("\nScript stopped.")

if __name__ == "__main__":
        press_e_every_five_seconds()

        #eeeeeeeeeeeeeeeeeeeeeeeee