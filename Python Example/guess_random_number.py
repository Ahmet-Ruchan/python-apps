
#guess the number

import random 

min = 0 
for max in range(20):
    number = random.randint(min,max)

print(number)

while(1):
    print("Guess the number?")
    guess = int(input("=> "))

    if guess == number:
        print("You are correct")
        break
