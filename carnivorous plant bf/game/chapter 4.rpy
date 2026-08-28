label chapter4:
    if slept_together == True:
        scene living room light with fade
    else:
        scene bedroom
    "You awake to the growling of your stomach."
    if slept_together == True:
        "You rise from the couch and work out a kink out of back as you find your way to your feet, moving gently to not wake your plant."
    else:
        "You pull the covers off and unbar the door."
        scene living room light with dissolve
        "You feel relieved and then a little silly to see that the [boyfriend] has not somehow moved from its perch in the night."
    scene table light
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
    b "Mmh?"
    "He's kinda cute."
    extend " Not really in like a boyfriend way yet, more like a pet way."
    if boyfriend == "flytrap":
        "His little heads are still droopy with sleep."
    if boyfriend == "spider":
        "The eyes blink inside his curled finger-leaves, still dewy with sleep."
    if boyfriend == "foxglove":
        "The tubular flowers waving sleepily, lips dewy even though it's inside."
    if boyfriend == "thistle":
        "His big eye blinks sleepily and the leaves wave softly at you. For a moment his thorns seem less threatening."
    if boyfriend == "orb":
        "The orb shines like the morning sun, his leaves seemingly stretching up toward its warm glow."
    p "Ah, sorry. I was trying not to wake you."
    p "Did you sleep okay? Is that the right word?"
    b "Yesh yea--"
    extend "Sleepem. Hungrem. Brafiss?"
    "Half asleep it seems ... less sentient, less human."
    "He looks sad, a bit forlorn. But still cute."
    extend " And still hungry."
    p "Breakfast?"
    "The [boyfriend] nods, each gentle shake wilting him toward the window."
    scene kitchen light with wipeleft
    p "Huh ..."
    "Your fridge is even more bare than yesterday. Amazing how that happens. A fly emerges from inside as you open it."
    p "Well, I guess I gotta buy something then."
    scene table light with wiperight
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
    p "How about you just keep sleeping, and I'll go get some eggs from the convenience store around the block?"
    b "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    p "..."
    if boyfriend == "foxglove":
        "The snore emanates from all of his mouths. It's so weird."
    else:
        p "{i}How is he snoring without making any noise?{/i}"

    scene outside light with dissolve
    "Gray clouds have kept it cooler than usual outside, enough that morning dew still clings to the ground even as we decidedly have passed the morning."
    "You realize only a few steps into your journey that you forgot to bring a grocery bag."
    scene underpass with wipeleft
    "Ugh, screw it. You can get one more reusable one, right?"
    "You're trying to think of a clever way to describe this to your [boyfriend] when you get home."
    scene alley with wipeleft
    "Some way of framing the irony of buying another, somehow equally disposable but thicker plastic bag to care for your plant."
    show dogtective with easeinright
    show dogtective with hpunch
    "As you're lost in this thought, a large and dangerous looking lady steps into your path."
    d "I'm Dogtective Sasq'ets. I'm a PI. I need to talk to you."
    p "Don't you need a warrant? Or like, probable cause or something?"
    d "That's a cop, dumbass. I'm a PI. That means Private Investigator."
    p "Well, my privates may soon be spoken for, so if you don't mind ..."
    show dogtective at left with move
    "You move to step aside.{nw}"
    show dogtective at center with hpunch
    extend " But she's faster and stronger, and blocks you again."
    d "That's gross but actually what I'm here to talk to you about."
    "Her serious expression softens."
    d "Please, I think you might be in danger."
    p "Wait, danger? What are you talking about?"
    "She hands you a piece of paper. A missing poster."
    d "Look, do you know this girl?"
    p "Hmm, no?"
    p "No, I've never seen her in my life, why?"
    d "She went missing about three weeks back. She's the daughter of someone important, who can afford me."
    d "So I took the case, and I found out she's not the only one who's gone missing around here."
    d "There have been three other disappearances this year."
    p "Is that so? I mean, like, that's awful but I don't see how this has anything to do with--{nw}"
    d "That's not the danger. I followed up on the last known whereabouts for each missing person."
    d "Every single one, within a few days of their disappearance, went to the same shop you visited yesterday. I need to know why."
    p "I, uh ... wow ..."
    p "That's a lot to take in. And thanks for telling me. Um. Did you like, interview the witch though?"
    "Despite her stoic expression you can sense the dogtective is stifling a laugh."
    d "I'm not uh ... pure of heart enough ..."
    p "Pure of heart? The fuck does that mean."
    "She looks away from you."
    d "Dude, she only lets virgins in the shop. Everyone else just sees an abandoned blockbuster video rental place from the outside."
    p "H-hey, wait, you don't know I. I mean. Uhh--{nw}"
    d "Look, we're getting off track. The point is that each of these missing persons went to that shop for some reason."
    d "And then a few days later they disappeared."
    d "Some of them have other reasons they might have disappeared but some didn't. And the shop. I can't explain the shop, and I don't trust what I can't explain."
    p "So what? What do you think I should do?"
    "She hands you a card. It's a little wet in the corner, with indents from her teeth."
    d "I don't know kid, Just take my card and call me if you need help."
    d "If you want to tell me anything I'm all ears too. And remember what we talked about, so if you go missing I can know I at least tried."
    "She's wrapping up the conversation. Maybe she thinks you won't tell her anything."
    "But you want to know more too, what is all of this about people going missing? Is it something to do with the witch? Your boyfriend? It can't be, right?"
    p "Wait, I have some questions ...{nw}"

