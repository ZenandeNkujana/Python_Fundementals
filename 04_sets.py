#Favourite Movie Genres

# ======================================
# CREATE SET
# ======================================

genres = {"Romance", "Action", "Drama", "Comedy", "Thriller"}

#=======================================
#SET DISPLAY
#=======================================

#Display the entire set.
print(genres)

#Display how many different genres are in the set.
print(len(genres))

#========================================
#SET ANALYSIS
#========================================

#Check whether "Romance" exists.
if "Romance" in genres:
    print("True")
else:
    print("WE DO NOT HAVE THIS GENRE")
    
#Check whether "Horror" exists.
if "Horror" in genres:
    print("True")
else: 
    print("WE DO NOT HAVE THIS GENRE")
    
#Add "Horror" to your genres.
genres.add("Horror")
print(genres)

#Try adding "Drama" again.
genres.add("Drama")
print(genres)#Drama has not been added, two same things are not allowed in sets.

#==========================================
#SET GENRES
#==========================================

#Create a second set representing genres that your friend likes
friend_genres = {"Action", "Drama", "Horror", "Science Fiction", "Fantasy"}

#Genres you both like
genres.intersection(friend_genres)
print(genres)

#Genres only you like
mine = genres.difference(friend_genres)
print(mine)

#All genres between both sets
all_genres = genres.union(friend_genres)
print(all_genres)

#Genres your friend likes that you don't
friend = friend_genres.difference(genres)
print(friend)

