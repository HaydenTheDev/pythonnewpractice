low = 1
high = 1000

print("Please enter a number between {} and {}".format(low, high))
input("Press enter to start")

guesses = 1
while low != high:
    # print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2 #  formula for game
    high_low = input("My guess is {}. Should i guess higher or lower? "
                     "Enter h or l, or c if my guess was correct. "
                     .format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses! ".format(guesses))
        break
    else:
        print("Please enter h, l, c")
    # guesses = guesses + 1
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))
