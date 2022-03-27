# 2022 DataH Challenge

Compares two hands of poker and returns if the first has won or not. 

# Recommended Usage for recruiters
Put every pair of hand that must be tested in tests.txt in a .csv format and let the program do the job for you using:
```bash
python main.py
```
```
1. Ask the dealer to draw a new pair of hands
2. Be the dealer and manually input the pair of hands
3. Execute the given samples for this Challenge
4. Exit
(1,2,3 or 4)=>
```
Choose option 3 and then option 2 if you are interested only if the result the program is returning is right with the ground-truth given, or choose option 3 and then option 1 to see it in a more user-friendly way :wink:.

# About Documentation
You can obtain more detailed APIs documentation here in github on the [wiki's tab of this repository](https://github.com/gustavobraga98/desafio-python-datah/wiki).

# Modularity

The program was made with modularity in mind. Thus it can be broken into 3 modules:  
1. PokerHand
2. Dealer
3. Menu

## PokerHand
This class has everything that the challenge required following the instructions's PDF you can import the class PokerHand and use it to compare with another hand. It can be done with either a String or another PokerHand Class.

### Usage:
```python
from PokerHand import PokerHand
hand1 = PokerHand("TC TH 5C 5H KH") # Creates the first hand (Notice that this is a PokerHand Class)
hand2 = PokerHand("TS TD KC JC 7C") # Creates the second hand (Notice that this is another PokerHand Class)
print(hand1.compare_with(hand2)) #Print outputs the returned value of this function (Either Win or LOSS)
```
```
WIN
```
***

```python
from PokerHand import PokerHand
hand1 = PokerHand("TC TH 5C 5H KH") # (Notice that this is another PokerHand Class)
hand1.compare_with("TS TD KC JC 7C") # (Notice that this is a string)
```
```
WIN
```

## Dealer
This class is responsible to make things a little more versatile and more poker-ish(?).
It comes with functions to generate two hands of poker whitout repeating cards and display the game in a more user-friendly way.

## Menu
This class is responsible for making a user-friendly interface in wich there are some perks that can help the recruiters test this program. Executing from a terminal:
```bash
python main.py
```
Outputs:
```
1. Ask the dealer to draw a new pair of hands
2. Be the dealer and manually input the pair of hands
3. Execute the given samples for this Challenge
4. Exit
(1,2,3 or 4)=>
```
If option 3 is selected the program will read every pair of Hand that is in the tests.txt file and return if the program is giving the right results or not.
