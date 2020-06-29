# cities = ["Metropolis", "Paducah", "Murray", "Princeton"]
#
# with open("cities.txt", 'w') as city_files:
#     for city in cities:
#         print(city, file=city_files)
# cities = []
#
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Ring"), (2, "Pyscho"), (3, "Mayhem"))
#
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

# with open("imelda3.txt", 'r') as imelda_file:
#     contents = imelda_file.readline()
#
# imelda = eval(contents)
#
# print(imelda)
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)

#Challenge

with open("sample.txt", 'w') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=tables)
        print("-" * 20, file=tables)