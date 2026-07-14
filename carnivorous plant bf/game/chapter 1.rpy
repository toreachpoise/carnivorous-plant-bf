label chapter1:
  # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene greenhouse bg

    "The tagline on the sign says 'Grow your wishes!'"
    "The exterior is overgrown with ivy."

    ARE "scene transition to interior plant shop"

    "The shop interior is messy."
    "There are straggly and overgrown plants under hot pink artificial lights all over the room."
    menu:
        "Look at the plants":
            "The shop is tiny. You can hardly see into it from all the shelves and tables crammed with plants."
            "You look at one table, with a bunch of smaller plants crammed on it. They're all in different shaped pots, some of them clearly spraypainted plastic food containers."
            "There's something off about the plants themselves ..."
            menu:
                "Look closer":
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
    ARE "here is where it will progress to the witch part"


return