label doginterview:
    menu:
        p "Wait, I have some questions ...{fast}"
        "Did the missing people have no blood?" if (blood_question == False):
            $ brains -= 1
            d "What? I didn't autopsy them, obviously. Because they're, y'know? Missing?"
            p "... never mind ..."
            $ blood_question = True
            $ dog_questions += 1
            jump doginterview
        "Did the missing people have any weird expenses before they vanished?" if (expenses_question == False):
            $ brains += 1
            d "Hmm ... yeah, actually."
            d "Each person before they disappeared started spending a lot of money on groceries. Like, enough food to host a holiday dinner for 20 people."
            d "And they also each stocked up on first aid supplies shortly before going missing. Specifically bandages and a tourniquet."
            "She trains her eyes on you."
            d "Do you know why they would spend so much money on food and woundcare items before they went missing?"
            p "{i}Should I tell her? I mean ...{/i}"
            if optimism < 3:
                p "{i}If people are going missing that's really scary, right?{/i}"
                if brains > 2:
                    p "{i}And if I'm being honest I feel like I kind of am getting an inkling of how ...{/i}"
                    p "{i}... but ... I feel like I'm starting to love that little plant ...{/i}"
            else:
                p "{i}I love my little [boyfriend]. He's so sweet and weird and cute.{/i}"
                p "{i}Sure the disappearances sound scary but ...{nw}{/i}"
                if brains < 2:
                    extend "{i} it's definitely not a big deal right?{/i}"
                p "{i}It's not like the plants could be responsible for people vanishing ... right?{/i}"
            menu:
                p "Do I tell her? Am I betraying my plant?"
                "I have to":
                    $ brains += 1
                    $ optimism -= 1
                    p "I'm actually on my way to get groceries now."
                    p "The plants from the witch are ... hungry."
                    p "The one I got, it ... he ... bit me last night."
                    d "Shit. That's definitely significant."
                    d "Be careful. I think that she has some way of bonding the plants to people once they've bought them."
                    if brains > 3:
                        p "Like a contract? She made me sign one."
                        d "Yes. Do you have it?"
                        p "No ... it's at home right now ..."
                    d "At any rate, you probably can't stop feeding it now. Otherwise it might decide to eat you."
                    $ expenses_question = True
                    $ dog_questions += 1
                    jump doginterview
                "I can't":
                    $ optimism += 3
                    $ brains -= 1
                    p "Nah, no I was just. I was just wondering. Maybe it's from a true crime show I saw on TV."
                    "She looks at you hard."
                    d "You suck at lying, did anyone ever tell you that?"
                    $ expenses_question = True
                    $ dog_questions += 1
                    jump doginterview
        "Do you believe in risking it all for love?" if (love_question == False):
            $ optimism += 1
            "Her expression becomes puzzled."
            d "I don't know what that means."
            d "But I do know that a worrying number of the cases involved people being obsessed about their romantic entanglements."
            d "Tell me, [player_name], are you lonely? Are you looking for love?"
            show dogtective at lower
            menu:
                "I am alone ...":
                    show dogtective at center
                    $ optimism -= 2
                    p "I live alone. I ride the train alone even though I'm surrounded by people to my box where I work alone."
                    p "I come home alone and I eat alone then I watch TV alone, until I sleep. Alone."
                    p "I feel like I need someone, anyone, to love me or I might die."
                    d "Hmm ... I mean when you put it like that it sounds sad but, isn't that life?"
                    d "Most people are alone most of the time nowadays. I think that's okay."
                "I'm okay":
                    show dogtective at center
                    $ optimism += 2
                    p "I like my neighbors and my coworkers well enough. Especially Ms Espera next door. She brings me food sometimes."
                    p "I try to spend as much time as I can with my friends too, online and in person. We play games. We go swimming in the lake in the summer when we can."
                    p "But they're all busy, y'know? I don't have my Person. The one person my life revolves around."
            p "... Isn't that how it's supposed to be?"
            d "I just don't think love is worth all that, y'know, risking your life for?"
            p "Woof, I mean, isn't that kind of bleak? Without love what is there? Isn't that all we have?{nw}"
            d "BARKBARKBARK BARKBARKBARKBARKBARKBARKBARKBARK barkbarkbark BARKBARKBARKBARK BARKBARKBARK BARKBARKBARKBARKBARKBARKBARKBARK barkbarkbark BARKBARKBARKBARKBARKBARKBARK BARKBARKBARKBARKBARKBARKBARKBARK barkbarBARKBARKBARkbark BARKBARKBARKBARKBARKBARKBARKBARKBARKBARKBARKBARK{nw}"
            "She barks uncontrollably for about a minute before stopping."
            "Now she's gazing off to the side, looking embarrassed."
            p "What the hell was that?"
            d "Sorry ... you said bark. I misread the situation."
            p "..."
            $ love_question = True
            $ dog_questions += 1
            jump doginterview
        "Okay, but like, why are you a dog?" if (dog_question == False):
            d "What are you, a cop? Some kind of speciesist?"
            menu:
                "Sorry":
                    p "I didn't mean to offend you ... my bad ... I just ... never met a talking dog before ..."
                    $ dog_question = True
                    $ dog_questions += 1
                    jump doginterview
        "(Move on)" if (dog_questions > 1):
            if blood_question == False:
                $ brains -= 1
            if expenses_question == False:
                $ brains -= 1

"At last the dogtective steps out of your way."
scene shopping arcade with wipeleft
"You carry on with your gray morning walk, questions dancing in your head as you pick up groceries."
"The wound on your hand is still tender as you walk back home, with your newly purchased grocery bag digging into your grip."
scene underpass with wipeleft
"..."
$ chapter = 5
jump start
