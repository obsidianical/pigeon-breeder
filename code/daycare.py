from creature import *
from common import *
from random import getrandbits, randint

class daycare:
    def __init__(self, name):
        self.name = name

        self.creatures = dict()
        self.historicCreatures = dict()
        self.breedingGroups = dict()
        """
        breedingGroups = {
            groupUID:{
                "all":[List of creatures],
                "male":[List of males],
                "female":[List of females]
            }
        }
        """

    def getCreatureUID(self):
        return len(self.historicCreatures)

    def getGroupUID(self):
        return len(self.breedingGroups)

    def createCreature(self, name, sex, parents:list=None):
        newCreature = creature(self.getCreatureUID(), name, sex, parents)
        self.historicCreatures[str(newCreature.uid)] = newCreature
        self.creatures[str(newCreature.uid)] = newCreature

        return newCreature

    def generateRandomCreature(self):
        randomCreature = self.createCreature("Randy", getrandbits(1))

        return randomCreature

    def updateGroups(self):
        for group in self.breedingGroups:
            for pigeon in group["all"]:
                
                pass
            pass
        pass

    def reproduce(self, target):

        pass

    def death(self, target):

        pass

    def update(self):

        pass
