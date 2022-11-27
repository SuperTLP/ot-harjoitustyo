class DefaultTreat:
    def __init__(self, effect):
        self.effect=effect
    def consume(self, snake):
        new_position=[i[:] for i in snake.position[:]]
        blocks = snake.pending_blocks
        if self.effect>=0:
            snake.set_pending_blocks(snake.pending_blocks+self.effect)
        if self.effect<0:
            if len(new_position)+self.effect>0:
                del new_position[:abs(self.effect)]
                snake.set_position(new_position)
            elif  len(snake.position)+self.effect<=0:
                leftover=len(new_position)+self.effect
                new_position=[new_position[len(new_position)-1][:]]
                blocks=blocks+leftover
                blocks = max(blocks,0)
                snake.set_pending_blocks(blocks)
                snake.set_position(new_position)
