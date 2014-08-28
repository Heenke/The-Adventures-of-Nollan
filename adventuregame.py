import time

class room:
	def __init__(self, name, description, monster_nick, key, x, y):
		self.name = name
		self.description = description
		self.monster_nick = monster_nick
		self.key = key
		self.x = x
		self.y = y

	def getName(self):
		print self.name
	
	def getDes(self):
		print self.description

	def getMonster(self):
		return self.monster_nick

	def getKey(self):
		return self.key

	def printKey(self):
		print self.key

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def printY(self):
		print 'Y cor for %s' %self.name
		print self.y

class monster:
	def __init__(self, enemy, loot, question, answer):
		self.enemy = enemy
		self.loot = loot
		self.question = question
		self. answer = answer

	def getEnemy(self):
		print self.enemy

	def getLoot(self):
		return self.loot	

	def getQuestion(self):
		print self.question	

	def getAnswer(self):
		return self.answer

Sp = monster('The Creepy Spider', 'Keyboard', 'How many legs does a spider have?', '8')
Tbb = monster('The big Bat', 'Screen', 'Is tha bat blind (y/n)', 'y')
Wk = monster('Wizard King', 'Computer', '4 + 4', '8')

TDF = room('The Dark Forest', 'The forest is dark, there is a monster guarding the loot, attack the spider for the loot', Sp, '0', '-1', '0')
CC = room('Concrete Cave', 'The caves are deep and narrow, there is a Big Bat guarding the loot', Tbb, '0', '1', '0')
Start = room('Start', 'Empty, maybe you want to walk east or west or north', 0, '0', '0', '0')
WP = room('Wizards Palace', 'Classy', Wk, '2', '0', '1')

places = [TDF, CC, Start, WP]

def check_cor_x():
	global new_cor, y, x, places, arg_cor, destination, km
	if new_cor > 1:
		print 'Cannot go further in this direction'
	elif new_cor < -1:
		print 'Cannot go further in this direction'
	else:
		for i in places:
			if i.getX() == str(new_cor) and i.getY() == str(y):
				if len(km) >= int(i.getKey()):
					destination = i
					x = new_cor
				else:
					print 'Kill more enemies first and get more loot'
					print 'You need %s' %int(i.getKey()),
					print 'to go there, check you inventory by typing inv'

def check_cor_y():
	global new_cor, y, x, places, arg_cor, destination, km
	if new_cor > 1:
		print 'Cannot go further in this direction'
	elif new_cor < -1:
		print 'Cannot go further in this direction'
	else:
		for i in places:
			if i.getY() == str(new_cor) and i.getX() == str(x):
				if len(km) >= int(i.getKey()):
					destination = i
					y = new_cor
				else:
					print 'Kill more enemies first and get more loot'
					print 'You need %s' %int(i.getKey()),
					print 'to go there, check you inventory by typing inv'
def move():
	global destination, new_cor, x, y
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
		print 'Cannot go to %s' %arg_cor	

def look():
	global destination
	if destination == 0:
		print 'This room is empty, you need to walk somewhere'
	else:
		destination.getDes()

# Here is the attack function 
def attack():
	global destination, hp, inventory, km
	if destination == Start:
		print 'Nothing to attack here, you need to WALK somewhere'
	elif destination.getMonster() in km:
		print "You have already slained this enemy"
	else:
		att_enemy = destination.getMonster()
		att_enemy.getQuestion()
		answer = raw_input('> ')
		if answer == att_enemy.getAnswer():
			print "Correct! You get the loot =)"
			inventory.append(att_enemy.getLoot())
			km.append(destination.getMonster())
			if len(km) == 2:
				print 'Travel north to the Palace and battle the mighty Wizard'
		else:
			hp = hp - 2
			print 'You have lost 2 hp, remaining %s hp' %hp
def inv():
	global inventory
	if len(inventory) == 0:
		print 'It is empty...'
	else:
		print inventory

def done():
	global km
	print km	

def help():
	print 'Available commands'
	print "walk, look, attack, inv"

hp = 10
inventory = []
km = []
x = 0
y = 0
new_cor = 0
destination = Start
newdestination = 0

print 'Welcome to The adventures of Nollan'
time.sleep(1)
print 'To navigate through the world type walk and then east, west or north'
time.sleep(1)
print 'The quest is to collect the loot from The Dark Forest in the west and'
time.sleep(1)
print 'the loot from Concrete Caves in the east'
time.sleep(1)
print 'When you have all the parts it is time to battle the Wizard in his Palace in the north'
time.sleep(1)
while hp > 0:
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