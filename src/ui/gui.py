import pygame
from math import ceil
pygame.init()
pygame.font.init()
from pygame_button import Button
from ui.styles import (
MEDIUM_BUTTON_STYLE, HARD_BUTTON_STYLE, 
EASY_BUTTON_STYLE,DEFAULT_BUTTON_STYLE,
DARK_RED,DARK_GREEN,DARK_YELLOW
)
#generate rgb color given positivity / negativity of defaulttreat effect.
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

WHITE=(255, 255, 255)
main_font = pygame.font.SysFont('Comic Sans MS', 30)
secondary_font=pygame.font.SysFont('Comic Sans MS', 20)
events = pygame.event.get()

HARD_BUTTON_STYLE["font"]=main_font
MEDIUM_BUTTON_STYLE["font"]=main_font
EASY_BUTTON_STYLE["font"]=main_font
DEFAULT_BUTTON_STYLE["font"]=main_font
MENU_BUTTON_STYLE=dict(DEFAULT_BUTTON_STYLE)
MENU_BUTTON_STYLE["text"]="Menu"

GAME_OVER=[[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0]]

class View:
    def __init__(self, game, score):
        self.score=score
        self.game=game
        self.screen=pygame.display.set_mode([700, 500])
        self.display_run=True
        self.game_run=False

    def start_game(self, name, difficulty):
        self.difficulty_selector_run=False
        self.game_run=True
        starting_image=self.game.start(name, difficulty)
        interval=difficulty_map[difficulty]
        started=False
        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_run=False
                if event.type == pygame.KEYDOWN:
                    started=True
                    if event.key == pygame.K_LEFT:
                        self.game.change_direction(3)
                    if event.key == pygame.K_RIGHT:
                        self.game.change_direction(1)
                    if event.key == pygame.K_UP:
                        self.game.change_direction(0)
                    if event.key == pygame.K_DOWN:
                        self.game.change_direction(2)
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (0, 255, 255), pygame.Rect(0, 0, 750, 50))
            image=starting_image
            if started:
                image = self.game.advance()
            
            if image==GAME_OVER:
                self.game_run=False
                self.start_ending_screen(self.game.points)
                break
            for i in range(0, len(image)):
                for j in range(0, len(image[0])):
                    color=(0, 0, 0)
                    if image[i][j].type=="snake":
                        color=(255, 255, 255)
                    text=""
                    if image[i][j].tier!=0:
                        color=tier_color_map[image[i][j].tier]
                        text=str(image[i][j].symbol)
                    if image[i][j].tier==1:
                        color=color_map[image[i][j].action.effect/abs(image[i][j].action.effect)]
                    if image[i][j].tier==5:
                        color=(0, 255, 255)
                    effect = main_font.render(text, False, (255, 255, 255))
                    pygame.draw.rect(self.screen, (color), pygame.Rect(j*50,50+50*i, 50, 50))
                    self.screen.blit(effect, (j*50+15,50+50*i))
            points = main_font.render("points: "+str(self.game.points), False, (0, 0,0))
            self.screen.blit(points, (10,10))
            pygame.display.flip()
            pygame.time.wait(interval)

    def start_difficulty_selector(self, name):
        self.difficulty_selector_run=True
        self.name_view_run=False
        player_name=name
        ##One of these functions is executed when a button is pressed
        def start_hard():
            self.start_game(player_name, "hard")
        def start_medium():
            self.start_game(player_name, "medium")
        def start_easy():
            self.start_game(player_name, "easy")
        def quit():
            self.difficulty_selector_run=False

        #Create buttons for difficulties.
        hard_button = Button(rect=(250, 150, 150, 50),color=DARK_RED,function=start_hard,**HARD_BUTTON_STYLE)
        medium_button = Button(rect=(250, 250, 150, 50),color=DARK_YELLOW,function=start_medium,**MEDIUM_BUTTON_STYLE)
        easy_button = Button(rect=(250, 350, 150, 50),color=DARK_GREEN,function=start_easy,**EASY_BUTTON_STYLE)
        menu_button = Button(rect=(0, 0, 150, 50),color=DARK_YELLOW,function=quit,**MENU_BUTTON_STYLE)
        #The loop
        while self.difficulty_selector_run:
            #Go through all events to tell what the user has done
            for event in pygame.event.get():
                hard_button.check_event(event)
                if event.type == pygame.QUIT:
                    self.display_run=False
                    self.difficulty_selector_run=False
                if event.type==pygame.KEYDOWN:
                    if str(event.unicode) in " abcdefghijklmnopqrstuvwxyzoåäö"+"abcdefghijklmnopqrstuvwxyzoåäö".upper():
                        player_name+=event.unicode
                    if event.key==pygame.K_BACKSPACE:
                        player_name=player_name[:-1]
                medium_button.check_event(event)
                easy_button.check_event(event)
                menu_button.check_event(event)

            self.screen.fill((0, 0, 0))

            #text on top of the screen
            title = main_font.render(
                """Select difficulty to start game""", False, (255, 0, 0))
            self.screen.blit(title, (20, 50))
            #These methods are required to update button visuals on hover.
            hard_button.update(self.screen)
            medium_button.update(self.screen)
            easy_button.update(self.screen)
            menu_button.update(self.screen)
            pygame.display.update()

    def start_name_view(self):
        self.name_view_run=True
        player_name=""
        def select_name():
            self.start_difficulty_selector(player_name)
        def quit():
            self.name_view_run=False
        NEXT_BUTTON_STYLE=dict(DEFAULT_BUTTON_STYLE)
        NEXT_BUTTON_STYLE["text"]="Next"
        NEXT_BUTTON_STYLE["font"]=main_font
        next_button = Button(rect=(250, 400, 200, 50),color=DARK_YELLOW,function=select_name,**NEXT_BUTTON_STYLE)
        menu_button = Button(rect=(0, 0, 150, 50),color=DARK_YELLOW,function=quit,**MENU_BUTTON_STYLE)
        while self.name_view_run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.name_view_run=False
                    self.display_run=False
                if event.type==pygame.KEYDOWN:
                    if str(event.unicode) in " abcdefghijklmnopqrstuvwxyzoåäö"+"abcdefghijklmnopqrstuvwxyzoåäö".upper():
                        player_name+=event.unicode
                    if event.key==pygame.K_BACKSPACE:
                        player_name=player_name[:-1]
                next_button.check_event(event)
                menu_button.check_event(event)
            self.screen.fill((0, 0, 0))
            if len(player_name)>=1:
                next_button.update(self.screen)
            menu_button.update(self.screen)
            name_prompt=main_font.render("Your name: "+player_name, False, (255, 255, 255))
            self.screen.blit(name_prompt, (150, 80))
            pygame.display.flip()

                
    def start_ending_screen(self, points):
        self.ending_screen_run=True
        def quit():
            self.ending_screen_run=False
        menu_button = Button(rect=(250, 230, 150, 50),color=DARK_YELLOW,function=quit,**MENU_BUTTON_STYLE)
        while self.ending_screen_run:
            for event in pygame.event.get():
                pass
                if event.type==pygame.QUIT:
                    self.ending_screen_run=False
                menu_button.check_event(event)
            self.screen.fill((0, 0, 0))
            menu_button.update(self.screen)
            game_over_text=main_font.render("Game over", False, (255, 0,0))
            points_text=main_font.render("Your points: "+str(points), False, (255, 255, 255))
            self.screen.blit(game_over_text, (220, 120))
            self.screen.blit(points_text, (220, 150))

            pygame.display.flip()
            pygame.time.wait(20)

    def start_high_score(self):
        self.high_score_run=True
        page=0
        while self.high_score_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.high_score_run=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        page=min(page+1,ceil(len(self.score.all())/5)-1)
                    if event.key==pygame.K_LEFT:
                        page=max(page-1, 0)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if menu_button.collidepoint(event.pos):
                        self.high_score_run=False
            self.screen.fill((0, 0, 0))
            menu_button=pygame.draw.rect(self.screen, (255, 255,0), pygame.Rect(0, 0, 150, 50))
            menu_button_text = secondary_font.render('Back to menu', False, (255, 0, 0))
            self.screen.blit(menu_button_text, (20, 10))
            title = main_font.render('High scores', False, (255, 0, 0))
            self.screen.blit(title, (250, 20))

            page_text = main_font.render("Page {}/{}".format(
                page+1, ceil(len(self.score.all())/5)), False, (255, 0, 0))
            self.screen.blit(page_text, (550, 20))
            data = self.score.all()[page*5:page*5+5]

            for i in range(0, len(data)):
                score = "{}: {} Pts.".format(data[i][1], data[i][2])
                text = main_font.render(score, False, (255, 0, 0))
                self.screen.blit(text, (250,150+50*i))
            pygame.time.wait(300)
            pygame.display.flip()



    def run(self):
        self.display_run=True
        PLAY_BUTTON_STYLE=dict(DEFAULT_BUTTON_STYLE)
        PLAY_BUTTON_STYLE["text"]="Play"
        PLAY_BUTTON_STYLE["font"]=main_font
        HIGH_SCORE_BUTTON_STYLE=dict(HARD_BUTTON_STYLE)
        HIGH_SCORE_BUTTON_STYLE["text"]="High scores"
        play_button = Button(rect=(250, 100, 200, 50),color=DARK_YELLOW,function=self.start_name_view,**PLAY_BUTTON_STYLE)
        high_score_button = Button(rect=(250, 200, 200, 50),color=DARK_RED,function=self.start_high_score,**HIGH_SCORE_BUTTON_STYLE)
        while self.display_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.display_run=False
                if event.type == pygame.KEYDOWN:
                    pass
                play_button.check_event(event)
                high_score_button.check_event(event)

            self.screen.fill((0, 0, 0))
            title = main_font.render('Snake Ultimate', False, (255, 0, 0)) 
            play_button.update(self.screen)
            high_score_button.update(self.screen)
            self.screen.blit(title, (250, 20))
            pygame.display.flip()



