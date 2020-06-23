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
        pass
