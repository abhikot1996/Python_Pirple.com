
FavoriteSong={'SongName':"nayan ne bandh rakhine",
                  'Singer':"Darshan Raval" ,
                  'Cast':"Darshan Raval & Zaara" ,
                  'SongLang':"Gujrati and Hindi",
                  'SongTiming':03.31,'Likes':721000 ,
                  'RelasedOn':"'DarshanRavalDZ' YouTube Channel",
                  'RelasedYear':2017 }

# Homework Assignment,
for KeyValue in FavoriteSong:
    print(KeyValue,":",FavoriteSong[KeyValue])
print(end="\n")


# For Extra Credit
def GuessKeyValue(Key,Value):
   if Key in FavoriteSong:
       if Value in FavoriteSong[Key]:
           return True
       else:
           return False
   return False

print(GuessKeyValue("Singer","Darshan Raval"))


