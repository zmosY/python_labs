import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    a = json.load(open(json_path))
    w = csv.DictWriter(open(csv_path, 'w', newline='', encoding="utf-8"), fieldnames=a[0].keys())
    w.writeheader()
    w.writerows(a)

# json_to_csv(f"data/lab05/samples/people.json", f"data/lab05/out/people_from_json.csv")

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    a = list(csv.DictReader(open(csv_path, 'r', newline='', encoding="utf-8")))
    json.dump(a, open(json_path, 'w', newline='', encoding="utf-8"), ensure_ascii=False, indent=2)

# csv_to_json(f"data/lab05/samples/people.csv", f"data/lab05/out/people_from_csv.json")
