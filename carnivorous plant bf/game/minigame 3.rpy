init python:
    import math, pygame

    class Chungus():
        max_height = 250
        min_height = -250
        chungus_speed = 1
        chungus_direction = 1


    def player_update(st):
        speed = 1

        keyinput = pygame.key.get_pressed()
        if keyinput is not None:
            if keyinput[pygame.K_LEFT]:
                player_sprite.x -= speed
            elif keyinput[pygame.K_RIGHT]:
                player_sprite.x += speed
            
            if keyinput[pygame.K_UP]:
                player_sprite.y -= speed
            elif keyinput[pygame.K_DOWN]:
                player_sprite.y += speed

        return .01

    chungus_direction = 1

    def chungus_update(st):
        if chungus_sprite.y < c.max_height and chungus_sprite.y > c.min_height:
            chungus_sprite.y += c.chungus_speed * c.chungus_direction
        elif chungus_sprite.y >= c.max_height or chungus_sprite.y <= c.min_height:
            c.chungus_direction *= -1
            chungus_sprite.y += c.chungus_speed * c.chungus_direction

        return .01

label minigame3:

    python:
        # Create a sprite manager.
        player = SpriteManager(update=player_update)

        player_img = Image("minigame imgs/Plant-bf-minigame-mockup_0016_Right-hand.png")
        player_sprite = player.create(player_img)

        del player_img

        chungus = SpriteManager(update=chungus_update)

        chungus_img = Image("minigame imgs/Plant-bf-minigame-mockup_0015_Knife.png")
        chungus_sprite = chungus.create(chungus_img)

        c = Chungus()

        del chungus_img

    # Add the repulsor to the screen.
    show expression player

    show expression chungus

    "..."

    hide player

    # Clean up.
    python:
        del player
        del player_sprite