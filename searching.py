shopping_list = ["milk", "pasta", "eggs", "chips", "bread", "rice"]

item_to_find = "eggs"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print("Item found at position {}".format(found_at))