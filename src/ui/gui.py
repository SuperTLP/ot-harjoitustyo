import pygame
from math import ceil
pygame.init()
pygame.font.init()

main_font = pygame.font.SysFont('Comic Sans MS', 30)
secondary_font=pygame.font.SysFont('Comic Sans MS', 20)
events = pygame.event.get()

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

    def start_game(self, name):
        self.game_run=True
        self.game.start(name)
        color_map={
            -1:(255, 0, 0),
            1: (0, 255, 0)
        }
        tier_color_map={
            1: (255, 0, 0),
            2: (0, 150, 150),
            3: (200, 200, 0),
        }
        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_run=False
                if event.type == pygame.KEYDOWN:
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
            image = self.game.advance()
            if image==GAME_OVER:
                break
            for i in range(0, len(image)):
                for j in range(0, len(image[0])):
                    color=(0, 0, 0)
                    if image[i][j].type=="snake":
                        color=(255, 255, 255)
                    text=""
                    if image[i][j].tier!=0:
                        color=tier_color_map[image[i][j].tier]
                        text=str(image[i][j].effect)
                    if image[i][j].tier==1:
                        color=color_map[image[i][j].effect/abs(image[i][j].effect)]
                    if image[i][j].tier==5:
                        color=(0, 255, 255)
                    effect = main_font.render(text, False, (255, 255, 255))
                    pygame.draw.rect(self.screen, (color), pygame.Rect(j*50,50+50*i, 50, 50))
                    self.screen.blit(effect, (j*50+15,50+50*i))
            points = main_font.render("points: "+str(self.game.points), False, (0, 0,0))
            self.screen.blit(points, (10,10))
            pygame.display.flip()
            pygame.time.wait(300)

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
        options = ["Name", "Play", "High scores"]
        active_option=0
        self.display_run=True
        name=""
        while self.display_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.display_run=False
                if event.type == pygame.KEYDOWN:
                    if event.unicode in " abcdefghijklmnopqrstuvwxyzoåäöABCDEFGHIJKLMNOPQRSTUVWXYZOÅÄÖ" and options[active_option]=="Name":
                        name+=event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        name=name[:-1]
                    if event.key==pygame.K_RIGHT:
                        if options[active_option]=="Play":
                            self.start_game(name)
                        if options[active_option]=="High scores":
                            self.start_high_score()
                    if event.key==pygame.K_DOWN:
                        active_option=min(len(options)-1, active_option+1)
                    if event.key==pygame.K_UP:
                        active_option=max(0, active_option-1)

            self.screen.fill((0, 0, 0))
            title = main_font.render('Snake Ultimate', False, (255, 0, 0))
            self.screen.blit(title, (250, 20))
            for i in range(0, len(options)):
                color=(150, 150, 150)
                if active_option==i:
                    color=(255, 255, 255)
                new_text=main_font.render(options[i], False, color)
                if options[i]=="Name":
                    new_text=main_font.render(options[i]+": "+name, False, color)
                self.screen.blit(new_text, (250,200+80*i))

            pygame.display.flip()



