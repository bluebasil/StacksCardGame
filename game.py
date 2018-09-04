import dealer

verbose = True

#dealer.print_deck(deck)

class new_board:
	heads = None
	stacks = None

def validate(board):
	all_cards = []
	for head in board.heads.values():
		all_cards += head
	for stack in board.stacks:
		all_cards += stack
	if len(set(all_cards)) != 52:
		print("MISSING CARD(S)! (only " + len(set(all_cards)) + " accounted for)")
		#print_board(board)
	else:
		print("(deck good)")



def start():
	deck = dealer.make_deck()
	# initialize head lists
	heads = {}
	for suit in range(4):
		heads[suit] = []

	stacks = []
	while len(deck) > 0:
		stack = []
		for i in range(4):
			if len(deck) > 0:
				stack.append(deck.pop())
		stacks.append(stack)


	board = new_board()
	board.stacks = stacks
	board.heads = heads

	return board

def print_board(board):
	print("**************************")
	validate(board)
	row = ""
	for suit, head in board.heads.items():
		if len(head) > 0:
			row +=  " {:>10} ".format(dealer.colors[suit] + dealer.value_names[head[-1].value])
	print(row)
		#print(dealer.colors[suit] + dealer.value_names[suit[-1].value], end = '')
	print(dealer.reset_colors + "::::::::::::::::::::::::::")
	for stack_num, stack in enumerate(board.stacks):
		row = ""
		for card in stack:
			row += " {:>10} ".format(dealer.colors[card.suit] + str(card.value))
		print(dealer.reset_colors + "{:>4}".format(str(stack_num)) + ":  " + row)

	print(dealer.reset_colors)

def output_board(board):
	all_cards = []
	for stack in board.stacks:
		all_cards += stack
	for card in all_cards:
		print(card.suit,card.value)


def has_won(board):
	if len(board.stacks) == 0:
		return True
	else:
		return False


#print_board(board)


#operations
def to_head(board,stack_num):
	#print(stack_num, len(board.stacks))
	if len(board.stacks) <= stack_num:
		if verbose: print("Stack does not exist")
		return False
	for suit, head in board.heads.items():
		if board.stacks[stack_num][-1].suit == suit:
			
			if (len(head) == 0 and board.stacks[stack_num][-1].value == 1)\
					or (len(head) > 0 and head[-1].value + 1 == board.stacks[stack_num][-1].value):
				head.append(board.stacks[stack_num].pop())
				if len(board.stacks[stack_num]) == 0:
					board.stacks = [stack for stack in board.stacks if len(stack) != 0]
				return True
			else:
				if verbose: print("The " + board.stacks[stack_num][-1].name + " cannot be added to the head")
				return False

def move(board,from_stack,to_stack):
	if len(board.stacks) <= max(from_stack,to_stack):
		if verbose: print("Stack does not exist")
		return False
	model_suit = board.stacks[to_stack][-1].suit
	model_value = board.stacks[to_stack][-1].value - 1

	depth = -1
	for i in range(1, len(board.stacks[from_stack]) + 1):
		if board.stacks[from_stack][-i].value == model_value and \
				board.stacks[from_stack][-i].suit == model_suit:
			depth = i

	if depth == -1:
		if verbose: print("No matching card")
		return False

	#print(depth,"DEEEPTT")
	if not verbose and depth == len(board.stacks[from_stack]) and to_stack == from_stack - 1:
		return False

	if depth > 1:
		expected_value = model_value - 1
		for i in range(depth - 1,0,-1):
			if board.stacks[from_stack][-i].suit != model_suit or \
					board.stacks[from_stack][-i].value != expected_value:
				if verbose: print("Non 1 depth while not a run")
				return False
			expected_value -= 1

	#checkes all passed
	for i in range(depth,0,-1):
		board.stacks[to_stack].append(board.stacks[from_stack].pop(-i))

	if len(board.stacks[from_stack]) == 0:
		board.stacks = [stack for stack in board.stacks if len(stack) != 0]
	return True

def shift(board):
	def grab_next_card(stacks,stack_num):
		for from_stack in range(stack_num + 1,len(stacks)):
			if len(stacks[from_stack]) != 0:
				stacks[stack_num].append(stacks[from_stack].pop(0))
				return True
		return False

	shift_change = False

	for stack_num, stack in enumerate(board.stacks):
		while len(stack) < 4:
			if not grab_next_card(board.stacks,stack_num):
				#no more cards to grab
				board.stacks = [stack for stack in board.stacks if len(stack) != 0]
				return shift_change
			else:
				shift_change = True


		while len(stack) > 4:
			shift_change = True
			if stack_num + 1 == len(board.stacks):
				board.stacks.append([])
			board.stacks[stack_num + 1].insert(0,stack.pop())

	# even
	board.stacks = [stack for stack in board.stacks if len(stack) != 0]
	return shift_change
			



