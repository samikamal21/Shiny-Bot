from pyautogui import *
import time
import ShinyBot

def shinyHunt(posX, posY, pixelRGB):
    """
    1 iteration is approximately 30 seconds
    """
    shinyFound = False
    count = 0
    
    time.sleep(11)
    ShinyBot.moveWindow("DeSmuME 0.9.14 git#91efef9 x64-JIT SSE2 | Pokémon Platinum",0,0)

    while(not shinyFound):
        ShinyBot.keyPress('x', 2)
        ShinyBot.keyPress('x',2.5) 
        ShinyBot.keyPress('x',2)
        ShinyBot.keyPress('x',1)
        ShinyBot.keyPress('x',1)

        time.sleep(9)
        shinyFound = ShinyBot.checkShiny(posX, posY, pixelRGB)
        if(shinyFound):
            break

        count+=1
        print(count) 
        ShinyBot.keyPressShortCut('ctrl','r',11) 

# Main

# pyautogui.displayMousePosition()
shinyHunt(410,243, (174,223,101))
