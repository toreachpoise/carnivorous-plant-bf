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

            self.image = Image("/images/minigame imgs/Plant-bf-minigame-Knife.png")
            
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
                cur_level.get_active_ingredient().progress += 1
                sandwich_display.display_ingredient_progress()
            else:
                hit_or_miss_indicator.set_state("miss")
                # renpy.music.play("/audio/miss-cut-"+path_end+".wav", loop = False) #can't find a second good 'cut self sound'
                renpy.music.play("audio/miss-cut.mp3", loop = False)

    class GameImage(Sprite):
        def __init__(self, image, zoom, width, height, x, y):
            Sprite.__init__(self, width, height, x, y)
            self.image = Transform(Image(image), xzoom=zoom,yzoom=zoom)
            self.zoom = zoom

        def crop(self,x,y,width,height):
            self.image = Transform(self.image,crop=(x,y,width,height))

        def change_brightness(self,brightness):
            self.image = Transform(self.image,matrixcolor=BrightnessMatrix(brightness))

    class Time():
        def __init__(self):
            self.time = 0

        def update(self):
            self.time += 1

        def reset(self):
            self.time = 0

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

        def update(self):
            if len(self.beats) > 0:

                for beat in self.beats:
                    if beat.past_end == True:
                        self.beats.remove(beat)
                    else:
                        beat.update()
            else:
                if cur_level.check_for_victory():
                    handler.stage_complete = True
                    handler.next_stage()
                else:
                    handler.game_over = True

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
            self.position = position #initial position, Vector
            self.speed = speed #move speed, negative to move right to left
            self.margin = margin #margin of error timingwise for a hit to be considered on time
            self.image = GameImage("/images/minigame imgs/Plant-bf-minigame-Beat.png",ui_scale,2,15,position.x,position.y)
            self.beat_end = 5*ui_scale
            self.beat_hit_h_loc = 30*ui_scale
            # self.player_attempted_hit = False # this flag is set but not used
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
            else:
                self.miss = True

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

        def reset(self):
            self.reset_time = 0
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
                print(ingredient.image_path)
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

        def render(self, render, st, at, active_ingredient):
            self.cutting_board_img.render(render,st,at)
            for ingredient_img in self.ingredient_images:
                ingredient_img.render(render,st,at)
            self.place_icon_image(active_ingredient)
            self.active_icon_img.render(render,st,at)

        def reset(self):
            self.ingredients = cur_level.ingredients
            self.ingredient_images = []
            self.init_ingredient_images()
            self.place_icon_image(0)


    class SandwichDisplay():
        def __init__(self):
                self.overlay_x_pos = 3*display_width/4
                self.overlay_img = GameImage('/images/minigame imgs/Plant-bf-minigame-Overlay-box.png',5,257,192,self.overlay_x_pos,0)
                self.bread_img = GameImage('/images/minigame imgs/Plant-bf-minigame-Bread.png',5,257,192,self.overlay_x_pos,0)
                self.ingredient_progress_images = []
                self.display_ingredient_progress()
                self.ingredient_silhouettes = []
                self.display_ingredient_silhouettes()

        def display_ingredient_silhouettes(self):
            index = 0

            for ingredient in cur_level.ingredients:
                cur_img = GameImage(ingredient.image_path,ui_scale,0,0,self.overlay_x_pos + (5.5*ui_scale),index * 100 + 48 * ui_scale)
                cur_img.change_brightness(-0.75)
                self.ingredient_silhouettes.append(cur_img)
                index += 1

        def display_ingredient_progress(self):
            self.ingredient_progress_images = []

            index = 0

            for ingredient in cur_level.ingredients:
                cur_img = GameImage(ingredient.image_path,ui_scale,0,0,self.overlay_x_pos + (5.5*ui_scale),index * 100 + 48 * ui_scale)
                # crop the image so that it's a fraction of its width equal to how much of it has been chopped so far
                cur_img.crop(0,0,int(ingredient.image_width * (ingredient.progress / ingredient.beats_req)),300)
                self.ingredient_progress_images.append(cur_img)
                index += 1

        def render(self, render, st, at):
            self.overlay_img.render(render,st,at)
            self.bread_img.render(render,st,at)

            for img in self.ingredient_silhouettes:
                img.render(render,st,at)

            for img in self.ingredient_progress_images:
                img.render(render,st,at)

        def reset(self):
            self.ingredient_progress_images = []
            self.display_ingredient_progress()
            self.ingredient_silhouettes = []
            self.display_ingredient_silhouettes()    

    class LevelIngredient():
        def __init__(self, name, beats_req, image_path, image_width):
            self.name = name
            self.progress = 0
            self.beats_req = beats_req
            self.image_path = image_path
            self.image_width = image_width

    class Level():
        def __init__(self, ingredients, timing):
            self.ingredients = ingredients
            self.cur_ingredient_index = 0
            self.max_ingredient_index = len(self.ingredients)
            self.timing = timing

        def swap_ingredient(self):
            if self.cur_ingredient_index < (self.max_ingredient_index - 1):
                self.cur_ingredient_index += 1
            else:
                self.cur_ingredient_index = 0

        def check_for_victory(self):
            victory = True

            for ingredient in self.ingredients:
                if ingredient.progress < ingredient.beats_req:
                    victory = False

            return victory

        def get_active_ingredient(self):
            return self.ingredients[self.cur_ingredient_index]

        def reset(self):
            self.cur_ingredient_index = 0
            self.max_ingredient_index = len(self.ingredients)

    class Handler(renpy.Displayable):
        def __init__(self, player):
            renpy.Displayable.__init__(self)
            self.level = "level 1"
            # self.cur_level = instantiate_level("level 1")
            self.window_size = Vector(1920, 960)
            self.keyboard_held = {"chop": False, "swap": False}
            self.first_render = True
            self.game_over = False
            # self.song = "/audio/neonsigns.wav"
            self.stage_complete = False
            self.first_try = True
            # self.cutting_board = CuttingBoard(self.cur_level.ingredients)

        def render(self, width, height, st, at):
            display = renpy.Render(display_width, display_height)

            hit_or_miss_indicator.update()
            hit_or_miss_indicator.render(display,st,at)

            cutting_board.render(display,st,at,cur_level.cur_ingredient_index)
            
            sandwich_display.render(display,st,at)
                        
            self.update()

            chop_rhythm_box.update()
            chop_rhythm_box.render(display,st,at)
            player.render(display, st, at)

            renpy.redraw(self, 0)
            self.first_render = False
            return display

        def update(self):    
            for beat_time in cur_level.timing:
                if time.time == beat_time:
                    chop_rhythm_box.add_beat()
            if self.first_try == True:
                self.first_try = False

            time.update()

        def event(self, ev, x, y, st):
            # calling functions that trigger on key press here seems to be the best way to guarantee they only get called once
            # also for this, we track if a key is held so that we only fire the function the first tick it's pressed but not every tick it's held

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_a:
                    if self.keyboard_held["chop"] == False:
                        self.keyboard_held["chop"] = True
                        player.chop()
                if ev.key == pygame.K_d:
                    if self.keyboard_held["swap"] == False:
                        self.keyboard_held["swap"] = True
                        cur_level.swap_ingredient()
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_a:
                    self.keyboard_held["chop"] = False
                if ev.key == pygame.K_d:
                    self.keyboard_held["swap"] = False

            # Ensure the screen updates
            renpy.restart_interaction()

            raise renpy.IgnoreEvent()

        def instantiate_level(self,level):
            # try not to make the gap between times shorter than the reset time for the hit/miss indicator (currently 20)
            # a full bar is ~480 units of time?

            print(level)
            if level == "level 1":
                return Level([LevelIngredient("borger",3,"/images/minigame imgs/Plant-bf-minigame-Borger-cropped.png", 55*ui_scale),LevelIngredient("lettuce", 2,"/images/minigame imgs/Plant-bf-minigame-Lettuce-cropped.png", 55*ui_scale)], [0,30,60,90,130,160,190])
            elif level == "level 2":
                return Level([LevelIngredient("chicken",2,"/images/minigame imgs/Plant-bf-minigame-Chicken-cropped.png", 55*ui_scale),LevelIngredient("tomato", 3,"/images/minigame imgs/Plant-bf-minigame-Tomato-cropped.png", 55*ui_scale),LevelIngredient("lettuce", 3,"/images/minigame imgs/Plant-bf-minigame-Lettuce-cropped.png", 55*ui_scale)], [0,25,50,75,100,125,185,210,235,300,325])
            # return Level([LevelIngredient("chicken",2,"/images/minigame imgs/Plant-bf-minigame-Chicken-cropped.png", 55*ui_scale),LevelIngredient("chicken", 3,"/images/minigame imgs/Plant-bf-minigame-Chicken-cropped.png", 55*ui_scale)], [0,30,60,90,120,180])
            

        def next_stage(self):
            if self.level == "level 1":
                self.level = "level 2"

        def reset(self):
            print(self.stage_complete)
            print(self.game_over)
            print(cur_level.timing)

            self.keyboard_held = {"chop": False, "swap": False}
            self.stage_complete = False
            self.game_over = False
            time.reset()

            global cur_level
            cur_level = self.instantiate_level(self.level)
            
            chop_rhythm_box.reset()
            sandwich_display.reset()
            cutting_board.reset()
            pass

    time = Time()

    # try not to make the gap between times shorter than the reset time for the hit/miss indicator (currently 20)
    # a full bar is ~480 units of time?
    # this is now set in handler.instantiate level, but since the other stuff is globally called here I'm gonna also set it here since deadline is in >7 days
    cur_level = Level([LevelIngredient("borger",3,"/images/minigame imgs/Plant-bf-minigame-Borger-cropped.png", 55*ui_scale),LevelIngredient("lettuce", 2,"/images/minigame imgs/Plant-bf-minigame-Lettuce-cropped.png", 55*ui_scale)], [0,30,60,90,130,160,190])

    player = Player(32, 32, 1, 1)
    cutting_board = CuttingBoard()
    hit_or_miss_indicator = HitMissIndicator(20, 9*ui_scale, -20)
    sandwich_display = SandwichDisplay()
    chop_rhythm_box = ChopRhythmBox()

default handler = Handler(player)

screen minigame(level):
    if handler.game_over == True: #game over screen
        # $ handler.reset()
        frame:
            yminimum 1080
            background "#cc3300"
            add '/minigame imgs/bad_sandwich_gameover.jpg' yalign 0.5
            textbutton "This sandwich sucks ass, try again? (Click here)":
                yoffset 920
                xalign 0.5
                action Return()
    elif handler.stage_complete == True: #level success screen
        # For some GOD FORSAKEN FUCKING REASON this evaluates even when handler.stage_complete prints as false.
        # I don't have time to figure out why, so instead we need to set handler.next_stage() to be written somewhere else
        # TODO: that ^
        # $ print(handler.stage_complete)
        # $ handler.next_stage()
        # $ handler.reset()
        frame:
            yminimum 1080
            background "#66cc66"
            add '/minigame imgs/victory_sandwich.png' yalign 0.5
            textbutton "Tasty!! (Click here to continue)":
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
