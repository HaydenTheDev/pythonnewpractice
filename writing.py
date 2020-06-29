cities = ["Metropolis", "Paducah", "Murray", "Princeton"]

with open("cities.txt", 'w') as city_files:
    for city in cities:
        print(city, file=city_files)