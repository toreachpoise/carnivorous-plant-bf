init python:
    import pygame, random
    FPS = 60
    animationspeed = 3  #fps of the animation will be 'FPS' divided by this number
    #screen = pygame.display.set_mode(window_size, 0, 32)
    display_width = 1920
    display_height = 960
    display = renpy.Render(display_width, display_height)


    class Vector:
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y
        ##math operations for our vectors
        def __add__(self, other):
            if isinstance(other, self.__class__):
                return Vector(self.x + other.x, self.y + other.y)
            return Vector(self.x + other, self.y + other)

        def __sub__(self, other):
            if isinstance(other, self.__class__):
                return Vector(self.x - other.x, self.y - other.y)
            return Vector(self.x - other, self.y - other)

        def __mul__(self, other):
            if isinstance(other, self.__class__):
                return Vector(self.x * other.x, self.y * other.y)
            return Vector(self.x * other, self.y * other)

        def __rmul__(self, other):
            return self.__mul__(other)

        def __truediv__(self, other):
            if isinstance(other, self.__class__):
                return Vector(self.x / other.x, self.y / other.y)
            return Vector(self.x / other, self.y / other)

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.x == other.x and self.y == other.y
            return self.x == other and self.y == other

        def __neg__(self):
            return Vector(-self.x, -self.y)

        def make_int_tuple(self):
            return int(self.x), int(self.y)

        def set(self, vec):
            self.x = vec.x
            self.y = vec.y

    class Sprite():
        def __init__(self, width, height, x, y):
            self.width = width
            self.height = height
            self.position = Vector(x,y)

        def render(self, render, st, at):
            display = renpy.render(self.image, self.width, self.height, st, at)
            render.blit(display, (int(self.position.x), int(self.position.y)))

    class Player(Sprite):
        def __init__(self, width, height, x, y):
            Sprite.__init__(self, width, height, x, y)
            self.position = Vector(x,y)
            # self.position = self.start_position
            self.width, self.height = width, height

            self.image = Image("/images/minigame imgs/Plant-bf-minigame-Knife.png")
            self.slowdown_frame = 0
            self.move_frame = 0

            self.died = False

            self.idle_ani = []
            self.chop_ani = []

            self.idle_ani.append(Image("/images/minigame imgs/Plant-bf-minigame-Knife.png"))

            self.chop_ani.append(Image("/images/minigame imgs/Plant-bf-minigame-Knife.png"))
            
            self.image = self.idle_ani[self.move_frame]

        def update(self, keyboard):
            self.move(keyboard)
            self.animate()

        def move(self, keyboard):
            print("no controls implemented yet")

        def animate(self):
            # control block will go here to determine current animation state, which should be just idle or chop
            self.slowdown_frame += 1
            if self.slowdown_frame >= 2*animationspeed:
                self.move_frame += 1
                self.slowdown_frame = 0
            if self.move_frame > 7:
                self.move_frame = 0

        def reset(self):
            print("reset currently does nothing, deprecate me?")

    class GameImage(Sprite):
        def __init__(self, image, zoom, width, height, x, y):
            Sprite.__init__(self, width, height, x, y)
            self.image = Transform(Image(image), xzoom=zoom,yzoom=zoom)
            self.zoom = zoom

    class Handler(renpy.Displayable):
        def __init__(self, player):
            renpy.Displayable.__init__(self)
            self.level = "level 1"
            self.window_size = Vector(1920, 960)
            self.keyboard = {"left": False, "right": False, "space": False, "enter": False}
            self.first_render = True
            self.game_over = False
            # self.song = "/audio/neonsigns.wav"
            self.stage_complete = False
            self.first_try = True

        def render(self, width, height, st, at):
            display = renpy.Render(display_width, display_height)
            # # background.render(display, st, at)
            for img in game_images:
                img.render(display, st, at)
            player.render(display, st, at)
            self.update()
            renpy.redraw(self, 0)
            self.first_render = False
            return display

        def update(self):
            if player.died:
                player.reset()
                self.game_over = True
                renpy.timeout(0)
            if self.first_try == True:
                self.first_try = False

        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    self.keyboard["left"] = True
                elif ev.key == pygame.K_RIGHT:
                    self.keyboard["right"] = True
                elif ev.key == pygame.K_SPACE:
                    self.keyboard["space"] = True
                elif ev.key == pygame.K_LSHIFT or ev.key == pygame.K_RSHIFT:
                    self.keyboard["shift"] = True
                elif ev.key == pygame.K_RETURN:
                    self.keyboard["enter"] = True
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_LEFT:
                    self.keyboard["left"] = False
                elif ev.key == pygame.K_RIGHT:
                    self.keyboard["right"] = False
                elif ev.key == pygame.K_SPACE:
                    self.keyboard["space"] = False
                elif ev.key == pygame.K_LSHIFT or ev.key == pygame.K_RSHIFT:
                    self.keyboard["shift"] = False
                elif ev.key == pygame.K_RETURN:
                    self.keyboard["enter"] = False
            else:
                if renpy.map_event(ev, "pad_a_press"):
                    self.keyboard["space"] = True
                elif renpy.map_event(ev, "pad_a_release"):
                    self.keyboard["space"] = False

                if renpy.map_event(ev, "pad_b_press"):
                    self.keyboard["enter"] = True
                elif renpy.map_event(ev, "pad_b_release"):
                    self.keyboard["enter"] = False

                if renpy.map_event(ev, "pad_leftx_neg") or renpy.map_event(ev, "pad_rightx_neg") or renpy.map_event(ev, "pad_dpleft_press"):
                    self.keyboard["left"] = True
                elif ((renpy.map_event(ev, "pad_leftx_zero") or renpy.map_event(ev, "pad_rightx_zero")) and self.keyboard["left"]) or renpy.map_event(ev, "pad_dpleft_release"):
                    self.keyboard["left"] = False

                if renpy.map_event(ev, "pad_leftx_pos") or renpy.map_event(ev, "pad_rightx_pos") or renpy.map_event(ev, "pad_dpright_press"):
                    self.keyboard["right"] = True
                elif ((renpy.map_event(ev, "pad_leftx_zero") or renpy.map_event(ev, "pad_rightx_zero")) and self.keyboard["right"]) or renpy.map_event(ev, "pad_dpright_release"):
                    self.keyboard["right"] = False

            # Ensure the screen updates
            renpy.restart_interaction()

            # If the player loses, return it
            #if self.player.died:
            #    return self.player.died
            #else:
            raise renpy.IgnoreEvent()

        def next_stage(self):
            if self.level == "level 1":
                self.level = "level 2"
            self.stage_complete = True

        def reset(self):
            self.keyboard = {"up": False, "down": False, "left": False, "right": False, "space": False, "shift": False, "enter": False}
            self.game_over = False
            player.reset()
            # renpy.music.play(self.song, loop = True)
            pass

    player = Player(32, 32, 1, 1)
    print("just init player")
    print(player)
    print(player.position)
    # background = Background(display_width, display_height, 0,0)
    cutting_board_img = GameImage('/images/minigame imgs/Plant-bf-minigame-Chopping-block.png',6,257,192,0,0)
    overlay_box_img = GameImage('/images/minigame imgs/Plant-bf-minigame-Overlay-box.png',5,257,192,display_width/4,0)
    bread_img = GameImage('/images/minigame imgs/Plant-bf-minigame-Bread.png',5,257,192,display_width/4,0)

    game_images = [cutting_board_img,overlay_box_img,bread_img]

default handler = Handler(player)

screen minigame(level):
    if handler.game_over == True: #game over screen
        $ handler.game_over = False
        # $ player.position = persistent.player_start
        frame:
            yminimum 1080
            background "#cc3300"
            add '/images/minigame imgs/Plant-bf-minigame-Background.png' yalign 0.5
            textbutton "continue ... ?":
                yoffset 920
                action Return()
    elif handler.stage_complete == True: #level success screen
        $ handler.game_over = False
        # $ player.position = persistent.player_start
        $ player.fallcount = 0
        frame:
            yminimum 1080
            background "#66cc66"
            add '/images/minigame imgs/Plant-bf-minigame-Background.png' yalign 0.5
            textbutton "keep going! almost there!":
                yoffset 920
                xalign 0.5
                action Call("leveldone")
    else: #gameplay screen
        frame:
            yminimum 1080
            background "#3f6c50"
            # add '/images/minigame imgs/Plant-bf-minigame-Background.png' yalign 0.5
            add handler yalign 0.5
            textbutton "click to skip":
                action Return()