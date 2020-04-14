class Student:
    def __init__(self, first_name, last_name, slack, cohort):
        self.first_name = ""
        self.last_name = ""
        self.slack = ""
        self.cohort = ""
        self.exercises = list()

    def add_exercise(self, exercise):
        self.exercises.append(exercise)