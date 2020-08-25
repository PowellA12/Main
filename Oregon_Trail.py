import random
from DeBug import DebugMenu
DM = False #Change To True To Enable The DebugMenu WIP
Selection = None
health_level = 5
days_left = 300
player_name = "Null"
miles_traveled = 0
food_remaining = 500

MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7


MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5

FOOD_PER_HUNT = 100
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5

FOOD_EATEN_PER_DAY = 5
DAYS_PER_ILLNESS = 20
HEALTH_CHANGE_PER_ILLNESS = 1

MILES_BETWEEN_NYC_AND_OREGON = 2000



##################
def StartMenu():
	print("""
Welcome to the Oregon Trail! The year is 1850 and Americans are
headed out West to populate the frontier. Your goal is to travel
by wagon train from Independence, MO to Oregon (2000 miles). You start
on March 1st, and your goal is to reach Oregon within 300 days.
The trail is arduous. Each day costs you food and health. You
can hunt and rest, but you have to get there before winter! Type Help If You Don't Know The Commands
""")
	if DM:
		Selection = str(input("\n\n		Start Game\n		Press Enter to Begain\n		Options\Debug Menu [D]\n")).lower()
		if "d" == Selection:
			DebugMenu()
		else:
			StartGame()
	else:
		input("\n\n			Start Game\n		Press Enter to Begain\n")
		StartGame()
######################
def GameEnd(WinLose):
	global health_level, food_remaining, days_left, player_name
	if WinLose == "Win":
		print("Great Job " + player_name)
		print("You Have Made It To The End With Stats Of")
		
	elif WinLose == "Lose":
		if health_level <= 0:
			print("You Have Died From Heath Being To Low. With Stats of")
		elif food_remaining <= 0:
			print("You Have Died From Hunger Being To Low. With Stats of")
		elif days_left <= 0:
			print("You Have Ran Out Of Days To Make it. With Stats of")
	
	print(Status())
	if input("1 To Restart And Reset Or AnyChar To Restart\n") == 1:
		ResetVars("All")
		StartMenu()
	else:
		ResetVars("Active")
		StartMenu()
def CmdFind():
	Command = str(input("Please Input a command\n")).lower()
	if Command == "t" or Command == "travel":
		Travel()
	elif Command == "r" or Command == "rest":
		Rest()
	elif Command == "h" or Command == "hunt":
		Hunt()
	elif Command == "s" or Command == "status":
		print(Status())
		CmdFind()
	elif Command == "?" or Command == "help":
		Help()
	elif Command == "q" or Command == "quit":
		Quit()
	elif (Command == "d" or Command == "debug") and DM:
		DebugMenu()
	else:
		print("That Is An Invalid Input")
		CmdFind()
	
def Status():
	return("You have Traveled " + str(miles_traveled) + " Miles\n"
 + "You Have " + str(food_remaining) + " Food Remaining\n"
 + "Your Heath is " + str(health_level) + "\n"
 + "You Have " + str(days_left) + " Days Left\n"
 + "And Your Name Still Is " + player_name + "\n")

def Help(): 
	print("""
Each turn you can take one of 3 actions:

  travel - moves you randomly between 30-60 miles and takes
           3-7 days (random).
  rest   - increases health 1 level (up to 5 maximum) and takes
           2-5 days (random).
  hunt   - adds 100 lbs of food and takes 2-5 days (random).

When prompted for an action, you can also enter one of these
commands without using up your turn:

  status - lists food, health, distance traveled, and day.
  help   - lists all the commands.
  quit   - will end the game.
  
You can also use these shortcuts for commands:

  't', 'r', 'h', 's', '?', 'q'
  
""")

	return
def Quit():
	StartMenu()
########################	
def Travel():
	global miles_traveled, days_left, food_remaining, MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL, MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL, FOOD_EATEN_PER_DAY
	PMTT = str(random.randint(MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL))
	PDPT = str(random.randint(MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL))
	miles_traveled = miles_traveled + int(PMTT)
	days_left = days_left - int(PDPT)
	food_remaining = food_remaining - FOOD_EATEN_PER_DAY * int(PDPT)
	print("You Have Traveled " + str(PMTT) + " Miles")
	print("You Have Traveled For " + str(PDPT) + " Days" )
	print("You Have Eaten " + str(FOOD_EATEN_PER_DAY * int(PDPT)) + " Pounds of Food While Traveling")
	GameTurn()
