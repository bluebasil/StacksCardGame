import game
from copy import deepcopy

game.verbose = True

board = game.start()
state_list = []
change = True

while True:
	if change:
		game.print_board(board)
		state_list.append(deepcopy(board))
	change = False
	move = input("awaiting move: ").split(" ")
	if move[0] == 's':
		game.shift(board)
		change = True
	elif move[0] == 'h':
		if len(move) != 2:
			print("invalid arguments")
			continue
		game.to_head(board,int(move[1]))
		change = True
	elif move[0] == 'm':
		if len(move) != 3:
			print("invalid arguments")
			continue
		else:
			game.move(board,int(move[1]),int(move[2]))
			change = True
	elif move[0] == 'p':
		game.print_board(board)
	elif move[0] == 'u':
		state_list.pop()
		board = state_list[-1]
		game.print_board(board)

	if game.has_won(board):
		print("YOU WIN!")
		exit()
		