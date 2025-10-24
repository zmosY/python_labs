#  lab05

### Задание A — JSON ↔ CSV

```py
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

json_to_csv(f"data/lab05/samples/people.json", f"data/lab05/out/people_from_json.csv")
```

![Код и демонстрация работы](/images/lab05/imgA_01.png)
![Код и демонстрация работы](/images/lab05/imgA_02.png)

```py
import json
import csv

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    a = list(csv.DictReader(open(csv_path, 'r', newline='', encoding="utf-8")))
    json.dump(a, open(json_path, 'w', newline='', encoding="utf-8"), ensure_ascii=False, indent=2)

csv_to_json(f"data/lab05/samples/people.csv", f"data/lab05/out/people_from_csv.json")
```

![Код и демонстрация работы](/images/lab05/imgA_03.png)

![Код и демонстрация работы](/images/lab05/imgA_04.png)

---

### Задание B — CSV → XLSX

```py
import csv
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    awb = Workbook()
    b =  awb.active
    b.title = 'Sheet1'

    f = open(csv_path, 'r', newline='', encoding="utf-8")
    reader = csv.reader(f)
    for row in reader:
        b.append(row)

    awb.save(xlsx_path)

csv_to_xlsx('data/lab05/samples/people.csv', 'data/lab05/out/people.xlsx')
```

![Код и демонстрация работы](/images/lab05/imgA_03.png)
![Код и демонстрация работы](/images/lab05/imgB_01.png)


