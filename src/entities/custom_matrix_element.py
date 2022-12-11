class CustomMatrixElement:
    #This is an element that is used for any matrix element that is not treat.
    #This reduces the amount of classes that need to be created.
    def __init__(self, type):
        #type tells whether this element is treat, part of snake or empty block.
        #tier tells the rarity of this element. This can be used to color
        #blocks a certain way, and adjust probabilities of spawn.
        self.type=type
        self.tier=0
        