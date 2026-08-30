label dreamsetup:

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

            return "self.contents"


    class DreamBank(object):
        def __init__(self):
            self.dreamlist = []
            self.build()


        #display all cards in the deck
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
                    self.dreamlist[i], self.dreamlist[randi] = self.dreamlist[randi], self.cards[i]

            # you can also use the built-in shuffle method
            # random.shuffle(self, dreamlist)

        def calldream(self):
            if self.dreamlist:
                return self.dreamlist.pop()
            else:
                self.build()
                self.shuffle()
                return self.cards.pop()


    class Player(object):
        def __init__(self):
            self.name = name
            self.dreams = []

        def draw(self, dreambank, num=1):
            for n in range(num):
                dream = DreamBank.calldream()
                if dream:
                    self.dreams.append(dream)
                else:
                    return False
            return True        

