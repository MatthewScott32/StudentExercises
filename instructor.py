from student import Student
from nss_person import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, first_name, last_name, slack, cohort, specialty):
        super().__init__(first_name, last_name, slack, cohort)
        self.specialty = specialty


    def assign(self, student, exercise):
        student.add_exercise(exercise)
