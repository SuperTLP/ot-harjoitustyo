class MatrixElement:
    """This is a default wrapper for all elements that appear on game_matrix. And
        contains their basic information"""
    def __init__(self, action,_type, tier, points,symbol):
        """
        arguments:
            action:
                a treat instance. Is None if the instance is not a treat.

            symbol:
                symbol displayed on GUI for this element (can also be used for
                identification)

            type:
                defines whether this block is part of snake, empty block, treat affecting
                a game instance or a treat affecting a snake instance.
                Possible values respectively:
                snake, empty, matrix_treat, treat.

            tier:
                this is a number representing how big of an impact this element has for
                the player's success. Higher tier represents greater positive impact
                and higher rarity.

            points:
                the number of points colliding with this block awards the player."""

        self.action=action
        self.symbol=symbol
        self.type=_type
        self.tier=tier
        self.points=points
        