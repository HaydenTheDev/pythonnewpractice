number ="9,233;372:036 854,775;807"
separations = ""

#  stepping through a for loop in debugger
for char in number:
    if not char.isnumeric():
        separations = separations + char

print(separations)

values = "".join(char if char not in separations else " " for char in number).split()
print([int(val) for val in values])