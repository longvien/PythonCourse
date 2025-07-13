import random
computer_choice = random.choice(['rock', 'paper', 'scissors'])
player_choice  = input('Enter your choice: rock, paper or scissors?\n')
if player_choice == computer_choice:
    print('Draw!')
elif computer_choice == 'rock' and  player_choice == 'paper':
    print('You win!')

