# The script of the game goes in this file.

default player_name = "You"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("player_name", dynamic=True)
define w = Character("The Witch")
define n = Character("", what_color="#4927F5") ## ARE: this is the narrator; there might be a better way to do this i just want the text color to be different lol
define ARE = Character ("aaron note", what_color="#F54927", who_color="#F54927")


# The game starts here.

label start:

    ## ARE: in previous projects ive just used this space to declare variables
    ## and do chapter selection and the like; nothing happens till chapter 1

    jump chapter1

    return
