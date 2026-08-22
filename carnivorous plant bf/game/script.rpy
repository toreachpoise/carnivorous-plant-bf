# The script of the game goes in this file.
    ## ARE: as in previous projects ive just used this space to declare variables
    ## and do chapter selection and the like; nothing happens till chapter 1

# VARIABLES
default player_name = "You"
default deepest_desire = "to be loved"
default boyfriend_description = "... someone who is nice and makes me feel good, I guess?"
default name_set = False
default chapter = 1
default optimism = 0 ## ARE: not sure if this will even be a game mechanic but i'm tracking it lol
default brains = 0 ## idk lmao
default boyfriend = "flytrap"
default soil = False
default water = False
default light = False
default fed_plant = 0
default slept_together = False
default dog_questions = 0
default blood_question = False
default expenses_question = False
default love_question = False
default dog_question = False
default player_bled_ch5 = False

# DRAMATIS PERSONAE
# The color argument colorizes the name of the character.
define p = Character("player_name", dynamic=True, who_color="#82f0d7")
define w = Character("The Witch", who_color="#b0eb88")
#define n = Character("", what_color="#4927F5") ## ARE: turns out defining the narrator in this way causes issues lol
define ARE = Character ("aaron note", what_color="#82f0d7", who_color="#F54927")
define b = Character("boyfriend")
define d = Character("dogtective")

# IMAGES
# bgs
image living room light = "/bgs/_0001_living-room-light.png"
image living room dark = "/bgs/_0002_living-room-dark.png"
image kitchen dark = "/bgs/_0003_kitchen-dark.png"
image kitchen light = "/bgs/_0004_kitchen-light.png"
image table light = "/bgs/_0005_table-light.png"
image table light 2 = "/bgs/_0006_table-light-2.png"
image bedroom = "/bgs/_0007_bedroom.png"
image aquarium = "/bgs/_0008_aquarium.png"
image convenience entrance = "/bgs/_0009_convenience-entrance.png"
image shopping arcade = "/bgs/_0010_shopping-arcade.png"
image alley = "/bgs/_0011_alley.png"
image apartment entrance = "/bgs/_0012_apartment-entrance.png"
image outside dark = "/bgs/_0013_outside-dark.png"
image outside light = "/bgs/_0014_outside-light.png"
image underpass = "/bgs/_0015_underpass.png"
image greenhouse 1 = "/bgs/_0016_greenhouse-1.png"
image greenhouse 2 = "/bgs/_0017_greenhouse-2.png"
image greenhouse 3 = "/bgs/_0018_greenhouse-3.png"
image greenhouse 4 = "/bgs/_0019_greenhouse-4.png"
image plant store exterior 1 = "/bgs/_0020_plant-store-exterior-1.png"
image plant store exterior 2 = "/bgs/_0021_plant-store-exterior-2.png"


# character sprites


# minigame images






# GAME STARTS HERE

label start:
    scene plant store exterior 1
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
            if chapter == 4:
                jump chapter4
            if chapter == 5:
                jump chapter5
            if chapter == 6:
                jump chapter6
            else:
                "More coming soon ..."
                extend " we hope!"
                menu:
                    "Play Again?"
                    "Replay Story":
                        jump chapter1
                    "Minigame":
                        jump minigame
                    "Quit":
                        pass

    return
