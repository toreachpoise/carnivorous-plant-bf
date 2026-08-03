label chapter2:

scene greenhouse bg
"The greenhouse is lush and green, suffused with the dim, pinkish light of dozens of LED grow lights."
"It smells wet and warm and vegetal in there. And a bit like boy sweat."
p "I don't just want to fuck the plant."
extend " . . right?"
p "I mean, honestly, what the hell do I want? Like, in life?"

label deepestdesire:
    python:
        deepest_desire = renpy.input("What do I really want, like deep down?")
        deepest_desire.strip()
        if deepest_desire == "":
            deepest_desire = "Someone I love who loves me."
            no_deepest_desire = True
            optimism -= 1
            renpy.say(p,"It's kinda hard to put it into words but like, ...")
            renpy.say(p, "I guess someone who loves me? And who I love? Isn't that what everyone wants?")
        else:
            no_deepest_desire = False
            renpy.say(p, "[deepest_desire]")
            optimism += 1

## ARE note: option to process the depeest desire here in some fashion but idk what to do about that for now

p "Damn, is that really my deepest desire?"
menu:
    p "That's kinda ... "
    "Beautiful":
        $ optimism += 1
        pass
    "Pathetic":
        $ optimism -= 1
        pass
    "Iconic":
        $ optimism += 1
        pass
    "Boring":
        pass
p "I guess for now what I get is a plant boyfriend who will love me unconditionally forever. Y'know, [boyfriend_description]."
menu:
    p "... that's pretty good right?"
    "I don't know about all this ...":
        $ optimism -= 1
        p "It's not as if I have any better choice, right?"
        p "Otherwise I'll probably die a virgin ..."
    "I could do worse ...":
        $ optimism += 1
        pass

p "I guess I better try to pick one out ..."
## some kind of visual transition; maybe a CG goes here
"There are plants everywhere. On shelves, on the ground, hanging from the ceiling."
"Each one you rest your attention on reveals a human form or body part incorporated into it:"
"a tree with a human torso, rooted in the ground, its branches resembling upstretched arms;"
"grapevines made of hands grasping one another at the wrist, fingers cupping fruit, or resting empty, waiting."
menu:
    p "These plants are so weird, it's kinda ..."
    "delightful":
        $ optimism += 1
        p "I really love seeing the different shapes that living things take on."
        extend " . . And these are some cool ass shapes!"
    "freaking me out": 
        p "I should just pick one before I lose my nerve and realize this is a dumb idea ..."
        $ optimism -= 1

label chooseboyfriend:
menu:
    p "But which do I pick?"
    "flytrap":
        show flytrap
        "Four little heads rest at the ends of four leafy arms."
        "One at a time, the heads turn to you as if to a beat. They almost seem to be striking a pose?"
        menu:
            p "Is this gonna be my plant boyfriend?"
            "Yes":
                $ boyfriend = "flytrap"
                jump boyfriendchosen
            "No":
                p "No, it can't be, this thing is too weird ..."
                $ optimism -= 1
                p "I have to find something else ..."
                jump chooseboyfriend
    "spider":
        show spider
        "His many eyes scan the room lazily."
        extend " If there's a pattern to what he follows, it's not clear."
        "But now that you are looking at him, one of his has trained and holds its gaze on you."
        menu:
            p "Is this gonna be my plant boyfriend?"
            "Yes":
                $ boyfriend = "spider"
                jump boyfriendchosen
            "No":
                p "No, it can't be, this thing is too weird ..."
                $ optimism -= 1
                p "I have to find something else ..."
                jump chooseboyfriend
    "foxglove":
        show thistle_n_foxglove
        "Its many lips pucker and shine. The glossy surface of them smells like sweet syrup."
        $ foxglove_impulse = renpy.input("You know you want to ...", default = "touch it.")
        menu:
            p "Is this gonna be my plant boyfriend?"
            "Yes":
                $ boyfriend = "foxglove"
                jump boyfriendchosen
            "No":
                p "No, it can't be, this thing is too weird ..."
                $ optimism -= 1
                p "I have to find something else ..."
                jump chooseboyfriend
    "thistle":
        show thistle_n_foxglove
        "This plant has a one foot gap between it and every other object around it."
        "You notice the spikes, no, the fangs around its head. They seem sturdy and heavy."
        "It's menacing. Like a sword in a museum that has not stopped being a tool for killing just because it is on display."
        p "Aww, you wouldn't bite me though, right?"
        "The eye stares back. Your hands stay by your side."
        menu:
            p "Is this gonna be my plant boyfriend?"
            "Yes":
                $ boyfriend = "thistle"
                jump boyfriendchosen
            "No":
                p "No, it can't be, this thing is too weird ..."
                $ optimism -= 1
                p "I have to find something else ..."
                jump chooseboyfriend
    "orb":
        "Your gaze is drawn to this plant's light even as its brilliance hurts your eyes."
        if optimism > 5:
            "It fills you with a sense of deep joy and contentment."
        elif optimism < 0:
            "It fills you with a deep, addictive feeling dread."
            "Like warm, deep water you could close your eyes and fall ever deeper into."
            extend " Never to surface again."
        else:
            "You feel your mind clear finally from all the noise it's constantly filled with."
            "A deep quiet suffuses your consciousness."
        "The feeling remains as an image resolves in your head. [deepest_desire]"
        "Then you blink and it's just a plant in front of you. Some kind of succulent with a glowing orb poised above it as if delicately balanced on its upraised fingertips."
        menu:
            p "Is this gonna be my plant boyfriend?"
            "Yes":
                $ boyfriend = "orb"
                jump boyfriendchosen
            "No":
                p "No, it can't be, this thing is too weird ..."
                $ optimism -= 1
                p "I have to find something else ..."
                jump chooseboyfriend

label boyfriendchosen:
$ optimism += 1

p "Yess ..."
p "I've got him. This sweet [boyfriend] is gonna be my sweet boyfriend."
if optimism < 3:
    extend " I think? I hope?"
"On some unseen timer, sprinklers activate all over the greenhouse, watering the plants and soaking you."
p "*sigh* ... Time to bring him home."

$ chapter = 3
jump start
