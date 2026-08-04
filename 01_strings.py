
# ======================================
# GET USER INFORMATION
# ======================================

#Full name
#Favourite movie
#Favourite food
#Favourite city
#Remove any unwanted spaces at the beginning and end of every user input.
#The full name is stored with each word starting with a capital letter.
name = input("Enter your full name: ").strip().title()
#The favourite movie is stored with each word starting with a capital letter.
favourite_movie = input("What is your favourite movie? ").strip().title()
#The favourite food is stored completely in lowercase.
favourite_food = input("What is your favorite food? ").strip().lower()
#The favourite city is stored in uppercase.
favourite_city = input("What is your favourite city? ").strip().upper()

# ======================================
# DISPLAY PROFILE
# ======================================

#Display them nicely using f-strings.
print(f"{name}, Your favourite movie to watch is: {favourite_movie}, you love eating: {favourite_food} and your most favorite city is: {favourite_city}. ")

print(F'Thank you, {name}, for completing your profile!')


# ======================================
# STRING CASE CONVERSION
# ======================================


#Print your full name in UPPERCASE.
print(name.upper())

#Print your favourite movie in lowercase.
print(favourite_movie.lower())

#Print your favourite city in Title Case.
print(favourite_city.title())

# ======================================
# STRING ANALYSIS
# ======================================

#Print the length of your full name.
print(len(name))

#Print only the first name using indexing or slicing.
space = name.find(" ")
print(name[:space])

#Print the last three letters of your favourite movie.
print(favourite_movie[-3:])

#Check whether your favourite movie contains the word "the".
if "the" in favourite_movie.lower():
    print(favourite_movie)
    
# ======================================
# STRING MODIFICATION
# ======================================


#Replace one word in your favourite movie.
new_movie = favourite_movie.replace("Wuthering", "Rembel")
print(new_movie)

#Replace one word in your favourite movie using .replace().
greeting = "      Hello Python      "
greeting = greeting.strip()
print(greeting)
  