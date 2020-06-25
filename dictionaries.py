fruit = {"orange": "a sweet, orange, citrus fruit",
        "apple":"good for making cider",
        "lemon":"a sour yellow citrus fruit",
        "grape": "a small sweet fruit growing in bunches",
        "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])  #  this is the key to access description
# fruit["pear"] = "an odd shaped apple" #  adding a new value
# print(fruit)
fruit["pear"] = "great with tequila"
# print(fruit["pear"])
# del fruit["lemon"] #  deletes key lemon
# # del fruit #would delete entire dictionary
# print(fruit)
while True:
    dict_key = input("Please enter a fruit")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We dont have have {}".format(dict_key))