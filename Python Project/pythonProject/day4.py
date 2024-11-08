import random

# random_integer = random.randint(1, 50)
# print(random_integer)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# random_heads_or_tails =  random.randint(0,1)
# if random_heads_or_tails == 0:
#     print("Heads")
# else:
#     print("Tails")
#
# states_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado"]
#
# states_america.append("Nebraska")
#
# print(states_america)
#
# states_america.extend(["Angeland", "Dominica"])
#
# print(states_america)
#
# print(len(states_america))

#Assignment

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#
# random_friend = random.randint(0,4)
#
# print(friends[random_friend])
# print(random.choice(friends))

#Project: Rock Paper Scissors
rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ | / __| |/ /
| | | (_) | (__|   < 
|_|  (___/ |___|_||_|                    
'''
paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ ) / _` | '_ | / _ | '__|
| |_) | (_| | |_) |  __/ |   
| .__/ (__,_| .__/ (___|_|   
| |         | |              
|_|         |_|           
'''
scissor = '''
  ____
  / __ )
 ( (__) |___ ___
  /________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  (____/
'''
game_images = [rock, paper, scissor]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissor. \n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("It's a draw!")

