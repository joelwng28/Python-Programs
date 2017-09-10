#  File: War.py
#  Description: Simulates a game of War
#  Student's Name: Zi Zhou Wang
#  Student's UT EID: zw3948
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 6/14/2017
#  Date Last Modified: 6/14/2017

import random

# defines a Python class called Card
# @param suit identifies the card's suit
# @param rank identifies the card's number or value
# a to string method has been written for Card


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank + self.suit).rjust(4, " ")
# defines a Python class called Deck
# a to string method has been writted for Deck


class Deck:
    # fills a list with cards of ordered suit and rank
    def __init__(self):
        self.cardList = []
        suits = ["C", "D", "H", "S"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for i in range(4):
            for j in range(13):
                self.cardList.append(Card(suits[i], ranks[j]))

    # shuffles the values of the deck
    def shuffle(self):
        random.shuffle(self.cardList)

    def __str__(self):
        temp = ""
        for i in range(52):
            temp += str(self.cardList[i]).rjust(4, " ")
            if (i + 1) % 13 == 0:
                temp += "\n"
        return temp

    # deals a card from called deck to a player object
    def dealOne(self, player):
        player.hand.append(self.cardList.pop(0))
        player.handTotal += 1
# defined a Python class called Player


class Player:
    # a player object is initialized with instance variables of hand and handTotal
    def __init__(self):
        self.hand = []
        self.handTotal = 0

    # a to string method has been written for Player
    def __str__(self):
        temp = ""
        for i in range(len(self.hand)):
            temp += str(self.hand[i]).rjust(4, " ")
            if (i + 1) % 13 == 0:
                temp += "\n"
        return temp

    # determines if a player's hand is empty
    def handNotEmpty(self):
        self.handTotal = len(self.hand)
        if self.handTotal > 0:
            return True
        else:
            return False
# defines the playGame method that computes the turns of War


def playGame(player1, player2):
    # valid ranks for cards and their respective values
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    # tests for exception that player does not have the necessary amount of cards left
    round = 1
    try:
        while player1.handNotEmpty() and player2.handNotEmpty():
            index = 0
            print("ROUND", str(round) + ":")
            print("Player 1 plays:" + str(player1.hand[index]))
            print("Player 2 plays:" + str(player2.hand[index]))
            print()
            while player1.hand[index].rank == player2.hand[index].rank:
                print("War starts:" + str(player1.hand[index]), "=" + str(player2.hand[index]))
                for i in range(index + 1, index + 4):
                    print("Player 1 puts" + str(player1.hand[i]), "face down")
                    print("Player 2 puts" + str(player2.hand[i]), "face down")
                print("Player 1 puts" + str(player1.hand[index + 4]), "face up")
                print("Player 2 puts" + str(player2.hand[index + 4]), "face up")
                print()
                index += 4
            if values[player1.hand[index].rank] > values[player2.hand[index].rank]:
                print("Player 1 wins round", str(round) + ":" + str(player1.hand[index]), ">", str(player2.hand[index]))
                for i in range(index + 1):
                    player1.hand.append(player1.hand.pop(0))
                for i in range(index + 1):
                    player1.hand.append(player2.hand.pop(0))
            else:
                print("Player 2 wins round", str(round) + ":" + str(player2.hand[index]), ">", str(player1.hand[index]))
                for i in range(index + 1):
                    player2.hand.append(player1.hand.pop(0))
                for i in range(index + 1):
                    player2.hand.append(player2.hand.pop(0))
            print()
            print("Player 1 now has", str(len(player1.hand)), "card(s) in hand:")
            print(str(player1))
            print("Player 2 now has", str(len(player2.hand)), "card(s) in hand:")
            print(str(player2))
            print()
            print()
            round += 1
    # process the situation in which a player runs out of cards
    except IndexError:
        if player1.handTotal < player2.handTotal:
            temp = len(player1.hand)
            for i in range(temp):
                player2.hand.append(player1.hand.pop(0))
            for i in range(temp):
                player2.hand.append(player2.hand.pop(0))
        else:
            temp = len(player2.hand)
            for i in range(temp):
                player1.hand.append(player1.hand.pop(0))
            for i in range(temp):
                player1.hand.append(player2.hand.pop(0))


def main():
    cardDeck = Deck()  # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)  # print the deck so we can see that you built it correctly

    random.seed(15)  # leave this in for grading purposes
    cardDeck.shuffle()  # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)  # print the deck so we can see that your shuffle worked

    player1 = Player()  # create a player
    player2 = Player()  # create another player

    for i in range(26):  # deal 26 cards to each player, one at
        cardDeck.dealOne(player1)  # a time, alternating between players
        cardDeck.dealOne(player2)

    print()
    print()
    print("Initial hands:")
    print("Player 1:")
    print(player1)
    print()
    print("Player 2:")
    print(player2)
    print()
    print()

    playGame(player1, player2)

    if player1.handNotEmpty():
        print("Game over.  Player 1 wins!")
    else:
        print("Game over.  Player 2 wins!")

    print("\n\nFinal hands:")
    print("Player 1:   ")
    print(player1)  # printing a player object should print that player's hand
    print("\nPlayer 2:")
    print(player2)  # one of these players will have all of the cards, the other none


main()