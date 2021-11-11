from creature import *
from common import *
from random import getrandbits, randint

class daycare:
    def __init__(self, name):
        self.name = name

        self.month = 1
        self.year = 0

        self.creatures = dict()
        self.historicCreatures = dict()

        self.breedingDifficulty = 25

    def getCreatureUID(self):
        return len(self.historicCreatures)

    def createCreature(self, uid, name, sex, parents:list=None):
        newCreature = creature(uid, name, sex, parents)
        self.historicCreatures[str(newCreature.uid)] = newCreature
        self.creatures[str(newCreature.uid)] = newCreature

        return newCreature

    def generateRandomCreature(self):
        randomCreature = self.createCreature(self.getCreatureUID(), "Randy", getrandbits(1))

        return randomCreature

    def reproduce(self, parents:list, numberOfChildren:int):
        for i in range(numberOfChildren):
            uid = self.getCreatureUID()
            child = self.createCreature(uid, "Pigeon" + str(uid), getrandbits(1), parents)

            for parent in parents: #Supports more than two parents!
                parent.addChild(child)
                parent.timesBreed += 1

    def breed(self, male, female):
        tB = [female.timesBreed, male.timesBreed]
        mod = 0

        for value in tB:
            if value == 0:
                mod += 1
                break

            mod += 1 / value

        if randint(0, 100) < self.breedingDifficulty * mod:
            self.reproduce([male, female], 2)

    def death(self, target):
        del self.creatures[str(target.uid)]
        target.isAlive = False

    def update(self):
        self.month += 1

        for pigeon in self.creatures:
            pigeon = self.creatures[str(pigeon)]
            pigeon.age += 1

        print("Month: " + str(self.month))
