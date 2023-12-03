import pyautogui
from time import sleep

sleep(5)
for i in range(0,10):
    pyautogui.moveTo(1935,475,1)
    sleep(1)
    pyautogui.leftClick()
    # sleep(.5)
    # pyautogui.click(1935,475)
    sleep(1)
    pyautogui.scroll('up')
    sleep(1)