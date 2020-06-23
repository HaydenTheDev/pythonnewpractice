# ipAddress = input("Please enter an IP address")
# print(ipAddress.count("."))

parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]

parrot_list.append("A Norwegian Blue")
for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers.sort()  # This sorts the lists of even and odd
print(numbers)