from common import *

class creature:
    def __init__(self, uid, name, sex, parents:list=None):
        self.uid = uid
        self.name = name
        self.isFemale = sex
        self.parents = parents
        self.relations = dict()
        """
        {
            "partner":partner,
            "children":dict(),
            "isActive":bool()
        }
        """
        self.currentRelation = None
        self.children = dict() #Dictionary of all children

        self.isInRelation = False
        self.canReproduce = True
        self.isAlive = True

    def determinSpecies(self):
        
        pass

    def checkIfInRelation(self):
        if isEmpty(self.relations):
            return False #If the dictionary is empty return that they are not in a relationship

        for relation in self.relations:
            if relation["partner"].isAlive == False and relation["isActive"] == True:
                relation["isActive"] = False #Sets as false if the partner is dead, fail safe should been missed elsewhere

            if relation["isActive"] == True:
                self.currentRelation = relation
                relation["partner"].currentRelation = relation

                return True

        return False

    def addChild(self, relation, child):
        #Adds child where needed
        relation["children"][str(child.uid)] = child
        relation["partner"].children[str(child.uid)] = child
        self.children[str(child.uid)] = child
