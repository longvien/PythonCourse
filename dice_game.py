# import random
# 
# def roll_dice():
#     dice_total = random.randint(1, 6) + random.randint(1, 6)
#     return dice_total
# def main():
#     player1 = input("Enter player 1's name:\n")
#     player2 = input("Enter player 2's name:\n")
# 
#     roll1 = roll_dice()
#     roll2 = roll_dice()
# 
#     print(player1, 'rolled', roll1)
#     print(player2, 'rolled', roll2)
#     if roll1 > roll2:
#         print(player1, 'wins')
#     elif roll1 < roll2:
#         print(player2,'wins')
#     else:
#         print('Draw')
# main()


import random
def roll_dice():
    roll = random.randint(1, 6) * 2
    return roll

def main():
    player1 = input('Please enter your name:\n')
    player2 = input('Please enter your name:\n')
        
    roll1 = roll_dice()
    roll2 = roll_dice()
        
    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)
    if roll1 > roll2:
        print(player1, 'wins')
    elif roll1 < roll2:
        print(player2, 'wins')
    else:
        print('Tie')
main()










