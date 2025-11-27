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
