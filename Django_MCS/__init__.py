import random

'''using OOPs concept. 
Class is a blueprint of an object. 
Object is derived from class. 
It is an instance of the class. 
Which means class is a copy of object. 
An object of a class has the same attributes and functions of a class.
'''


# creating a class of a real world object
# creating class Card
class Card:
    # _init_ function is called when object of class is created
    def __init__(self, a, b):  # whenever an object encounters self it points to itself(i.e. that object only)
        self.suit = a  # creating suit attribute of class Card
        self.value = b  # creating value attribute of class Card

    def show_card(self):  # function to display a card
        if (2 <= self.value <= 10):
            print(self.value, " of ", self.suit)
        elif (self.value == 1):
            print("A of ", self.suit)
        elif (self.value == 11):
            print("J of ", self.suit)
        elif (self.value == 12):
            print("Q of ", self.suit)
        elif (self.value == 13):
            print("K of ", self.suit)


# creating a class of a real world object called Deck
class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    # function to build the deck
    def build(self):
        for s in ("Clubs", "Spades", "Diamonds", "Hearts"):
            for v in range(1, 14):
                # print("s = ",s," v = ",v)
                self.cards.append(Card(s, v))

    # function to show the deck
    def show_deck(self):
        print("-------------SHOWING DECK OF SHUFFLED CARDS---------")
        for i in self.cards:
            i.show_card()
        print("----------------------------------------------------")

    # function to shuffle the deck
    def shuffle(self):
        for i in range((len(self.cards) - 1), 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    # function to draw a card
    def draw_card(self):
        return self.cards.pop()


# creating a player class
class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    # function to show name of player
    def show_name(self):
        return self.name

    # function for player to draw a card
    def draw(self, Deck):
        self.hand.append(Deck.draw_card())

    # function to show player's hand
    def show_hand(self):
        print("SHOWING HAND OF ", self.show_name(), "-------------")
        for card in self.hand:
            card.show_card()

    # function to display sum of the cards in hand
    def display_sum_of_hand(self):
        sum = 0
        for card in self.hand:
            sum += card.value
        print("For player ", self.show_name())
        print("SUM OF HAND = ", sum)

    # function to return sum of cards in hand
    def return_sum_of_hand(self):
        sum = 0
        for card in self.hand:
            sum += card.value
        return sum


# creating a game class
class Game():

    def __init__(self, p1, p2):
        self.player1 = Player(p1)
        self.player2 = Player(p2)
        self.players = [self.player1, self.player2]

    # function to shuffle players
    def shuffle_players(self):
        first = random.randint(1, 3)
        if (first == 2):
            self.players[0], self.players[1] = self.players[1], self.players[0]
        print(self.players[0].show_name(), " goes first : ")

    # function to distribute cards to players
    def distribute(self, Deck):
        for i in range(1, 27):
            for p in self.players:
                p.draw(Deck)

    # function to show players hand after distributing cards
    def show_after_distribute(self):
        for player in self.players:
            player.show_hand()

    # function to display sum of cards
    def sum_of_cards(self):
        for player in self.players:
            player.display_sum_of_hand()

    # function to display who is winner
    def WINNER_AND_LOSER(self):
        sum1 = self.players[0].return_sum_of_hand()
        sum2 = self.players[1].return_sum_of_hand()
        if (sum1 > sum2):
            print(self.players[0].show_name(), " IS WINNER!!!")
        else:
            print(self.players[1].show_name(), " IS WINNER!!!")


# creating objects through players
CONTESTANT1 = input("Enter player 1 name : ")
CONTESTANT2 = input("Enter player 2 name : ")
game_object = Game(CONTESTANT1, CONTESTANT2)
deck_object = Deck()
deck_object.shuffle()
deck_object.show_deck()
game_object.shuffle_players()
game_object.distribute(deck_object)
game_object.show_after_distribute()
game_object.sum_of_cards()
game_object.WINNER_AND_LOSER()

# card1 = Card("Diamond",1)
# card1.show_card()
