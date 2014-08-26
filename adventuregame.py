class room:
	def __init__(self, name, description, monster, loot, question, answer, key, x, y):
		self.name = name
		self.description = description
		self.monster = monster
		self.loot = loot
		self.question = question
		self.answer = answer
		self.key = key
		self.x = x
		self.y = y

	def getName(self):
		print self.name
	
	def getDes(self):
		print self.description

	def getMonster(self):
		return self.monster

	def getLoot(self):
		return self.loot	

	def getQuestion(self):
		print self.question	

	def getAnswer(self):
		return self.answer
	def key(self):
		return self.key

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def printY(self):
		print 'Y cor for %s' %self.name
		print self.y
			

TDF = room('The Dark Forest', 'The forset is dark, there is a monster guarding the loot, attack the spider for the loot', 'Spider', 'Keyboard', 'How many legs does a spider have?', '8', '0', '-1', '0')
CC = room('Concrete Cave', 'Damp', 'The big Bat', 'Screen', 'Is tha bat blind (y/n)', 'y', '0', '1', '0')
Start = room('Start', 'Empty, maybe you want to walk east or west or north', '0', '0', '0', '0', '0', '0', '0')
WP = room('Wizards Palace', 'Classy', 'Wizard', 'Computer', '4 + 4', '8', '2', '0', '1')
places = [TDF, CC, Start, WP]
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

def check_cor_x():
	global new_cor, x, places, arg_cor, destination
	if new_cor > 1:
		print 'Cannot go further in this direction'
	elif new_cor < -1:
		print 'Cannot go further in this direction'
	else:
		x = new_cor
		for i in places:
			#print 'New Cor = ',
			#print x
			#i.printx()
			if i.getX() == str(x):
				destination = i 
def check_cor_y():
	global new_cor, y, places, arg_cor, destination
	if new_cor > 1:
		print 'Cannot go further in this direction'
	elif new_cor < -1:
		print 'Cannot go further in this direction'
	else:
		y = new_cor
		for i in places:
			#print 'New Cor = ',
			#print y
			#i.printY()
			if i.getY() == str(y):
				destination = i 
def move():
	global destination, new_cor, y, x
	arg_cor = str(raw_input('Which Direction? > '))
	if arg_cor == 'north':
		new_cor = y + 1
		check_cor_y()
	elif arg_cor == 'south':
		new_cor = y - 1
		check_cor_y()
	elif arg_cor == 'east':
		new_cor = x + 1
		check_cor_x()
	elif arg_cor == 'west':
		new_cor = x - 1
		check_cor_x()
	else:
		print 'Cannot go to %s' %arg	
def look():
	global destination
	if destination == 0:
		print 'This room is empty, you need to walk somewhere'
	else:
		destination.getDes()
# Here is the attack function 
def attack():
	global destination, hp, inventory, km
	if destination == 'Start':
		print 'Nothing to attack here, you need to WALK somewhere'
	elif destination.getMonster() in km:
		print "You have already slained this enemy"
	else:
		destination.getQuestion()
		answer = raw_input('> ')
		if answer == destination.getAnswer():
			print "Correct! You get the loot =)"
			inventory.append(destination.getLoot())
			km.append(destination.getMonster())
			if len(km) == 2:
				print 'Travel north to the wizard, he will help you build your computer'
		else:
			hp = hp - 2
			print 'You have lost 2 hp, remaining %s hp' %hp
def inv():
	global inventory
	print inventory

def done():
	global km
	print km	

def help():
	print 'Available commands'
	print "walk, look, attack, inv"


destination = 0
hp = 10
inventory = []
km = []
x = 0
y = 0
new_cor = 0
destination = Start
while hp > 0 and len(inventory) < 2:
	print x, y
	print 'You are now in',
	destination.getName()
	arg = str(raw_input("What is your next move? > "))
	if arg == "walk":
		move()
	elif arg == "look":
		look()
	elif arg == "attack":
		attack()
	elif arg == "inv":
		inv()
	elif arg == "help":
		help()
	elif arg == "done":
		done()	
	else:
		print 'cant do that, type help for help'
		continue