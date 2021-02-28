"""
Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:

- для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов
принимаем список студентов и название курса);
- для подсчета средней оценки за лекции всех лекторов в рамках конкретного курса (в качестве аргументов принимаем
список лекторов и название курса).
"""
from classes import Student, Lecturer, Reviewer

def average_grades_key(persons: list, key: str) -> float:
    """
    Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов
    принимаем список студентов и название курса
    Также способна работать с оценками лекторов.
    """
    grades = [one_person.get_average_grade(key) for one_person in persons]
    return sum(grades)/len(grades)

def average_grades_lectors(lectors: list, course: str):
    grades = [one_lector.get_average_grade() for one_lector in lectors if course in one_lector.courses_attached]
    return sum(grades)/len(grades)


def main():
    lec_1 = Lecturer("Лев", "Матанов")
    lec_2 = Lecturer("Леонид", "Гуманитариев")
    rev_1 = Reviewer("Роман", "Добров")
    rev_2 = Reviewer("Родион", "Недобров")
    stu_1 = Student("Степан", "Хорошистов", "муж.")
    stu_2 = Student("Сергей", "Троечников", "муж.")

    lec_1.courses_attached = ["Матан", "IT", "Cpp", "НЛП"]
    lec_2.courses_attached = ["ИЗО", "История", "НЛП"]

    rev_1.courses_attached = ["Матан", "IT", "НЛП"]
    rev_2.courses_attached = ["ИЗО", "История", "Cpp", "НЛП"]

    stu_1.courses_in_progress = ["Матан", "IT", "Cpp", "НЛП"]
    stu_1.finished_courses = ["ИЗО", "История", "НЛП"]

    stu_2.courses_in_progress = ["ИЗО", "История", "НЛП"]
    stu_2.finished_courses = ["Матан", "IT", "Cpp", "НЛП"]

    stu_1.rate_lecture(lec_1, 5)
    stu_1.rate_lecture(lec_2, 3)

    stu_2.rate_lecture(lec_1, 9)
    stu_2.rate_lecture(lec_2, 3)

    rev_1.rate_hw(stu_1, "Матан", 4)
    rev_1.rate_hw(stu_1, "Матан", 5)
    rev_1.rate_hw(stu_1, "IT", 4)

    rev_1.rate_hw(stu_2, "ИЗО", 4)
    rev_1.rate_hw(stu_2, "История",3)

    rev_2.rate_hw(stu_1, "Сpp", 3)
    rev_2.rate_hw(stu_1, "НЛП", 5)

    rev_2.rate_hw(stu_2, "НЛП", 2)
    rev_2.rate_hw(stu_2, "История", 4)

    stu_1.rate_lecture(lec_1, 3)
    stu_1.rate_lecture(lec_2, 5)
    stu_2.rate_lecture(lec_1, 4)
    stu_2.rate_lecture(lec_2, 7)

    all_people = [str(man) for man in [lec_1, lec_2, rev_1, rev_2, stu_1, stu_2]]
    print(";\n\n".join(all_people))
    print("Средняя оценка за Матан: ", end='')
    print(average_grades_key([stu_1, stu_2], "Матан"))
    print("Средняя оценка за НЛП: ", end='')
    print(average_grades_key([stu_1, stu_2], "НЛП"))

    print("Средняя оценка лекторов на Матане: ", end='')
    print(average_grades_lectors([lec_1, lec_2], "Матан"))
    print("Средняя оценка лекторов на НЛП: ", end='')
    print(average_grades_lectors([lec_1, lec_2], "НЛП"))

    if stu_1 > stu_2:
        print(f"\nЛучше учится:\n{stu_1}")
    else:
        print(f"\nЛучше учится:\n {stu_2}")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
