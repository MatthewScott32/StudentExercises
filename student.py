from nss_person import NSSPerson


class Student(NSSPerson):
    def __init__(self, first_name, last_name, slack, cohort):
        super().__init__(first_name, last_name, slack, cohort)
        self.exercises = list()

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def assigned_exercise(self):
        exercises = []
        for exercise in self.exercises:
            exercises.append(f'{exercise.name} {exercise.language}')

