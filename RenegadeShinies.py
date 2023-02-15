from pyautogui import *
import time
import ShinyBot

# this bot is meant to be executed immediately when you open the game.
def shinyHunt(posX, posY, pixelRGB):
    """
    1 iteration is approximately 30 seconds
    """
    shinyFound = False
    count = 0
    
    time.sleep(11) # 11 second delay, so the start up screens gets to the main menu before the bot starts pressing any buttons.
    ShinyBot.moveWindow("DeSmuME 0.9.14 git#91efef9 x64-JIT SSE2 | Pokémon Platinum",0,0)

    # number of times the bot will hit 'x' to start a battle with the Pokemon you are shiny hunting
    while(not shinyFound):
        ShinyBot.keyPress('x', 2)
        ShinyBot.keyPress('x',2.5) 
        ShinyBot.keyPress('x',2)
        ShinyBot.keyPress('x',1)
        ShinyBot.keyPress('x',1)

        time.sleep(9) # 9 second delay to transition to battle once you encounter the Pokemon.
        shinyFound = ShinyBot.checkShiny(posX, posY, pixelRGB)
        
        if(shinyFound): 
            break # loop ends once the bot looks at the pixel coordinates if it's != pixelRGB

        # displays number of times the bot has to go back to the main menu and repeat this whole process
        count+=1
        print(count) 
        ShinyBot.keyPressShortCut('ctrl','r',11) 

# Main
shinyHunt(410,243, (174,223,101))
