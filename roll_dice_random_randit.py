import random
roll = random.randint(1,6)
guess = int(input("Which number do you think that the dice rolled?\n"))
if guess == roll:
    print("The Computer rolled a " + str(roll) + " and you guess a " + str(guess) + " and that's mean you are right!")
else:
        print("The Computer rolled a " + str(roll) + " and you guess a " + str(guess) + " and that's mean you aren't right!")