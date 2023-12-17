from collections import namedtuple
Student = namedtuple('Student', 'name age grade city')
students = (
   Student('Александра', '13', 4.3, 'Москва'),
   Student('Полина', '21', 5, 'Чулым'),
   Student('Елизавета', '17', 2.9, 'Санкт-Петербург'),
   Student('Евгений', '18', 3, 'Новосибирск'),
   Student('Ольга', '17', 4.5, 'Астана'),
   Student('Людмила', '18', 3.2, 'Барнаул'),
   Student('Константин', '16', 3.7, 'Сыктывкар')
)
def gs(students):
   tg = 0

   for student in students:
       tg += student.grade
   a = tg / len(students)

   g = [student.name for student in students if student.grade >= a]
   print('Ученики ', ', '.join(g), ' в этом семестре хорошо учатся!')

gs(students)
