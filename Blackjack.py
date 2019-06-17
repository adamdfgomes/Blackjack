#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

class Deck():
    
    rank = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
    suit = ['Spades','Clubs','Hearts','Diamonds']

    def deal(self,no):
        x=0
        cards=[]
        while x!=no:
            cards.append(random.choice(self.rank))
            cards.append(random.choice(self.suit))
            x=x+1
        return cards
    
class Dealer():
    
    def __init__(self,balance=0):
        self.balance=balance
    
    def __str__(self):
        return 'Your balance is £({})'.format(self.balance)
        
    def Bet(self,amount):
        self.balance=self.balance-amount
        print('You have bet £{}, your balance is now £({})\n---------------'.format(amount,self.balance))
        
    def Win(self,amount):
        self.balance=self.balance+amount
        print('The dealer has paid you £{}\n---------------\nYour balance is now: £({})'.format(amount,self.balance))
        
class Player():
    
    def twist(self):
        return Deck.deal(1)
    
    def stick(self):
        print('You have stuck with your current hand')
        
class Counter():
    
    card_values={'Ace':0,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}
    
    def Blackjack(self,Phand):
        hand=[]
        for i in Phand[::2]:
            hand.append(self.card_values[i])
            s_player=sum(hand)

        if 0 in hand:
            y=0
            for i in hand:
                if i==0:
                    y=y+1
            if y==1:
                s_count=s_player+11
                if s_count>21:
                    s_count=s_player+y
            if y>1:
                s_count=s_player+y+10
                if s_count>21:
                    s_count=s_player+y
        else:
            s_count=s_player
        return s_count
        
class Game():
    
    def __init__(self,Game_name):
        self.Game_name=Game_name
    
    def play(self):
        print('Welcome to {}\n---------------'.format(self.Game_name))
        print(Dealer)
        while True:
            try:
                bet=int(input('How much would you like to bet on this hand?'))
            except:
                print('Please enter a number')
            else:
                break
        Dealer.Bet(bet)
        Phand=Deck.deal(2)
        print('You have been dealt: The {} of {} and the {} of {}'.format(Phand[0],Phand[1],Phand[2],Phand[3]))
        Dhand=Deck.deal(2)
        print('The dealer has been dealt: The {} of {} and a face down card'.format(Dhand[0],Dhand[1]))
        print('---------------')
        while True:
            s_player=Counter.Blackjack(Phand)
            if s_player==21:
                print('You have Blackjack!')
                P_go=2
            else:
                while True:
                        try:
                            P_go=int(input('Press 1 to twist, Press 2 to stick'))
                        except:
                            print('Please enter "1" or "2"')
                        else:
                            if P_go==1 or P_go==2:
                                break
                            else:
                                print('Please enter "1" or "2"')
            s_dealer=Counter.Blackjack(Dhand)
            if P_go==1:
                New_card=Player.twist()
                Phand.append(New_card[0])
                Phand.append(New_card[1])
                s_player=Counter.Blackjack(Phand)                
                print('The {} of {} has been added to your hand'.format(Phand[-2],Phand[-1]))
                if s_player>21:
                    print('You are BUST! You lose your bet!')
                    print('---------------')
                    print(Dealer)
                    break
                else:
                    print('---------------')
            elif P_go==2:               
                s_player=Counter.Blackjack(Phand) 
                print('TOTAL = {}'.format(s_player))
                print('---------------')
                print('The dealer has: The {} of {} and the {} of {}'.format(Dhand[0],Dhand[1],Dhand[2],Dhand[3]))
                print('---------------')
                while True:
                    if s_dealer==21 and s_player==21:
                        print('Both you and the dealer have Blackjack!')
                        Dealer.Win(bet)
                        break
                    elif s_dealer==21 and s_player<21:
                        print('The dealer has Blackjack and wins! You lose your bet!')
                        print('---------------')
                        print(Dealer)
                        break
                    elif s_dealer>21:
                        print('The dealer is bust! You win double your bet!')
                        Dealer.Win(bet*2)
                        break
                    elif s_dealer>s_player and s_dealer<=21:
                        print('The dealer wins! You lose your bet!')
                        print('---------------')
                        print(Dealer)
                        break
                    elif s_dealer<21 and s_dealer<=s_player:
                        New_card=Player.twist()
                        Dhand.append(New_card[0])
                        Dhand.append(New_card[1])
                        s_dealer=Counter.Blackjack(Dhand)
                        print('The {} of {} has been added to the dealers hand'.format(Dhand[-2],Dhand[-1]))
                break

Deck=Deck()
Dealer=Dealer()
Player=Player()
Counter=Counter()
Game=Game('Blackjack')

while True: 
    Game.play()
    while True:
        try:
            x=input('Want to play again?: Press any key\nWant to end the game?: Press enter\n').upper()
        except:
            print('Please enter "Yes" or press enter to end')
        else:
            break
    if x=='':
        print('Thanks for playing')
        break