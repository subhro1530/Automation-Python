from pyautogui import click, locateOnScreen, write, press
from time import sleep

x = 550
y = 272
k = 63

sleep(2)

while k >= 0:
    button_position = locateOnScreen('inp_button.png')  # Replace 'button.png' with the actual filename of your button image
    if button_position:
        click(button_position[0], button_position[1])
        click(x, y)
        sleep(0.5)
        click(280, 740)
        sleep(0.5)
        write("B" + str(k // 10) + str(k % 10))  # Concatenate the tens and ones digits for 'B'
        
        sleep(0.5)
        x += 30
        press("enter")
        sleep(0.5)
        click(button_position[0], button_position[1])
        click(x, y)
        sleep(0.5)
        click(280, 740)
        sleep(0.5)
        write("A" + str(k // 10) + str(k % 10))  # Concatenate the tens and ones digits for 'A'
        sleep(0.5)
        x += 30
        press("enter")
        sleep(0.5)
        k -= 1
        if k==42:
            x=550
            y=320
        if k==20:
            x=550
            y=350
    else:
        sleep(0.5)
