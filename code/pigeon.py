from common import *
import textwrap as tw

class pigeonClass:
	def __init__(self, pigeonUID, name, sex, parents:list=None):
		self.uid = pigeonUID
		self.name = name
		self.age = 0 # Age in months

		self.isFemale = sex
		self.canReproduce = True
		self.isAlive = True
		self.timesBreed = 0

		self.didAct = True

		self.genetics = {
			"fluff":1,
			"speed":1,
			"size":1
		}

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
			Age: {self.age} Months
			Gender: {self.getGender()}
			Alive: {self.isAlive} {parents}
			Fluffiness: {self.genetics["fluff"]}
			Size: {self.genetics["size"]}
			Speed: {self.genetics["speed"]}"""

		return tw.dedent(stringyBoi)
