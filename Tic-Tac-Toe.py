#Import Area
import random

PlayerPoints = [0, 0]
PWinTie = 0

def game_loop():
	TieRound = 1
	Deck = list(range(2, 15)) * 4
	random.shuffle(Deck)
	PlayerNames = [str(input("Please Input Player One's Name.\n")), str(input("Please Input Player Two's Name.\n"))]
	PlayerOneDeck = Deck[0:25]
	PlayerTwoDeck = Deck[26:-1]
	def compareturn(): #Compare the Two Player Cards
		PlayerCards = [PlayerOneDeck.pop(0), PlayerTwoDeck.pop(0)]
		PWinTie = ("Tie" if PlayerCards[0] == PlayerCards[1] else ("P0" if PlayerCards[0] >= PlayerCards[1] else "P1"))	
		print("It's A Tie Round!\n" if PWinTie == "Tie" and TieRound <= 2 else "") 
		print("----" + PlayerNames[0] + "----")
		print("Has Drawn A: " + str(PlayerCards[0]) + "\nAnd Has Declared War" if PlayerCards[0] <= 10 else ("Has Drawn An: Ace" if PlayerCards[0] == 14 else ("Has Drawn A: King" if PlayerCards[0] == 13 else ("Has Drawn A: Queen" if PlayerCards[0] == 12 else "Has Drawn A: Jack"))) + "\nAnd Has Declared War")
		print("\nIt's A Tie Between The Players\n" if PWinTie == "Tie" else "\n" + (str(PlayerNames[0] + " Has Won\n") if PWinTie == "P0" else "\n" + str(PlayerNames[1] + " Has Won\n")))
		print("And Has Declared War\n" + "Has Drawn A: " + str(PlayerCards[1]) if PlayerCards[1] <= 10 else ("And Has Declared War\nHas Drawn An: Ace" if PlayerCards[1] == 14 else ("And Has Declared War\nHas Drawn A: King" if PlayerCards[1] == 13 else ("And Has Declared War\nHas Drawn A: Queen" if PlayerCards[1] == 12 else "And Has Declared War\nHas Drawn A: Jack"))) + "")
		print("----" + PlayerNames[1] + "----")
		return(PWinTie)
		
		
	while not((PlayerOneDeck == []) and (PlayerTwoDeck == [])):
		Temp = compareturn()
		if Temp == "Tie":
			TieRound = ((TieRound + 1) if Temp == "Tie" else 1)
			Temp = compareturn()
		else:
			if Temp == "P0":
				PlayerPoints[0] = PlayerPoints[0] + (TieRound * 2)
			else:
				PlayerPoints[1] = PlayerPoints[1] + (TieRound * 2)
		print(PlayerNames[0] + " Has: " + str(PlayerPoints[0]) + " Points!")
		print(PlayerNames[1] + " Has: " + str(PlayerPoints[1]) + " Points!")
	print(PlayerNames[0] + " And " + PlayerNames[1] + "\nAre In A Tie" if PlayerPoints[0] == PlayerPoints[1] else (PlayerNames[0] + " Has Won The Game!" if PlayerPoints[0] >= PlayerPoints[1] else PlayerNames[1] + " Has Won The Game!"))	
game_loop()