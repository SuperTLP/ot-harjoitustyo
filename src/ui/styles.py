LIGHT_YELLOW=(255, 255, 0)
DARK_YELLOW=(200, 200, 0)
LIGHT_RED=(255, 0, 0)
DARK_RED=(200, 0, 0)
WHITE=(255, 255, 255)
DARK_GREEN=(0, 220, 0)
LIGHT_GREEN=(0, 255, 0)
BLACK=(0, 0, 0)

#This file is GUI, and thus is not tested

DEFAULT_BUTTON_STYLE = {
    "hover_color": LIGHT_YELLOW,
    "hover_font_color":BLACK,
    "font_color": WHITE,

}
HARD_BUTTON_STYLE={
    "text": "Hard",
    "hover_color": LIGHT_RED,
    "font_color": WHITE,
}
MEDIUM_BUTTON_STYLE=dict(DEFAULT_BUTTON_STYLE)
MEDIUM_BUTTON_STYLE["text"]="Medium"

EASY_BUTTON_STYLE={
    "hover_color":LIGHT_GREEN,
    "font_color":WHITE,
    "text":"Easy"
}