number = input("Please enter a series of numbers, using any separators you like: ")
separations = ""

#  stepping through a for loop in debugger
for char in number:
    if not char.capitalize():
        separations = separations + char

#print(separations)

values = "".join(char if char not in separations else " " for char in number).split()
print(sum([int(val) for val in values]))