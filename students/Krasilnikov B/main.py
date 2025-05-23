# цель: автоматизировать работу с данными студентов

# действия:
# - отчисление при падении успеваемости

import threading
import time

# имя, пол, курс, возраст, группа, форма обучения
students = {"Богдан": ["м", 8, 18, "python41", "очно", "учится", "должен денег"]}
students["Игнат"] = ["м", 1, 58, "вторая", "очно", "учится", "должен денег"]
grades = [["Богдан", "19:11", 5]]

lesson_time = 60
break_time = 15


def add_student():
    global students
    name = input('Введи имя нового студента')
    gender = input('Пол студента:"м","ж"')
    level = int(input('введите курс студента'))
    age = int(input('введите возраст студента'))
    group = input('Введите группу студента')
    form = input('Введите форму обучения студента')
    status = input(f'Введите статус студента \n обучается, отчислен или закончил обучение')
    dont_pay = input(f'укажите, есть ли долг по оплате')

    students[name] = [gender, level, age, group, form, status, dont_pay]

    print(students)


def del_student():
    global students
    name = input('какого студента удаляем? ')
    if name in students:
        students = list(students)
        students.remove(deleted_name)
        students = dict(students)
        print(students)
    else:
        print('Такого студента не существует')


def new_grade():
    while True:
        student_name = input("Введите имя студента: ")
        if student_name in students:
            time_of_grade = input("Введите время получения оценки через двоеточие: ")
            grade_number = input("Введите оценку: ")
            grades.append([student_name, time_of_grade, grade_number])
            print(f"Оценка {grade_number} для студента {student_name} добавлена")
            break
        else:
            print(f"Студент с именем {student_name} не найден.")


def dont_pay():
    print("Должники: ")
    for student in students:
        if students[student][6] == "должен денег":
            print(student)


def student_data():
    global students
    name = input('данные какого студента смотрим? ')
    if name in students:
        new_name = name.upper()
        obr_mame = new_name[::-2]
        print(f'имя     пол     курс        возраст     группа      форма обучения      статус      задолженность')
        print(obr_mame,students[name][0],students[name][1],students[name][2],students[name][3],students[name][4],students[name][5],students[name][6])
    else:
        print('Такого студента не существует')




def show_groups():
    group = input("Введите название группы: ")
    print(f"Студенты группы {group}: ")
    for student in students:
        if students[student][3] == group:
            print(student)


def top_students():
    pass
    students_grades ={}
    for grade in grades:
        if grade[0] in students_grades:
            students_grades[grade[0]].append(grade[2])
        else:
            students_grades[grade[0]] = [grade[2]]

    avg_grades = {}
    for student_grades in students_grades:
        avg_grades[student_grades] = sum(students_grades[student_grades]) / len(students_grades[student_grades])

    sorted_dict = dict(sorted(avg_grades.items(), key=lambda x: x[1], reverse=True))

    top_students = list(sorted_dict.items())[:3]
    for top_student in top_students:
        print(top_student[0])

def loop_task():
    while True:
        time.sleep(1)  # Simulate work

        # TODO: обработка данных


def user_input_task():
    while True:
        pass

        menu = """Список действий:
1) добавить студента
2) удалить студента
3) добавить оценку
4) вывести список неплательщиков
5)*просмотр данных студента
6) просмотреть состав группы
7)*топ 3 студента

Введите цифру действия: """

        # выбор действия
        selection = input(menu)

        # обработка пользовательского взаимодействия
        if selection == "1":
            add_student()
        elif selection == "2":
            del_student()
        elif selection == "3":
            new_grade()
        elif selection == "4":
            dont_pay()
        elif selection == "5":
            student_data()
        elif selection == "6":
            show_groups()
        elif selection == "7":
            top_students()
        else:
            print("Такого действия в списке нет")

        time.sleep(1)
        print("")

        # - просмотр данных студента
        # - вывести топ 3 студента


# Run loop in a separate thread
thread = threading.Thread(target=loop_task, daemon=True)
thread.start()

# Run user input in the main thread
user_input_task()