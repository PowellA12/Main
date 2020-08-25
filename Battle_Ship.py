import random
complete = 0
counter = 0

  

showen = ['-', '-', '-', '-', '-', '-', '-', '-', '-',] # the borad
hidden = ['-', '-', '-', '-', '-', '-', '-', '-', '-',] # ship location

exec('''while not(hidden.count("X") == 3):\n  hidden[(random.randint(0, 8))] = "X"''')






def playborad():
  print("   A   B   C\n1  " + showen[0] + "   " + showen[1] + "   " + showen[2] + "\n2  " + showen[3] + "   " + showen[4] + "   " + showen[5] + "\n3  " + showen[6] + "   " + showen[7] + "   " + showen[8])
while (not(complete == 3)): 
	playborad()
	shipguess = list(input("Please Guess A Ship Location\n Capital Letter Then Number.\n" if counter == 0 else "Please Guess Again:\n").lower)
	counter = counter + 1
	currentguess = int(0)
	exec('''if shipguess[0] == "a":\n	  currentguess = currentguess + 0\n	elif shipguess[0] == "b":\n	  currentguess = currentguess + 1\n	elif shipguess[0] == "c":\n	  currentguess = currentguess + 2\n	if shipguess[1] == "1":\n	  currentguess = currentguess + 0\n	elif shipguess[1] == "2":\n	 currentguess = currentguess + 3\nelif shipguess[1] == "3":\n	  currentguess = currentguess + 6\n''')
	if hidden[currentguess] == "X":
	  showen[currentguess] = "X"
	  if complete == 1:
	    print("You Sunk The Jimmy's Rune\n")
	  elif complete == 2:
	    print("You Sunk The Astral Attack\n")
	  else:
	    print("You Sunk The Battle Voulge\n")
	  complete = complete + 1
	else:
	  showen[currentguess] = "O"
	  print("Splooooosh You Missed\n")
  
print("You Have Sunk all of the battle ships\n You Have Won")


