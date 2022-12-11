from entities.default_treat import DefaultTreat
from entities.flood_treat import FloodTreat
from entities.purge_treat import PurgeTreat
from entities.reverse_treat import ReverseTreat
from random import choice, randint

all_treats=[
DefaultTreat(1), DefaultTreat(1), 
DefaultTreat(1), DefaultTreat(1), 
DefaultTreat(-1), DefaultTreat(-2),
FloodTreat(), PurgeTreat(),
ReverseTreat()
]

class TreatFactory:
    #This class handles creation of entities.
    def __init__(self):
        pass
    def new_treat(self, tier):
        #This method creates a new treat of a certain tier and returns it.
        possible_treats=[treat for treat in all_treats if treat.tier==tier]
        new_treat=choice(possible_treats)
        return new_treat
    def new_random_treat(self):
        #This method creates completely random treat and returns it.
        tier=choice([1, 2, 3])
        lottery = randint(0, 50)
        if lottery!=50:
            tier=1
        new_treat=self.new_treat(tier)
        return new_treat
