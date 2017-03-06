#!/usr/bin/python3

import sys
import datetime

from random import randint
from random import shuffle

#import sys
#sys.stdout = open("./goat.txt", "w")
#print ("test sys.stdout")

filename  = open("outputfile",'a')
sys.stdout = filename
#print("Anything printed will go to the output file")

today = datetime.datetime.today()
print(today)

Clubs = ['AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC']
Diamonds = ['AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD']
Hearts = ['AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH']
Spades = ['AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS']
Jokers = ['RJ','BJ']

Deck = Clubs+Diamonds+Hearts+Spades+Jokers

# Note: The old grey haired kings have been removed.

Deck2 = list(Deck)
Deck3 = list(Clubs)

Hand = []
Extras = []
Ticket = []
two = []
five = []

#Num = range(1, 51)
#R_Num = randint(0, 49)

shuffle(Deck2)
shuffle(Deck3)

Card = Deck2.pop()

for i in range(5):

	Card = Deck2.pop()
	Hand.append(Card)
	Num = Deck.index(Card)+1
	Ticket.append(Num)

for i in range(2):

	Card = Deck3.pop()
	Extras.append(Card)
	Num = Deck.index(Card)+1
	Ticket.append(Num)

#print(Hand),
#print(Extras)
#print(Ticket)

for i in range(2):
	a = Ticket.pop()
	two.append(a)
two.sort()

for i in range(5):
	a = Ticket.pop()
	five.append(a)
five.sort()

print(five)
print(two)
print()

