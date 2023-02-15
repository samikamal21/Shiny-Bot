from pyautogui import *
import pyautogui
import time
import win32gui

shinyFound = False
count = 0
time.sleep(8)

window = win32gui.FindWindow(None, "Pokemon Insurgence")
win32gui.MoveWindow(window, 0, 0, 1030, 797, True)

def keyPress(interval):
    pyautogui.keyDown('c')
    time.sleep(0.1)
    pyautogui.keyUp('c')
    time.sleep(interval)

while(not shinyFound):
    # load into game
    keyPress(3)

    keyPress(2)

    # pick pokemon
    keyPress(1)

    keyPress(1)

    keyPress(1)

    keyPress(1)

    keyPress(1)

    pyautogui.keyDown('down')
    time.sleep(0.1)
    pyautogui.keyUp('down')

    keyPress(1)

    # check for shiny
    shinyFound = pyautogui.pixel(512,454) != (115, 73, 105)
    #shinyFound = pyautogui.pixel(1135,635) == (233, 148, 26)
    
    if(shinyFound):
        print("Shiny Found")
        break
   
    print("Not Shiny")
    count+=1
    print(count)

    pyautogui.keyDown('f12')
    time.sleep(0.1)
    pyautogui.keyUp('f12')
    time.sleep(8)












        

    






