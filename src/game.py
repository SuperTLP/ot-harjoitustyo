GAME_OVER=[[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2],
        [0, 2, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0]]
from random import randint
class Game:
    def __init__(self, snake, map=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        ):
        self.map=map
        self.active_treat=True
        self.snake=snake
        self.direction=1
        self.game_over=False
        for i in snake.position:
            self.map[i[0]][i[1]]=1
    def change_direction(self, direction):
        self.direction=direction
    def start(self):
        self.game_over=False
    def out_out_bounds(self, head):  
        return (head[1]<0 or head[0]>=len(self.map) or head[0]<0 or head[1]>=len(self.map[0]))
    def square_is_free(self, coordinates):
        return self.map[coordinates[0]][coordinates[1]]!=1
    def clear_map(self):
        for i in self.map:
            for j in range(0, len(i)):
                if i[j]==1:
                    i[j]=0
    def eat_treat(self):
        success=False
        while success==False:
            x=randint(0, len(self.map)-1)
            y=randint(0, len(self.map[0])-1)
            if self.map[x][y]!=1:
                self.snake.eat()
                self.map[x][y]=2
                success=True
    def is_treat(self, head):
        if self.map[head[0]][head[1]]==2:
            return True
    def update_map(self,snake): 
        for i in range(0, len(snake)):
            self.map[snake[i][0]][snake[i][1]]=1

    def advance(self):

        snake_image = self.snake.advance(self.direction)
        head = snake_image[len(snake_image)-1]
        if self.out_out_bounds(head) or not self.square_is_free(head):
            self.game_over=True
        if self.game_over:
            return GAME_OVER
        if self.is_treat(head):
            self.eat_treat()
        self.clear_map()
        self.update_map(snake_image)
        return self.map
        

        
    

