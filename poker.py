'''
classes to model poker card game

class card():
	rank_map
	suit_map
	att:[rank, suit],
	meth:[str, lt, gt, eq]

class Deck():
	att:[all_cards], 
	meth:[str, add_card, rem_card, shuffle, sort, move_cards]

class hand(Deck):
	att:[],
	
class PokerHand(Hand):
	hands_map
	att:[], 
	meth:[lt, gt, eq, score,beats]
	

***ranks: [None,1,2,3...., j,q,k] #ace is low (ace==1)
***suits: [clubs, diamonds, hearts, spades]
****poker_hands: {
	straight_flush:[consecutive_cards, same suits], 
	four_of_akind:[same ranks, any suits], 
	full_house:[three_of_akind and pair], 
	flush:[any cards, same suits], 
	straight:[consecutive cards, any suits], 
	three_of_akind:[3 cards of same rank, any suits], 
	two_pair:[two pairs, any suits], 
	one_pair:[2 cards of same rank, any suits], 
	high_card:[highest rank card, any suit]
	}
'''

class Card():
	"""
	Defines a card by bsuit and rank
	ranks: [None,1,2,3...., j,q,k]
	suits: [clubs, diamonds, hearts, spades]
	"""
	suit_map={k:v for (k,v) in enumerate(['Clubs','Diamonds','Hearts','Spades'])}
	rank_map={k:v for (k,v) in enumerate([str(i) for i in range(1,11)]+['Jack','Queen','King',],1)}
	
	def __init__(self, rank=1, suit=1):
		"""Initialize the card rank, suit, rasie valueError for invalid inputs"""
		if 0<rank<=13:
			self.rank=rank
		else:
			raise ValueError('card rank must be in range [1:13]')
		if 0<= suit<=3:
			self.suit=suit
		else:
			raise ValueError('card suit m ust be in range [0:3]')
	
	def __str__(self):
		"""return as tring representation of Card rank, suit"""
		if self.rank==1:
			return 'Ace of {}'.format(self.suit_map[self.suit])
		else:
			return '{} of {}'.format(self.rank_map[self.rank],self.suit_map[self.suit])
	
	def __lt__(self, other):
		return (self.suit, self.rank)<(other.suit, other.rank)
	
	def __gt__(self, other):
		return (self.suit, self.rank)>(other.suit, other.rank)
	
	def __eq__(self, other):
		return (self.suit, self.rank)==(other.suit, other.rank)
	

class Deck():
	"""Create a full cards deck, with methods [shuffle, deal, remove]"""
	import random
	
	def __init__(self):
		self.cards=None
		if self.cards is None:
			self.cards=[]
			for suit in range(4):
				for rank in range(1,14):
					self.cards.append(Card(rank, suit))
		return None
	
	def __str__(self):
		return '\n'.join([str(card) for card in self.cards])
	
	def shuffle(self):
		"""shuffles the cards, modifies the list, return None"""
		self.random.shuffle(self.cards)
		return None
	
	def sort(self):
		"""sort the cards in the deck, modifies the list, return None"""
		self.cards.sort()
		return None
	
	def deal_card(self):
		"""returns a card"""
		return self.cards.pop()
	
	def add_card(self,card):
		"""adds a card to the deck, returns None"""
		if isinstance(card, Card):
			self.cards.append(card)
		else:
			raise TypeError('Card must be a card object')
		return None
	
	def move_cards(self, hand, num):
		"""
		moves N cards from this (hand or deck) to a given (hand or deck), returns None
		"""
		if isinstance(hand,Hand) or isinstance(hand, Deck):
			for i in range(num):
				hand.add_card(self.deal_card())
		else:
			raise TypeError('hand must be either a Hand or a Deck object')
		return None


class Hand(Deck):
	"""
	defines a hand of N playing cards
	"""
	def __init__(self):
		"""initialize an empty hand"""
		self.cards=[]
		return None


class PokerHand(Deck):
	"""
	poker_hands: {
	
	straight_flush:[consecutive_cards, same suits], 
	four_of_akind:[same ranks, any suits], 
	full_house:[three_of_akind and pair], 
	flush:[any cards, same suits], 
	straight:[consecutive cards, any suits], 
	three_of_akind:[3 cards of same rank, any suits], 
	two_pair:[two pairs, any suits], 
	one_pair:[2 cards of same rank, any suits], 
	high_card:[highest rank card, any suit]
	
	}
	to determine win:
	1- compare hands (higher wins) if equal:
	2- compare card value (higher wins) else:
	tie
	"""
	hands=['high card','one pair','two pairs','three of a kind','straight','flush','full house','four of a kind','straight flush']
	score_map={k:v for (k,v) in enumerate(hands,1)}
	def __init__(self):
		self.cards=[]
		return None
	
	def hand_cards(self):
		"""returns a tuple of the cards in the hand"""
		return [(card.rank, card.suit) for card in self.cards]
	
	def flush(self):
		"""returns True if the hand is a flush"""
		return len(set([card.suit for card in self.cards]))==1
	
	def four_of_akind(self):
		"""returns true if the hand is a four of a kind"""
		return len(set([card.rank for card in self.cards]))==1
	
	def straight(self):
		"""returns True if the hand is a straight"""
		'''subtracting the smallest value in a seq of 5 numbers from all the numbers
		seq=[0,1,2,3,4] or some other order, sum of sequence is 10
		'''
		small=min(self.cards)
		return sum([(card.rank-small.rank) for card in self.cards])==10
	
	def straight_flush(self):
		"""returns True if a hand is straight flush"""
		return (self.straight() and self.flush())
	
	def rank_list(self):
		"""returns a list of card ranks"""
		return [card.rank for card in self.cards]
	
	def suit_list():
		"""returns a list of card suits"""
		return [card.suit for card in self.cards]
	
	def three_of_akind(self):
		"""returns True for three of a kind"""
		return len(set(self.rank_list()))==3
	
	def pair(self):
		"""returns True for a hand with one pair"""
		return len(set(self.rank_list()))==4
	
	def two_pairs(self):
		"""returns True for a hand with 2 pairs"""
		ranks= self.rank_list()
		tmp=set(ranks)
		freq=[ranks.count(rank) for rank in tmp]
		return freq.count(2)==2
		
	def full_house(self):
		"""returns True if a hand has a full house"""
		return len(set(self.rank_list()))==2
	
	def high_card(self):
		"""returns highest card"""
		return max(self.cards).rank



#ace=Card(1,3)
deck=Deck()
deck.shuffle()

joe=PokerHand()
deck.move_cards(joe, 4)
pete=PokerHand()
print(joe,'\n',joe.hand_cards())
#print('\n'.join(['{}:{}'.format(v,k) for (k,v) in joe.score_map.items()]))


pete.cards.append(Card(3,1))
pete.cards.append(Card(3,0))
pete.cards.append(Card(5,2))
pete.cards.append(Card(6,2))
pete.cards.append(Card(6,2))

print([eval('pete.{}()'.format(fun)) for fun in ['flush', 'four_of_akind','straight']])
print([eval('pete.{}()'.format(fun)) for fun in ['straight_flush','three_of_akind','pair']])
print([eval('pete.{}()'.format(fun)) for fun in ['two_pairs','full_house','high_card']])

#print(pete)
