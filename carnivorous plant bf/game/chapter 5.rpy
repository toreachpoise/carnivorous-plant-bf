label chapter5:

scene apartment entrance with fade
scene apartment entrance overgrown with dissolve
"You come up on your apartment building, its exterior now overgrown with grasping vines and reaching roots."
"The snaking greenery seems to be centered on the window of your basement apartment."
"As you approach the door, a root coils around your leg like a constrictor, stopping you."
"It bites into your leg, too tight at first before loosening."
"Your [boyfriend]'s voice is far more resonant than before, emanating from deep inside your apartment."
b "Oh! You're back. Sorry, um, I just need a second~!"
menu:
    "What have you done to my house??":
        "There is silence for a moment from behind the door."
    "Push through the door":
        "You shake free of the grip on your ankle."
        "There are vines gripping the door like gnarled fingers."
        "As you grasp the doorknob and try to pull the door open you feel the vines contract and pull the door back in."
        b "Wait!!! Just wait!"
        "Its voice is singsongy, but unearthly and terrifying."
    "Wait?":
        "You patiently wait."
"Inside you hear something cry out. It sounds like a small animal. In fact, it sounds like your neighbor's little scotty dog."
p "Is that my neighbor's dog?? What's wrong with you?"
b "Please!! I need it! I Need It! I NEED IT NOW!"
"His voice shakes the windows as he bellows."
"You throw yourself against the door. Your shoulder twinges with pain but otherwise you achieve nothing."
"You go again, and again as the dog's panicked yelps grow louder."
"Finally, you crash through the door, tearing against the vines and roots and exposing the verdant tangle that has overtaken your apartment."
scene living room overgrown
with pushright
if boyfriend == "flytrap":
    show flytrap at midright with dissolve
if boyfriend == "spider":
    show spider at midright with dissolve
if boyfriend == "foxglove":
    show foxglove at midright with dissolve
if boyfriend == "thistle":
    show thistle at midright with dissolve
if boyfriend == "orb":
    show orb at midright with dissolve
show captured dog at left
"In the center of the thicket, struggling against a knot of plant material, is your neighbor's dog. Extending over it is your plant, poised to kill."
"He pretends to notice you casually."
b "Heyyyyyyyyy ...."
p "What? Don't you 'hey' me! What the fuck is happening?? What is all this?"
b "Well ... when I eat I get bigger ..."
p "I can see that."
b "And the bigger I get, the hungrier I get ... And this meat thing was barking outside ... So I thought, why wait for breakfast?"
p "YOU CAN'T JUST KILL MY NEIGHBOR'S DOG??"
b "....... Why?"
p "Wha- Be-Because he belongs to my neighbor?"
b "He can get another one, right?"
p "No, she, look, she loves that dog. I love that dog. You know how that feels, right?"
"Your [boyfriend] looks ashamed, drooping a little."
"He doesn't let go of the dog, though."
menu:
    p "Just put down the dog and ..."
    "I'll make you something":
        "You proffer the impossibly small feeling bag of groceries."
        p "Look, I went to the grocery store to buy you food. I can have it ready in just a minute."
        p "Okay quick breakfast let's do it."
        jump minigame
    "You can have some of my blood":
        p "Look, if you really can't wait, take me instead. You can have a drink, and this fluffy guy will get to live."
        "Roots and vines lift you before you know what's happening and carry you to face your [boyfriend], although it's hard to feel like you're the owner now."
        if boyfriend == "flytrap":
            "All four heads lean in and bite you across your neck, thighs, and back."
            "They drink greedily until you feel lightheaded."
        if boyfriend == "spider":
            "The sharp claws dig into you and siphon your blood."
            "Each eye stares into yours as you feel yourself being sapped away."
        if boyfriend == "foxglove":
            "Every mouth leans in and sucks againsts your skin, small spiked tongues prick your flesh so that you can be bled."
            "They drink greedily until you feel lightheaded."
        if boyfriend == "thistle":
            "His fanged mass presses against your neck, digging into your flesh."
            "He drinks greedily until you feel lightheaded."
        if boyfriend == "orb":
            "Brilliant light overwhelms everything you can see."
            "You feel your mind fade, as memories of anything but this moment are pulled out of your conscious mind."
        $ ch5cut = True
        b "THANK YOU, oh my god thank you."
        b "You're still gonna make breakfast though, right?"
        p "Are you fucking kidding me?"
        jump minigame

