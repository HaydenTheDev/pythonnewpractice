games = {"WoW": "Best game ever back then",
         "Runescape": "I Still like to play this game occasionally",
         "RocketLeague": "When I want a good challenge",
         "7 Days to Die": "If you like survival check this one out.",
         "Heroes of the Storm": "Is more for strategy nerds, but great."}

f_tuple = tuple(games.items())
print(f_tuple)

for game in f_tuple:
    item, description = game
    print((item + " is " + description))

print(dict(f_tuple))