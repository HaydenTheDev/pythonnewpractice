# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# even = set(range(0, 40, 2))
# print(even)
# square_tuple = (4, 6, 9, 16, 25)
# squares = set(square_tuple)
# print(square)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
# print("-" * 40)
# print("|" * 40)
# square_tuple = (4, 6, 9, 16, 25)
# squares = set(square_tuple)
# print(squares)
# print(len(squares))
# print("-" * 40)
# print("|" * 40)
# print(even.union(squares))
# print(len(even.union(squares)))
# print("-" * 40)
# print("|" * 40)
# print(squares.union(even))
#
# print("-" * 40)
# print("|" * 40)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("Squares minus even")
print(squares.difference(even))
print(squares - even)