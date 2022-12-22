class DefaultTreat:
    """instances of this class are consumable treats in the game,
    that alter snake's length by effect. Effect can be negative or positive."""
    def __init__(self, effect):
        self.effect=effect
        self.type="treat"
        self.points=1
        self.tier=1
    def new_pending_blocks(self,position, blocks):
        """Calculate how much snakes pending blocks should be after consumption."""
        leftover=len(position)+self.effect-1
        new_blocks=blocks+leftover
        new_blocks = max(new_blocks,0)
        return new_blocks
    def consume(self, snake):
        """This method changes the snake's length depending on
        effect. If effect is greater than or equal to 0, this amount will
        be added to snake's pending blocks. Snake will then extend itself.
        If effect is negative, snake's length will first be reduced by removing
        elements from snake's position. Then pending blocks will be removed
        if the effect would make snake's position shorter than 1 block."""
        new_position=[i[:] for i in snake.position[:]]
        blocks = snake.pending_blocks
        if self.effect>=0:
            snake.set_pending_blocks(snake.pending_blocks+self.effect)
            return
        if len(new_position)+self.effect>0:
            del new_position[:abs(self.effect)]
            snake.set_position(new_position)
        elif len(snake.position)+self.effect<=0:
            snake.set_pending_blocks(self.new_pending_blocks(new_position,blocks))
            new_position=[new_position[-1][:]]
            snake.set_position(new_position)
