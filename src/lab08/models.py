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