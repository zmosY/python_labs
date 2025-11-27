#  lab08

### Задание A. Реализовать класс Student (models.py)

```py
from datetime import datetime, date
from dataclasses import dataclass

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            raise (ValueError("warning: birthdate format might be invalid"))

        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 10")

    def age(self) -> int:
        b = datetime.strptime(self.birthdate, "%Y/%m/%d").date()
        today = date.today()
        return today.year - b.year - ((today.month, today.day) < (b.month, b.day))

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(fio=d["fio"],
                   birthdate=d["birthdate"],
                   group=d["group"],
                   gpa=float(d["gpa"]))

    def __str__(self):
        return f"Студент: {self.fio}, Группа: {self.group}, gpa: {self.gpa}"


#test Student
# s1 = Student(fio="Иванов И.И.", birthdate="2000/05/12", group="CS-101", gpa=3.3)
# print(s1)
# print(f"Возраст: {s1.age()}")
# print(s1.to_dict())
# data = {"fio": "Петров П.П.", "birthdate": "2001/01/01", "group": "MATH-2", "gpa": 4.0}
# s2 = Student.from_dict(data)
# print(f"Студент 2 создан: {s2.fio}")
```

![Код и демонстрация работы](/images/lab08/imgA_01.png)


---

### Задание B. Реализовать модуль serialize.py

```py
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
```
```py
students = [
    Student(fio="Додиков А.А.", birthdate="2003/05/10", group="ГР-1", gpa=1.0),
    Student(fio="Слабаков Б.Б.",   birthdate="2002/11/12", group="ГР-1", gpa=2.0),
    Student(fio="Середняков В.В.", birthdate="2003/01/20", group="ГР-2", gpa=3.0),
    Student(fio="Хорошистов Г.Г.", birthdate="2001/09/01", group="ГР-2", gpa=4.0),
    Student(fio="Отличников Д.Д.", birthdate="2002/03/15", group="ГР-3", gpa=5.0)
]

students_to_json(students, path='data/lab08/out/students_output.json')
```
![Код и демонстрация работы](/images/lab08/imgB_01.png)




```py
s = students_from_json(path='data/lab08/samples/students_input.json')
for student in s:
    print(student)
```

![Код и демонстрация работы](/images/lab08/imgB_02.png)
![Код и демонстрация работы](/images/lab08/imgB_03.png)

