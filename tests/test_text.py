import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "text, casefold, yo2e, expected",
    [
        ("ПрИвЕт\nМИр\t", True, True, "привет мир"),
        ("ёжик, Ёлка", True, True, "ежик, елка"),
        ("Hello\r\nWorld", True, True, "hello world"),
        ("  двойные   пробелы  ", True, True, "двойные пробелы"),
        ("Hello", False, True, "Hello"),
        ("ёжик", True, False, "ежик"),
        ("", True, True, ""),
        ("   \n\t\r   ", True, True, ""),
    ],
)
def test_normalize(text, casefold, yo2e, expected):
    result = normalize(text, casefold=casefold, yo2e=yo2e)
    assert result == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
        ("!!!???...", []),
        ("Hello-world, это test-123!", ["Hello-world", "это", "test-123"]),
    ],
)
def test_tokenize(text, expected):
    result = tokenize(text)
    assert result == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"bb": 2, "aa": 2, "cc": 1}),
        ([], {}),
        (["hello"], {"hello": 1}),
        (["x", "x", "x"], {"x": 3}),
    ],
)
def test_count_freq(tokens, expected):
    result = count_freq(tokens)
    assert result == expected


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({"bb": 2, "aa": 2, "cc": 1}, None, [("aa", 2), ("bb", 2), ("cc", 1)]),
        ({"z": 2, "a": 2, "b": 2}, None, [("a", 2), ("b", 2), ("z", 2)]),
        ({}, 5, []),
        ({"a": 1, "b": 1}, 10, [("a", 1), ("b", 1)]),
        ({"a": 5, "b": 3}, 0, []),
    ],
)
def test_top_n(freq, n, expected):
    result = top_n(freq, n)
    assert result == expected
