# ======================================
# BASIC EXCEPTION HANDLING
# ======================================
#Try converting the string into an integer
try:
    number = int("10")
    print(number)
# If the conversion fails, handle the ValueError   
except ValueError:
    print("That is not a valid number.")
    
    
# ======================================
# HANDLING INVALID DATA
# ======================================

# Store the movie rating as a string.
rating = "excellent"

# Try converting the rating into a decimal number.
try:
    rating = float(rating)
    print(f"Movie rating: {rating}")

# Handle the error if the rating cannot be converted into a number.
except ValueError:
    print("Movie rating must be a number.")
    

# ======================================
# HANDLING MULTIPLE EXCEPTIONS
# ======================================

# Try converting the string into an integer and then divide 100 by it.
try:
    number = int("hello")
    result = 100 / number
    print(result)

# Handle the error if the string cannot be converted into an integer.
except ValueError:
    print("Please provide a valid number.")

# Handle the error if the number is zero and division is attempted.
except ZeroDivisionError:
    print("You cannot divide by zero.")
    
# ======================================
# USING ELSE WITH EXCEPTION HANDLING
# ======================================

# Try converting the string into an integer.
try:
    number = int("10")

# Handle the error if the string cannot be converted into an integer.
except ValueError:
    print("Invalid number.")

# Run this code only if no error occurred in the try block.
else:
    print(f"Successfully converted: {number}")
    
    
# ======================================
# USING FINALLY WITH EXCEPTION HANDLING
# ======================================

# Try converting the string into an integer.
try:
    number = int("10")

# Handle the error if the string cannot be converted into an integer.
except ValueError:
    print("Invalid number.")

# Run this code whether an error occurs or not.
finally:
    print("Program finished.")