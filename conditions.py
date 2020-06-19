age = int(input("How old are you? "))

if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your time")
print("-" * 80)

if age < 16 or age > 65:
    print("enjoy your time.")
else:
    print("Have a good day at work")
