# game/zzz_choice_random_positions.rpy
# 1920x1080: black background, fixed spacing, and per-run left/right swap
# that DOES NOT change mid-game (rollback-safe via persistent).

screen choice(items):

    modal True
    zorder 200

    # Fullscreen true-black overlay.
    add Solid("#000"):
        xysize (config.screen_width, config.screen_height)

    # 30 second timer support (requires: default choice_timeout = None somewhere ONCE)
    if choice_timeout:
        timer 30.0 action Jump(choice_timeout)

    # Rollback-safe: persistent is not reverted by rollback.
    $ swap = getattr(persistent, "_gf_choice_lr_swap", 0)

    # Fixed card geometry
    $ CARD_W = 650
    $ CARD_H = 170

    # Fixed positions for 1920x1080 (centers)
    $ LEFT_X   = 346
    $ RIGHT_X  = 1574
    $ MID_X    = 960

    $ MID_Y    = 540
    $ TOP_Y    = 432
    $ BOTTOM_Y = 734

    # ------------------------------------------------------------
    # 2 choices: fixed left/right at mid-screen, swapped per run
    # ------------------------------------------------------------
    if len(items) == 2:

        $ left_item  = items[1] if swap else items[0]
        $ right_item = items[0] if swap else items[1]

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
    # 3 choices: two top swapped per run, third bottom centered
    # ------------------------------------------------------------
    elif len(items) == 3:

        $ top_left  = items[1] if swap else items[0]
        $ top_right = items[0] if swap else items[1]
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