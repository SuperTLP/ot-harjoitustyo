class DefaultTreat:
    """instances of this class are consumable treats in the game,
    that give one point each and either extend or contract snake
    length by effect."""
    def __init__(self, effect):
        """
        These class-variables are used by all treats in the game.
        - Effect is the symbol displayed on a treat
        - Type tells what kind of element this object is. It is used
        for example, to differentiate between snake block, empty block and a treat.
        - points defines how many points consuming this candy awards to the player.
        - tier tells how rare and how useful this candy is to the player. Higher
        tier means greater help in playing."""
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
