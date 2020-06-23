# # ipAddress = input("Please enter an IP address")
# # print(ipAddress.count("."))
#
# parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]
#
# parrot_list.append("A Norwegian Blue")
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# numbers_in_order = sorted(numbers)
# # numbers.sort()  # This sorts the lists of even and odd
# print(numbers_in_order) #  sorted gives the same result as .sort()
#
# if numbers == numbers_in_order:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
# if numbers_in_order == sorted(numbers):
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
# print(list("The lists are equal"))

# even = [2, 4, 6, 8]
#
# another_even = sorted(even, reverse=True)
# print(another_even == even)
# another_even.sort(reverse=True)
# print(even)
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = [even, odd]
# print(numbers)
# for numbers_set in numbers:
#     print(numbers_set)
#     for value in numbers_set:
#         print(value)

menu = []
menu.append(["Egg", "Spam", "Bacon"])
menu.append(["Egg", "Sausage", "Bacon"])
menu.append(["Egg", "Spam"])
menu.append(["Egg", "Spam", "Bacon"])
menu.append(["Egg", "Spam", "Sausage"])
menu.append(["Egg", "Spam", "Spam", "Bacon"])
menu.append(["Egg", "Bacon"])

#print(menu)

for meal in menu:
    if not "Spam" in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)