screen choice(items):

    style_prefix "choice"

    # ---- DO NOT TOUCH (logging hook) ----
    $ _cid = getattr(store, "choice_id", None) or "unknown_choice"
    on "show" action Function(log_choice_shown, _cid)
    # -------------------------------------

    add Solid("#000000")

    fixed:
        xfill True
        yfill True

        # Left option (item 0)
        if len(items) > 0:
            $ caption = items[0].caption
            button:
                xpos 80
                ypos 420
                xsize 720
                ysize 220
                padding (30, 25)
                background Solid("#1a1a1a")
                hover_background Solid("#333333")

                action [
                    Function(log_choice_clicked, _cid, caption),
                    items[0].action
                ]

                text caption:
                    size 44
                    color "#FFFFFF"
                    xalign 0.5
                    yalign 0.5

        # Right option (item 1)
        if len(items) > 1:
            $ caption = items[1].caption
            button:
                xpos 1120
                ypos 420
                xsize 720
                ysize 220
                padding (30, 25)
                background Solid("#1a1a1a")
                hover_background Solid("#333333")

                action [
                    Function(log_choice_clicked, _cid, caption),
                    items[1].action
                ]

                text caption:
                    size 44
                    color "#FFFFFF"
                    xalign 0.5
                    yalign 0.5

        # Extra options (item 2+) – fixed center stack lower down
        if len(items) > 2:
            vbox:
                xpos 600
                ypos 700
                spacing 25

                for i in items[2:]:
                    $ caption = i.caption
                    button:
                        xsize 720
                        ysize 200
                        padding (30, 25)
                        background Solid("#1a1a1a")
                        hover_background Solid("#333333")

                        action [
                            Function(log_choice_clicked, _cid, caption),
                            i.action
                        ]

                        text caption:
                            size 40
                            color "#FFFFFF"
                            xalign 0.5
                            yalign 0.5