############
def Rest():
	global health_level, food_remaining, MIN_DAYS_PER_REST, MAX_DAYS_PER_REST, MAX_HEALTH, HEALTH_CHANGE_PER_REST, FOOD_EATEN_PER_DAY, days_left
	if not health_level >= 5:
		health_level = health_level + int(HEALTH_CHANGE_PER_REST)
		print("You Have Gained " + str(HEALTH_CHANGE_PER_REST) + " Health.")
		PDPT = str(random.randint(MIN_DAYS_PER_REST, MAX_DAYS_PER_REST))
		days_left = days_left - int(PDPT)
		food_remaining = food_remaining - FOOD_EATEN_PER_DAY * (int(PDPT) // 2)
		print("You Have Rested For " + str(PDPT) + " Days." )
		print("You Have Eaten " + str(FOOD_EATEN_PER_DAY * int(PDPT)) + " Pounds of Food While Resting.")
		GameTurn()
	else:
		print("Your Heath Is Alreadly Max You Can Not Rest At This Time")
		CmdFind()
############
def Hunt():
	global days_left, food_remaining, MAX_DAYS_PER_HUNT, MIN_DAYS_PER_HUNT, FOOD_PER_HUNT
	PDPH = str(random.randint(MIN_DAYS_PER_HUNT, MAX_DAYS_PER_HUNT))
	days_left = days_left - int(PDPH)
	food_remaining = food_remaining - FOOD_EATEN_PER_DAY * int(PDPH)
	food_remaining = food_remaining + FOOD_PER_HUNT
	print("You Have Gained " + str(FOOD_PER_HUNT) + " Pounds Of Food.")
	print("You Have Hunted For " + str(PDPH) + " Days." )
	print("You Have Eaten " + str(FOOD_EATEN_PER_DAY * int(PDPH)) + " Pounds of Food While Hunting.")
	print("In Total You Have Gained " + str(int(FOOD_PER_HUNT - FOOD_EATEN_PER_DAY * int(PDPH))) + " Pounds Of Food.")
	GameTurn()
###########

###########
def StartGame():
	global player_name
	player_name = str(input("What Is Your Name?\nMy Name Is "))
	print("Good Luck Out There " + str(player_name))
	GameTurn()
def GameTurn():
	global DAYS_PER_ILLNESS, miles_traveled, food_remaining, health_level, days_left, MILES_BETWEEN_NYC_AND_OREGON, HEALTH_CHANGE_PER_ILLNESS, player_name
	if random.randint(0, DAYS_PER_ILLNESS) == 15:
		health_level = health_level - HEALTH_CHANGE_PER_ILLNESS
		print("You Have Lost " + str(HEALTH_CHANGE_PER_ILLNESS) + " Health Due To Illness")
	if health_level <= 0 or food_remaining <= 0 or days_left <= 0:
		GameEnd("Lose")
	elif miles_traveled >= MILES_BETWEEN_NYC_AND_OREGON:
		GameEnd("Win")
	else:
		print("Please Make An Action " + player_name)
		CmdFind()



######################
def ResetVars(FuncInput):#vaild inputs are. All, Active, Stable
	global health_level, days_left, player_name, miles_traveled, food_remaining, MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL, MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL, MIN_DAYS_PER_REST, MAX_DAYS_PER_REST, HEALTH_CHANGE_PER_REST, MAX_HEALTH, FOOD_PER_HUNT, MIN_DAYS_PER_HUNT, MAX_DAYS_PER_HUNT, FOOD_EATEN_PER_DAY, MILES_BETWEEN_NYC_AND_OREGON, DAYS_PER_ILLNESS, HEALTH_CHANGE_PER_ILLNESS

	if FuncInput == "All" or FuncInput == "Active":
		health_level = 5
		days_left = 300
		player_name = "Null"
		miles_traveled = 0
		food_remaining = 500
	if FuncInput == "All" or FuncInput == "Stable":
		MIN_MILES_PER_TRAVEL = 30
		MAX_MILES_PER_TRAVEL = 60
		MIN_DAYS_PER_TRAVEL = 3
		MAX_DAYS_PER_TRAVEL = 7


		MIN_DAYS_PER_REST = 2
		MAX_DAYS_PER_REST = 5
		HEALTH_CHANGE_PER_REST = 1
		MAX_HEALTH = 5

		FOOD_PER_HUNT = 100
		MIN_DAYS_PER_HUNT = 2
		MAX_DAYS_PER_HUNT = 5

		FOOD_EATEN_PER_DAY = 5
		DAYS_PER_ILLNESS = 20
		HEALTH_CHANGE_PER_ILLNESS = 1
		MILES_BETWEEN_NYC_AND_OREGON = 2000








