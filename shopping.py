shopping_list = ["milk", "pasta", "eggs", "chips", "bread", "rice"]

# for item in shopping_list:
#     if item != "pasta":
#         print("buy " + item)

for item in shopping_list:
    if item == "eggs":
        break

    print("Buy " + item)