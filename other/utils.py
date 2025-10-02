from pathlib import Path

def get_project_root() -> Path:
    """возвращает корень проэкта"""
    current = Path(__file__).resolve()
    # Поднимаемся до тех пор, пока не найдём папки 'src' и 'data' рядом
    for parent in current.parents:
        if (parent / "src").is_dir() and (parent / "data").is_dir():
            return parent