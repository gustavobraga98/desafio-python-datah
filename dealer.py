import random
from PokerHand import PokerHand
class Dealer():
#Dealer Class was created to operate the game after the cards were drawn
#It is responsible for telling if the Hand being compared Wins or Lose.
#it can aswell generate a pair of hands just like in a real cards's deck
    def __init__(self):
        #__init__ method only generates a deck of cards wich will be used to drawn cards.
        self.cardsDeck = (
            [
            "2S","3S","4S","5S","6S","7S","8S","9S","TS","JS","QS","KS","AS",
            "2H","3H","4H","5H","6H","7H","8H","9H","TH","JH","QH","KH","AH",
            "2D","3D","4D","5D","6D","7D","8D","9D","TD","JD","QD","KD","AD",
            "2C","3C","4C","5C","6C","7C","8C","9C","TC","JC","QC","KC","AC"
             ]
            )
    
    def deal(self):
    #This method draws from the self.cardsDeck two hands containing 5 cards each
    #and returns it as a string.
        self.__init__()
        deck = self.cardsDeck #Instantiate a copy of self.cardsDeck
        self.hand1 = ""
        self.hand2 = ""
        #For loop draws a card from deck and instantly make that specific card
        #unavailable to be drawn, thus avoiding two hands with the same card
        for i in range(5):
            self.hand1+=deck.pop(random.randint(0,len(deck)-1))
            self.hand2+=deck.pop(random.randint(0,len(deck)-1))
            if i == 4:
                break
            self.hand1+=" "
            self.hand2+=" "
        return (self.hand1, self.hand2)
    
    def display_game(self):
    #This method is responsible for displaying the actual game in a user-friendly way.
        self.formattedhand1 = self.hand1.format_cards() #Calls for the format_cards method in PokerHand Class \
        self.formattedhand2 = self.hand2.format_cards() #format_cards will transform the data into a user-friendly way of reading \
                                                        #like changing "S" for ♤
        print("({0}) [{1}]   VS   ({2}) [{3}]".format(self.formattedhand1,self.hand1.game,self.formattedhand2,self.hand2.game))
        print("")
        print("Hand 1: {}!".format(self.result))

    def play(self,pokerHand1,pokerHand2,verbose = True):
    #This method receives both poker hands and compare them
    #Finally it returns the result (if the first hand beats the second)
    #Thus:
    #If First Hand beats Second - WIN
    #If Second Hand beats Second - Lose
            self.hand1 = PokerHand(pokerHand1)
            self.hand1.sort_hand()
            self.hand1.analyse_hand()
            self.hand2 = PokerHand(pokerHand2)
            self.hand2.sort_hand()
            self.hand2.analyse_hand()
            self.result = self.hand1.compare_with(self.hand2.groupCards,self.hand2.points,self.hand2.highCard)
            if verbose == True:         #This works just for the "run_tests" in the menuClass. \
                self.display_game()     #If the user asks to display the game it will display it user-friendly \
                return (self.result)    #Both hands and the result 
            else:                       #If the user asks to display only the result the program will just output \
                return(self.result)     #A sequence of prints with just True or False in case the program judged \
                                        #The hands right or wrong.