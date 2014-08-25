class room:
	def __init__(self, name, description, monster, loot, question, answer):
		self.name = name
		self.description = description
		self.monster = monster
		self.loot = loot
		self.question = question
		self.answer = answer

	def getName(self):
		print self.name
	
	def getDes(self):
		print self.description

	def getMonster(self):
		print self.monster

	def getLoot(self):
		return self.loot	

	def getQuestion(self):
		print self.question	

	def getAnswer(self):
		return self.answer
			

TDF = room('The Dark Forest', 'The forset is dark, there is a monster guarding the loot, attack the spider for the loot', 'Spider', 'Keyboard', 'How many legs does a spider have?', '8')
CC = room('Concrete Cave', 'Damp', 'The big Bat', 'Screen', 'Is tha bat blind', 'YES')
# Here is the walk function
def walk():
	global destination
	arg = str(raw_input('left or right? > '))
	if arg == "left":
		destination = TDF
	elif arg == "right":
		destination = CC
	print "You are now in the",
	destination.getName()

def look():
	global destination
	destination.getDes()
# Here is the attack function 
def attack():
	global destination, hp, inventory
	destination.getQuestion()
	answer = raw_input('> ')
	if answer == destination.getAnswer():
		print "Correct! You get the loot =)"
		inventory.append(destination.getLoot())
	else:
		hp = hp - 2
		print 'You have lost 2 hp, remaining %s hp' %hp
def inv():
	global inventory
	print inventory


destination = 0
hp = 10
inventory = []

while hp > 0 and len(inventory) < 2:
	arg = str(raw_input("What is your next move? > "))
	if arg == "walk":
		walk()
	elif arg == "look":
		look()
	elif arg == "attack":
		attack()
	elif arg == "inv":
		inv()
