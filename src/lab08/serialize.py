import json
from models import Student


def students_to_json(students, path):
    data = [s.to_dict() for s in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data_list = json.load(f)
    return [Student.from_dict(d) for d in data_list]


#test students_to_json & students_from_json
# students = [
#     Student(fio="Додиков А.А.", birthdate="2003/05/10", group="ГР-1", gpa=1.0),
#     Student(fio="Слабаков Б.Б.",   birthdate="2002/11/12", group="ГР-1", gpa=2.0),
#     Student(fio="Середняков В.В.", birthdate="2003/01/20", group="ГР-2", gpa=3.0),
#     Student(fio="Хорошистов Г.Г.", birthdate="2001/09/01", group="ГР-2", gpa=4.0),
#     Student(fio="Отличников Д.Д.", birthdate="2002/03/15", group="ГР-3", gpa=5.0)
# ]
#
# students_to_json(students, path='data/lab08/out/students_output.json')
#
# s = students_from_json(path='data/lab08/samples/students_input.json')
# for student in s:
#     print(student)