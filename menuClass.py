import os
from dealer import Dealer

#Menu Class is responsible for showing the interface for the user
#It also is responsible for getting input from the user and directing him to the right interface

class Menu():
    def __init__(self):
        self.option = None
        self.dealer = Dealer() #Creates a dealer class which is responsible for controlling the poker game

    def clean_screen(self):
    #This function as its name stands for, its responsible for cleaning the screen
    #it works for Unix, Windows and MAC, and it even has an urgency mode if the command
    #does not work.
        
        success = os.system("clear") #Try for Unix and MAC system
        if success == 0:
            pass
        else:
            success = os.system("cls") #Tries for Windows System
            if success == 0:
                pass
            else:
                print("\
                The program faced some issues trying to clean the\
                screen. Going back to the main menu with an override"
                    )
                print("\n"*100)
                print("-"*100)
                pass

    def dealer_draws(self):
    #This function will generate two sets of hands whithout repeating the cards
    #and then it will compare it
        self.hand1, self.hand2 = self.dealer.deal() #Calls the function that will generate both hands
        self.dealer.play(self.hand1, self.hand2) #Calls the method that display both hands and gives the result
        print("")
        print(" ♣ ♤ ♥ ♦"*10) #Displays a nice divider to make the interface cooler
        input("Press any Key to continue")

    def manually_play(self):
    #This function ables the user to input two hands manually and then proceeds to compare them
        print("Input 5 cards separated by a space")
        print("E.g = AS 5H 6D 8D JS")
        self.hand1 = input("First Hand =>") #Receives the first hand
        self.hand2 = input("Second Hand =>") #Receives the first hand
        self.dealer.play(self.hand1, self.hand2) #Calls the method that display both hands and gives the result
        print("")
        print(" ♣ ♤ ♥ ♦"*10) #Displays a nice divider to make the interface cooler
        input("Press any Key to continue")

    def run_tests(self, verbose = True):
    #This function enables the user to store all wanted hands in a file called "tests.txt"
    #and then the program will output all hands given and check if the result was correct.
    #Hence, Two options are available.
    #1.Displays a user-friendly interface comparing the hands
    #2.Displays only if the result given by the program was correct or not
        print("1.Display games")
        print("2.Display only the results")
        self.option = int(input("(1 or 2)=>"))
        if self.option == 1:
            verbose = True
        elif self.option == 2:
            verbose = False
        tests = open('tests.txt','r') #Opens the file tests.txt
        for sample in tests.readlines(): #Reads line by line of the file
            #Data read in the file is as follows hand1,hand2 and result
            #in the file it appers like that (N - number, S - Suit): NS NS NS NS NS, NS NS NS NS NS, Result
            #This is all readed as a string, and by that the program must break it and gets its information
            sample = sample.split(',') #Separate the information given by the line [hand1, hand2, result]
            self.hand1 = sample[0] #Receives hand1
            self.hand2 = sample[1] #Receives hand2
            self.trueResult = sample[2].strip() #Receives result
            self.result = self.dealer.play(self.hand1,self.hand2, verbose = verbose) #Calls the function that will compare the hands \
            #self.result will receive the answer from the program

            if verbose == True: #If option 1 was selected in the initiation of the function
                print("The result is:", self.trueResult == self.result)
                print("")
                print(" ♣ ♤ ♥ ♦"*10)
                input("Press any Key to continue")
                self.clean_screen()
            if verbose == False: #If option 2 was selected in the initiation of the function
                print(self.trueResult == self.result)
        if verbose == False: #If option 2 was selected in the initiation of the function
            input("Press any Key to continue")


    def display_menu(self):
        #This function is the main entry of the program, it will show the user options
        #to choose
        self.clean_screen() #Clean screen before showing the menu
        print("1. Ask the dealer to draw a new pair of hands") #This takes the user to "dealer_draws" function
        print("2. Be the dealer and manually input the pair of hands") #This takes the user to "manually_play" function
        print("3. Execute the given samples for this Challenge") #This takes the user to "run_tests" function
        print("4. Exit") #This ends the program. SIGTERM such as CTRL+C doesn't work while this program is running
        try:
            self.option = int(input("(1,2,3 or 4)=>"))
            if self.option == 1:
                self.clean_screen()
                self.dealer_draws()
                self.display_menu()
            elif self.option == 2:
                self.clean_screen()
                self.manually_play()
                self.display_menu()
            elif self.option == 3:
                self.clean_screen()
                self.run_tests(verbose = False)
                self.display_menu()
            elif self.option == 4:
                self.clean_screen()
                pass
            else:
                print("The input was not valid, try 1,2,3 or 4")
                input("Press any Key to continue")
                self.display_menu()
        except:
            print("")
            print("The input was not valid, try 1,2,3 or 4")
            input("Press any Key to continue")
            self.display_menu()
