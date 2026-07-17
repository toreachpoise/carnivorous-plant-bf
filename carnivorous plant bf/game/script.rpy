# The script of the game goes in this file.

default player_name = "You"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("player_name", dynamic=True, who_color="#82f0d7")
define w = Character("The Witch")
#define n = Character("", what_color="#4927F5") ## ARE: turns out defining the narrator in this way causes issues lol
define ARE = Character ("aaron note", what_color="#82f0d7", who_color="#F54927")

## space for defining all the images because ren'py's image summoner is messy and this lets you transform them

# bgs
image greenhouse bg:
    "greenhouse bg.png"
    zoom 1.5

# character sprites

image test:
    "images.jpg"

# minigame images

# The game starts here.

label start:

    ## ARE: in previous projects ive just used this space to declare variables
    ## and do chapter selection and the like; nothing happens till chapter 1

    jump minigame

    return
