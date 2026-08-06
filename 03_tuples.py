
# ======================================
# CREATE STUDENT RECORD
# ======================================

#This information should never change during the program, so a tuple is the perfect choice.
#Student number
#Full name
#Course
#Year of study
#Campus
student = ("UJ167732", "Zenande Nkujana", "Software Engineering", "2025", "Cape Town Campus")

# ======================================
# DISPLAY STUDENT RECORD
# ======================================

#Display the complete tuple.
print(student)

#Then display each piece of information neatly.
print(f"Your student number is: {student[0]}\nYour name is: {student[1]}\nYour course is: {student[2]}\nThe year is: {student[3]}\nYou are at: {student[4]}")

# ======================================
# TUPLE ANALYSIS
# ======================================

#Display how many pieces of information are stored.
print(len(student))
#Display the first value.
print(student[0])
#Display the last value.
print(student[4])
#Display the middle values using slicing.
print(student[1:4])

# ======================================
# TUPLE OPERATIONS
# ======================================

#Check whether a certain course exists.
if "Software Engineering" in student:
    print("That's one of the best courses, Softare Enginnering")
else:
    print("Unfortunately, we do not have the course")
#Find the position of one value.
position = student.index("2025")
print(position)
#Create another tuple containing three modules.
module = ("Module1", "Module2", "Module3")
#Combine the two tuples into one new tuple.
new_student = student + module
#Display the final combined tuple.
print(new_student)