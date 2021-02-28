class AveragedGrade:
    def get_average_grade(self, key=""):
        if self.grades:
            if key:
                if key in self.grades:
                    return sum(self.grades[key]) / len(self.grades[key])
            else:
                _sum = sum([sum(one_line) for one_line in self.grades.values()])
                _len = sum([len(one_line) for one_line in self.grades.values()])
                return _sum / _len
        return 0

    def __eq__(self, other, key=""):
        if type(self) == type(other):
            return self.get_average_grade(key) == other.get_average_grade(key)
        else:
            return "Ошибка"

    def __ne__(self, other, key=""):
        if type(self) == type(other):
            return self.get_average_grade(key) != other.get_average_grade(key)
        else:
            return "Ошибка"

    def __lt__(self, other, key=""):
        if type(self) == type(other):
            return self.get_average_grade(key) < other.get_average_grade(key)
        else:
            return "Ошибка"

    def __le__(self, other, key=""):
        if type(self) == type(other):
            return self.get_average_grade(key) <= other.get_average_grade(key)
        else:
            return "Ошибка"

    def __gt__(self, other, key=""):
        if type(self,) == type(other):
            return self.get_average_grade(key) > other.get_average_grade(key)
        else:
            return "Ошибка"

    def __ge__(self, other, key=""):
        if type(self) == type(other):
            return self.get_average_grade(key) >= other.get_average_grade(key)
        else:
            return "Ошибка"


class Student(AveragedGrade):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, grade):
        if isinstance(lecturer, Lecturer) and 1 <= grade <= 10:
            my_courses = set(self.finished_courses + self.courses_in_progress)
            for one_course in my_courses:
                if one_course in lecturer.courses_attached:
                    # Один студент - одна оценка
                    lecturer.grades[self.surname + " " + self.name] = [grade]
        return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.get_average_grade()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, AveragedGrade):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\n" \
        f"Фамилия: {self.surname}\n" \
        f"Средняя оценка за лекции: {self.get_average_grade()}"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
