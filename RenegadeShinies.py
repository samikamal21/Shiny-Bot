from pyautogui import *
import time
import ShinyBot

def slowOverworldLegendary(posX, posY, pixelRGB):
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

def fastOverworldLegendary(posX, posY, pixelRGB):
    """
    1 iteration is approximately 12 seconds
    """
    
    shinyFound = False
    count = 0
    
    time.sleep(3) 
    ShinyBot.moveWindow("DeSmuME 0.9.14 git#91efef9 x64-JIT SSE2 | Pokémon Platinum",0,0)

    while(not shinyFound):
        ShinyBot.keyPress('x', 1.5)
        ShinyBot.keyPress('x',0.6)  
        ShinyBot.keyPress('x', 1.8) 
        ShinyBot.keyPress('x',0.1)
        ShinyBot.keyPress('x',0.1)

        time.sleep(3.5)
        shinyFound = ShinyBot.checkShiny(posX, posY, pixelRGB)
        if(shinyFound):
            break

        count+=1
        print(count)
        ShinyBot.keyPressShortCut('ctrl','r',3)
  
def testShinyFound(posX, posY, pixelRGB):
    time.sleep(3)
    ShinyBot.moveWindow("DeSmuME 0.9.14 git#91efef9 x64-JIT SSE2 | Pokémon Platinum",0,0)
   
    for i in range(1,100):
        ShinyBot.keyPress('x', 1.5)
        ShinyBot.keyPress('x',0.6) 
        ShinyBot.keyPress('x', 1.5) 
        ShinyBot.keyPress('x',0.1)
        ShinyBot.keyPress('x',0.1)

        time.sleep(3)
        shinyFound = ShinyBot.checkShiny(posX, posY, pixelRGB)
        ShinyBot.keyPressShortCut('ctrl','r',3)
        print(i)

def shinyLatias(posX, posY, pixelRGB):
    """
    Specifically made to catch Latias
    """
    
    shinyFound = False
    count = 0
    
    time.sleep(3) 
    ShinyBot.moveWindow("DeSmuME 0.9.14 git#91efef9 x64-JIT SSE2 | Pokémon Platinum",0,0)

    while(not shinyFound):
        ShinyBot.keyPress('x', 1.5)
        ShinyBot.keyPress('x',0.6)  
        ShinyBot.keyPress('x', 1.8) 
        ShinyBot.keyPress('x',0.1)
        ShinyBot.keyPress('x',0.1)
        ShinyBot.keyPress('x',0.1)
        ShinyBot.keyPress('x',0.3)
        ShinyBot.keyPress('x',0.2)
        ShinyBot.keyPress('x',0.4)
        ShinyBot.keyPress('x',0.3)
        ShinyBot.keyPress('x',2)
        ShinyBot.keyPress('x',0.1)

        time.sleep(3.5)
        shinyFound = ShinyBot.checkShiny(posX, posY, pixelRGB)
        if(shinyFound):
            break

        count+=1
        print(count)
        ShinyBot.keyPressShortCut('ctrl','r',2.8)       

def shinyLatios(posX, posY, pixelRGB):
    """
    Specifically made to catch Latios
    """
    
    shinyFound = False
    count = 0
    
    time.sleep(3) 
    ShinyBot.moveWindow("DeSmuME 0.9.14 git#91efef9 x64-JIT SSE2 | Pokémon Platinum",0,0)

    while(not shinyFound):
        ShinyBot.keyPress('x', 1.5)
        ShinyBot.keyPress('x',0.6)  
        ShinyBot.keyPress('x', 1.8) 
        ShinyBot.keyPress('x',0.1)
        ShinyBot.keyPress('x',0.1)
        ShinyBot.keyPress('x',0.1)
        ShinyBot.keyPress('x',0.3)
        ShinyBot.keyPress('x',0.5)
        ShinyBot.keyPress('x',1)
        ShinyBot.keyPress('down',0.3)
        ShinyBot.keyPress('x',0.2)
        ShinyBot.keyPress('x',0.8)
        ShinyBot.keyPress('x',0.1)

        time.sleep(3.5)
        shinyFound = ShinyBot.checkShiny(posX, posY, pixelRGB)
        if(shinyFound):
            break

        count+=1
        print(count)
        ShinyBot.keyPressShortCut('ctrl','r',2.8) 

def shinyRegigigas(posX, posY, pixelRGB):
    """
    Specifically made to catch Regigigas
    """
    
    shinyFound = False
    count = 0
    
    time.sleep(3) 
    ShinyBot.moveWindow("DeSmuME 0.9.14 git#91efef9 x64-JIT SSE2 | Pokémon Platinum",0,0)

    while(not shinyFound):
        ShinyBot.keyPress('x', 1.5)
        ShinyBot.keyPress('x',0.6)  
        ShinyBot.keyPress('x', 1.8)

        ShinyBot.keyPress('x',0.3)
        ShinyBot.keyPress('x',0.4)
        ShinyBot.keyPress('x',0.3)
        ShinyBot.keyPress('x',0.4)
        ShinyBot.keyPress('x',0.3)
        ShinyBot.keyPress('x',0.4)
        ShinyBot.keyPress('x',0.3)
        ShinyBot.keyPress('x',0.4)
        ShinyBot.keyPress('x',0.3)
        ShinyBot.keyPress('x',0.4)

        time.sleep(3.5)
        shinyFound = ShinyBot.checkShiny(posX, posY, pixelRGB)
        if(shinyFound):
            break

        count+=1
        print(count)
        ShinyBot.keyPressShortCut('ctrl','r',3)

