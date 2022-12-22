class DefaultTreat:
    """instances of this class are consumable treats in the game,
    that alter snake's length by effect. Effect can be negative or positive."""
    def __init__(self, effect):
        """
        argument:
        - effect tells by how much snake's length is altered. Negative
        effect indicates snake is contracted.
        """
        self.effect=effect

    def new_pending_blocks(self,position, blocks):
        """
        argument:
        -position: position of a snake instance
        - blocks: snake instance's pending blocks

        This method calculates how much snake's pending blocks should be
        after it's length is contracted. This value is then returned.
        """
        leftover=len(position)+self.effect-1
        new_blocks=blocks+leftover
        new_blocks = max(new_blocks,0)
        return new_blocks

    def consume(self, snake):
        """
        argument:
        -snake: instance of Snake class to be modified

        This method alters snake's length by effect. Snake's position
        will first be reduced and then pending blocks will be deleted if snake's
        current length is smaller than 1 after being modified.
        """
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
