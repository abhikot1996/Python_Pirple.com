
"""
To Access Keys and Values from Dictionaries
"""

FavoriteSong={'SongName':"nayan ne bandh rakhine",
                  'Singer':"Darshan Raval" ,
                  'Cast':"Darshan Raval & Zaara" ,
                  'SongLang':"Gujrati and Hindi",
                  'SongTiming':03.31,'Likes':721000 ,
                  'RelasedOn':"'DarshanRavalDZ' YouTube Channel",
                  'RelasedYear':2017 }

for KeysOrValues in FavoriteSong:
    # print(KeysOrValues) # Prints Keys Only
    # print(FavoriteSong[KeysOrValues]) # Prints Values Only
    print(KeysOrValues,":",FavoriteSong[KeysOrValues]) # Prints Keys and Values

# o/p
# SongName : nayan ne bandh rakhine
# Singer : Darshan Raval
# Cast : Darshan Raval & Zaara
# SongLang : Gujrati and Hindi
# SongTiming : 3.31
# Likes : 721000
# RelasedOn : 'DarshanRavalDZ' YouTube Channel
# RelasedYear : 2017
