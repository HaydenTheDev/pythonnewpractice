fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "pear": "great with tequila"}

print(fruit)

veg = {"cabbage": "Everyone's favorite vegetable",
       "sprouts": "So good mate",
       "spinach": "can I have more fruit, please?"}

print(veg)

veg.update(fruit) # adds 2 dictionaries together.
print(veg)

print(fruit.update(veg))
print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)