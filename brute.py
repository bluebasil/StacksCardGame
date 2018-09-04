import game
import dealer
from copy import deepcopy

game.verbose = False

board = game.start()
#game.output_board(board)
game.print_board(board)

def recurse(board, moves):
	#print(len(moves))
	if game.has_won(board):
		print(len(moves), " moves")
		print(moves)
		exit()
	elif len(moves)> 200:
		print("ERR?")
		print(moves)
		return
	if len(moves) == 52:
		print(".", end = '')
	# Head all

	for from_stack in range(len(board.stacks)):
		f = deepcopy(board)
		if game.to_head(f,from_stack):
			new_moves = deepcopy(moves)
			new_moves.append(f"h {from_stack}")
			recurse(f,new_moves)

		for to_stack in range(len(board.stacks)):
			
			t = deepcopy(board)
			if game.move(t,from_stack,to_stack):
				new_moves = deepcopy(moves)
				new_moves.append(f"m {from_stack} {to_stack}")
				recurse(t,new_moves)

	s = deepcopy(board)
	if game.shift(s):
		new_moves = deepcopy(moves)
		new_moves.append(f"s")
		recurse(s,new_moves)


	
recurse(board,[])