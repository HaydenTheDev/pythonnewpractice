# def python_food():
#     width = 80
#     print("pizza and fries")
#
#
# print(python_food())
#
#
# def center_text(text):
#     text = str(text)
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text)
# center_text("pizza is amazing")


def some_text(*args):
    text = ""
    for arg in args:
        text += str(arg) + ""
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

some_text("first", "Second", 3, 4, "Pizza")
