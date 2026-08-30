label minigame:
if handler.first_try == True:
    label controls_explanation:

    scene black

    show tutorial beats
    p "This is the cooking screen, in the red bar blue beats will come from right to left."
    show tutorial chop
    p "Press A when a beat is in the green section to Chop!"
    show tutorial progress
    p "When you Chop! at the right time, you will fill up the selected ingredient on the right somewhat. The amount is unique to each ingredient."
    show tutorial one_ingredient_done
    p "Fill up the ingredient all the way to completely chop it."
    show tutorial swap
    p "Press D to Swap! your selected ingredient."
    show tutorial swap_progress
    p "Now when you Chop! it will fill up that ingredient on the right."
    show tutorial win
    p "Fully chop all ingredients to make a Tasty sandwich."
    p "If you don't fully chop all ingredients before running out of beats your sandwich will Suck Ass."
    p "Let's get cooking!"
# menu:
#     "Do you need to hear about the controls again?"
#     "yes":
#         jump controls_explanation
#     "no":
#         pass

# python:
#     handler.game_over = False
$ handler.reset()
#     player.died = False
call screen minigame("level 1")
menu:
    "do you want to try again?"
    "yes":
        jump minigame
    "I need to hear the controls again":
        jump controls_explanation
    # "no thanks, let's skip this level":
    #     # $ handler.next_stage()
        pass
label leveldone:
$ handler.stage_complete = False
if handler.level == "level 2":
    jump chapter3minigamedone
if handler.level == "level 3":
    jump chapter5minigamedone