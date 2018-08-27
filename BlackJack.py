# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 20:38:38 2018

@author: Michael
"""

#BLACKJACK GAME
import random

print "Lets play BlackJack!"'\n'
play = True

deck = {'Ace of Spades': 1,
        'Two of Spades': 2,
        'Three of Spades': 3,
        'Four of Spades': 4,
        'Five of Spades': 5,
        'Six of Spades': 6,
        'Seven of Spades': 7,
        'Eight of Spades': 8,
        'Nine of Spades': 9,
        'Ten of Spades': 10,
        'Jack of Spades': 10,
        'Queen of Spades': 10,
        'King of Spades': 10}

def draw():
    card_drawn = (random.sample(deck, 1)[0])
    card_value = deck.get(str(card_drawn))
    print str(card_drawn)
    return card_value

def choice(x):
    global play
    stick_twist = raw_input("Would you like to stick or twist?: ")
    if stick_twist.lower() == 'stick':
        play = False
        print "Okay lets' see what the house has..."'\n'
    elif stick_twist.lower() == 'twist':
        print "***drawing card***"
        play = True
        x = x + int(draw())
        print ("Your hands' worth %d" %x)
    if x > 21:
        play = False
        print "Oops, looks like you're bust!" 
    return x

def win_condition(y, x):    
    if y > 21:
        print "The house is bust, you win!"
    elif y == x:
        print "It's a tie! The house wins."
    elif y > x:
        print "The house wins."
    elif y < x:
        print "You win!"

def game():
    hand_value = 0
    dealer_value = 0
    print "Here's your first two cards..."
    
    for i in range(2):
        print '\n'"***drawing card***"
        hand_value = hand_value + int(draw())
    print ("Your hands' worth %d" %hand_value)
    
    while play == True:
        hand_value = int(choice(hand_value))
              
    if play == False and hand_value > 21:
        return
        
    if play == False:
        for i in range(2):
            print "***drawing card***"
            dealer_value = dealer_value + int(draw())
        print ('\n'"The house has %d" %dealer_value)    
    if dealer_value > hand_value:
        print "The house wins."  
    else:
        while dealer_value <= 16:
            print "***drawing card***"
            dealer_value = dealer_value + int(draw())
            print ("The house has %d" %dealer_value)
        win_condition(dealer_value, hand_value)
        
game()    