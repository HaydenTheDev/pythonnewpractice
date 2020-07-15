import os

listings = os.walk('.')
for root, directories, files in listings:
    print(root)
    for d in directories:
        print(d)
    for file in files:
        print(file)
