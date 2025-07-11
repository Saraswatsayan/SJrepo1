class Student():
    def __init__(self, name, subject1, subject2, subject3):
        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

    def avg(self):
        return (self.subject1 + self.subject2 + self.subject3) / 3

s1 = Student("Ravi", 67,89,77)
print(s1.avg())

