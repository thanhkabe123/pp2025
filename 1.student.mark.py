n = int(input("Number of students: "))

# Function print all Students
def printStudents(students):
    for i, student in enumerate(students):
        print("--------------------")
        print(f"Index: {i}")
        print(f"Students ID: {student['id']} ")
        print(f"Students Name: {student['name']} ")
        print(f"Students DoB: {student['DoB']} ")
        marks = student['marks']
        for course, mark in marks.items():
            print(f"{course} {mark}")
        print("--------------------")
# Function print all Course
def printCourse(courses):
    for i, course in enumerate(courses):
        print("--------------------")
        print(f"Index: {i}")
        print(f"Course ID: {course['id']}")
        print(f"Course Name: {course['name']}")
        print("--------------------")

students = []
for i in range(n):
    person = {}
    person["id"] = str(input(f"Enter id of students {i}: "))
    person["name"] = input(f"Enter Name of students {i}: ")
    person["DoB"] = input(f"Enter DoB of students {i}: ")
    person['marks'] = {}
    students.append(person)

c = int(input("Number of courses: "))
courses = []
for i in range(c):
    course = {}
    course["id"] = str(input(f"Enter id of Course {i}: "))
    course["name"] = input(f"Enter Name of Course {i}: ")
    courses.append(course)

print(courses)

print("Enter index course want to add mark to students: ")
printStudents(students)
indexC = int(input())
course = courses[indexC]
print("Enter index students: ")
printCourse(courses)
indexP = int(input())
person = students[indexP]
marks = person['marks']
marks[course['name']] = int(input(f"Enter mark of {course['name']}: "))

# Print again
printStudents(students)
printCourse(courses)
