class Student:

    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.courses = []

    def __str__(self):
        output = f"{self.last_name}, {self.first_name}: {self.id}\n"
        course_list = ','.join[(map(str(a), self.courses))]
        return output

    def add_course(self, *args):
        for item in args:
            self.courses.append(item)


class Classes:

    def __init__(self, course, teacher, grade):
        self.course = course
        self.teacher = teacher
        self.grade = grade

    def __str__(self):
        output = f"{self.course}:\n"


test = Student("Scott", "Urista", 34024668)


math = ("Math E-3", "Connely", "A")
python = ("CSCI E-7", "Parker", "A-")
rhetoric = ("Expo E-34", "Akbuhr", "A")

test.add_course(math, python, rhetoric)
print(test)
