import pygame
pygame.init()
pygame.font.init()

main_font = pygame.font.SysFont('Comic Sans MS', 30)

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
    def __init__(self, game):
        self.game=game
        self.screen=pygame.display.set_mode([700, 500])
        self.display_run=True
        self.game_run=False

    def start_game(self, name):
        print("nyt o peli pääl")
        self.game_run=True
        self.game.start(name)
        colormap={
            -1:(255, 0, 0),
            1: (0, 255, 0)
        }
        while self.game_run:
            for event in pygame.event.get():
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
                    if image[i][j].type=="treat":
                        if image[i][j].action.effect==0:
                            color=(255, 0, 0)
                        else:
                            color=colormap[image[i][j].action.effect/abs(image[i][j].action.effect)]
                    text=""
                    if image[i][j].type=="treat":
                        text=str(image[i][j].action.effect)
                        print(text)
                    effect = main_font.render(text, False, (255, 255, 255))
                    pygame.draw.rect(self.screen, (color), pygame.Rect(j*50,50+50*i, 50, 50))
                    self.screen.blit(effect, (j*50+15,50+50*i))
            points = main_font.render("points: "+str(self.game.points), False, (0, 0,0))
            self.screen.blit(points, (10,10))
            pygame.display.flip()
            pygame.time.wait(300)

    def run(self):
        self.display_run=True
        name=""
        while self.display_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.display_run=False
                if event.type == pygame.KEYDOWN:
                    if event.unicode in " abcdefghijklmnopqrstuvwxyzoåäöABCDEFGHIJKLMNOPQRSTUVWXYZOÅÄÖ":
                        name+=event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        name=name[:-1]
                    if event.key==pygame.K_RIGHT:
                        print("started now")
                        self.start_game(name)
            self.screen.fill((0, 0, 0))
            title = main_font.render('Snake', False, (0, 255, 0))
            help=main_font.render("Type in your name, and press right arrow to play", False,(255, 255, 255))
            help2=main_font.render("Or press arrow left to see high scores", False,(255, 255, 255))
            name_text=main_font.render(name, False, (255, 0, 0))
            self.screen.blit(title, (250,50))
            self.screen.blit(help, (0, 100))
            self.screen.blit(name_text, (300, 150))
            self.screen.blit(help2, (0, 350))
            pygame.display.flip()



