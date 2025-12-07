# Class students
class Student:
    def __init__(self, id, name, DoB): 
        self.id = id
        self.name = name
        self.DoB = DoB
        self.marks = {}
        
    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_DoB(self):
        return self.DoB

    def get_marks(self):
        return self.marks

    def add_mark(self, course_name, mark):
        self.marks[course_name] = mark

    def list(self):
        print("--------------------")
        print(f"Student ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"DoB: {self.DoB}")
        for course, mark in self.marks.items():
            print(f"{course}: {mark}")
        print("--------------------")


# Class Course
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def list(self):
        print("--------------------")
        print(f"Course ID: {self.id}")
        print(f"Course Name: {self.name}")
        print("--------------------")


# Main
if __name__ == "__main__":
    students = []
    courses = []

    # Input students
    print("Number of students:")
    n = int(input())
    for i in range(n):
        id = input(f"Enter ID of student {i}: ")
        name = input(f"Enter name of student {i}: ")
        DoB = input(f"Enter DoB of student {i}: ")
        students.append(Student(id, name, DoB))

    # Input courses
    print("Number of courses:")
    c = int(input())
    for i in range(c):
        cid = input(f"Enter ID of course {i}: ")
        name = input(f"Enter name of course {i}: ")
        courses.append(Course(cid, name))

    print("Enter index of course to add marks:")
    for idx, cr in enumerate(courses):
        print(f"{idx}. {cr.name}")
    course_index = int(input())
    selected_course = courses[course_index]

    print("Enter index of student:")
    for idx, st in enumerate(students):
        print(f"{idx}. {st.name}")
    student_index = int(input())
    selected_student = students[student_index]

    mark = float(input(f"Enter mark for {selected_course.name}: "))
    selected_student.add_mark(selected_course.name, mark)

    print("Students:")
    for s in students:
        s.list()

    print("Courses:")
    for cr in courses:
        cr.list()
