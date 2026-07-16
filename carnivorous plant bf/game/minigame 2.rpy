init -1 python:

    # need some imports
    import random, pygame

    # and some constants
    TOTAL_STARS = 500
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # renpy.pygame does not contain sprite??? not sure how/if that can be fixed :/
    # class PlayerSprite(pygame.sprite.Sprite):

    #     # Constructor. Pass in the color of the block,
    #     # and its x and y position
    #     def __init__(self, image, width, height):
    #     # Call the parent class (Sprite) constructor
    #         pygame.sprite.Sprite.__init__(self)

    #         # Create an image of the block, and fill it with a color.
    #         # This could also be an image loaded from the disk.
    #         self.image = pygame.image.load("images/images.jpg")

    #         # Fetch the rectangle object that has the dimensions of the image
    #         # Update the position of this object by setting the values of rect.x and rect.y
    #         self.rect = self.image.get_rect()
    # C:/Users/rmaxw/OneDrive/Documents/Carnivorous Plant Boyfriend/renpy-8.5.3-sdk/carnivorous-plant-bf/carnivorous plant bf/game/images

    class Player(object):
        color = (255,0,0)
        position = [0,0]
        speed = 1

        def __init__(self):
            self.position = [SCREEN_WIDTH/2,SCREEN_HEIGHT/2]
            # with open(os.path.join(sys.path[0], "game\\images\\bmp_24.bmp"), "r") as file:
            #     player_img = pygame.image.load_basic(file)
            # player_img = pygame.image.load("game\\images\\bmp_24.bmp")

        def update(self):
            keyinput = pygame.key.get_pressed()
            if keyinput is not None:
                if keyinput[pygame.K_LEFT]:
                    self.position[0] -= self.speed
                elif keyinput[pygame.K_RIGHT]:
                    self.position[0] += self.speed

        def draw(self, canvas):
            xpos = int(self.position[0])
            ypos = int(self.position[1])
            canvas.rect(self.color, pygame.Rect(xpos, ypos, 100, 100))

    # and the Star class
    class Star(object):
        color = (0,0,0)
        position = [0,0]
        speed = 1

        def __init__(self):
            self.generateStartPosition(xrandom=True)

        def generateStartPosition(self, xrandom=False):
            # start at right of screen, scroll left
            if xrandom:
                xpos = random.randint(1, SCREEN_WIDTH - 1)
            else:
                xpos = SCREEN_WIDTH - 1
            self.position = [xpos, random.randint(1, SCREEN_HEIGHT - 1)]
            brightness = random.randint(1, 255)
            self.color = (brightness, brightness, brightness)
            self.speed = float(brightness / 400.0)

        def update(self):
            self.position[0] -= self.speed
            if(self.position[0] < 0):
                # generate new star
                self.generateStartPosition()

        def draw(self, canvas):
            xpos = int(self.position[0])
            ypos = int(self.position[1])
            canvas.rect(self.color, pygame.Rect(xpos, ypos, 0, 0))

    # now we add out own custom Displayable
    class StarDisplay(renpy.Displayable):
        def __init__(self, *args, **kwargs):
            super(StarDisplay, self).__init__(*args, **kwargs)
            self.stars = [Star() for x in range(TOTAL_STARS)]
            self.player = Player()

        def render(self, width, height, st, at):
            """Called when renpy needs to get the image to display"""
            # make a screen to draw on
            screen = renpy.Render(SCREEN_WIDTH, SCREEN_HEIGHT)
            canvas = screen.canvas()
            # fill with black and then put our stars on
            canvas.rect((0,0,0), pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            for star in self.stars:
                star.draw(canvas)
                star.update()

            self.player.draw(canvas)
            self.player.update()

            # just drawing once if not good enough. Tell Renpy to call this function again as soon as possible.
            renpy.redraw(self, 0)
            # now we just have to return this render
            return screen

        def visit(self):
            """This function needs to return all the child displayables.
               We have none, so just return the empty list."""
            return []

# we need the displayable to be attached to a screen
screen star_screen:
    add StarDisplay()

label minigame2:
    # now we need to add the display to the background of our game
    show screen star_screen
    "This is our test game"