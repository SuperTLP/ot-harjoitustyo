START=[[3, 1], [3, 2], [3, 3], [3, 4]]

class Snake:
    def __init__(self, position=START):
        self.pending_blocks=0
        self.start_position=position[:]
        self.position=position[:]
        self.directions={
            0: [-1, 0],
            1: [0, 1],
            2: [1, 0],
            3: [0, -1]
        }
    def reset(self):
        self.position=self.start_position[:]
        self.pending_blocks=0

    def new_head(self, direction):
        new_head=self.position[len(self.position)-1][:]
        new_head[0]+=self.directions[direction][0]
        new_head[1]+=self.directions[direction][1]
        return new_head
    def set_position(self, position):
        self.position=[i[:] for i in position[:]]
    def set_pending_blocks(self, blocks):
        self.pending_blocks=blocks
    def advance(self, direction):
        new_head=self.new_head(direction)
        self.position.append(new_head)
        if self.pending_blocks<=0:
            del self.position[0]
        else:
            self.pending_blocks-=1
        return self.position
