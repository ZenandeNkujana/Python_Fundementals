
#I am building a movie collection
#creating a list of movies
movies = ["The Notebook", "Titanic", "Avatar", "Interstellarr", "John Wick"]

#======================================
#LIST DISPLAY
#======================================
#Display the entire list.
print(movies)

# ======================================
# LIST ANALYSIS
# ====================================== 

#Display how many movies there are.
print(len(movies))

#Display the first movie.
print(movies[0])

#Display the last movie.
print(movies[-1])

#Display the first three movies.
print(movies[:3])

#Display the last two movies.
print(movies[-2:])

# ======================================
# LIST MODIFICATION
# ======================================

#Add one new movie.
movies.append("Wuthering Heights")
print(movies)

#Insert one movie at a specific position.
movies.insert(2, "Blood Diamonds")
print(movies)

#Replace one existing movie.
movies[0] = "Watermelon & sugar"
print(movies)

#Remove one movie.
movies.remove("Titanic")
print(movies)

#Display the updated list.
print(movies)

# ======================================
# LIST SEARCHING
# ======================================

#Using the same list:

#Check whether "Titanic" exists in the list.
if "Titanic" in movies:
    print("Yes the list does have titanic")
else:
    print("Titanic was removed")
#Display the position of "Avatar".
print(movies.index("Avatar"))


# ======================================
# LIST ORDERING
# ======================================

#Display the movies in alphabetical order.
print(sorted(movies))
#Display them in reverse alphabetical order.
print(sorted(movies, reverse=True))