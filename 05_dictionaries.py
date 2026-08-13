#Movie Profile 
#Using dictionaries

# ======================================
# CREATE MOVIE PROFILE
# ======================================

movie = {"Title": "The Notebook", "Genre": "Romance", "Year": 2004, "Rating": 7.8, "Director": "Nick Cassavetes"}

#=======================================
#DICTIONARY DISPLAY
#=======================================

#Display the entire dictionary.
print(movie)

#Display the movie's title.
print(movie.get("Title"))

#Display the genre.
print(movie.get("Genre"))

#Display the rating.
print(movie.get("Rating"))

#Display the director.
print(movie.get("Director"))

#=========================================
#DICTIONARY ANALYSIS
#=========================================

#Display how many pieces of information are stored.
print(len(movie))

#Check whether "Genre" exists as a key.
if "Genre" in movie:
    print("True")
else:
    print("False")

#Check whether "Actor" exists as a key.
if "Actor" in movie:
    print("True")
else:
    print("False")
    
#Display all the keys.
print(movie.keys())

#Display all the values.
print(movie.values())

#Display both the keys and values together.
print(movie.items())

#===============================================
#DICTIONARY MODIFICATION
#===============================================

#Change Rating from 7.8 to 8.5
movie.update({"Rating":8.5})
print(movie)

#Change Genre from "Romance" to "Romance / Drama".
movie.update({"Genre": "Romance / Drama"})
print(movie)

#Add "Duration" ,"2h 3m"
movie.setdefault("Duration","2h3m")
print(movie)
