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

# csv_to_xlsx('data/lab05/samples/people.csv', 'data/lab05/out/people.xlsx')