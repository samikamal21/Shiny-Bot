from pyautogui import *
import pyautogui
import time
import win32gui

def moveWindow(windowName, posX, posY):
    """
    Pass name of window and the window coordinate destination
    EX: moveWindow("Pokemon Insurgence", 0, 0) 

    Args:
        windowName: name of window you want to move
        posX: x-cord
        posY: y-cord
    """
    window = win32gui.FindWindow(None, windowName)
    windowRect = win32gui.GetWindowRect(window)
    x = windowRect[0]
    y = windowRect[1]
    w = windowRect[2] - x
    h = windowRect[3] - y
    win32gui.MoveWindow(window, posX, posY, w, h, True)

def keyPress(keyboardKey, interval):
    """
    Pass the keyboardKey for input and then the delay after it
    EX: keyPress('a', 1)

    Args:
        keyboardKey: input key
        interval: delay afer the input
    """
    pyautogui.keyDown(keyboardKey)
    time.sleep(0.1)
    pyautogui.keyUp(keyboardKey)
    time.sleep(interval)

def keyPressShortCut(keyboardKey1, keyBoardKey2, interval):
    """
    Pass keyboardKey1 and keyBoardKey2 to perform a shortcut input and then the delay after it
    EX: keyPress('ctrl', 'r', 1)

    Args:
        keyboardKey1: first input key
        keyboardKey2: second input key
        interval: delay after both inputs
    """
    pyautogui.keyDown(keyboardKey1)
    time.sleep(0.1)
    pyautogui.keyDown(keyBoardKey2)
    time.sleep(0.1)
    pyautogui.keyUp(keyboardKey1)
    pyautogui.keyUp(keyBoardKey2)
    time.sleep(interval)

def checkShiny(posX, posY, tPokemonRGB):
    """
    Pass the coordinates of where to check for shiny and the NON-shiny RGB
    EX: boolean variable = checkShiny(512, 454, (115, 73, 105))

    Args: 
        posX: x-coord
        posY: y-coord
        tPokemonRGB: pixel color of normal pokemon
    """

    if(pyautogui.pixel(posX,posY) != (tPokemonRGB)):
        bShiny = True
        print(bShiny)
    else:
        bShiny = False
        print(bShiny)

    return bShiny