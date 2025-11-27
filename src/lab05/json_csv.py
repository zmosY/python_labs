import json
import csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует JSON-файл в CSV.

    Ожидает на вход список словарей [{...}, {...}]. Для пустого или некорректного
    JSON будет поднят ValueError. FileNotFoundError для несуществующего пути не
    перехватывается (по умолчанию).
    """
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        raise ValueError("Invalid JSON file") from exc

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("JSON must be a non-empty list of objects")

    # first row must be a mapping to determine headers
    first = data[0]
    if not isinstance(first, dict):
        raise ValueError("JSON items must be objects / mappings")

    fieldnames = list(first.keys())
    with open(csv_path, "w", newline="", encoding="utf-8") as out:
        writer = csv.DictWriter(out, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# json_to_csv(f"data/lab05/samples/people.json", f"data/lab05/out/people_from_json.csv")

def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в JSON (список словарей).

    Если CSV повреждён, будет поднят ValueError. FileNotFoundError для
    несуществующего входного файла не перехватывается.
    """
    try:
        with open(csv_path, "r", newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except csv.Error as exc:
        raise ValueError("Malformed CSV file") from exc

    with open(json_path, "w", newline="", encoding="utf-8") as out:
        json.dump(rows, out, ensure_ascii=False, indent=2)

# csv_to_json(f"data/lab05/samples/people.csv", f"data/lab05/out/people_from_csv.json")
