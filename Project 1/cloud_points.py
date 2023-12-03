import time
import pyautogui

# Function to check if the button is visible on the screen
def is_button_visible():
    button_location = pyautogui.locateOnScreen('button.png')  # Replace 'button.png' with the actual image of the button
    return button_location is not None

# Endless loop to continuously check for the button and click it when visible
while True:
    try:
        if is_button_visible():
            button_location = pyautogui.center(pyautogui.locateOnScreen('button.png'))
            pyautogui.click(button_location, duration=0.01)  # Click with a shorter duration
        time.sleep(0.01)  # Wait for 0.1 seconds before checking again (adjust as needed)
    except Exception as e:
        print(f"An error occurred: {e}")