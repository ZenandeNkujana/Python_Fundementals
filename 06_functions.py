#Movie Collection Functions
#Create a function that displays all the movies in your collection neatly.
movies = ["The Notebook", "Titanic", "Avatar", "Interstellar", "John Wick"]

def movie_display():
    return movies
    
print(movie_display())

#Create a function that determines how many movies are in your collection.
def movie_count():
    return len(movies)

print(movie_count())

#Create a function that receives a movie name and checks whether that movie exists in your collection.
def movie_check(name_movie):
    if name_movie in movies:
        return True
    else:
        return False
print(movie_check("Avatar"))

#Create a function that receives a movie name and adds it to the collection.
def add_movie(name_movie):
    movies.append(name_movie)
    return movies
print(add_movie("Wuthering Heights"))


#Create a function that receives a position/index and gives back the movie at that position.
def movie_position(i):
    position = movies[i]
    return position
print(movie_position(1))
