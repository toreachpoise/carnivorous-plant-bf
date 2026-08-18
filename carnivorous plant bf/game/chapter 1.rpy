label chapter1:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene plant store exterior 2

    "The tagline on the sign says 'Grow your wishes!'"
    "The exterior is overgrown with ivy."

    scene greenhouse 1
    with dissolve

    "The shop interior is messy."
    "There are straggly and overgrown plants under hot pink artificial lights all over the room."
    menu:
        "Look at the plants":
            "The shop is tiny. You can hardly see into it from all the shelves and tables crammed with plants."
            "You look at one table, with a bunch of smaller plants crammed on it. They're all in different shaped pots, some of them clearly spraypainted plastic food containers."
            "There's something off about the plants themselves ..."
            menu:
                "Look closer":
                    scene greenhouse 3 with dissolve
                    $ optimism += 1
                    "When you pay attention to the plants, they each seem a bit too ... alive."
                    "I mean, you know plants are alive but they each emanate an energy that both draws you to them and kind of frightens you."
                    "At first you can't really see anything abnormal about them. You're not exactly an expert in plant anatomy."
                    "But then you start to notice oddities."
                    "There's a fiddle leaf fig tree in a gallon pot, each of its deeply lobed leaves is like a hand, the fingers softly waving despite the still hot air."
                    "One of those cacti with a big flower on the end but as you watch the flower slowly opens and closes around ... an eye?"
                "We don't have time for this, where is the shopkeeper?":
                    pass
        "Where is the shopkeeper":
            pass
    p "We don't have time for this, I have to talk to the witch."


    scene greenhouse 2
    show witch blink
    with dissolve
    "Her hair is messy and her long nails are undoubtedly full of dirt."
    "She's beautiful, in a haven't slept in three weeks kind of way."
    "You're not a magic user by any means but you can sense that strange power emanates from her."
    w "Welcome to the Magic Plant Shop(TM), where wishes really do grow on trees. What is your heart's desire?"
    "She doesn't even look up at you. Her voice has the sing-song quality of having delivered this monologue hundreds of times before."
    p "I want ... uh ... a boyfriend ...?"
    show witch neutral
    w "You know you don't have to hire a witch on the black market for that, right? They have men at most bars."
    p "not for me ....."
    show witch blink
    w "Ouch. Well, it's your eternal soul I guess."
    "She grabs a piece of paper from under the desk."
    show witch writing
    w "... a boyfriend ..."
    extend "can you describe this boyfriend please?"

label boyfrienddescription:
    python:
        boyfriend_description = renpy.input("What do I want in a boyfriend?")
        boyfriend_description.strip()
        if boyfriend_description == "":
            optimism -= 1
            boyfriend_description = "I don't know ... someone who is nice and makes me feel good, I guess?"
            no_bf_description = True
        else:
            optimism += 1
            no_bf_description = False
    p "[boyfriend_description]"
    if no_bf_description == True:
        show witch writing disgusted
        w "Wow ... Have you just not put any thought into it or what?"
        w "Seems like if you want to meet someone it would be good to know what kind of person you want to meet."
        p "Look, I just, I don't know how to describe it."
        extend " I don't have a lot of experience with these things ..."
        show witch writing
        w "Damn."
        menu:
            " ... That's all she has to say? She's kinda ..."
            "hard to read":
                pass
            "an asshole":
                pass
    else:
        show witch writing disgusted
        w "Well, I guess people like to stick their bits into and/or have their bits invaded by all sorts of things ..."
    if name_set == True:
        jump signcontract
    show witch writing
    w "So what's your name, anyway, for the contract?"
    " ... Contract?"
label namesetting:
    python:
        player_name = renpy.input("What do I tell her my  name is?")
        player_name.strip()
    if player_name == "":
        $ optimism -= 1
        w "... no response?"
        extend "... okay, I guess I'm gonna put 'nameless weirdo'."
    else:
        w "[player_name]?"
        extend " I highly doubt that's your government name, but if that's what you want to go with ...?"
    menu:
        "Is that what you want to go with?"
        "Yep, my name is [player_name]":
            $ optimism += 1
            jump nameset
        "Wait, no, I want to change it ...":
            $ optimism -= 1
            w "Yeah, that's what I thought."
            w "It doesn't really matter anyway, your soul has astrological coordinates that will be bound to your new boyfriend anyway,{w} but I have to put something on the form ..."
            jump namesetting

label nameset:
    $ name_set = True
    "Her tone becomes weirdly official again."
    show witch robo
    w "Now remember, like I told you before. You'll have to feed and water your boyfriend for as long as you live."
    "She didn't say that before, but like, isn't that true of most plants?"
    "Wait, as long as *I* live?"
    show witch neutral
    w "This is a till-death-do-us-part situation. He's going to love you forever whether you like it or not."
    w "And remember, you have to feed him."
    "Why does she keep saying that?"
    w "Okay, and just to reiterate though I would rather not cuz I find it a bit sad, you described your dream boyfriend as, and I quote, '[boyfriend_description]', end quote. Is that right?"
    menu:
        "Is that who you want to spend the rest of your life with until your death do you part? '[boyfriend_description]'?"
        "W-wait, no ...":
            p "Wait, sorry, I actually changed my mind."
            $ optimism -= 1
            w "Fuck, kids these days can't even describe their undying lover whom they want to care for for all eternity in one sentence anymore ..."
            jump boyfrienddescription
        "Yes. I'm sure.":
            p "After all, what choice do I have?"
            p "Otherwise I'll be alone forever."
            jump signcontract

label signcontract:
    w "Okay. {nw}"
    show witch reaching blink
    extend " ... "
    show witch reaching
    extend "Sign at the bottom."
    window hide
    show witch reaching blink
    w "Okay, well, good luck."
    show witch disgusted
    w "Since you apparently just want to fuck the plant, I guess you can go to the greenhouse and pick one out yourself."
    w "You can leave through the back door of the greenhouse."
    "She clearly doesn't want to see you again ..."
    w "And don't try taking two. I can see you on the security camera ... and you honestly couldn't handle it."
    w "Oh, and here's the manual."
    show witch reaching
    extend " Please be sure to read it thoroughly, your life depends on it!"
    w "Thank you for coming to the Magic Plant Shop, please give us a good review on Boogle Maps~!"
    $ chapter = 2

jump start


