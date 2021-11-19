from common import *

class creature:
    def __init__(self, uid, name, sex, parents:list=None):
        self.uid = uid
        self.name = name
        self.age = 0 # Age in months

        self.isFemale = sex
        self.canReproduce = True
        self.isAlive = True
        self.timesBreed = 0

        self.acted = True

        self.parents = parents
        self.children = dict() #Dictionary of all children

    def addChild(self, child):
        #Adds child where needed
        self.children[str(child.uid)] = child

    def show(self):
        parents = ""
        if self.parents != None:
            for parent in self.parents:
                parents += "Parent: " + str(parent.uid) + "\n"

        stringyBoi = "UID: " + str(self.uid) + "\nName: " + str(self.name) + "\nAge: " + str(self.age) + "\nFemale: " + str(self.isFemale) + "\nAlive: " + str(self.isAlive) + "\n" + parents
        return stringyBoi