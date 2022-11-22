import pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode([700, 400])
events = pygame.event.get()
class View:
    def __init__(self, game):
        self.game=game

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.game.change_direction(3)
                    if event.key == pygame.K_RIGHT:
                        self.game.change_direction(1)
                    if event.key == pygame.K_UP:
                        self.game.change_direction(0)
                    if event.key == pygame.K_DOWN:
                        self.game.change_direction(2)
            screen.fill((0, 0, 0))
            image = self.game.advance()
            for i in range(0, len(image)):
                for j in range(0, len(image[0])):
                    color=(0, 0, 0)
                    if image[i][j]==1:
                        color=(255, 255, 255)
                    if image[i][j]==2:
                        color=(255, 0, 0)
                    pygame.draw.rect(screen, (color), pygame.Rect(j*50,50*i, 50, 50))
            pygame.display.flip()
            pygame.time.wait(200)