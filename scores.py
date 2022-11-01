class Student:
    student_list=[]
    def __init__(self, name, surname, gender):
        Student.student_list.append(self)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _agv_grades(self):
        dict_G = self.grades
        sumG = 0
        countG = 0
        for key, val in dict_G.items():
            sumG += sum(dict_G[key])
            countG += len(val)
        agvG = round(sumG / countG, 2)
        return agvG

    def __str__(self):
        courses_in_progress = ','.join(self.courses_in_progress)
        finished_courses = ','.join(self.finished_courses)
        res = f'Студент\nИмя: {self.name} \nФамилия: {self.surname}\n' \
              f'Средния оценка за домашние задания: {self._agv_grades()}\n' \
              f'Курсы в процессе изучения: {courses_in_progress}\n' \
              f'Завершенные курсы: {finished_courses}\n '
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'Это не студент')
            return
        return self._agv_grades() < other._agv_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    L_list = []
    def __init__(self, name, surname):
        Lecturer.L_list.append(self)
        super().__init__(name, surname)
        self.grades = {}

    def _agv_grades(self):
        dict_G = self.grades
        sumG = 0
        countG = 0
        for key, val in dict_G.items():
            sumG += sum(dict_G[key])
            countG += len(val)
        agvG = round(sumG / countG, 2)
        return agvG

    def __str__(self):
        res = f'Лектор\nИмя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self._agv_grades()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'Это не Лектор')
            return
        return self._agv_grades() < other._agv_grades()




class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Проверяющий\nИмя: {self.name} \nФамилия: {self.surname}\n'
        return res

def agv_course(list_l, course):
    sum_g = 0
    count_g = 0
    for name_object in list_l:
        if course in name_object.grades.keys():
            sum_g += sum(list(map(int, name_object.grades[course])))
            count_g += len(list(map(int, name_object.grades[course])))
    lecturers_agv = round(sum_g/count_g, 2)
    return lecturers_agv



cool_lecturer = Lecturer("Barbara", 'Stels')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

lecturer = Lecturer("Victor", 'Kolomin')
lecturer.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.rate_hw(cool_lecturer, 'Python', 5)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Git', 5)
best_student.rate_hw(lecturer, 'Python', 10)
best_student.rate_hw(lecturer, 'Python', 10)

student = Student('Mark', 'Taylor', 'boy')
student.courses_in_progress += ['Python']
student.rate_hw(cool_lecturer, 'Python', 9)
student.rate_hw(cool_lecturer, 'Git', 8)
student.rate_hw(lecturer, 'Python', 9)
student.rate_hw(lecturer, 'Python', 6)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(student, 'Python', 10)
cool_reviewer.rate_hw(student, 'Python', 8)

cool_reviewer2 = Reviewer('Roby', 'Klark')
cool_reviewer2.courses_attached += ['Git']
cool_reviewer2.rate_hw(best_student, 'Git', 9)
cool_reviewer2.rate_hw(student, 'Git', 10)
cool_reviewer2.rate_hw(student, 'Git', 8)

print(cool_reviewer)
print(cool_reviewer2)

print(cool_lecturer)
print(lecturer)

print(best_student)
print(student)

print(student < best_student)
print(lecturer > cool_lecturer)
print(f'Средняя оценка за лекции всех лекторов в рамках курса Python: '
      f'{agv_course(Lecturer.L_list, "Python")}')

print(f'Средняя оценка за лекции всех лекторов в рамках курса Git: '
      f'{agv_course(Lecturer.L_list, "Git")}')

print(f'Cредняя оценка за домашнее задание по всем студентам в рамках курса Git: '
      f'{agv_course(Student.student_list, "Git")}')

print(f'Cредняя оценка за домашнее задание по всем студентам в рамках курса Python: '
      f'{agv_course(Student.student_list, "Python")}')

