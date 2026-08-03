# ARE: out of sheer laziness I'm just writing this directly into github on browser I'm sure it will be buggy as all fuck

label chapter3:
scene apartment
### bg apartment
"Your apartment. Dishes in the sink, mold in the dishes."
"A trail of clothes leads continuously from the front door to the bed, then the bathroom."
extend " All yours, of course."
"You'd say this place has seen better days, but you can't actually recall any."
"The closed curtains are nearly a public service."

p "Look, I haven't brought anyone home ... {nw}"
menu:
    p "Look, I haven't brought anyone home ...{fast}"
    "in a while ...":
        pass
    "ever, actually.":
        pass


"Your [boyfriend]'s leaves remain furled.{nw}"
if boyfriend == "flytrap":
    show flytrap
    "Your [boyfriend]'s leaves remain furled. {fast}The heads no longer seem to be dancing and are kind of downcast."
if boyfriend == "spider":
    show spider
    "Your [boyfriend]'s leaves remain furled. {fast}Most of its eyes are closed or look drowsily off at the walls."
if boyfriend == "foxglove":
    show foxglove
    "Your [boyfriend]'s leaves remain furled. {fast}The lips on each of their blossoms aren't as shiny anymore, they're dull and chapped looking now."
if boyfriend == "thistle":
    show thistle
    "Your [boyfriend]'s leaves remain furled. {fast}The thorns are still as sharp but the big eyestalk is drooping somewhat."
if boyfriend == "orb":
    show orb
    "Your [boyfriend]'s leaves remain furled. {fast}The fleshly leaves look a little pruney, and you could swear the orb is a little smaller."

p "I guess I should figure out how to take care of this little guy, huh?"
p "Maybe I should take a look at the instructions that Witch gave me ...{nw}"
menu:
    p "Maybe I should take a look at the instructions that Witch gave me ..."
    "Take a look":
        ### cg???
        $ brains += 1
        "The instruction sheet got wet when the sprinklers went off in the greenhouse."
        "The ink has bled so you can't read the little text there was printed on there."
        "You can kind of make out the simple illustration on the front page though."
        "There's a tree growing wads of cash ... I guess they make different assumptions about what you'd wish for."
        "There's a cartoon sun in the top corner of the drawing shining on the money tree."
        extend " It's in dirt obviously."
        extend " And someone is watering it."
        p "I mean it's a plant, right? That seems pretty basic."
        jump plantsetup
    "Nah":
        $ optimism += 1
        p "He's a plant, I know how to handle plants, right?"
        jump plantsetup

label plantsetup: 
if ((soil == False) or (light == False) or (water == False)):
    p "So the basic things a plant needs are ...{nw}"
    menu:
        p "So the basic things a plant needs are ...{fast}"
        "Soil." if (soil == False):
            p "I guess he's already in a pot."
            p "Maybe let's just find him a place to live."
            if optimism < 5:
                extend " ... somewhere in this mess."
            "You take a second to survey the architecture of your apartment, if it can be called architecture."
            "Directly in front of you is your couch and the coffee table. To the right are doors leading to your bedroom and the bathroom."
            "To the left is the kitchen with a large window over the counter. Beyond the couch is your dining table, and further is a screen door to the balcony."
            label locationselect:
                menu:
                    p "Where should I put my plant boyfriend?"
                    "on the coffee table?":
                        $ brains -= 1
                        "We would definitely hang out lots if I put my [boyfriend] here, since it's by the couch."
                        "The coffee table is kinda far from the windows though ..."
                        menu:
                            p "Is this the spot?" ## in this case it can't be selected as it's the worst spot
                            "I'm sticking with it ...":
                                $ optimism += 1
                                pass
                            "Nah, this spot isn't great.":
                                $ optimism -= 1
                                pass
                        p "I gotta choose somewhere else I think. Even with the curtains open the light won't reach here."
                        jump locationselect
                    "right by the window in the kitchen":
                        if brains >= 0: #checks if you chose the wrong option first lol, this will only work once
                            $ brains += 3
                        else:
                            $ brains += 1
                        "This feels like the right spot immediately."
                        "It's as if the [boyfriend] gets lighter in his pot and visibly more perky as you bring him near the window."
                        "You have to clear a bunch of dirty dishes off the counter and into the sink to place him right beside the window."
                        if light == False:
                            "The [boyfriend] would probably be even happier if the blinds were open ..."
                        "You step back to admire your handiwork."
                        p "There, if nothing else this place looks a bit more like a house with a plant in it now."
                        "And you'll do the dishes ... later ..."
                        $ soil = True
                        jump plantsetup
                    "on the dining table kinda near the balcony":
                        if brains >= 0:
                            $ brains += 1
                        "The plant seems to get lighter in weight the closer you get to a window, and heavier the further you bring it into the murk of the room."
                        p "So, yeah. It wants to be near a window obviously."
                        "Your dining table is more like a desk; you rarely eat there."
                        "At one end of the table is your computer setup."
                        if optimism > 5:
                            "At the other end of the table are the beginnings of several craft projects you're excited about."
                        else:
                            "At the other end of the table are the remains of several abandoned craft projects."
                        "You clear some room on the side of the table near your balcony screen doors."
                        "You step back to admire your handiwork."
                        p "There, if nothing else this place looks a bit more like a house with a plant in it now."
                        if light == False:
                            "The [boyfriend] would probably be even happier if the curtains were open ..."
                        $ soil = True
                        jump plantsetup
        "Light." if (light == False):
            p "My boyfriend definitely needs light."
            "The two main windows in your house are in the kitchen and the dining area at the end of your living room."
            if optimism < 0:
                "Your bedroom is a windowless box barely large enough for your bed ..."
            "When you open the curtains by your dining table you're almost blinded."
            "Outside the sun is setting, and as your eyes adjust you realize you've never noticed how nice the view of the sunset is here."
            "You pull open the windows, in case fresh air is also a thing plants need."
            "Your [boyfriend] rustles, but it must be the wind."
            $ light = True
            jump plantsetup
        "Water." if (water == False):
            p "I should have gotten a watering can, huh?"
            "You find the least dirty bowl you've got and fill it with tap water."
            "Water splashes over the rim as you carry it over to your plant."
            menu:
                "Pour the water.":
                    "You tip the bowl towards the planter and clean water spills over the [boyfriend] in a steady fall, soaking the soil."
                    $ water = True
                    jump plantsetup
else:
    "You admire your handiwork. Your [boyfriend] plant looks lovely in his little pot, casting a long shadow through the orange sunset glow that now fills the room."

p "Well, he looks nice I guess ..."
if optimism < 0:
    extend " It would be great if he could tell me if I'm doing any of this right ..."
p "Guess I'm done with these instructions."
"You go to toss them in the trash, before deciding that since he's a plant, maybe your new boyfriend would like you more if you recycled the pamphlet."
"As you drop it in the blue bin under the sink, you notice the waterlogged drawing on the backside."
"This image seems to show another money tree, being offered something ..."
p "Is that ... a steak?"
p "Okay, sure I guess it would be romantic to go out to eat together at some point or whatever."
p "For now though, let's see what's in the fridge."
### CG??
"Old milk, crumpled foil with trace amounts of butter."
"You spot most of a log of salami, and some lettuce that should be used now, if not yesterday."

label chapter3minigame:
menu:
    "try minigame?":
        jump minigame
    "skip":
        pass



