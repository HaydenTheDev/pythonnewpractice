answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it first try")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it correctly")
    else:
        print("Sorry, you guess incorrectly")
