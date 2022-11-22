class Snake:
    def __init__(self, position=[[3, 1], [3, 2], [3, 3], [3, 4]]):
        self.has_eaten=False
        self.position=position
        self.directions={
            0: [-1, 0],
            1: [0, 1],
            2: [1, 0],
            3: [0, -1]
        }
    def new_head(self, direction):
        new_head=self.position[len(self.position)-1][:]
        new_head[0]+=self.directions[direction][0]
        new_head[1]+=self.directions[direction][1]
        return new_head
    def eat(self):
        self.has_eaten=True
    def advance(self, direction):
        if not self.has_eaten:
            del self.position[0]
        self.has_eaten=False
        new_head=self.new_head(direction)
        self.position.append(new_head)
        return self.position