label chapter5minigamedone:
"The [boyfriend] inhales the first few bites of your breakfast."
"It's clearly a great act of will when it slows down to properly enjoy the rest of it, to savor your work."
"As each bite is absorbed to his satisfaction, the vines around the little puppy loosen, and he's left shaking but free."
"The vines around the room retreat as well, allowing you to pick up the dog."
"You offer them some reassuring pets, though they honestly seem frightened of you at this point."
scene outside dark with wipeleft
"You take the dog outside and return them to the pen your upstairs housemate has for them in your shared yard."
scene living room overgrown with wiperight
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
"You step back inside. Your apartment is in disarray. The vines have eaten through your furniture and walls alike."
"In the center of it is your [boyfriend]."
if boyfriend == "flytrap":
    "Four sets of eyes look back at you, each looking more apologetic than the last."
if boyfriend == "spider":
    "Many eyes, most able to meet your gaze, but some just sheepishly looking down."
if boyfriend == "foxglove":
    "Each of its mouths no longer tempting, but threatening. Most in various stages of a regretful frown."
if boyfriend == "thistle":
    "A single forlorn eye meets your gaze, fangs subtly retracted."
if boyfriend == "orb":
    "The orb grows more softly, cooler in color, with a warbling shape."
    "You can sense regret from it somehow, like it's beaming the feeling into your mind."
b "I don't know what it's worth, but I'm sorry."
b "I get so hungry ... That's not an excuse but. It is my nature."
b "I get hungry, and I grow, and when I get big enough I can do impossible things."
b "I'd like to show you one of those impossible things, if you'd like. Would that be okay?"
if ch5cut: 
    $ skeptical_comment = True
if optimism < 5:
    $ skeptical_comment = True
if skeptical_comment:
    p "How do I know I can trust you? I'm still bleeding from the last wounds you gave me."
    b "I know. Please. Just let me help ..."
"A thin vine caresses over your wounds, spreading a glowing balm that tingles against your flesh. Bruises fade. Cuts seal themselves. Your pain is gone."
b "Just a glimpse of what I can do. It will be so much more when I'm bigger."
b "I'd like to show you what I've been working on for you."
b "You have a good wish, I want it to come true."
b "When I'm strong enough, I'll make it real for you."
"A vine caresses your head, stroking your cheek before covering your eyes."
scene black
"Instead of darkness, you see light."
"You see the light of the sun reflected on dew drops in a garden."
"It's your garden, yours and his."
"You can see him now. Smiling at you, [boyfriend_description]. The sunlight gleaming off him."
"He's pulling fresh baby tomatoes from the plants you grew together to make you an omelette."
"You are warm, you are safe, and you are loved."
scene living room overgrown with fade
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
"You blink and the vine has pulled away from your eyes, leaving you back in your destroyed apartment."
b "That ... took a lot out of me, just to show you."
b "I'm not strong enough to make a world yet, but I'm close. I only need a bit more."
b "I think I can be ready tomorrow, if you are."
b "But now? I need to rest."
p "{i}He's looking at me expectantly ... I guess he wants to know if I'll sleep by him, but he's nervous to ask?{/i}"
menu:
    "sleep with the plant":
        $ slept_together = True
        $ optimism += 5
        p "Yeah, it's been a big and uh ... confusing day for sure. I wouldn't mind lying down on the couch near you too."
        "Every fiber of your plant seems to let out a tension it was carrying. The roots settle their wriggling into a gentle breathing pulse around the room."
        "As you drift off together, your fingers and his roots entangle in each other."
    "don't":
        $ optimism -= 5
        $ slept_together = False
        p "I'm. Um. I'm not really tired. Kinda buzzing actually."
        p "I'll be in my room but ... I'll see you in the morning."
        b "Oh. Okay, cool. Good night."
        "It's voice is booming, but clipped. Disappointed. It turns away from you."
        p "Good night."
        scene bedroom with wiperight
        "You go to your room, trying not to turn your back on it the whole time."
        p "......"
        p "What have I done?"
"..."
$ chapter = 6
jump start
        
