computer_choice = 'scissors'
user_choice = input("Let's play rock, paper, or scissors. What is your choice: rock, paper, or scissors?\n")
if computer_choice == user_choice:
    print("Computer choice is also " + computer_choice + " => TIE")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("Computer choice is " + computer_choice + " => YOU WON!")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("Computer choice is " + computer_choice + " => YOU WON!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("Computer choice is " + computer_choice + " => YOU WON!")
else:
    print("Computer choice is " + computer_choice + " => YOU LOSE!")
#My code:
#elif user_choice == 'scissors' and computer_choice == 'rock':
#    print("Computer choice is " + computer_choice + " => YOU LOSE!")
#elif user_choice == 'rock' and computer_choice == 'paper':
#    print("Computer choice is " + computer_choice + " => YOU LOSE!")
#elif user_choice == 'paper' and computer_choice == 'scissors':
#    print("Computer choice is " + computer_choice + " => YOU LOSE!")