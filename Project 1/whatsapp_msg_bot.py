import pyautogui
from time import sleep

sleep(2)
for i in range(0,10000000000):
    pyautogui.hotkey('ctrl', 'v')
    # You can copy something to send by uncommenting the above line and commenting the below line
    # pyautogui.write("")
    pyautogui.press("enter")
    

