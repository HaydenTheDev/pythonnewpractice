#  Menu Options
options = """1.\tWoW 
2.\tRunescape
3.\tRocketLeague 
4.\tHots
5.\tWarZone
0.\tExit"""

char = ""
#  While Loop for options
while char in options:
    print(options)
    char = input("Please choose options 1-5 or 0 to exit: ")
    if char == "0":
        print("You have quit the options.")
        break
    elif char == "1":
        print("You have chosen WoW")
    elif char == "2":
        print("You have chosen Runescape")
    elif char == "3":
        print("You have chosen RocketLeague")
    elif char == "4":
        print("You have chosen Hots")
    elif char == "5":
        print("You have chosen WarZone")
    else:
        print("Please choose a valid number from the menu.")
        print(options)


#  This is the solution! so my code could have been condensed by alot,
#  still got the right output.
# choice = "-"
# while choice != "0":
#     if choice in "12345":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your options")
#         print("1:\tYou have chosen WoW")
#         print("2:\tYou have chosen Runescape")
#         print("3:\tYou have chosen RocketLeague")
#         print("4:\tYou have chosen Hots")
#         print("5:\tYou have chosen WarZone")
#         print("0:\tExit")
#     choice = input()
