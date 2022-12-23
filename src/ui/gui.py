import pygame
from math import ceil
pygame.init()
pygame.font.init()
from pygame_button import Button
from ui.styles import (
MEDIUM_BUTTON_STYLE, HARD_BUTTON_STYLE, 
EASY_BUTTON_STYLE,DEFAULT_BUTTON_STYLE,
NEXT_BUTTON_STYLE,PREVIOUS_BUTTON_STYLE,
MENU_BUTTON_STYLE,HIGH_SCORE_BUTTON_STYLE,
PLAY_BUTTON_STYLE,
DARK_RED,DARK_GREEN,DARK_YELLOW
)
from ui.ui_config import (
    color_map,tier_color_map,difficulty_map,GAME_OVER,ACCEPTED_LETTERS
)

class View:
    """
    This class is responsible for graphical views of the game. Each method
    corresponds to a certain view.
    """
    main_font = pygame.font.SysFont('Comic Sans MS', 30)

    def __init__(self, game, score):
        """
        arguments:
            game: instance of Game class
            score: instance of Score class
        """
        self.score=score
        self.game=game
        self.screen=pygame.display.set_mode([700, 500])

    def start_game(self, name, difficulty):
        """
        This is the main game loop. Game's change_direction method is called on
        arrowkeys to change the direction the snake advances. depending on selected
        difficulty, the game updates once every 100, 200 or 300 milliseconds.

        arguments:
            name: name of the player
            difficulty: the difficulty level the game is played on.
        """

        self.game_run=True
        starting_image=self.game.start(name, difficulty)
        interval=difficulty_map[difficulty]
        started=False
        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_run=False
                    self.display_run=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.game.snake.change_direction(3)
                    if event.key == pygame.K_RIGHT:
                        self.game.snake.change_direction(1)
                        started=True
                    if event.key == pygame.K_UP:
                        self.game.snake.change_direction(0)
                    if event.key == pygame.K_DOWN:
                        self.game.snake.change_direction(2)

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
                    text=""
                    if image[i][j].type=="snake":
                        color=(255, 255, 255)
                    if image[i][j].tier!=0:
                        color=tier_color_map[image[i][j].tier]
                        text=str(image[i][j].symbol)
                    if image[i][j].tier==1:
                        color=color_map[image[i][j].action.effect/abs(image[i][j].action.effect)]

                    effect = View.main_font.render(text, False, (255, 255, 255))
                    pygame.draw.rect(self.screen, (color), pygame.Rect(j*50,50+50*i, 50, 50))
                    self.screen.blit(effect, (j*50+15,50+50*i+5))
            if not started:
                start_prompt = View.main_font.render("Press right arrowkey to start", False, (255, 255, 255)) 
                self.screen.blit(start_prompt, (200,100))
            points = View.main_font.render("points: "+str(self.game.points), False, (0, 0,0))
            self.screen.blit(points, (10,10))
            pygame.display.flip()
            pygame.time.wait(interval)

    def start_difficulty_selector(self, name):
        """
        This is loop of the view where user can select desired difficulty level.
        when a difficulty level is selected, the control transitions to the
        game loop.

        argument:
            name: name of the player.
        """

        self.difficulty_selector_run=True

        def quit():
            self.difficulty_selector_run=False

        def start_game(difficulty):
            self.difficulty_selector_run=False
            self.start_game(name, difficulty)

        buttons =[
        Button(rect=(250, 150, 150, 50),color=DARK_RED,function=lambda: start_game("hard"),**HARD_BUTTON_STYLE),
        Button(rect=(250, 250, 150, 50),color=DARK_YELLOW,function=lambda:start_game("medium"),**MEDIUM_BUTTON_STYLE),
        Button(rect=(250, 350, 150, 50),color=DARK_GREEN,function=lambda: start_game("easy"),**EASY_BUTTON_STYLE),
        Button(rect=(0, 0, 150, 50),color=DARK_YELLOW,function=quit,**MENU_BUTTON_STYLE),
        ]

        while self.difficulty_selector_run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.display_run=False
                    self.difficulty_selector_run=False
                for button in buttons:
                    button.check_event(event)

            self.screen.fill((0, 0, 0))
            title = View.main_font.render(
                """Select difficulty to start game""", False, (255, 0, 0))
            self.screen.blit(title, (20, 50))

            for button in buttons:
                button.update(self.screen)
            pygame.display.update()

    def start_name_view(self):
        """
        This is loop of the view where user can enter their name. The name is passed
        to the difficulty selection after next button is pressed.
        """

        self.name_view_run=True
        player_name=""

        def select_name():
            self.name_view_run=False
            self.start_difficulty_selector(player_name)

        def quit():
            self.name_view_run=False

        next_button = Button(rect=(250, 400, 200, 50),color=DARK_YELLOW,function=select_name,**NEXT_BUTTON_STYLE)
        menu_button = Button(rect=(0, 0, 150, 50),color=DARK_YELLOW,function=quit,**MENU_BUTTON_STYLE)

        while self.name_view_run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.name_view_run=False
                    self.display_run=False
                if event.type==pygame.KEYDOWN:
                    if str(event.unicode) in ACCEPTED_LETTERS:
                        player_name+=event.unicode
                    if event.key==pygame.K_BACKSPACE:
                        player_name=player_name[:-1]
                next_button.check_event(event)
                menu_button.check_event(event)

            self.screen.fill((0, 0, 0))
            if len(player_name)>=1:
                next_button.update(self.screen)
            menu_button.update(self.screen)
            name_prompt=View.main_font.render("Your name: "+player_name, False, (255, 255, 255))
            self.screen.blit(name_prompt, (150, 80))
            pygame.display.flip()

                
    def start_ending_screen(self, points):
        """
        This view starts after the player loses the game. On this view
        the player sees how many points he got, and can then return to main menu.

        argument:
            points: number of points the player got.
        """

        self.ending_screen_run=True

        def quit():
            self.ending_screen_run=False

        menu_button = Button(rect=(250, 230, 150, 50),color=DARK_YELLOW,function=quit,**MENU_BUTTON_STYLE)
        while self.ending_screen_run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.ending_screen_run=False
                    self.display_run=False
                menu_button.check_event(event)

            self.screen.fill((0, 0, 0))
            menu_button.update(self.screen)
            game_over_text=View.main_font.render("Game over", False, (255, 0,0))
            points_text=View.main_font.render("Your points: "+str(points), False, (255, 255, 255))
            self.screen.blit(game_over_text, (220, 120))
            self.screen.blit(points_text, (220, 150))

            pygame.display.flip()
            pygame.time.wait(20)

    def start_high_score(self):
        """
        This is the high score window loop. User can use buttons to
        navigate between windows and see scores players have gotten.
        """

        self.high_score_run=True
        self.page=0
        num_of_pages=ceil(len(self.score.all())/5)

        def next_page():
            self.page=min(self.page+1,num_of_pages-1)

        def previous_page():
            self.page=max(self.page-1, 0)

        def menu():
            self.high_score_run=False
            
        next_page_button = Button(rect=(550, 450, 150, 50),color=DARK_YELLOW,function=next_page,**NEXT_BUTTON_STYLE)
        previous_page_button=Button(rect=(0, 450, 150, 50),color=DARK_RED,function=previous_page,**PREVIOUS_BUTTON_STYLE)
        menu_button = Button(rect=(0, 0, 150, 50),color=DARK_YELLOW,function=menu,**MENU_BUTTON_STYLE)
        buttons = [next_page_button,previous_page_button,menu_button]

        while self.high_score_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.high_score_run=False
                    self.display_run=False
                for button in buttons:
                    button.check_event(event)

            self.screen.fill((0, 0, 0))
            if num_of_pages==0:
                self.page=-1
            title = View.main_font.render('High scores', False, (255, 0, 0))
            page_text = View.main_font.render("Page {}/{}".format(
                self.page+1, num_of_pages), False, (255, 0, 0))

            self.screen.blit(title, (250, 20))
            self.screen.blit(page_text, (550, 20))
            data = self.score.all()[self.page*5:self.page*5+5]

            for button in buttons:
                button.update(self.screen)

            for i in range(0, len(data)):
                score = "({}) {}: {} Pts.".format(data[i][3],data[i][1], data[i][2])
                text = View.main_font.render(score, False, (255, 0, 0))
                self.screen.blit(text, (220,150+50*i))
            pygame.display.flip()



    def run(self):
        """
        This is the main menu loop. Here the player can either continue
        to select their name or continue to inspect high scores
        """

        self.display_run=True
        play_button = Button(rect=(250, 100, 200, 50),color=DARK_YELLOW,function=self.start_name_view,**PLAY_BUTTON_STYLE)
        high_score_button = Button(rect=(250, 200, 200, 50),color=DARK_RED,function=self.start_high_score,**HIGH_SCORE_BUTTON_STYLE)

        while self.display_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.display_run=False
                play_button.check_event(event)
                high_score_button.check_event(event)

            self.screen.fill((0, 0, 0))
            title = View.main_font.render('Snake Ultimate', False, (255, 0, 0)) 
            play_button.update(self.screen)
            high_score_button.update(self.screen)
            self.screen.blit(title, (250, 20))
            pygame.display.flip()



