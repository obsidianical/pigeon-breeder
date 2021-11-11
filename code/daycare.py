from creature import *
from common import *
from random import getrandbits, randint

class daycare:
    def __init__(self, name):
        self.name = name

        self.creatures = dict()
        self.historicCreatures = dict()
        self.breedingGroups = dict()

    def getCreatureUID(self):
        return len(self.historicCreatures)

    def getGroupUID(self):
        return len(self.breedingGroups)

    def createCreature(self, uid, name, sex, parents:list=None):
        newCreature = creature(uid, name, sex, parents)
        self.historicCreatures[str(newCreature.uid)] = newCreature
        self.creatures[str(newCreature.uid)] = newCreature

        return newCreature

    def generateRandomCreature(self):
        randomCreature = self.createCreature(self.getCreatureUID(), "Randy", getrandbits(1))

        return randomCreature

    def updateGroups(self):
        for group in self.breedingGroups:
            for pigeon in group["all"]:
                pass

    def reproduce(self, parents:list):
        uid = self.getCreatureUID()
        child = self.createCreature(uid, "Pigeon" + str(uid), getrandbits(1), parents)
        for parent in parents: #Supports more than two parents!
            parent.addChild(child)
            parent.timesBreed += 1

    def breed(self, male, female):
        try:
            mod = (1 / female.timesBreed) + (1 / male.timesBreed)
            
        except ZeroDivisionError: # Cuz fucking zero doesn't want to play nice
            if female.timesBreed == 0 and male.timesBreed == 0:
                mod = 2
            elif female.timesBreed == 0:
                mod = 1 + (1 / male.timesBreed)
            elif male.timesBreed == 0:
                mod = (1 / female.timesBreed) + 1

        if randint(0, 100) < 25 * mod:
            self.reproduce([male, female])

    def death(self, target):
        pass

    def update(self):
        pass
