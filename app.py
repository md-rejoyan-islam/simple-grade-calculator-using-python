# range
range= range(-1, 101)

# range check function
def range_check(mark, subject):

    # invalid value check
    if mark == "":
        print("You did not enter any value for {}".format(subject))
        exit()

    # type check
    if not mark.isnumeric():
        print("Please enter a positive number value for {} subject".format(subject))
        exit()
    
    # invalid range
    if not (eval(mark) >=0 and eval(mark) <= 100):
        print("Subject mark will be between 0 to 100")
        exit()
    

# Input Mark for Bangla 
bangla = input("Enter Bangla Marks: ")
range_check(bangla, "Bangla")


# Input Mark for English
english = input("Enter English Marks: ")
range_check(english, "English")


# Input Mark for Math
math = input("Enter Math Marks: ")
range_check(math, "Math")


# Input Mark for Science
science = input("Enter Science Marks: ")
range_check(science, "Science")

# avaerage calculation
average = (eval(bangla) + eval(english) + eval(math) + eval(science)) / 4


# grade calculation
grade = ""

if average >= 91 and average <= 100:
    grade = "A+"
elif average >= 81 and average <= 90:
    grade = "A"
elif average >= 71 and average <= 80:
    grade = "B"
elif average >= 61 and average <= 70:
    grade = "C"
elif average >= 41 and average <= 60:
    grade = "D"
else :
    grade = "F"


# print result
print("Your Avarage mark is: {} and  Grade is: {}".format(average,grade))


