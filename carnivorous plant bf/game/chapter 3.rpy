# ARE: out of sheer laziness I'm just writing this directly into github on browser I'm sure it will be buggy as all fuck

label chapter3:
scene living room dark
with dissolve
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

if boyfriend == "flytrap":
    show flytrap
    "Your [boyfriend]'s leaves remain furled. The heads no longer seem to be dancing and are kind of downcast."
if boyfriend == "spider":
    show spider
    "Your [boyfriend]'s leaves remain furled. Most of its eyes are closed or look drowsily off at the walls."
if boyfriend == "foxglove":
    show foxglove
    "Your [boyfriend]'s leaves remain furled. The lips on each of their blossoms aren't as shiny anymore, they're dull and chapped looking now."
if boyfriend == "thistle":
    show thistle
    "Your [boyfriend]'s leaves remain furled. The thorns are still as sharp but the big eyestalk is drooping somewhat."
if boyfriend == "orb":
    show orb
    "Your [boyfriend]'s leaves remain furled. The fleshly leaves look a little pruney, and you could swear the orb is a little smaller."

p "I guess I should figure out how to take care of this little guy, huh?"
p "Maybe I should take a look at the instructions that Witch gave me ...{nw}"
menu:
    p "Maybe I should take a look at the instructions that Witch gave me ...{fast}"
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
if ((location == "none") or (light == False) or (water == False)):
    p "So the basic things a plant needs are ...{nw}"
    menu:
        p "So the basic things a plant needs are ...{fast}"
        "Soil." if (location == "none"):
            p "I guess he's already in a pot."
            p "Maybe let's just find him a place to live."
            if optimism < 5:
                extend " ... somewhere in this mess."
            "You take a second to survey the architecture of your apartment, if it can be called architecture."
            if light == False:
                scene living room dark
            else:
                scene living room light
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
                        if light == False:
                            scene kitchen dark
                            with dissolve
                        else:
                            scene kitchen light
                            with dissolve
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
                        $ location = "kitchen"
                        jump plantsetup
                    "on the dining table kinda near the balcony":
                        if brains >= 0:
                            $ brains += 1
                        "The plant seems to get lighter in weight the closer you get to a window, and heavier the further you bring it into the murk of the room."
                        p "So, yeah. It wants to be near a window obviously."
                        scene table light
                        with dissolve
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
                        $ location = "dining"
                        jump plantsetup
        "Light." if (light == False):
            p "My boyfriend definitely needs light."
            "The two main windows in your house are in the kitchen and the dining area at the end of your living room."
            if optimism < 0:
                scene bedroom
                with dissolve
                "Your bedroom is a windowless box barely large enough for your bed ..."
            scene table dark
            with dissolve
            "When you open the curtains by your dining table you're almost blinded."
            "Outside the sun is setting, and as your eyes adjust you realize you've never noticed how nice the view of the sunset is here."
            "You pull open the windows, in case fresh air is also a thing plants need."
            "Your [boyfriend] rustles, but it must be the wind."
            $ light = True
            jump plantsetup
        "Water." if (water == False):
            p "I should have gotten a watering can, huh?"
            if light == True:
                scene kitchen light
            else:
                scene kitchen dark
            "You find the least dirty bowl you've got and fill it with tap water."
            "Water splashes over the rim as you carry it over to your plant."
            if location == "none":
                if light == True:
                    scene living room light
                else:
                    scene living room dark
            else:
                if light == True:
                    scene table light
                else:
                    scene table dark
            
            menu:
                "Pour the water.":
                    "You tip the bowl towards the planter and clean water spills over the [boyfriend] in a steady fall, soaking the soil."
                    $ water = True
                    jump plantsetup
else:
    scene table dark
    with dissolve
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
scene kitchen light
### CG??
"Old milk, crumpled foil with trace amounts of butter."
"You spot most of a log of salami, and some lettuce that should be used now, if not yesterday."

label chapter3minigame:
$ chapter = 3.5
"Well, lets get cooking."
jump minigame

label chapter3minigamedone:
scene kitchen light with dissolve
if ch3cut:
    "You drive the knife down, expecting to cut meat, but it knicks your own flesh instead."
    "Your face scrunches as you feel the shock of pain, and the knife slips from your hand."
    "You don't hear it fall."
    "Instead, you hear a rustling of leaves, and a cool wet sensation over your thumb."
    if boyfriend == "flytrap":
        show flytrap
    if boyfriend == "spider":
        show spider
    if boyfriend == "foxglove":
        show foxglove
    if boyfriend == "thistle":
        show thistle
    if boyfriend == "orb":
        show orb
    "As you open your eyes, you see {i}him{/i} suckling at your wound like it's sweet ambrosia."
    if boyfriend == "flytrap":
        "Despite the sharpness of its teeth, it scoops the liquid into one of its jaws gently."
    if boyfriend == "spider":
        "Its leaves funnel the blood into its eye, which blinks up the blood. Like crying in reverse."
    if boyfriend == "foxglove":
        "The lips are as plush and tender as you imagined."
        "You can't help but imagine how they would feel on other parts of your body."
    if boyfriend == "thistle":
        "Its thorns funnel the blood into its eye, which blinks up the blood. Like crying in reverse."
    if boyfriend == "orb":
        "The drops are drawn magically from your fingers into the air."
        "They swirl about the orb and then become absorbed into it."
    jump alittlemore
