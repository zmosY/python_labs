#  lab03

### Задание A — src/lib/text.py

```py
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('Ё','Е').replace('ё','е')
    text = text.replace('\n',' ').replace('\t',' ').replace('\r',' ')
    text = re.sub(r'\s+', ' ', text.strip())
    return text

#test normalize
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка",yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```

![Код и демонстрация работы](/images/lab03/img01_1.png)

```py
def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)

# test tokenize
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```

![Код и демонстрация работы](/images/lab03/img01_2.png)

```py
def count_freq(tokens: list[str]) -> dict[str, int]:
    ans = {}
    for token in tokens:
        if token not in ans:
            ans[token] = 1
        else:
            ans[token] += 1
    return ans

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1],x[0]))[:n]

#test count_freq and top_n
print(count_freq(["a","b","a","c","b","a"]))
print(top_n(count_freq(["a","b","a","c","b","a"]), 2))
print(count_freq(["bb","aa","bb","aa","cc"]))
print(top_n(count_freq(["bb","aa","bb","aa","cc"]), 2))
```

![Код и демонстрация работы](/images/lab03/img01_3.png)

---

### Задание B — src/text_stats.py (скрипт со stdin)

```py
def text_stats(s, beautiful = False):
    from src.lib.text import tokenize,normalize,count_freq
    s = tokenize(normalize(s))
    print(f'Всего слов: {len(s)}')
    print(f'Уникальных слов: {len(set(s))}')
    print('Топ-5:')
    s = count_freq(s)
    if beautiful:
        max_word_len = max([len(x) for x in s]) + 3
        print(f"{'слово':<{max_word_len}} | частота")
        print("-" * (max_word_len + 10))
        cnt = 0
        for word, freq in s.items():
            if cnt == 5: break
            print(f"{word:<{max_word_len}} | {freq}")
            cnt += 1
    else:
        cnt = 0
        for word, freq in s.items():
            if cnt == 5: break
            print(f"{word}:{freq}")
        cnt += 1

#test
print(text_stats(input(),beautiful=True))
```

![Код и демонстрация работы](/images/lab03/img02.png)


