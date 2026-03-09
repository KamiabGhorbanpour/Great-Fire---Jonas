# game/zzz_choice_override.rpy
# Tuned for 1920x1080.

default _choice_lr_swap = None   # None until first choice screen shows this run.

screen choice(items):

    modal True
    zorder 200

    # Fullscreen black overlay (true black).
    # Using config.* avoids edge cases with scaling/windowed mode.
    add Solid("#000"):
        xysize (config.screen_width, config.screen_height)

    # 30 second timer support (requires: default choice_timeout = None)
    if choice_timeout:
        timer 30.0 action Jump(choice_timeout)

    # One-time randomization per game launch (NOT per menu).
    # 0 = normal order, 1 = swapped.
    if _choice_lr_swap is None:
        $ _choice_lr_swap = renpy.random.randint(0, 1)

    # Fixed card geometry
    $ CARD_W = 650
    $ CARD_H = 170

    # Fixed positions for 1920x1080 (centers)
    $ LEFT_X   = 346     # ~0.18 * 1920
    $ RIGHT_X  = 1574    # ~0.82 * 1920
    $ MID_X    = 960

    $ MID_Y    = 540
    $ TOP_Y    = 432     # ~0.40 * 1080
    $ BOTTOM_Y = 734     # ~0.68 * 1080

    # ------------------------------------------------------------
    # 2 choices: fixed left/right at mid-screen (like your original)
    # Randomize by swapping which item goes left/right (once per run).
    # ------------------------------------------------------------
    if len(items) == 2:

        $ left_item  = items[1] if _choice_lr_swap else items[0]
        $ right_item = items[0] if _choice_lr_swap else items[1]

        frame:
            xcenter LEFT_X
            ycenter MID_Y
            xsize CARD_W
            ysize CARD_H
            padding (20, 20)
            background "#1c1c1c"

            textbutton left_item.caption:
                action [SetVariable("choice_timeout", None), left_item.action]
                xfill True
                yfill True
                text_size 38
                text_align 0.5
                text_xalign 0.5
                text_yalign 0.5

        frame:
            xcenter RIGHT_X
            ycenter MID_Y
            xsize CARD_W
            ysize CARD_H
            padding (20, 20)
            background "#1c1c1c"

            textbutton right_item.caption:
                action [SetVariable("choice_timeout", None), right_item.action]
                xfill True
                yfill True
                text_size 38
                text_align 0.5
                text_xalign 0.5
                text_yalign 0.5

    # ------------------------------------------------------------
    # 3 choices: two top (fixed left/right), third bottom centered
    # Randomize ONLY the top pair left/right; keep the 3rd bottom.
    # ------------------------------------------------------------
    elif len(items) == 3:

        $ top_left  = items[1] if _choice_lr_swap else items[0]
        $ top_right = items[0] if _choice_lr_swap else items[1]
        $ bottom    = items[2]

        frame:
            xcenter LEFT_X
            ycenter TOP_Y
            xsize CARD_W
            ysize CARD_H
            padding (20, 20)
            background "#1c1c1c"

            textbutton top_left.caption:
                action [SetVariable("choice_timeout", None), top_left.action]
                xfill True
                yfill True
                text_size 38
                text_align 0.5
                text_xalign 0.5
                text_yalign 0.5

        frame:
            xcenter RIGHT_X
            ycenter TOP_Y
            xsize CARD_W
            ysize CARD_H
            padding (20, 20)
            background "#1c1c1c"

            textbutton top_right.caption:
                action [SetVariable("choice_timeout", None), top_right.action]
                xfill True
                yfill True
                text_size 38
                text_align 0.5
                text_xalign 0.5
                text_yalign 0.5

        frame:
            xcenter MID_X
            ycenter BOTTOM_Y
            xsize CARD_W
            ysize CARD_H
            padding (20, 20)
            background "#1c1c1c"

            textbutton bottom.caption:
                action [SetVariable("choice_timeout", None), bottom.action]
                xfill True
                yfill True
                text_size 38
                text_align 0.5
                text_xalign 0.5
                text_yalign 0.5

    # ------------------------------------------------------------
    # 1, 4, 5...: stable vertical stack centered
    # (No randomization here, because there isn't a canonical "left/right".)
    # ------------------------------------------------------------
    else:

        vbox:
            xcenter MID_X
            ycenter MID_Y
            spacing 20

            for i in items:
                frame:
                    xsize CARD_W
                    ysize CARD_H
                    padding (20, 20)
                    background "#1c1c1c"

                    textbutton i.caption:
                        action [SetVariable("choice_timeout", None), i.action]
                        xfill True
                        yfill True
                        text_size 38
                        text_align 0.5
                        text_xalign 0.5
                        text_yalign 0.5