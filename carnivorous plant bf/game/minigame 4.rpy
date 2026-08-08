init python:
    import pygame, random
    FPS = 60
    animationspeed = 3  #fps of the animation will be 'FPS' divided by this number
    #screen = pygame.display.set_mode(window_size, 0, 32)
    ui_scale = 6
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

        # def move(self, keyboard):
        #     print("no controls implemented yet")

        def animate(self):
            # control block will go here to determine current animation state, which should be just idle or chop
            self.slowdown_frame += 1
            if self.slowdown_frame >= 2*animationspeed:
                self.move_frame += 1
                self.slowdown_frame = 0
            if self.move_frame > 7:
                self.move_frame = 0

        def chop(self):
            hit = chop_rhythm_box.check_for_hit()

            path_end = ""

            if time.time % 2 == 0: #arbitrarily decide on which audio file to play based on if current tick is odd or even
                path_end = "1"
            else:
                path_end = "2"

            if hit:
                hit_or_miss_indicator.set_state("hit")
                renpy.music.play("/audio/good-chop-"+path_end+".mp3", loop = False)
            else:
                hit_or_miss_indicator.set_state("miss")
                renpy.music.play("/audio/miss-cut-"+path_end+".wav", loop = False)


        def reset(self):
            self.died = False

    class GameImage(Sprite):
        def __init__(self, image, zoom, width, height, x, y):
            Sprite.__init__(self, width, height, x, y)
            self.image = Transform(Image(image), xzoom=zoom,yzoom=zoom)
            self.zoom = zoom

    class Time():
        def __init__(self):
            self.time = 0

        def update(self):
            self.time += 1

    class MultiSpriteObject():
        def __init__(self, sprites):
            self.sprites = []
            for sprite in sprites:
                self.sprites.append(sprite)

        def append_sprite(self, sprite):
            self.sprites.append(sprite)

        def render(self, render, st, at):
            for sprite in self.sprites:
                sprite.render(render, st, at)

    class ChopRhythmBox(MultiSpriteObject):
        def __init__(self):
            self.rhythm_box_background_img = GameImage("/images/minigame imgs/Plant-bf-minigame-Rhythm-box.png",ui_scale,257,192,0,0)
            self.beats = []
            self.rhythm_box_position_indic_img = GameImage("/images/minigame imgs/Plant-bf-minigame-Position-indicator.png",ui_scale,257,192,0,0)

        def update(self, keyboard):
            if len(self.beats) > 0:

                for beat in self.beats:
                    if beat.past_end == True:
                        self.beats.remove(beat)
                    else:
                        beat.update()

        # called in Player by Handler when a space key event is handled
        # Returns if the hit (True) or missed (False)
        def check_for_hit(self):
            if len(self.beats) > 0:
                for beat in self.beats: #loop until we get the first beat past the hit loc
                    if beat.past_hit_loc:
                        continue
                    else: #check if we hit it
                        return beat.check_for_hit()
            
                # if we got to the end with out finding a beat past_hit_loc, then the player should miss
                # or if the player was trying to hit and there are no beats, that should miss
            hit_or_miss_indicator.set_state("miss")
            return False

        def render(self, render, st, at):
            self.rhythm_box_background_img.render(render,st,at)

            for beat in self.beats:
                display = renpy.render(beat.image.image, beat.image.width, beat.image.height, st, at)
                render.blit(display, (int(beat.position.x), int(beat.position.y)))
            
            self.rhythm_box_position_indic_img.render(render,st,at)

        def add_beat(self):
            self.beats.append(ChopRhythmBeat(Vector(169*ui_scale,18*ui_scale),15,-2))

        def reset(self):
            self.beats = []

    class ChopRhythmBeat():
        def __init__(self, position, margin, speed):
            self.position = position
            self.speed = speed
            self.margin = margin
            self.image = GameImage("/images/minigame imgs/Plant-bf-minigame-Beat.png",ui_scale,2,15,position.x,position.y)
            self.beat_end = 5*ui_scale
            self.beat_hit_h_loc = 30*ui_scale
            self.player_attempted_hit = False # this flag is set but not used
            self.miss = False
            self.past_end = False
            self.past_hit_loc = False

        def update(self):
            self.position.x += self.speed
            if self.position.x <= self.beat_end:
                self.past_end = True
            if self.position.x + self.margin <= self.beat_hit_h_loc: #checking specifically that the beat is past the hit location AND the margin of error
                self.past_hit_loc = True

        def check_for_hit(self):
            # these two commented lines limited the player to one try per beat, I don't think that's desireable anymore
            # if self.player_attempted_hit == False:
            #     self.player_attempted_hit = True
            if self.position.x <= self.beat_hit_h_loc + self.margin and self.position.x >= self.beat_hit_h_loc - self.margin:
                self.miss = False
                # hit_or_miss_indicator.set_state("hit") #now set in Player.chop()
            else:
                self.miss = True
                # hit_or_miss_indicator.set_state("miss")

            return not self.miss

    class HitMissIndicator():
        def __init__(self, time_to_neutral, position_x, position_y):
            self.hit_img = GameImage("/images/minigame imgs/Plant-bf-minigame-Hit-Indicator.png",1,268,109,position_x,position_y)
            self.miss_img = GameImage("/images/minigame imgs/Plant-bf-minigame-Miss-Indicator.png",1,268,109,position_x,position_y)
            self.neutral_img = GameImage("/images/minigame imgs/Plant-bf-minigame-Neutral-Indicator.png",1,268,109,position_x,position_y)
            self.active_img = self.neutral_img
            self.reset_time = 0
            self.time_to_neutral = time_to_neutral

        def set_state(self, state):
            match state:
                case "hit":
                    self.active_img = self.hit_img
                    self.reset_time = time.time + self.time_to_neutral
                case "miss":
                    self.active_img = self.miss_img
                    self.reset_time = time.time + self.time_to_neutral
                case _:
                    self.active_img = self.neutral_img

        def render(self, render, st, at):
            self.active_img.render(render, st, at)

        def update(self):
            if time.time == self.reset_time:
                self.set_state("neutral")

    class CuttingBoard():
        def __init__(self):
            self.cutting_board_img = GameImage('/images/minigame imgs/Plant-bf-minigame-Chopping-block.png',ui_scale,257,192,0,0)
            self.ingredients = cur_level.ingredients
            self.ingredient_images = []
            self.active_icon_img = GameImage('/images/minigame imgs/Plant-bf-minigame-Active-Ingredient-Indicator.png',ui_scale,21,15,0,0)

            self.init_ingredient_images()
            self.place_icon_image(0)

        def init_ingredient_images(self):
            # the cutting board is about 145 * 89 pixels before scaling
            # so to place up to 4 ingredients, we need to have an offset of half * ui_scale
            # we also have to place these with their offsets so that they go to where the cutting board is
            # the cutting board starts 22 pixels across, and 55 down
            width = 145 * ui_scale
            height = 89 * ui_scale
            x_offset = 22 * ui_scale
            y_offset = 55 * ui_scale

            ing_count = 0

            for ingredient in cur_level.ingredients:
                match ing_count:
                    case 0:
                        self.ingredient_images.append(GameImage(ingredient.image_path,ui_scale,250,250,x_offset,y_offset))
                    case 1:
                        self.ingredient_images.append(GameImage(ingredient.image_path,ui_scale,250,250,x_offset + (width / 2),y_offset))
                    case 2:
                        self.ingredient_images.append(GameImage(ingredient.image_path,ui_scale,250,250,x_offset,y_offset + (height / 2)))
                    case 3:
                        self.ingredient_images.append(GameImage(ingredient.image_path,ui_scale,250,250,x_offset + (width / 2),y_offset + (height / 2)))

                ing_count += 1

        # index is an int 0-3 for the current active ingredient
        def place_icon_image(self,index):
            # cutting board is 151 pixels long without offset from wall
            width = 145 * ui_scale
            height = 89 * ui_scale
            y_offset = 38 * ui_scale

            match(index):
                case 0:
                    self.active_icon_img.position = Vector(width / 4, y_offset)
                case 1:
                    self.active_icon_img.position = Vector(width * 3 / 4, y_offset)
                case 2:
                    self.active_icon_img.position = Vector(width / 4, y_offset + (height / 2))
                case 3:
                    self.active_icon_img.position = Vector(width * 3 / 4, y_offset + (height / 2))

        def render(self, render, st, at):
            self.cutting_board_img.render(render,st,at)
            for ingredient_img in self.ingredient_images:
                ingredient_img.render(render,st,at)
            self.active_icon_img.render(render,st,at)


    class LevelIngredient():
        def __init__(self, name, timing, image_path):
            self.name = name
            self.timing = timing
            self.image_path = image_path

    class Level():
        def __init__(self, ingredients):
            self.ingredients = ingredients
            self.cur_ingredient_index = 0
            self.max_ingredient_index = len(self.ingredients)

        def swap_ingredient(self):
            if self.cur_ingredient_index < (self.max_ingredient_index - 1):
                self.cur_ingredient_index += 1
            else:
                self.cur_ingredient_index = 0

            cutting_board.place_icon_image(self.cur_ingredient_index)

        def get_active_ingredient(self):
            return self.ingredients[self.cur_ingredient_index]

        def reset(self):
            self.cur_ingredient_index = 0

    class Handler(renpy.Displayable):
        def __init__(self, player):
            renpy.Displayable.__init__(self)
            self.level = "level 1"
            self.window_size = Vector(1920, 960)
            self.keyboard = {"left": False, "right": False, "space": False, "enter": False}
            self.keyboard_held = {"left": False, "right": False, "space": False, "enter": False}
            self.first_render = True
            self.game_over = False
            # self.song = "/audio/neonsigns.wav"
            self.stage_complete = False
            self.first_try = True
            self.time = 0

        def render(self, width, height, st, at):
            time.update()
            display = renpy.Render(display_width, display_height)
            # # background.render(display, st, at)
            for img in game_images:
                img.render(display, st, at)
            chop_rhythm_box.update(self.keyboard)
            chop_rhythm_box.render(display,st,at)
            hit_or_miss_indicator.update()
            hit_or_miss_indicator.render(display,st,at)
            cutting_board.render(display,st,at)
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
            else:
                for beat_time in cur_level.get_active_ingredient().timing:
                    if self.time == beat_time:
                        chop_rhythm_box.add_beat()
                self.time += 1
            if self.first_try == True:
                self.first_try = False

        def event(self, ev, x, y, st):
            # calling functions that trigger on key press here seems to be the best way to guarantee they only get called once
            # also for this, we track if a key is held so that we only fire the function when it's pressed but not held

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    if self.keyboard_held["space"] == False:
                        self.keyboard["space"] = True
                        self.keyboard_held["space"] = True
                        player.chop()
                        cur_level.swap_ingredient()
                    else:
                        self.keyboard["space"] = False
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_SPACE:
                    self.keyboard_held["space"] = False
            # if ev.type == pygame.KEYDOWN:
            #     if ev.key == pygame.K_LEFT:
            #         self.keyboard["left"] = True
            #     elif ev.key == pygame.K_RIGHT:
            #         self.keyboard["right"] = True
            #     elif ev.key == pygame.K_SPACE:
            #         self.keyboard["space"] = True
            #     elif ev.key == pygame.K_LSHIFT or ev.key == pygame.K_RSHIFT:
            #         self.keyboard["shift"] = True
            #     elif ev.key == pygame.K_RETURN:
            #         self.keyboard["enter"] = True
            # elif ev.type == pygame.KEYUP:
            #     if ev.key == pygame.K_LEFT:
            #         self.keyboard["left"] = False
            #     elif ev.key == pygame.K_RIGHT:
            #         self.keyboard["right"] = False
            #     elif ev.key == pygame.K_SPACE:
            #         self.keyboard["space"] = False
            #     elif ev.key == pygame.K_LSHIFT or ev.key == pygame.K_RSHIFT:
            #         self.keyboard["shift"] = False
            #     elif ev.key == pygame.K_RETURN:
            #         self.keyboard["enter"] = False
            # else:
            #     if renpy.map_event(ev, "pad_a_press"):
            #         self.keyboard["space"] = True
            #     elif renpy.map_event(ev, "pad_a_release"):
            #         self.keyboard["space"] = False

            #     if renpy.map_event(ev, "pad_b_press"):
            #         self.keyboard["enter"] = True
            #     elif renpy.map_event(ev, "pad_b_release"):
            #         self.keyboard["enter"] = False

            #     if renpy.map_event(ev, "pad_leftx_neg") or renpy.map_event(ev, "pad_rightx_neg") or renpy.map_event(ev, "pad_dpleft_press"):
            #         self.keyboard["left"] = True
            #     elif ((renpy.map_event(ev, "pad_leftx_zero") or renpy.map_event(ev, "pad_rightx_zero")) and self.keyboard["left"]) or renpy.map_event(ev, "pad_dpleft_release"):
            #         self.keyboard["left"] = False

            #     if renpy.map_event(ev, "pad_leftx_pos") or renpy.map_event(ev, "pad_rightx_pos") or renpy.map_event(ev, "pad_dpright_press"):
            #         self.keyboard["right"] = True
            #     elif ((renpy.map_event(ev, "pad_leftx_zero") or renpy.map_event(ev, "pad_rightx_zero")) and self.keyboard["right"]) or renpy.map_event(ev, "pad_dpright_release"):
            #         self.keyboard["right"] = False

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
            self.time = 0
            player.reset()
            cur_level.reset()
            chop_rhythm_box.reset() # TURN THIS BACK ON ONCE BEATS ARE SPAWNED BY HANDLER
            # renpy.music.play(self.song, loop = True)
            pass

    time = Time()

    player = Player(32, 32, 1, 1)
    overlay_box_img = GameImage('/images/minigame imgs/Plant-bf-minigame-Overlay-box.png',5,257,192,3*display_width/4,0)
    bread_img = GameImage('/images/minigame imgs/Plant-bf-minigame-Bread.png',5,257,192,3*display_width/4,0)
    hit_or_miss_indicator = HitMissIndicator(20, 9*ui_scale, -20)

    game_images = [overlay_box_img,bread_img]

    chop_rhythm_box = ChopRhythmBox()

    # try not to make the gap between times shorter than the reset time for the hit/miss indicator (currently 20)
    # a full bar is ~480 units of time?
    ingredients_list = [LevelIngredient("chicken", [0,30,60,90,120,180,450,480],"/images/minigame imgs/Plant-bf-minigame-Chicken-cropped.png"),LevelIngredient("chicken", [0,30,60,90,120,180,450,480],"/images/minigame imgs/Plant-bf-minigame-Chicken-cropped.png")]
    level1 = Level(ingredients_list)
    cur_level = level1
    cutting_board = CuttingBoard()


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
