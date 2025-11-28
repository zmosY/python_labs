import csv
from pathlib import Path
from src.lab08.models import Student
from src.lab08.serialize import students_from_json, students_to_json


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self.fieldnames = ["fio", "birthdate", "group", "gpa"]
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()

    def _read_all(self) -> list[Student]:
        self._ensure_storage_exists()
        students = []
        with open(self.path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(Student.from_dict(row))
        return students

    def list(self) -> list[Student]:
        return self._read_all()

    def add(self, student: Student):
        self._ensure_storage_exists()

        with open(self.path, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writerow(student.to_dict())

    def find(self, substr: str) -> list[Student]:
        students = self._read_all()
        q = []
        for s in students:
            if substr.lower() in s.fio.lower():
                q.append(s)
        return q

    def remove(self, fio: str):
        students = self._read_all()
        new_students = [s for s in students if s.fio != fio]
        if len(students) != len(new_students):
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                for s in new_students:
                    writer.writerow(s.to_dict())

    def remove_all(self):
        students = []
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for s in students:
                writer.writerow(s.to_dict())

    def update(self, fio: str, **ost):
        students = self._read_all()
        flag = False
        for s in students:
            if s.fio == fio:
                for key, value in ost.items():
                    if hasattr(s, key):
                        setattr(s, key, value)
                flag = True
                break
        if flag:
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                for s in students:
                    writer.writerow(s.to_dict())

    def stats(self) -> dict:
        students = self._read_all()
        if not students:
            return {"count": 0}
        groups = {}
        for u in students:
            if u.group not in groups:
                groups[u.group] = 1
            else:
                groups[u.group] += 1
        top = [{"fio": s.fio, "gpa": s.gpa} for s in students]
        top = sorted(top, key=lambda x: (-x["gpa"], x["fio"]))
        gpas = [s.gpa for s in students]
        return {
            "count": len(students),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "avg_gpa": round(sum(gpas) / len(students), 2),
            "groups": groups,
            "top_5_students": top[5:]
        }


#test Group
# students = students_from_json("data/lab08/samples/students_input.json")
# q = Group("data/lab09/students.csv")
# q.remove_all()
# for i in students:
#     q.add(i)
# print(*q.list(),sep='\n')
# print()
# print(*q.find("ов"),sep='\n')
# q.remove("Алексеева А.М.")
# q.update("Борисов Б.В.",birthdate = '2011/11/05',group='dsadfg-101',gpa=1.0)
# print()
# print(q.stats())
