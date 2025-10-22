#  lab02

### Задание A

```py
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """При вызове можно выбрать кодировку при помощи аргумента encoding , например encoding="cp1251"""
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

import csv
from pathlib import Path
from typing import Iterable, Sequence

def ensure_parent_dir(path: str | Path) -> None:
    """"Создает родительские папки если нет"""
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    ensure_parent_dir(p.parent)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

#early tests
txt = read_text(f"data/input.txt")  # должен вернуть строку
print(txt)
write_csv([("word","count"),("test",3)], f"data/check.csv")
```
**intput.txt**

![Код и демонстрация работы](/images/lab04/img01_1.png)

**Вывод в кансоль строки**

![Код и демонстрация работы](/images/lab04/img01_2.png)

**check.csv**

![Код и демонстрация работы](/images/lab04/img01_3.png)

---

### Задание B

## Тест A

```py
from src.lab04.io_txt_csv import read_text,write_csv
from src.lab03.text_stats import text_stats
from src.lib.text import *

def text_rep(input, output,encoding = 'utf-8'):
    """
    input: Относительный путь к входному файлу (от корня проекта), например "data/lab04/input.txt"
    output: Относительный путь к выходному CSV-файлу, например "data/lab04/report.csv"
    """


    input_path =  input
    output_path =  output

    txt = read_text(input_path,encoding=encoding)
    # print(txt)
    text_stats(txt)
    txt = top_n(count_freq(tokenize(normalize(txt))))
    # print(txt)
    txt = [('word','count')] + txt
    write_csv(txt, output_path)



#test_A
text_rep("data/lab04/test_A/input.txt","data/lab04/test_A/result.csv")
```
**intput.txt**

![Код и демонстрация работы](/images/lab04/imgA_1.png)

**report.csv**
![Код и демонстрация работы](/images/lab04/imgA_2.png)

**Консоль**

![Код и демонстрация работы](/images/lab04/imgA_3.png)

---

## Тест B

```py
#test_B
text_rep("data/lab04/test_B/input.txt","data/lab04/test_B/result.csv")
```
**intput.txt**

![Код и демонстрация работы](/images/lab04/imgB_1.png)

**report.csv**

![Код и демонстрация работы](/images/lab04/imgB_2.png)

**Консоль**

![Код и демонстрация работы](/images/lab04/imgB_3.png)

---

## Тест C

```py
#test_C
text_rep("data/lab04/test_C/input.txt","data/lab04/test_C/result.csv",encoding='cp1251')
```
**intput.txt**

![Код и демонстрация работы](/images/lab04/imgC_1.png)

**report.csv**

![Код и демонстрация работы](/images/lab04/imgC_2.png)

**Консоль**

![Код и демонстрация работы](/images/lab04/imgC_3.png)

---

## Тест D

```py
def text_rep_multi(input : list, output,encoding = 'utf-8'):
    """
    input: Спиксок из Относительных путей к входным файлам (от корня проекта), например ["data/lab04/a.txt, data/lab04/b.txt"]"
    output: Относительный путь к выходной папке в которой будет лежать report_per_file.csv и report_per_file.csv, например "data/lab04"
    """


    output_path =  f"{output}/report_per_file.csv"
    txt_per_file = []
    txt_total = ''
    for i in range(len(input)):
        input_path =  input[i]
        txt = read_text(input_path, encoding=encoding)
        txt_total += ' ' + txt
        txt = top_n(count_freq(tokenize(normalize(txt))))
        txt = [(str(input_path).split('/')[-1],) + i for i in txt]
        txt_per_file += txt
    txt_per_file = [('file','world','count')] + txt_per_file
    write_csv(txt_per_file, output_path)

    output_path =  f"{output}/report_total.csv"
    txt_total = top_n(count_freq(tokenize(normalize(txt_total))))
    txt_total = [('word','count')] + txt_total
    write_csv(txt_total, output_path)

#test_D
text_rep_multi(['data/lab04/test_D/a.txt','data/lab04/test_D/b.txt'],"data/lab04/test_D")
```
**a.txt**

![Код и демонстрация работы](/images/lab04/imgD_1.png)

**b.csv**

![Код и демонстрация работы](/images/lab04/imgD_2.png)

**report_per_file.csv**

![Код и демонстрация работы](/images/lab04/imgD_3.png)

**report_total.csv**

![Код и демонстрация работы](/images/lab04/imgD_4.png)





