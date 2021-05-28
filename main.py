print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

q1 = input('You\'re at a crossroads. Do you want to go left or right? Type "left" or "right".\n').lower()

if q1 == "left":
  print ("You made it through. You come to a river. ")
  q2 = input("Do you swim through the river or wait for a boat?\n").lower()

  if q2 == "wait":
    print("Good choice. A friendly fisherman comes and takes your across")
    q3 = input("You come to three doors. Which do you chose? Red, blue, or yellow?\n").lower()
  else: 
    print("GAME OVER. Too bad, you were attacked by a shark.")

  if q3 == "blue":
    print("GAME OVER. You were eaten by a goat behind the blue door.")
  elif q3 == "red":
    print("GAME OVER. You were burned alive after walking through the red door.")
  elif q3 == "yellow":
    print("YOU WIN! Well done, you found the treasure.")
  else: 
    print("GAME OVER.")

else:
  print("GAME OVER! You fell into a hole.")