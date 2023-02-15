# Shiny-Bot
This bot is capable of shiny hunting Pokémon in any game.

## How to set up:
In ShinyBot.py, you can use the methods to set up a bot if you provide the following information:
- Window name of game, ex: "Pokémon  Insurgence"
- Non-shiny Pokémon  RGB value, ex: (115, 73, 105)
- Window coordinates of what pixel you want to check. ex: (410, 243)

*Note that the bot will automically move the screen to (0,0), which is the top left of your screen. So first make sure to have the bot move your game window to (0,0) using the Shinybot.moveWindow(windowName, posX, posY) method. 
 
Next, in order to figure out out the RGB value and window coordinates for the bot to check, open the idle shell in python and write the following:
- import pyautogui
- pyautogui.displayMousePosition()
<p align="center">
  <img src="pyauto.PNG"/>
</p>

Ater doing the following, your mouse position and the RGB value of where your mouse is will be constantly updated, so in your Pokémon Game, hover over any pixel of the Pokémon to get it's RGB value and coordinates.

Now, you must set up the bot using the Shinybot.py methods. If you take a look at RenegadeShinies.py, that is a good example of how I automated the bot to find shinies in Pokémon Renegade Platinum. 

*Before you run your bot, make sure to not cover the game window or else the bot will not check the correct pixel. 
