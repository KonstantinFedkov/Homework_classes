

from cgitb import reset
from turtle import st


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        n_rates = 0
        rate_sum = 0
    
        for rates in self.grades.values():
            n_rates += len(rates)
            rate_sum += sum(rates)

        mean_rate = rate_sum / n_rates
        res = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {mean_rate}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
            

        )
        
        return res    

    # выставляет оценку преподу за курс
    def rate_course(self, lect, course, grade):
        if grade < 1 or grade > 10:
            # оценка вне предела 
            print('# оценка вне предела ')
            return
        # ??? оцениваем текущие или завершенные? 
        if course not in self.finished_courses:
            # todo: у студента такого то либо курс не завершен либо вообще этого курса нет ай-яй-яй
            print('todo: у студента такого то либо курс не завершен либо вообще этого курса нет ай-яй-яй')
            return

        if course in lect.course_rates:
            lect.course_rates[course].append(grade)
        else:
            if course in lect.courses_attached:
                lect.course_rates[course] = [grade]
            else:
                print('ЗА ЭТИМ ЛЕКТОРОМ НЕ ЗАКРЕПЛЕН ДАННЫЙ КУРС')
        
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
class Lecturer(Mentor):
    # оценки от студентов {название курса : список оценок}
    course_rates = {}

    def __str__(self):
        n_rates = 0
        rate_sum = 0

        for course, rates in self.course_rates.items():
            # for rate in rates:
                # rate_sum += rate
                # n_rates += 1
            n_rates += len(rates)
            rate_sum += sum(rates)

        mean_rate = rate_sum / n_rates
        res = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {mean_rate}\n"
        )
        
        return res

class Reviewer(Mentor):
    def __str__(self):
        res = (f"Имя: {self.name}\n"
               f"Фамилия: {self.surname}\n")
        
        return res

def mean_course_hw_grade(students, course):
    n_rates = 0
    rate_sum = 0

    for student in students:
        grades = student.grades[course]
        n_rates += len(grades)
        rate_sum += sum(grades)

    return rate_sum / n_rates

def mean_course_rate(lecturers, course):
    n_rates = 0
    rate_sum = 0

    for lecturer in lecturers:
        rates = lecturer.course_rates[course]
        n_rates += len(rates)
        rate_sum += sum(rates)

    return rate_sum / n_rates



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)


best_student.finished_courses += ['Python', 'Sql', 'Math']
best_student.rate_course(cool_mentor, 'Python', 1)
best_student.rate_course(cool_mentor, 'Python', 2)
best_student.rate_course(cool_mentor, 'Python', 3)

print(best_student)
# print(cool_mentor)
