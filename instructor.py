# from student import Student

class Instructor:
    def __init__(self, first_name, last_name, slack, cohort, specialty):
        self.first_name = ""
        self.last_name = ""
        self.slack = ""
        self.cohort = ""
        self.specialty = ""


    def assign(self, student, exercise):
        student.add_exercise(exercise)
