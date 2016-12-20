class Student:
    def __init__(self, name, grade):
        self.name = name
        self.attend = 0
        self.grade = []

    def __str__(self):
        return self.name

    def addGrade(self, grade):
        self.grade.append(grade)

    def attendDay(self):
        #self.attend = 0
        self.attend += 1

    def getAverage(self):
        return sum(self.grade)/len(self.grade)


class GradStudent(Student):
    def __init__(self, name, grade, adviser):
        Student.__init__(self, name, grade)
        self.adviser = adviser

    def __str__(self):
        return Student.__str__(self) + self.adviser

    # def test(self):
    #   return 'test'

student1 = Student('Mike', 100)
student2 = GradStudent('Mark', 90, 'Prof Jeff')
#student3 = student('Bruce')
#student2.test()
print(student1)
student1.attendDay()
for i in range(0,10):
    student2.attendDay()
print(student2.attend)
print(student1.attend)