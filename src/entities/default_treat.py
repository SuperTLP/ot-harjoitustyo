class DefaultTreat:
    """instances of this class are consumable treats in the game,
    that give one point each and either extend or contract snake
    length by effect."""
    def __init__(self, effect):
        self.effect=effect
        self.type="treat"
        self.points=1
        self.tier=1
    def consume(self, snake):
        """This method changes the snake's length depending on
        effect."""
        new_position=[i[:] for i in snake.position[:]]
        blocks = snake.pending_blocks
        if self.effect>=0:
            snake.set_pending_blocks(snake.pending_blocks+self.effect)
        if self.effect<0:
            if len(new_position)+self.effect>0:
                del new_position[:abs(self.effect)]
                snake.set_position(new_position)
            elif  len(snake.position)+self.effect<=0:
                leftover=min(len(new_position)+self.effect, 0)
                new_position=[new_position[len(new_position)-1][:]]
                blocks=blocks+leftover
                blocks = max(blocks,0)
                snake.set_pending_blocks(blocks)
                snake.set_position(new_position)
