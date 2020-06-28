jabber = open("/Users/power/Desktop/original.txt", 'r')
for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()