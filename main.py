from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

exercise1 = Exercise("High", "CSS") 
exercise2 = Exercise("Low", "HTML") 
exercise3 = Exercise("Mid", "JavaScript") 
exercise4 = Exercise("Gone", "Python") 

cohort1 = Cohort("Cohort 101")
cohort2 = Cohort("Cohort 100")
cohort3 = Cohort("Cohort 99")

student1 = Student("Slim", "Pickens", "SlimPick", "Cohort 100")
student2 = Student("Luke", "Jackson", "LJ", "Cohort 99")
student3 = Student("Martin", "Riggs", "Lethal_Weapon", "Cohort 101")
student4 = Student("Roger", "Murtaugh", "Too_Old", "Cohort 101")

instructor1 = Instructor("Jisie", "David", "JD", "Cohort 101", "JavaScript")
instructor2 = Instructor("Chase", "Fite", "CF", "Cohort 100", "Python")
instructor3 = Instructor("Kristen", "Norris", "KN", "Cohort 99", "HTML")

instructor1.assign(student3, exercise1)
instructor1.assign(student3, exercise2)
instructor1.assign(student4, exercise1)
instructor1.assign(student4, exercise2)
instructor2.assign(student1, exercise3)
instructor2.assign(student1, exercise4)
instructor3.assign(student2, exercise1)
instructor3.assign(student2, exercise4)