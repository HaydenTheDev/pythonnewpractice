fruit = {"orange": "a sweet, orange, citrus fruit", "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit", "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit", "pear": "great with tequila"}

# print(fruit)
# print(fruit["lemon"])  #  this is the key to access description
# fruit["pear"] = "an odd shaped apple" #  adding a new value
# print(fruit)
# print(fruit["pear"])
# del fruit["lemon"] #  deletes key lemon
# # del fruit #would delete entire dictionary
# print(fruit)
# while True:
#     dict_key = input("Please enter a fruit")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We dont have have {}".format(dict_key))
#
# for snack in fruit:
#     print(fruit[snack])

# WAYS OF CREATING DICTIONARIES THAT LOOK GOOD.

# ordered_key = list(fruit.keys())
# ordered_key.sort()

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])
