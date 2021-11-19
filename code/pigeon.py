from common import *
import textwrap as tw

class pigeonClass:
    def __init__(self, uid, name, sex, parents:list=None):
        self.uid = uid
        self.name = name
        self.age = 0 # Age in months

        self.isFemale = sex
        self.canReproduce = True
        self.isAlive = True
        self.timesBreed = 0

        self.didAct = True

        self.fluffiness = 0
        self.speed = 0
        self.size = 0

        self.parents = parents
        self.children = dict() #Dictionary of all children

    def addChild(self, child):
        #Adds child where needed
        self.children[str(child.uid)] = child

    def getGender(self):
        return "Female" if self.isFemale else "Male"

    def show(self):
        parents = ""
        if self.parents != None:
            for parent in self.parents:
                parents += f"Parent: {parent.uid}\n"

        stringyBoi = f"""\
            UID: {self.uid}
            Name: {self.name}
            Age: {self.age}
            Gender: {self.getGender()}
            Alive: {self.isAlive} {parents}
            "Fluffiness: {self.fluffiness}
            Size: {self.size}
            Speed: {self.speed}
        """

        return tw.dedent(stringyBoi)
