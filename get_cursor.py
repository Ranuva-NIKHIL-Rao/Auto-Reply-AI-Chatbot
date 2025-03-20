#Use this script to get the current position of the cursor on the screen.
#Run this script and move the cursor to the desired position on the screen.
#The current position of the cursor will be printed to the console.
#Use these coordinates in the pyautogui.click() function in the bot.py script to simulate mouse clicks at that position.
#This can help you accurately simulate mouse clicks at specific positions on the screen.
#This can be useful when automating tasks that require precise mouse movements and clicks.
import pyautogui
while True:
    coordinate_pos=pyautogui.position()
    print(coordinate_pos,end='\r')