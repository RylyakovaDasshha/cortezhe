from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'grade', 'city'])

def good_students(students):
    total_grades = 0
    for student in students:
        total_grades += student.grade
    avg_grade = total_grades / len(students)
    
    good_students_list = []
    for student in students:
        if student.grade >= avg_grade:
            good_students_list.append(student.name)
    
    print(f"Ученики {', '.join(good_students_list)} в этом семестре хорошо учатся!")

students = [
    Student("Иван", 20, 80, "Москва"),
    Student("Мария", 22, 90, "Санкт-Петербург"),
    Student("Алексей", 21, 75, "Новосибирск"),
    Student("Екатерина", 23, 85, "Екатеринбург"),
    Student("Андрей", 20, 92, "Казань"),
    Student("Ольга", 21, 88, "Уфа"),
    Student("Дмитрий", 22, 78, "Новосибирск")
]

good_students(students)
