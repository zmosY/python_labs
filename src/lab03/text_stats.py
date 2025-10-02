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
# print(text_stats(input(),beautiful=True))
