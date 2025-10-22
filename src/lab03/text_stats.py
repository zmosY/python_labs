from src.lib.text import top_n


def text_stats(s, beautiful = False):
    from src.lib.text import tokenize,normalize,count_freq
    s = tokenize(normalize(s))
    print(f'Всего слов: {len(s)}')
    print(f'Уникальных слов: {len(set(s))}')
    print('Топ-5:')
    s = top_n(count_freq(s),5)
    # print(s)
    if beautiful:
        max_word_len = max([len(x[0]) for x in s]) + 3
        print(f"{'слово':<{max_word_len}} | частота")
        print("-" * (max_word_len + 10))
        for word, freq in s:
            print(f"{word:<{max_word_len}} | {freq}")
    else:
        for word, freq in s:
            print(f"{word}:{freq}")

#test
# text_stats(input(),beautiful=True)