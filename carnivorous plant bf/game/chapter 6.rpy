label chapter6:
if slept_together == True:
    scene living room overgrown
else:
    scene bedroom
"In the morning you discover two things."
"First, that you've shifted in your sleep."
if slept_together == True:
    if boyfriend == "flytrap":
        show flytrap with dissolve
    if boyfriend == "spider":
        show spider with dissolve
    if boyfriend == "foxglove":
        show foxglove with dissolve
    if boyfriend == "thistle":
        show thistle with dissolve
    if boyfriend == "orb":
        show orb with dissolve
    "You now have your arms wrapped around your [boyfriend], your face buried against the soft coolness of his stem."
else:
    "You now have your arms wrapped around your pillow. Your back hurts from sleeping like this, without proper support."
scene kitchen overgrown with dissolve
if boyfriend == "flytrap":
    show flytrap with dissolve
if boyfriend == "spider":
    show spider with dissolve
if boyfriend == "foxglove":
    show foxglove with dissolve
if boyfriend == "thistle":
    show thistle with dissolve
if boyfriend == "orb":
    show orb with dissolve
"The second is that your plant has continued to grow."
"Every inch of the apartment is now coated in a tangled mass of roots and vines."
"Even the windows are covered, so that the light in the room enters with a soft green tinge."
b "Good morning!"
if boyfriend == "flytrap":
    "One head is looking at you, but the other three look to each other as if in some nervous conference."
if boyfriend == "spider":
    "The eyes face the corners of the room, the window. Only one musters the nerve to face you."
if boyfriend == "foxglove":
    "His many lips are many degrees of pursed."
if boyfriend == "thistle":
    "His eye is not quite meeting yours."
if boyfriend == "orb":
    "The orb shines palely despite its renewed size, a little dimmer than usual."
p "*yawn*"
menu:
    "Good morning!":
        $ optimism += 2
    "... Is something wrong?":
        $ optimism -= 2
b "........"
extend "I'm big enough now ..."
b "Big enough to grant your wish. If you still want me to."
p "Last night you said you'd need {i}a bit more{/i}. What did that mean?"
b "It's you. You're the last piece."
b "That's how this kind of magic works. We eat and we grow, and when we're big enough we eat you--{nw}"
p "Wha--"
b "--we eat{fast} just the version of you that exists in this world,{nw}"
if optimism < 0:
    extend "the world you hate. Where you're depressed, alone, anxious."
else:
    extend "the world you were born into. Where you've lived up to this point."
b "And with your energy, your life force, and your wish, we stitch a new world into being. One that gives you what you deserve. [deepest_desire] with the love of your life: [boyfriend_description]."
p "..."
b "I know. I know that it's a lot. I know you might not trust me. So if you don't want me to make your wish, you don't have to. It's up to you."
p "Why didn't you tell me this sooner? Why now?"
b "I thought there would be a better time. I thought I would get to grow slower, and I--"
if boyfriend == "foxglove":
    "It sighs from its many mouths all at once. An echoing rush."
else:
    "It sighs despite having no mouth. A whistle of breath from nowhere."
b "I've liked my time with you. I didn't want to scare you ... more than I do."
if optimism < 6:
    $ skeptical_comment = True
elif brains > 2:
    $ skeptical_comment = True
else:
    $ skeptical_comment = False
menu:
    "I liked it too, for what it's worth" if (optimism > -2):
        $ optimism += 5
        p "It's been strange, but. It's been a beautiful experience."
        if brains > 2:
            p "I guess I kinda knew you were some kind of unearthly creature the whole time."
            p "There were definitely warning signs ..."
        p "It's been really cool to watch you grow, and honestly I needed the company."
        "You see your [boyfriend]'s anxiety soothe, just a little."
        if boyfriend == "foxglove":
            "His flowers perk up, some of the lips quirk with little smiles."
        elif boyfriend == "orb":
            "The orb shines brighter again."
        else:
            "Your gazes finally meet."
    "Is there anything else you aren't telling me?" if skeptical_comment:
        $ optimism -= 2
        $ brains += 2
        b "..."
        p "Please. At this point all you've done is hide things from me."
        b "I don't think I should."
        extend " This won't help you, and it wouldn't be fair."
        p "I don't care. I want to know what I'm choosing before I choose for once."
        b "I guess I owe you that much at least ..."
        b "Today, either I grant your wish and bloom, or ..."
        p "Or?"
        b "Or I die. Or my body consumes itself, and I fade from this world."
        p "...{nw}"
        p "Oh."
        if boyfriend == "thistle":
            "His big eyestalk droops."
        elif boyfriend == "orb":
            "The orb's light wavers."
        else:
            "His many heads droop."
        b "I didn't want you to know. I want you to choose as you wish. That's what I was cultivated to give you."
b "I'm sorry, but time is up now."
b "I can feel the new world starting to bloom inside me. You need to choose. Your life here, or your wish?"
menu:
    b "Your life here, or your wish?{fast}"
    "Your life here" if (optimism > -5):
        scene black with dissolve
        "You're pulling weeds from the neglected plot in the shared garden of your building."
        "You toss the unwanted plants to a pile by your side, to be composted back into nutrients for your garden."
        "Even though your [boyfriend] has only been gone a few weeks, most things are back to normal."
        "The vines and roots that had grown all through your building shriveled back into themselves."
        "The [boyfriend] contracted into something tiny, a mass of roots and old stalks barely larger than your hand."
        "Even the memories of him are leaving. Ms Espera's dog seems to have forgiven you. Even you're forgetting about your [boyfriend] a little more each day."
        "But you have one lesson from your plant boyfriend that you won't let go of."
        "You pull a fresh raspberry from the bush you planted, and take a bite."
        "You know that if you keep a seed safe, if you feed and protect it as it grows, that its fruit will one day emerge, for you to have and to share with the people around you."
    "Your wish" if (optimism < 10):
        scene black with dissolve
        "You're picking strawberries from a bush in your garden, as he waters the flower beds."
        "You take a bite of one, and with a mischievous smile you flick the leafy top at him."
        "It bounces off his cheek, leaving a sweet red stain."
        "He drops the watering can and charges at you, sending the two of you rolling in the grass, smiles unremovable from your faces."
        "This is just like how you met, you think."
        if (optimism < 5) OR (brains > 3):
            "Though if you think about it, you can't remember how you met."
        "As you spin, the two of you are constant, the center of all that exists."
        "Finally, your greatest desire."
scene aquarium with fade
"..."
ARE "Thank you so much for playing the demo version of Carnivorous Plant Boyfriend!"
ARE "This game was created in Ren'Py as an entry to the 2026 Trans Representation Game Jam."
ARE "The concept was created by Aaron El Sabrout and Rhys Maxwell."
ARE "Rhys wrote the script and created the minigame. Aaron did the art, Ren'Py programming, and some editing/additional writing."
ARE "We hope you find your greatest desire ... if it's actually good for you!"
$ chapter = 7
jump start
