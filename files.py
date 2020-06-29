jabber = open("C:\\Users\\power\\Desktop\\original.txt", 'r')
for line in jabber:
    if "did" in line.lower():
        print(line, end='')

jabber.close()

# with open("original.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("original.txt" 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("original.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

# with open("original.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')