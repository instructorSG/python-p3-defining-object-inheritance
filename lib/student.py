from lib.user import User


class Student(User):
    def __init__(self, name, grade):
        print("Student.__init__called.")
        super().__init__(name)
        self.grade = grade

    def log_in(self):
        super().log_in()
        self.in_class = True
