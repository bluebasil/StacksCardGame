import random
from colorama import init
init()

# Suits are: 
suits = {0:"Spades", 1:"Hearts", 2:"Clubs", 3:"Diamonds"}
colors = {0:"\033[1;34m", 1:"\033[1;31m", 2:"\033[0;32m", 3:"\033[1;37m"}
value_names = {1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven",\
	8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}
reset_colors = "\033[0;0m"
#
class new_card:
	name = ""
	suit = -1
	value = -1

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
		self.name = value_names[value] + " of " + suits[suit]


def make_deck():
	#return craft_deck(test_deck)
	"""return [new_card(2,2),new_card(3,2),new_card(1,1),new_card(3,1),\
			new_card(0,6),new_card(3,7),new_card(2,11),new_card(3,9),\
			new_card(2,9),new_card(0,4),new_card(2,7),new_card(3,13),\
			new_card(1,13),new_card(0,3),new_card(0,2),new_card(3,8),\
			new_card(1,5),new_card(3,4),new_card(0,13),new_card(3,5),\
			new_card(3,11),new_card(2,10),new_card(0,7),new_card(3,10),\
			new_card(2,3),new_card(1,3),new_card(2,12),new_card(1,9),\
			new_card(0,5),new_card(0,8),new_card(1,8),new_card(0,11),\
			new_card(2,4),new_card(2,1),new_card(3,3),new_card(1,7),\
			new_card(1,4),new_card(0,12),new_card(3,12),new_card(0,1),\
			new_card(1,2),new_card(2,6),new_card(1,6),new_card(3,6),\
			new_card(2,5),new_card(1,10),new_card(2,8),new_card(2,13),\
			new_card(0,9),new_card(0,10),new_card(1,11),new_card(1,12)]"""
	deck = []

	for suit in range(4):
		for value in range(1,14):
			deck.append(new_card(suit,value))

	random.shuffle(deck)

	output_deck(deck)
	return deck

def print_card(card):
	print(colors[card.suit] + card.name)

def print_deck(deck):
	for card in deck:
		print_card(card)

def output_deck(deck):
	print("[")
	for i, card in enumerate(deck):
		print(f"({card.suit},{card.value})", end = '')
		if i != len(deck):
			print(",", end = "")
	print("]")


def craft_deck(cards):
	deck = []
	for card in cards:
		deck.insert(0,new_card(card[0],card[1]))
	return deck


test_deck = [(3,13),(3,8),(3,9),(1,3),(2,9),(0,7),(2,1),(0,6),(0,1),(3,12),(3,3),(1,13),(3,11),(1,6),(0,12),(1,8),(1,10),(2,2),(2,11),(0,5),(2,13),(3,5),(2,6),(3,1),(2,10),(3,7),(0,9),(3,6),(1,5),(2,5),(0,11),(1,12),(3,2),(1,7),(0,3),(0,4),(0,13),(1,2),(1,4),(2,8),(0,10),(2,3),(0,2),(2,7),(2,12),(1,11),(2,4),(0,8),(3,10),(1,1),(1,9),(3,4)]


