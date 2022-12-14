color_map={
    -1:(255, 0, 0),
    1: (0, 255, 0)
}
#convert tier to rgb value
tier_color_map={
    1: (255, 0, 0),
    2: (0, 150, 150),
    3: (200, 200, 0),
}
#convert difficulty to timeout interval in gameloop.
difficulty_map={
    "hard":100,
    "medium":200,
    "easy":300
}

GAME_OVER=[[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0]]

ACCEPTED_LETTERS="{}{}".format(
    " 1234567890abcdefghijklmnopqrstuvwxyzoåäö",
    "abcdefghijklmnopqrstuvwxyzoåäö".upper())
