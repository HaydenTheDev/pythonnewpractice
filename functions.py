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


def some_text(*args, sep=' ', end_char='\n', centered_file=None, flush_me=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end_char, file=centered_file, flush=flush_me)


some_text("first", "Second", 3, 4, "Pizza", sep=': ')
print()
