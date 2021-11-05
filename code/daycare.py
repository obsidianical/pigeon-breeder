from creature import *

class daycare:
    def __init__(self, name):
        self.name = name

        self.creatures = dict()
        self.historicCreatures = dict()

    def getUID(self):
        return len(self.historicCreatures)

    def createCreature(self, name, sex, parents:list=None):
        newCreature = creature(self.getUID, name, sex, parents)
        self.historicCreatures[str(newCreature.uid)] = newCreature
        self.creatures[str(newCreature.uid)] = newCreature

    def reproduce(self, target):

        pass

    def death(self, target):

        pass

    def update(self):

        pass
