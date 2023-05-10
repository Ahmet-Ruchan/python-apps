#rock, paper, sicissors

import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for sicissors\n")
    computer = random.choice(['r','s','p'])
    print(computer)

    if user == computer:
        print("Draw!")
    elif user == 'r' and computer == 's' or user == 'p' and computer == 'r':
        print("You won!")
    elif user == 's' and computer == 'p':
        print("You won!")
    elif computer == 'r' and user == 's' or computer == 'p' and user == 'r':
        print("You lost!")
    elif computer == 's' and user == 'p':
        print("You lost!") 

play()