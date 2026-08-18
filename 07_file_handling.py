#Movie Watchlist 
#===========================================
#READ CONTENTS
#===========================================
#I will create a seperate txt file.

#Open the txt file
file = open("watchlist.txt", "r")

#Reads the contents
contents = file.read()

#Properly closes the file
file.close()

#Displays the movies
print(contents)

#=============================================
#ADD NEW CONTENT
#=============================================
# Add to the watchlist
file = open("watchlist.txt", "a")

# Add one new movie to the end of the file.
file.write("\nWuthering Heights")

file.close()

# Read the file again.
file = open("watchlist.txt", "r")
contents = file.read()
file.close()

# Display the updated watchlist.
print(contents)
#===============================================
#COUNT MOVIES
#===============================================

#Determine how many movies are currently stored in the file and display the number.
file = open("watchlist.txt", "r")
contents = file.readlines()
file.close()

print(f"There are {len(contents)} movies in your watchlist.")