import random

highest = 10
answer = random.randint(1, highest)
print(answer)

print("Please  guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("You guessed it first time")
else:
    while guess != answer:
        if guess == 0:
            print("You quit the game")
            break
        elif guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
            guess = int(input())
    else:
        print("Well done! You guessed it!")
