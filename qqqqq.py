def tpl_sort(tpl):
    if all(isinstance(i, int) for i in tpl):
        return tuple(sorted(tpl))
    else:
        return tpl
 
 
def slicer(tpl, element):
    if element in tpl:
        start = tpl.index(element)
        end = tpl.index(element, start + 1)
        return tpl[start:end + 1]
    else:
        return ()
        
        
def sieve(lst):
    return tuple(reversed(tuple(set(lst))))
    

def del_from_tuple(tpl, element):
    if element in tpl:
        return tuple(i for i in tpl if i != element)
    else:
        return tpl

from collections import namedtuple
        
Student = namedtuple('Student', ['name', 'age', 'grade', 'city'])

def good_students(students):
    total_grade = sum(student.grade for student in students)
    average_grade = total_grade / len(students)

    good_students_list = [student.name for student in students if student.grade >= average_grade]

    print(f"Ученики {', '.join(good_students_list)} в этом семестре хорошо учатся!")

students_tuple = (
    Student('Света', 20, 5, 'Москва'),
    Student('Коля', 21, 3, 'Санкт-Петербург'),
    Student('Петя', 19, 4, 'Новосибирск'),
    Student('Вася', 22, 5, 'Екатеринбург'),
    Student('Маша', 20, 2, 'Казань'),
    Student('Миша', 21, 5, 'Ростов-на-Дону'),
    Student('боб', 19, 4, 'Волгоград')
)

good_students(students_tuple)