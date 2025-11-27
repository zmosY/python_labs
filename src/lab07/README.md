#  lab07

### Задание A. Тесты для src/lib/text.py

```py
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n

@pytest.mark.parametrize(
    "text, casefold, yo2e, expected",
    [
        ("ПрИвЕт\nМИр\t", True, True, "привет мир"),              # normalize with case folding
        ("ёжик, Ёлка", True, True, "ежик, елка"),                 # yo2e replacement
        ("Hello\r\nWorld", True, True, "hello world"),             # newlines and carriage return
        ("  двойные   пробелы  ", True, True, "двойные пробелы"), # multiple spaces
        ("Hello", False, True, "Hello"),                           # casefold disabled
        ("ёжик", True, False, "ёжик"),                             # yo2e disabled
        ("", True, True, ""),                                       # empty string
        ("   \n\t\r   ", True, True, ""),                           # whitespace only
    ],
)
def test_normalize(text, casefold, yo2e, expected):
    result = normalize(text, casefold=casefold, yo2e=yo2e)
    assert result == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),                         # basic tokenization
        ("hello,world!!!", ["hello", "world"]),                    # punctuation removal
        ("по-настоящему круто", ["по-настоящему", "круто"]),      # hyphenated words
        ("2025 год", ["2025", "год"]),                             # numbers
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),           # emoji ignored
        ("", []),                                                   # empty string
        ("!!!???...", []),                                         # only punctuation
        ("Hello-world, это test-123!", ["Hello-world", "это", "test-123"]),  # mixed
    ],
)
def test_tokenize(text, expected):
    result = tokenize(text)
    assert result == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),  # basic counting
        (["bb", "aa", "bb", "aa", "cc"], {"bb": 2, "aa": 2, "cc": 1}),  # cyrillic
        ([], {}),                                                       # empty list
        (["hello"], {"hello": 1}),                                     # single element
        (["x", "x", "x"], {"x": 3}),                                   # all same
    ],
)
def test_count_freq(tokens, expected):
    result = count_freq(tokens)
    assert result == expected


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),                              # with limit
        ({"bb": 2, "aa": 2, "cc": 1}, None, [("aa", 2), ("bb", 2), ("cc", 1)]),          # without limit
        ({"z": 2, "a": 2, "b": 2}, None, [("a", 2), ("b", 2), ("z", 2)]),                # alphabetical sorting
        ({}, 5, []),                                                                      # empty dict
        ({"a": 1, "b": 1}, 10, [("a", 1), ("b", 1)]),                                    # limit > size
        ({"a": 5, "b": 3}, 0, []),                                                       # limit zero
    ],
)
def test_top_n(freq, n, expected):
    result = top_n(freq, n)
    assert result == expected
```

![Код и демонстрация работы](/images/lab07/imgA_01.png)


---

### Задание B. Тесты для src/lab05/json_csv.py

```py
import pytest
import json
import csv
from pathlib import Path

from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    csv_text = "name,age\nAlice,22\nBob,25\n"
    src.write_text(csv_text, encoding="utf-8")
    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) == 2
    assert {"name", "age"} <= set(data[0].keys())


def test_json_to_csv_empty_input_raises_or_indexerror(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "out.csv"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_nonexistent_input_raises(tmp_path: Path):
    src = tmp_path / "no_such.json"
    dst = tmp_path / "out.csv"

    with pytest.raises(FileNotFoundError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_nonexistent_input_raises(tmp_path: Path):
    src = tmp_path / "no_such.csv"
    dst = tmp_path / "out.json"

    with pytest.raises(FileNotFoundError):
        csv_to_json(str(src), str(dst))

```

![Код и демонстрация работы](/images/lab07/imgB_01.png)