def portalLegendarySpecialItem(posX, posY, pixelRGB):
    """
    Specifically made to catch legendaries that have additional text due to a special item reacting
    """

    shinyFound = False
    count = 0
    
    time.sleep(3) 
    ShinyBot.moveWindow("DeSmuME 0.9.14 git#91efef9 x64-JIT SSE2 | Pokémon Platinum",0,0)

    while(not shinyFound):
        ShinyBot.keyPress('x', 1.5)
        ShinyBot.keyPress('x',0.6)  
        ShinyBot.keyPress('x', 1.8)

        ShinyBot.keyPress('x',0.3)
        ShinyBot.keyPress('x',0.4)
        ShinyBot.keyPress('x',0.5)
        ShinyBot.keyPress('x',0.7)
        ShinyBot.keyPress('x',0.6)
        ShinyBot.keyPress('x',0.7)
        ShinyBot.keyPress('x',0.3)
        
        time.sleep(3.5)
        shinyFound = ShinyBot.checkShiny(posX, posY, pixelRGB)
        if(shinyFound):
            break

        count+=1
        print(count)
        ShinyBot.keyPressShortCut('ctrl','r',3)

def portalLegendary(posX, posY, pixelRGB):
    """
    Specifically made to catch portal legendaries with same amount of dialogue
    """

    shinyFound = False
    count = 0
    
    time.sleep(3) 
    ShinyBot.moveWindow("DeSmuME 0.9.14 git#91efef9 x64-JIT SSE2 | Pokémon Platinum",0,0)

    while(not shinyFound):
        ShinyBot.keyPress('x', 1.5)
        ShinyBot.keyPress('x',0.6)  
        ShinyBot.keyPress('x', 1.8)

        ShinyBot.keyPress('x',0.3)
        ShinyBot.keyPress('x',0.4)
        ShinyBot.keyPress('x',0.5)
        ShinyBot.keyPress('x',0.7)
        ShinyBot.keyPress('x',0.6)
        ShinyBot.keyPress('x',0.7)

        time.sleep(3.5)
        shinyFound = ShinyBot.checkShiny(posX, posY, pixelRGB)
        if(shinyFound):
            break

        count+=1
        print(count)
        ShinyBot.keyPressShortCut('ctrl','r',3)    

def shinyJirachi(posX, posY, pixelRGB):
    """
    Specifically made to catch Jirachi
    """

    shinyFound = False
    count = 0
    
    time.sleep(3) 
    ShinyBot.moveWindow("DeSmuME 0.9.14 git#91efef9 x64-JIT SSE2 | Pokémon Platinum",0,0)

    while(not shinyFound):
        ShinyBot.keyPress('x', 1.5)
        ShinyBot.keyPress('x',0.6)  
        ShinyBot.keyPress('x', 1.8)

        ShinyBot.keyPress('x',0.3)
        ShinyBot.keyPress('x',0.4)
        ShinyBot.keyPress('x',0.5)
        ShinyBot.keyPress('x',3)
        ShinyBot.keyPress('x',0.9)
        ShinyBot.keyPress('x',0.5)
        ShinyBot.keyPress('x',0.7)

        time.sleep(3.5)
        shinyFound = ShinyBot.checkShiny(posX, posY, pixelRGB)
        if(shinyFound):
            break

        count+=1
        print(count)
        ShinyBot.keyPressShortCut('ctrl','r',3)    

def shinyDeoxys(posX, posY, pixelRGB):
    """
    Specifically made to catch Deoxys
    """

    shinyFound = False
    count = 0
    
    time.sleep(3) 
    ShinyBot.moveWindow("DeSmuME 0.9.14 git#91efef9 x64-JIT SSE2 | Pokémon Platinum",0,0)

    while(not shinyFound):
        ShinyBot.keyPress('x', 1.5)
        ShinyBot.keyPress('x',0.6)  
        ShinyBot.keyPress('x', 1.8)

        ShinyBot.keyPress('down',2.3)
        ShinyBot.keyPress('x',0.4)
       
        time.sleep(3.5)
        shinyFound = ShinyBot.checkShiny(posX, posY, pixelRGB)
        if(shinyFound):
            break

        count+=1
        print(count)
        ShinyBot.keyPressShortCut('ctrl','r',3)   

# Main

# pyautogui.displayMousePosition()
fastOverworldLegendary(410,243, (174,223,101))