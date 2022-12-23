import pygame

LIGHT_YELLOW=(255, 255, 0)
DARK_YELLOW=(200, 200, 0)
LIGHT_RED=(255, 0, 0)
DARK_RED=(200, 0, 0)
WHITE=(255, 255, 255)
DARK_GREEN=(0, 220, 0)
LIGHT_GREEN=(0, 255, 0)
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)

main_font = pygame.font.SysFont('Comic Sans MS', 30)
DEFAULT_BUTTON_STYLE = {
    "hover_color": LIGHT_YELLOW,
    "hover_font_color":BLACK,
    "font_color": WHITE,
    "font":main_font,
    "text":"Next"
}
HARD_BUTTON_STYLE={
    "text": "Hard",
    "hover_color": LIGHT_RED,
    "font":main_font,
    "font_color": WHITE,
}
MEDIUM_BUTTON_STYLE=dict(DEFAULT_BUTTON_STYLE)
MEDIUM_BUTTON_STYLE["text"]="Medium"

EASY_BUTTON_STYLE={
    "hover_color":LIGHT_GREEN,
    "font_color":WHITE,
    "text":"Easy",
    "font":main_font,
}

MENU_BUTTON_STYLE=dict(DEFAULT_BUTTON_STYLE)
MENU_BUTTON_STYLE["text"]="Menu"
NEXT_BUTTON_STYLE=dict(DEFAULT_BUTTON_STYLE)
NEXT_BUTTON_STYLE["text"]="Next"
PREVIOUS_BUTTON_STYLE=dict(HARD_BUTTON_STYLE)
PREVIOUS_BUTTON_STYLE["text"]="Previous"
PLAY_BUTTON_STYLE=dict(DEFAULT_BUTTON_STYLE)
PLAY_BUTTON_STYLE["text"]="Play"
PLAY_BUTTON_STYLE["font"]=main_font
HIGH_SCORE_BUTTON_STYLE=dict(HARD_BUTTON_STYLE)
HIGH_SCORE_BUTTON_STYLE["text"]="High scores"