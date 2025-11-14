import random 

jackpot = random.randint(1,100)

guess_numer = int(input("Enter your guess number: "))

counter = 1

while guess_numer != jackpot:

    if guess_numer < jackpot:
        print("wrong! Please guess higher")

    else:
        print("wrong! Please guess lower")
    
    guess_numer = int(input("Enter your guess number: "))
    counter += 1

else:
    print("Correct Guess")
    print("Your attempt is: ", counter)