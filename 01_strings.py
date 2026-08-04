#Challenge 1 - Personal Profile Formatter

#Create a small profile using strings.

#Store the following:

#Full name
#Favourite movie
#Favourite programming language
#Favourite food
#Favourite city

name = input("Enter your full name: ")
favourite_movie = input("What is your favourite movie? ")
favourite_food = input("What is your favorite food? ")
favourite_city = input("What is your favourite city? ")

#Display them nicely using f-strings.
print(f"{name}, Your favourite movie to watch is: {favourite_movie}, you love eating: {favourite_food} and your most favorite city is: {favourite_city}. ")

#Print your full name in UPPERCASE.
print(name.upper())



#Print your favourite movie in lowercase.
print(favourite_movie.lower())

#Print your favourite city in Title Case.
print(favourite_city.title())

#Print the length of your full name.
print(len(name))

#Print only the first name using indexing or slicing.
print(name.lstrip())

#Print the last three letters of your favourite programming language.
print(favourite_movie[-1:-4])

#Check whether your favourite movie contains the word "the".
for "the" in favourite_movie:
    print()

#Replace one word in your favourite movie using 
new_movie = favourite_city.replace("Wuthering", "Rembel")

#Replace one word in your favourite movie using .replace().
greeting = "      Hello Python      "
greeting.strip()

   