else:
    "Your finished sandwich is nothing special, but it was made with care."
    "You approach the plant with it feeling ..."
    extend " nervous? Ridiculous? Both?"
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
    "You try to offer the sandwich to the [boyfriend] on your open palm."
    "..."
    "There's no motion, and now you are certain you just feel ridiculous."
    "You sigh."
    "You sigh {fast}and then it snaps."
    if boyfriend == "spider":
        "Its sharp leaves claw into you.{nw}"
    if boyfriend == "thistle":
        "Its flowerhead thuds into you.{nw}"
    if boyfriend == "orb":
        "A ray of white-hot light shoots out from the orb.{nw}"
    else:
        "Teeth on your fingers. Sharp teeth. Wooden teeth.{nw}"
    extend " Tearing into your offering and your hand like they're one and the same."
    $ fed_plant += 5
    jump alittlemore


label alittlemore:
b "Please, just a little more.{nw}"
menu:
    b "Please, just a little more.{fast}"
    "What, no!":
        "You shove his green fibrous flesh back."
        "After a little resistance he releases you, and shifts back sheepishly."
        jump ch3end
    "Indulge him":
        if ((boyfriend == "spider") or (boyfriend == "flytrap") or (boyfriend == "thistle")):
            "Your eyes meet his, and you give the slightest nod."
        else:
            "Your eyes meet what answer for his, and you give the slightest nod."
        $ fed_plant += 5
        "This time he siphons the warm blood straight from your veins."
        "The [boyfriend] grows greater in strength with each drop."
        "You feel like you can hear his roots growing deeper and stronger as his complexion takes on a deeper green."
        jump ch3end

label ch3end:
b "Fuck, sorry, thank you, wow."
p "..............................."
b "Oh, that sandwich also looks good. Is that for me?"
b "I'm so hungry ..."
p "......"
extend " Uh, yeah, that was the idea I guess ... here."
if boyfriend == "flytrap":
    "He descends on it with all for mouths, snapping it up instantly."
if boyfriend == "spider":
    "His hands snatch the sandwich up, tearing it to bits and disappearing it down his many throats."
if boyfriend == "foxglove":
    "He inhales with such force with each mouth that the sandwich is shredded through each set of lips."
    "You see the fragments travel down each of its tubular throats for a moment before it vanishes."
if boyfriend == "thistle":
    show thistle with vpunch
    show thistle with vpunch
    show thistle with vpunch
    "He smashes and smashes and smashes it into bits and blinks the crumbs into his great eye."
if boyfriend == "orb":
    show orb with vpunch
    "The orb emits a brilliant flash."
    "As your eyes adjust afterwards, the sandwich is gone, eroded without a trace."
$ fed_plant += 5
b "That was delicious, wow."
b "The witch only gave us these brown crunchy things. I couldn't read the bag, but there was a dog on it..."
p "I'm glad you enjoyed ... ah ... haha ..."
p "... Sorry, am I being weird?"
p "I'm super freaked out."
b "It's okay, this is all pretty weird."
extend "... But I'm glad I'm here!"
b "You've been doing a really good job with me so far."
p "That's uhm, that's good."
p "Let me know if you need anything else. I wanna keep doing a good uhm, doing good for uh, ... yeah ..."
if boyfriend == "flytrap":
    "All four heads look at you with all twelve of his eyes."
if boyfriend == "spider":
    "All of its hands point its eyes toward you."
if boyfriend == "foxglove":
    "Each mouth wears an earnest grin as he speaks."
if boyfriend == "thistle":
    "Its eye meets yours and you notice the gooey swirls of plasma around his pupil in part to avoid the intensity of his gaze."
if boyfriend == "orb":
    "The orb bathes the room in warm orange light."
b "You will. I know you will."
b "And I can't wait to be [boyfriend_description] for you."
b "It was really nice to meet you, [player_name]."
b "I need to rest now, though. I'll get stronger the more you feed me, but for now I need rest ..."
p "Oh, okay, I'll go to my room then."
b @ vpunch "Wait!"
extend " Stay. Or take me with you."
b "I'd just like to be near you if I could ..."
b "I'll be so vulnerable when I rest. I'd feel safer with you."
p "{i}Shit, god that is so cute. {/i}"
extend "{i}But also he did just drink my blood. {/i}"
extend "{i}But but I mean, he's very sweet? Like what's the worst that could happen, right?{/i}"
menu:
    "What if he eats me in my sleep?":
        $ optimism -= 3
        p "Sorry, I have a sleep ... uh"
        extend "... thing, where I like ...{nw}"
        b "Suck at lying? It's fine, I get it."
        b "I'll be here if you change your mind."
        "You give your [boyfriend] a half-smile before stepping into your bedroom and closing the door."
        scene bedroom
        "With a pang of guilt, you carefully place a chair to bar the door. You hope he doesn't hear you. You're pretty sure he does."
        "Sleep does not come easily, but eventually it takes hold and you drift off."
        $ slept_together = False
        scene black with fade
        "..."
        $ chapter = 4
        jump dream2
    "What if it's exactly what I wanted?":
        $ optimism += 2
        p "I'd like that." 
        p "I'd like to make you feel safe, if it would help."
        b "It really, really would."
        scene living room dark
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
        "You bring a blanket and pillow to your couch, it's easier at this point than moving your plant."
        "He shifts toward you as he finds his own comfortable position."
        "Your fingers and his leaves drift together as you both drift off."
        "..."
        scene black with fade
        $ slept_together = True
        $ chapter = 4
        jump dream2

label dream2:
$ dreamstonight.build()
$ dreamstonight.shuffle()
$ dreamer.draw(dreamstonight, 1)
$ this_dream = dreamer.dreams[2].show()
"[this_dream]"

jump startmenu

