label minigame:
if handler.first_try == True:
    label controls_explanation:
    p "I don't know why I feel compelled to say this but ..."
    p "... to move me, use the arrow keys. To jump, press SPACEBAR. To knife bad guys, hit ENTER"
    p "or if you're on a controller, use the D pad or joystick to move, A or X to jump, and B to attack. Or something, you'll figure it out."
menu:
    "Do you need to hear about the controls again?"
    "yes":
        jump controls_explanation
    "no":
        pass
p "alright, let's do this"
python:
    player.reset()
    handler.game_over = False
    handler.reset()
    player.died = False
call screen minigame("level 1")
menu:
    "do you want to try again?"
    "yep":
        jump minigame
    "no thanks, let's skip this level":
        $ handler.next_stage()
        pass
label leveldone:
$ handler.stage_complete = False
if handler.level == "level 2":
    jump chapter1