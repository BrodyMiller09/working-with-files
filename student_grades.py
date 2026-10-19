#-----------------------------
#brody Miller
# 10/19/2026
# student grades
#-----------------------------

student = []
grades = {}

name = input("enter student name: ")
grade = input("enter grade: ")

students.append(name)
grades[name] = grade

file = open("grades.txt", "w")
file.write(name + ": " + grade + "\n")
file.close()

print("saved to file!")

for name in students:
    print(name, grades[name])
    