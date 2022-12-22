from random import choice, randint
from entities.default_treat import DefaultTreat
from entities.flood_treat import FloodTreat
from entities.purge_treat import PurgeTreat
from entities.reverse_treat import ReverseTreat
from entities.matrix_element import MatrixElement

all_treats=[
MatrixElement(DefaultTreat(1), "treat", 1, 1, 1),
MatrixElement(DefaultTreat(1),"treat", 1, 1, 1),
MatrixElement(DefaultTreat(1),"treat", 1, 1, 1),
MatrixElement(DefaultTreat(1),"treat", 1, 1, 1),
MatrixElement(DefaultTreat(-1),"treat", 1, 1, -1),
MatrixElement(DefaultTreat(-2),"treat", 1, 1, -2),
MatrixElement(FloodTreat(),"matrix_treat",3,40,"$"),
MatrixElement(PurgeTreat(),"matrix_treat",2,20,"X"),
MatrixElement(ReverseTreat(),"treat", 2,20,"<-")
]

class TreatFactory:
    #This class handles creation of treats
    def __init__(self):
        pass
    def new_treat(self, tier):
        #This method creates a new treat of a certain tier and returns it.
        possible_treats=[treat for treat in all_treats if treat.tier==tier]
        new_treat=choice(possible_treats)
        return new_treat
    def new_random_treat(self):
        #This method selects a random tier for treat and selects a random
        #treat of that tier.
        tier=1
        lottery = randint(0, 150)
        if lottery in [148, 149]:
            tier=2
        if lottery==150:
            tier=3
        new_treat=self.new_treat(tier)
        return new_treat
