fruit = {"orange": "a sweet, orange, citrus fruit",
        "apple":"good for making cider",
        "lemon":"a sour yellow citrus fruit",
        "grape": "a small sweet fruit growing in bunches",
        "lime": "a sour, green citrus fruit"}

print(fruit)
print(fruit["lemon"])  #this is the key to access description
fruit["pear"] = "an odd shaped apple" #adding a new value
print(fruit)
fruit["pear"] = "great with tequila"
print(fruit["pear"])