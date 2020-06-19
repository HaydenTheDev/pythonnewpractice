# parrot = "Norwegian Blue"
#
# letter = input("enter a character")
#
# if letter in parrot:
#     print("{} is in {}".format(letter, parrot))
# else:
#     print("I don't need that letter")

# activity = input("What would you like to do today")
#
# if"cinema" not in activity.casefold():
#     print("But I want to go to the cinema")
name = input("What is your name?")
age = int(input("Nice to meet you {0}, What is your age?".format(name)))

if 18 < age < 30:
    print("Welcome to the holiday party {0}, enjoy!".format(name))
elif 18 > age or age > 30:
    print("Sorry {1} you are {0} and cannot enter.".format(age, name))

