#analyse student grades stored in a dictionary

#calculate the average for each student
#determine the highest average grade
#identify students with average grades (within a specific threshold)

#Procedure
# 1. Create a dictionary 
# - their names are the keys and their score (to be in a list)
#2. Calculate average grade of each student
# (average = total score / number of subjects)
# 3.Determine student with the highest grade average
# print their name
#Above threshold
#DICTIONARY OF STUDENTS
students = {
    "Jacob" : [90, 78, 84, 87, 70],
    "Leah" : [90, 80, 86, 77, 78],
    "Emir" : [100, 70, 68, 89, 70],
    "Rachel" : [88, 98, 78, 49, 89],
    "Leon" : [89, 95, 57, 87, 86]
}
#function to calculate the average and show the student
def calculation() :
    
    highest_grade = float("-inf") #set to this so that every time a grade is found higher than negative infinity the maximum will be updated

    #set the topstudent to none as we do not know who it is 
    top_student = None
    text = "Average grades per student : "
    x = text.title() #giving it a title
    print(x)
    for student, grades in students.items() : #we put items so that it can iterate through the list of items
        #the equation that is used to calculate the average of the grades
        average_grades = sum(grades) / len(grades)
        
        print(f"{student} : {average_grades}") #name of student and average grade will be printed
       
       #highest average grade
        if (average_grades > highest_grade) :
            highest_grade = average_grades
            top_student = student
    
        
    new_text = "Highest Average Grade : "
    j = new_text.title()
    print(j)
    print(f"{top_student} : {highest_grade}")

    ##THRESHOLD SECTION
    threshold = float(input("Enter a threshold value : ")) #user will give an input
    kin = "Students with average above threshold : "
    z = kin.title()
    print(z)
    #more of a repeated equation as i was not able to put them all together
    for student,grades in students.items() :
        average_grade = sum(grades) / len(grades)
        if (average_grade > threshold) :
            print(f"{student} ")

calculation()
