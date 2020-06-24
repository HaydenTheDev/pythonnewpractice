# t = ("a", "b", "c")
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

# welcome = "Welcome to my nightmare", "Alice Cooper", 1975
# bad ="Bad Company", "Bad Company", 1974
# metallica = "Ride the Lightning", "Metallica", 1984
# print(welcome[0])
#
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of puppets"
# print(metallica2)
#
# titles, artist, year = metallica
# print(titles)
# print(artist)
# print(year)

imelda = "Mrore Mayhem", "Imilda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"))

print(imelda)

title, artist, year, tracks= imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track,title))


