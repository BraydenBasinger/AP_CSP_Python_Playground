from calculator import calc
from diceroll import dice 
from hangman import hang
from madlibs import madl
from blackjack import blackj

fruits = "🍊 🍌 🍉" 

print(" ")
print("\u001b[35mB\u001b[32mr\u001b[36ma\u001b[33my\u001b[34md\u001b[31me\u001b[35m\u001b[32mn\u001b[36m'\u001b[33ms \u001b[37mPlaygroud     " + fruits)
print(" ")

while True:
  
  print("\u001b[40m====================")
  print(u"\u001B[0m")
  print("0 - Exit")
  print("1 - Dice roll")
  print("2 - Calculator")
  print("3 - Hangman")
  print("4 - Madlibs")
  print("5 - Blackjack")
  print("\u001b[40m====================")
  print(u"\u001B[0m")
  
  selection = int(input())

  if selection == 1:                                    
    print('\u001b[36mDice Roll')                        
    dice()
    
                                                 
                                                        
  if selection == 2:                                    
    print("\u001b[33mCalculator")                       
    calc()
    
    
  if selection == 3:
    print("\u001b[34mHangman")
    hang()
     
    
  if selection == 4:
    print("\u001b[31mMadlibs")
    madl()
    

  if selection == 5:
    print("\u001b[36mBlackjack")
    blackj()
    

  if selection == 0:
    exit()
    

    
  