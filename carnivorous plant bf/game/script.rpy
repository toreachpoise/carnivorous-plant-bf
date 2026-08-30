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
default location = "none"
default water = False
default light = False
default fed_plant = 0
default slept_together = False
default dog_questions = 0
default blood_question = False
default expenses_question = False
default love_question = False
default dog_question = False
default ch3cut = False
default ch5cut = False
default skeptical_comment = False

# DRAMATIS PERSONAE
# The color argument colorizes the name of the character.
define p = Character("player_name", dynamic=True, who_color="#82f0d7")
define w = Character("The Witch", who_color="#b0eb88")
#define n = Character("", what_color="#4927F5") ## ARE: turns out defining the narrator in this way causes issues lol
define ARE = Character ("aaron note", what_color="#82f0d7", who_color="#F54927")
define RM = Character("rhys note", what_color="#82f0d7", who_color="#F54927")
define b = Character("[boyfriend]")
define d = Character("dogtective")

# IMAGES
# bgs
image living room light = "/bgs/_0001_living-room-light.png"
image living room dark = "/bgs/_0002_living-room-dark.png"
image living room overgrown = "/bgs/living room overgrown.png"
image kitchen dark = "/bgs/_0003_kitchen-dark.png"
image kitchen light = "/bgs/_0004_kitchen-light.png"
image kitchen overgrown = "/bgs/kitchen overgrown.png"
image table light = "/bgs/_0005_table-light.png"
image table dark = "/bgs/_0006_table-dark.png"
image bedroom = "/bgs/_0007_bedroom.png"
image aquarium = "/bgs/_0008_aquarium.png"
image convenience entrance = "/bgs/_0009_convenience-entrance.png"
image shopping arcade = "/bgs/_0010_shopping-arcade.png"
image alley = "/bgs/_0011_alley.png"
image apartment entrance = "/bgs/_0012_apartment-entrance.png"
image apartment entrance overgrown = "/bgs/apartment entrance overgrown.png"
image outside dark = "/bgs/_0013_outside-dark.png"
image outside light = "/bgs/_0014_outside-light.png"
image underpass = "/bgs/_0015_underpass.png"
image greenhouse 1 = "/bgs/_0016_greenhouse-1.png"
image greenhouse 2 = "/bgs/_0017_greenhouse-2.png"
image greenhouse 3 = "/bgs/_0018_greenhouse-3.png"
image greenhouse 4 = "/bgs/_0019_greenhouse-4.png"
image plant store exterior 1 = "/bgs/_0020_plant-store-exterior-1.png"
image plant store exterior 2 = "/bgs/_0021_plant-store-exterior-2.png"

# custom sprite positions
transform midleft:
    xalign 0.33 yalign 0.5
transform midright:
    xalign 0.66 yalign 0.5
transform lower:
    xalign 0.5 yalign 0.75


# character sprites
image dogtective = "dogtective.png"

# minigame images

image tutorial background = Image("#3f6c50", xfill=True, yfill=True)
image tutorial beats = Image("/minigame imgs/tutorial/tutorial_beats.png", yalign=0)
image tutorial chop = "/minigame imgs/tutorial/tutorial_chop.png"
image tutorial progress = "/minigame imgs/tutorial/tutorial_progress_arrow.jpg"
image tutorial one_ingredient_done = "/minigame imgs/tutorial/tutorial_one_done_arrow.jpg"
image tutorial swap = "/minigame imgs/tutorial/tutorial_swap.png"
image tutorial swap_progress = "/minigame imgs/tutorial/tutorial_swap_progress.png"
image tutorial win = "/minigame imgs/tutorial/tutorial_win.png"

label start:
# sets dreams

init python:
    import random

    class Dream(object):
        def __init__(self, val, contents):
            self.value = val
            self.contents = contents

        def __unicode__(self):
            return self.show()
        def __str__(self):
            return self.show()
        def __repr__(self):
            return self.show()

        def show(self): #shows the dream
            val = self.value
            
            if self.value == 1:
                contents = "You dream of a forest burning down and becoming a city, then the city burning down and becoming a forest. Strange new animals with improbable quantities of limbs prowl among its trees."
            if self.value == 2:
                contents = "You dream of an engine powered by the wingbeats of moths. A hamster wheel with a light at the end that they ceaselessly chase, their wingbeats propelling it ever away from them around the circle."
            if self.value == 3:
                contents = "No dreams come to you this night."
            if self.value == 4:
                contents = "If you dreamed, you don't remember it. But you awake with a vague feeling of unease."
            if self.value == 5:
                contents = "Just before you wake you dream of yourself laying on the ground in a computer server room. They hum quietly, whispering encrypted secrets to you."
            if self.value == 6:
                contents = "This night your dream is just the night sky. You've never had a dream like this before. The stars twinkle above you. Were there always this many? You've lived in the city too long to remember."
            if self.value == 7:
                contents = "You dream you're lost in a mall trying to find your mom. What store was she in last?"
            if self.value == 8:
                contents = "You sleep restlessly and all your dreams are about bees chasing you."
            if self.value == 9:
                contents = "You dream you are a tree growing through an abandoned parking lot. Your branches press against the level above you, crawling horizontally along it till you reach the window openings and breaks in the roof."

            return "{}".format(contents)

    class DreamBank(object):
        def __init__(self):
            self.dreamlist = []
            self.build()


        #display all dreams in the list
        def show(self):
            for dream in self.dreamlist:
                print dream.show()


        # generate dreams
        def build(self):
            self.dreamlist = []
            dream_number = 9
            for val in range(1, dream_number):
                self.dreamlist.append(Dream(val, ""))


        # shuffle the dreams
        def shuffle(self, num=1):
            length = len(self.dreamlist)
            for n in range(num):
                # this is the fisher yates shuffle algorithm, whatever that is
                for i in range(length-1, 0, -1):
                    randi = random.randint(0, i)
                    if i == randi:
                        continue
                    self.dreamlist[i], self.dreamlist[randi] = self.dreamlist[randi], self.dreamlist[i]

            # you can also use the built-in shuffle method
            # random.shuffle(self, dreamlist)

        def calldream(self):
            if self.dreamlist:
                return self.dreamlist.pop()
            else:
                self.build()
                self.shuffle()
                return self.dreamlist.pop()


    class Dreamer(object):
        def __init__(self):
            #self.name = name
            self.dreams = []

        def draw(self, dreambank, num=1):
            for n in range(num):
                dream = dreambank.calldream()
                if dream:
                    self.dreams.append(dream)
                else:
                    return False
            return True        


$ dreamstonight = DreamBank()
$ dreamer = Dreamer()
$ dreamstonight.build()
$ dreamstonight.shuffle()

# GAME STARTS HERE

label startmenu:
    scene plant store exterior 1
    menu:
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
        "minigame":
            jump minigame

    return
