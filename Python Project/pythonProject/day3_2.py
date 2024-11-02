print('''
******************************************************************************
         |                  |                   |                     |                   
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the Treasure Island. \nYour mission is to find the treasure.")
choice1 = input('''You're at a cross road. Where do you want to go?\n\t Type "left" or  "right"\n''').lower()

if choice1 == "right" or choice1 != "left":
    print("Fall into a hole. \n  Game Over.")

elif choice1 == "left":
    choice2 = input('''You've come to a lake. There is a island in the middle of the lake.\n  Type "wait" to wait for a boat. Type "swim" to swim across.\n''').lower()

    if choice2 == "swim" or choice2 != "wait":
        print("Attacked by trout.\n  Game Over.")

    else:
        choice3 = input('''Which door? Type "blue", "red", or "yellow" \n''').lower()
        if choice3 == "red":
            print("Burned by fire.\n  Game Over.")

        elif choice3 == "yellow":
            print("You Win!")

        elif choice3 == "blue":
            print("Eaten by beasts.\n  Game Over.")

        else:
            print("Game Over.")


