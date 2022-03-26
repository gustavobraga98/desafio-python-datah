from collections import Counter
class PokerHand():
#This class instantiate a poker Hand containing all cards that compose it, \
#and a few methods like formatting in a user-friendly way, or comparing it \
#with another hand
    def __init__(self, cards):
        self.cards = cards #Receives the string containing the cards in hand

    def format_cards(self):
        #This method returns a string containing the cards at hand \
        #formatted in a more "poker-ish" way, with suits in their \
        #Respective symbol and converting "T" to 10. 
        cards = str(self.cards)
        cards = cards.replace("S","♤")
        cards = cards.replace("H","♥")
        cards = cards.replace("D","♦")
        cards = cards.replace("C","♣")
        cards = cards.replace("T","10")
        return(cards)

    def sort_hand(self):
        #This method will break the sting received with the cards \
        #at hand and then it will sort it in descending order. \
        #E.g "AS 5H 6D 8D JS", will create a matrix (2,5) \
        #                   [[14 5 6 8 11]
        #                    [S H D D S]]
        #Containing in the first line all the converted values of cards \
        #and in the second line all the suits. \
        #Finally it will sort the values of cards descending \
        #Then:
        #                   [[14 11 8 6 5]  <- Descending order Values
        #                    [S H D D S]] <- Doesn't matter ordering suits \
        self.sortedCards = [[],[]]
        for card in self.cards.split():
            number = card[0]
            if number == "A":
                number = "14"
            if number == "K":
                number = "13"
            if number == "Q":
                number = "12"
            if number == "J":
                number = "11"
            if number == "T":
                number = "10"
            self.sortedCards[0].append(int(number))
            self.sortedCards[1].append(card[1])
            self.sortedCards[0].sort(reverse=True)
            
    def analyse_hand(self):
        #This method is responsible for analysing the hand and attributing it a categorical point
        #The points follows the order of power of plays in poker:
        # 10 - Royal Straight Flush
        #  9 - Straight Flush
        #  8 - Four of a Kind
        #  7 - Full House
        #  6 - Flush
        #  5 - Straight
        #  4 - Three of a Kind
        #  3 - Two Pair
        #  2 - Pair
        #  1 - High Card
        self.check_suits() #Checks if there is a possibility of the hand being a Flush, Straight Flush \
                           # Or a Royal Straight Flush.
        self.highCard = max(self.sortedCards[0]) #Grabs the High Card of the hand
        self.groupCards = dict(Counter(self.sortedCards[0])) #Simplifies the hand grouping cards of the same value. \
                                                             #E.g = (14, 14, 8, 8, 2) turns into {14: 2, 8:2, 5:1}
        #Down here the program will try to find the pattern that the hand fits in
        if self.same_suits == True: #If all suits are equal, than it will descend here looking \
                                    #for flushes, Straight Flushes, and Royal Straight Flushes.
            if self.sortedCards[0] == [14,13,12,11,10]:
                self.points = 10
                self.game = "Royal Straight Flush"
            elif (
                self.sortedCards[0][0] == self.sortedCards[0][1]+1 and
                self.sortedCards[0][0] == self.sortedCards[0][2]+2 and
                self.sortedCards[0][0] == self.sortedCards[0][3]+3 and
                self.sortedCards[0][0] == self.sortedCards[0][4]+4
                ):
                self.points = 9
                self.game = "Straight Flush"
            else:
                self.points = 6
                self.game = "Flush"
        else: #If the suits are not all equal, the program descend here
            self.hand = list(self.groupCards.values()) #Grabs the format of the hand \
                                                       #E.g: [2,2,2,3,5] will return \
                                                       #[3,1,1] (One Trio, one single card, one single card)
            self.hand.sort(reverse=True)
            if self.hand == [4,1]:
                self.points = 8
                self.game = "Four of a Kind"
            elif self.hand == [3,2]:
                self.points = 7
                self.game = "Full House"
            elif self.hand == [3,1,1]:
                self.points = 4
                self.game = "Three of a Kind"
            elif self.hand == [2,2,1]:
                self.points = 3
                self.game = "Two Pair"
            elif self.hand == [2,1,1,1]:
                self.points = 2
                self.game = "Pair"
            elif self.hand == [1,1,1,1,1]:
                if (
                self.sortedCards[0][0] == self.sortedCards[0][1]+1 and
                self.sortedCards[0][0] == self.sortedCards[0][2]+2 and
                self.sortedCards[0][0] == self.sortedCards[0][3]+3 and
                self.sortedCards[0][0] == self.sortedCards[0][4]+4
                ):
                    self.points = 5
                    self.game = "Straight"
                else:
                    self.points = 1
                    self.game = "High-Card"

    def check_suits(self):
    #Method responsible for checking if all suits in a hand 
    #are equal or not.
        suit = self.sortedCards[1][0] #Grab the second line of sortedCards
                                      #Remembering sorted Cards = [[value,value,value,value,value]
                                      #                              suit, suit, suit, suit, suit]
        for card in self.sortedCards[1]:
            if suit == card:
                self.same_suits = True
            else:
                self.same_suits = False
                break

    def compare_with(self,groupCards2,points2,highCard2):
        #This function altough long can be simplifies as such: \
        #If the categorial point of hand1 is higher than hand 2 \
        #Then Hand1 wins, otherwise hand1 loses. \
        #And if the categorical point of both hands are equal \
        #Then the program proceeds to find the right method to \
        #Define wich hand wins
        if self.points > points2:
            return("WIN")
        elif self.points < points2:
            return("LOSS")
        else: #Here begins the cases where categorical points are the same.
              # E.g pair vs pair
            if self.points == 10:
                return("TIE")
            elif self.points == 9:
                if self.highCard > highCard2:
                    return("WIN")
                elif self.highCard < highCard2:
                    return("LOSS")
                else:
                    return("TIE")
            elif self.points == 8:
                if self.highCard > highCard2:
                    return("WIN")
                elif self.highCard < highCard2:
                    return("LOSS")
                else:
                    return("TIE")
            elif self.points == 7:
                if self.highCard > highCard2:
                    return("WIN")
                elif self.highCard < highCard2:
                    return("LOSS")
                else:
                    return("TIE")
            elif self.points == 6:
                if self.highCard > highCard2:
                    return("WIN")
                elif self.highCard < highCard2:
                    return("LOSS")
                else:
                    #Here is a little tricky because if the the high card of \
                    #Both hands are equal, than the program keeps comparing all \
                    #The cards in descending order until it finds one card that is \
                    #greater in one hand. If that is not possible, than it's a TIE.
                    i = 0
                    hand1 = list(self.groupCards.keys())
                    hand2 = list(self.groupCards.keys())
                    while i in range(4):
                        if hand1[i] == hand2[i]:
                            pass
                            if i == 4:
                                return("TIE")
                        elif hand1[i] > hand2[i]:
                            return("WIN")
                        elif hand1[i] < hand2[i]:
                            return("LOSS")
                        i +=1
                    
            elif self.points == 5:
                if self.highCard > highCard2:
                    return("WIN")
                elif self.highCard < highCard2:
                    return("LOSS")
                else:
                    return("TIE")
            elif self.points == 4:
                keys1 = list(self.groupCards.keys())
                values1 = list(self.groupCards.values())
                keys2 = list(groupCards2.keys())
                values2 = list(groupCards2.values())
                card1 = keys1[values1.index(3)]
                card2 = keys2[values2.index(3)]
                if card1 > card2:
                    return("WIN")
                else:
                    return("LOSS")
                
            elif self.points == 3:
                keys1 = list(self.groupCards.keys())
                values1 = list(self.groupCards.values())
                keys2 = list(groupCards2.keys())
                values2 = list(groupCards2.values())
                firstPair1 = keys1[values1.index(2)]
                firstPair2 = keys2[values2.index(2)]

                if firstPair1 > firstPair2:
                    return("WIN")
                elif firstPair1 < firstPair2:
                    return("LOSS")
                else:
                    position1 = values1.index(2)
                    position2 = values2.index(2)
                    keys1.pop(position1)
                    values1.pop(position1)
                    keys2.pop(position2)
                    values2.pop(position2)
                    secondPair1 = keys1[values1.index(2)]
                    secondPair2 = keys2[values2.index(2)]
                    if secondPair1 > secondPair2:
                        return("WIN")
                    elif secondPair1 < secondPair2:
                        return("LOSS")
                    else:
                        if self.highCard > highCard2:
                            return("WIN")
                        elif self.highCard < highCard2:
                            return("LOSS")
                        else:
                            return("TIE")
            elif self.points == 2:
                keys1 = list(self.groupCards.keys())
                values1 = list(self.groupCards.values())
                keys2 = list(groupCards2.keys())
                values2 = list(groupCards2.values())
                pair1 = keys1[values1.index(2)]
                pair2 = keys2[values2.index(2)]
                if pair1 > pair2:
                    return("WIN")
                elif pair1 < pair2:
                    return("LOSS")
                else:
                    if self.highCard > highCard2:
                        return("WIN")
                    elif self.highCard < highCard2:
                        return("LOSS")
                    else:
                        for i in range(5):
                            if keys1[i] > keys2[i]:
                                return("WIN")
                            elif keys1[i] < keys2[i]:
                                return("LOSS")
                            else:
                                if i == 4:
                                    return("TIE")
                                else:
                                    pass

            
            elif self.points == 1:
                keys1 = list(self.groupCards.keys())
                values1 = list(self.groupCards.values())
                keys2 = list(groupCards2.keys())
                values2 = list(groupCards2.values())
                if self.highCard > highCard2:
                    return("WIN")
                elif self.highCard < highCard2:
                    return("LOSS")
                else:
                    for i in range(5):
                        if keys1[i] > keys2[i]:
                            return("WIN")
                        elif keys1[i] < keys2[i]:
                            return("LOSS")
                        else:
                            if i == 4:
                                return("TIE")
                            else:
                                pass