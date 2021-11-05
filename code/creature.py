from common import *

class creature:
    def __init__(self, uid, name, sex, parents:list=None):
        self.uid = uid
        self.name = name
        self.sex = sex
        self.parents = parents
        self.relations = dict()
        """
        {
            "partner":partner,
            "children":dict(),
            "isActive":bool()
        }
        """
        self.children = dict() #Dictionary of all children

        self.isInRelation = False
        self.canReproduce = True
        self.isAlive = True

    def checkIfInRelation(self):
        if isEmpty(self.relations):
            return False #If the dictionary is empty return that they are not in a relationship

        for relation in self.relations:
            if relation["partner"].isAlive == False and relation["isActive"] == True:
                relation["isActive"] = False #Sets as false if the partner is dead, fail safe should been missed elsewhere

            if relation["isActive"] == True:
                return True

        return False

    def addChild(self, relation, child):
        #Adds child where needed
        relation["children"][str(child.uid)] = child
        relation["partner"].children[str(child.uid)] = child
        self.children[str(child.uid)] = child
