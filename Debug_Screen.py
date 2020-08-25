def DebugMenu():
	global health_level, days_left, player_name, miles_traveled, food_remaining, MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL, MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL, MIN_DAYS_PER_REST, MAX_DAYS_PER_REST, HEALTH_CHANGE_PER_REST, MAX_HEALTH, FOOD_PER_HUNT, MIN_DAYS_PER_HUNT, MAX_DAYS_PER_HUNT, FOOD_EATEN_PER_DAY, MILES_BETWEEN_NYC_AND_OREGON, DAYS_PER_ILLNESS, HEALTH_CHANGE_PER_ILLNESS

	print("""
Wellcome To The Options Menu Here You Can Change Things About The Journey.
Warning This Can Will Brake Things. Do Not Change Things In Here Unless You Know What They Do.
[func] To Use The Function Call.
Function List
DebugMenu
StartGame
StartMenu
Travel
Rest
Hunt
Status
Help
Quit
ResetVars(FuncInput)  All, Active, Stable
GameEnd(WinLose)  Win, Lose
"""
 + "miles_traveled                And The Current Value Is	" + str(miles_traveled) + "	 The default Value Is	0\n"
 + "food_remaining                And The Current Value Is	" + str(food_remaining) + "	 The default Value Is	500\n"
 + "health_level                  And The Current Value Is	" + str(health_level) + "	 The default Value Is	5\n"
 + "days_left                     And The Current Value Is	" + str(days_left) + "	 The default Value Is	300\n"
 + "player_name                   And The Current Value Is	" + str(player_name) + "	 The default Value Is	None\n"
 + "MIN_MILES_PER_TRAVEL          And The Current Value Is	" + str(MIN_MILES_PER_TRAVEL) + "	 The default Value Is	30\n"
 + "MAX_MILES_PER_TRAVEL          And The Current Value Is	" + str(MAX_MILES_PER_TRAVEL) + "	 The default Value Is	60\n"
 + "MIN_DAYS_PER_TRAVEL           And The Current Value Is	" + str(MIN_DAYS_PER_TRAVEL) + "	 The default Value Is	3\n"
 + "MAX_DAYS_PER_TRAVEL           And The Current Value Is	" + str(MAX_DAYS_PER_TRAVEL) + "	 The default Value Is	7\n"
 + "MIN_DAYS_PER_REST             And The Current Value Is	" + str(MIN_DAYS_PER_REST) + "	 The default Value Is	2\n"
 + "MAX_DAYS_PER_REST             And The Current Value Is	" + str(MAX_DAYS_PER_REST) + "	 The default Value Is	5\n"
 + "HEALTH_CHANGE_PER_REST        And The Current Value Is	" + str(HEALTH_CHANGE_PER_REST) + "	 The default Value Is	1\n"
 + "MAX_HEALTH                    And The Current Value Is	" + str(MAX_HEALTH) + "	 The default Value Is	5\n"
 + "FOOD_PER_HUNT                 And The Current Value Is	" + str(FOOD_PER_HUNT) + "	 The default Value Is	100\n"
 + "MIN_DAYS_PER_HUNT             And The Current Value Is	" + str(MIN_DAYS_PER_HUNT) + "	 The default Value Is	2\n"
 + "MAX_DAYS_PER_HUNT             And The Current Value Is	" + str(MAX_DAYS_PER_HUNT) + "	 The default Value Is	5\n"
 + "FOOD_EATEN_PER_DAY            And The Current Value Is	" + str(FOOD_EATEN_PER_DAY) + "	 The default Value Is	5\n"
 + "DAYS_PER_ILLNESS              And The Current Value Is	" + str(DAYS_PER_ILLNESS) + "	 The default Value Is	20\n"
 + "HEALTH_CHANGE_PER_ILLNESS     And The Current Value Is	" + str(HEALTH_CHANGE_PER_ILLNESS) + "	 The default Value Is	1\n"
 + "MILES_BETWEEN_NYC_AND_OREGON  And The Current Value Is " + str(MILES_BETWEEN_NYC_AND_OREGON) + "	 The default Value Is	2000\n")
	Selection = str(input("Please Input A Varible Name CAP Sencitive\n"))
	if Selection.lower() == "func":
		try:
			exec(str(input("Please Input A Function Name Be Sure To Add ()\n")))
			DebugMenu()
		except:
			print("Call Function Fail")
			DebugMenu()
	elif Selection.lower() == "runcmd":
		try:
			func = exec(str(input("Please Input A Command\n")))
			func
			DebugMenu()
		except:
			print("That Command Has Failed")
			DebugMenu()
	else:
		try:
			VarsValue = eval(input("Please Input A Value That You Want to Change the Varible To\n"))
			vars()[str(Selection)] = VarsValue 
			DebugMenu()
			
		except:
			print("Has Failed")
			DebugMenu()