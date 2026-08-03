# The script of the game goes in this file.
    ## ARE: in previous projects ive just used this space to declare variables
    ## and do chapter selection and the like; nothing happens till chapter 1

# VARIABLES
default player_name = "You"
default deepest_desire = "to be loved"
default boyfriend_description = "... someone who is nice and makes me feel good, I guess?"
default name_set = False
default chapter = 1
default optimism = 0 ## ARE: not sure if this will even be a game mechanic but i'm tracking it lol
default boyfriend = "flytrap"

# DRAMATIS PERSONAE
# The color argument colorizes the name of the character.
define p = Character("player_name", dynamic=True, who_color="#82f0d7")
define w = Character("The Witch", who_color="#b0eb88")
#define n = Character("", what_color="#4927F5") ## ARE: turns out defining the narrator in this way causes issues lol
define ARE = Character ("aaron note", what_color="#82f0d7", who_color="#F54927")

# IMAGES
# bgs
image greenhouse bg:
    "greenhouse bg.png"
    zoom 1.5

# character sprites
image test:
    "images.jpg"

# minigame images






# GAME STARTS HERE

label start:
    menu:
        ARE "chapter select menu for ease of testing"
        "minigame":
            jump minigame
        "story":
            if chapter == 1:
                jump chapter1
            if chapter == 2:
                jump chapter2
            if chapter == 3:
                jump chapter3

    return
