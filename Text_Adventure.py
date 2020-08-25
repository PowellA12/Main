## Text Monster Game
## The goal of this game is to beat the monsters and claim the prize at the end of the dungeon.

# Map of the dungeon
# Feel free to adapt and design your own level. The whole map must be at least 4 floors and 75 rooms total, though.
top_floor = [
    'prize', 'boss monster', 'sword', 'sword', 'stairs down', 'prize',
    'boss monster', 'sword', 'sword', 'stairs down', 'prize', 'boss monster',
    'sword', 'sword', 'stairs down', 'prize', 'boss monster', 'sword', 'sword',
    'stairs down', 'prize', 'boss monster', 'sword', 'sword', 'stairs down'
]
top_middle_floor = [
    'magic stones', 'monster', 'stairs down', 'empty', 'stairs up',
    'magic stones', 'monster', 'stairs down', 'empty', 'stairs up',
    'magic stones', 'monster', 'stairs down', 'empty', 'stairs up',
    'magic stones', 'monster', 'stairs down', 'empty', 'stairs up',
    'magic stones', 'monster', 'stairs down', 'empty', 'stairs up'
]
bottom_middle_floor = [
    'magic stones', 'monster', 'stairs down', 'empty', 'stairs up',
    'magic stones', 'monster', 'stairs down', 'empty', 'stairs up',
    'magic stones', 'monster', 'stairs down', 'empty', 'stairs up',
    'magic stones', 'monster', 'stairs down', 'empty', 'stairs up',
    'magic stones', 'monster', 'stairs down', 'empty', 'stairs up'
]
bottom_floor = [
    'empty', 'sword', 'stairs up', 'monster', 'empty', 'empty', 'sword',
    'stairs up', 'monster', 'empty', 'empty', 'sword', 'stairs up', 'monster',
    'empty', 'empty', 'sword', 'stairs up', 'monster', 'empty', 'empty',
    'sword', 'stairs up', 'monster', 'empty'
]

# Player's current position in the dungeon
# The player starts in the first room on floor 0
current_floor_index = 0
current_room_index = 0

# Items in the player's possession
inventory = []

# Keep track of whether the game is in progress or over (so we know when to stop the game loop)
game_state = 'ongoing'

while game_state == 'ongoing':
	# Describe the room the player is in
	if current_floor_index == 0:
		floor = bottom_floor
	elif current_floor_index == 1:
		floor = middle_floor
	else:
		floor = top_floor
	room = floor[current_room_index]

	if room == 'empty':
		print('You are in an empty room.')
	elif room == 'sword':
		print('You are in a sword room')
	elif room == 'stairs up':
		print('You are in a stairs up room')
	elif room == 'stairs down':
		print('You are in a stairs down room')
	elif room == 'monster':
		print('You are in a monster room')
	elif room == 'magic stones':
		print('You are in a magic stones room')
	elif room == 'prize':
		print('You are in a prize room')
	elif room == 'boss monster':
		print('You are in a boss monster room')

	# You need to handle describing the other cases..

	# Get command from the player
	choice = input('Command? ')

	# Respond to command
	if choice == 'help':
		print("help, grab, fight, left, right up, down, forword, back")
		pass
	elif choice == 'forword':
		if current_room_index <= 0:
			print("You Can't move left anymore")
		else:
			current_room_index = current_room_index - 1
	elif choice == 'left':
		if current_room_index <= 0:
			print("You Can't move left anymore")
		else:
			current_room_index = current_room_index - 1
	elif choice == 'left':
		if current_room_index <= 0:
			print("You Can't move left anymore")
		else:
			current_room_index = current_room_index - 1
	elif choice == 'right':
		if current_room_index >= 4:
			print("You Can't move right anymore")
		else:
			current_room_index = current_room_index + 1
	elif choice == 'up':
		if current_floor_index >= 3 and room == 'stairs up':
			print("You Can't Move up Anymore" if room == 'stairs down' or room
			      == 'stairs up' else "You Are Not In A Stair Room")
		else:
			current_floor_index = current_floor_index + 1
	elif choice == 'down':
		if current_floor_index <= 0 and room == 'stairs down':
			print("You Can't Move down Anymore" if (
			    room == 'stairs down' or room == 'stairs up'
			) else "You Are Not In A Stair Room")
		else:
			current_floor_index = current_floor_index - 1
	elif choice == 'grab':
		# Player wants to grab item from the room
		pass
	elif choice == 'fight':
		# Player wants to fight monster in the room
		pass
	else:
		print('Command not recognized. Type "help" to see all commands.')

if game_state == 'won':
	print('You won the game! :)')
else:
	print('You lost the game. :( Maybe next time.')
