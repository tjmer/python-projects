import random
items = ['rock', 'paper', 'scissors']
computer_choice = random.choice(items)
user_choice = input("rock, paper or scissors?\n")

if computer_choice == user_choice:
    print("comp: "+computer_choice)
    print("player: "+user_choice)
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("comp: "+computer_choice)
    print("player: "+user_choice)
    print("WIN")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("comp: "+computer_choice)
    print("player: "+user_choice)
    print('WIN')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("comp: "+computer_choice)
    print("player: "+user_choice)
    print('WIN')
else:
    print("comp: "+computer_choice)
    print("player: "+user_choice)
    print('You lose :) Computer wins :D')