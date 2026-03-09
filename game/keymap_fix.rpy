init python:
    # Restore keymap entries expected by Ren'Py's save/load screens.
    config.keymap.setdefault("save_page_next", [ "K_PAGEDOWN", "repeat_K_PAGEDOWN", "mousedown_5" ])
    config.keymap.setdefault("save_page_prev", [ "K_PAGEUP",   "repeat_K_PAGEUP",   "mousedown_4" ])