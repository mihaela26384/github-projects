imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

album, artist, year, tracks = imelda
print(album)
print(artist)
print(year)
print(tracks)
for song in tracks:
    number, song_title = song
    print("\t", number, song_title)


for item in imelda[3]:
    print('\t', item[1])


