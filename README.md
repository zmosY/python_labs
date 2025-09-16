# ДЗ за 10.09.2025 (lab01)

### Задание 1 — Привет и возраст

```name = input("Имя: ")
age = int(input("Возраст: "))
print(f'Привет, {name}! Через год тебе будет {age + 1}.')
```

![Код и демонстрация работы](/images/lab01/img01.png)

---

### Задание 2 — Сумма и среднее

```a = float(input("a: ").replace(',', '.'))
b = float(input("b: ").replace(',', '.'))
print(f'sum={a + b}; avg={((a + b) / 2):.2f}')
```

![Код и демонстрация работы](/images/lab01/img02.png)

---

### Задание 3 — Чек: скидка и НДС

```price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f'База после скидки: {base:.2f} ₽')
print(f'НДС: {vat_amount:.2f} ₽')
print(f'Итого к оплате: {total:.2f} ₽')
```

![Код и демонстрация работы](/images/lab01/img03.png)

---

### Задание 4 — Минуты → ЧЧ:ММ

```m = int(input('Минуты: '))
print(f'{(m // 60) % 24}:{(m % 60):02d}')
```

![Код и демонстрация работы](/images/lab01/img04.png)

---

### Задание 5 — Инициалы и длина строки

```fio = input('ФИО: ')
ansfio = ''
anscnt = 0
for i in fio:
    if i.isupper():
        ansfio += i
    if i != ' ':
        anscnt += 1
print(f'Инициалы: {ansfio}')
print(f'Длина (символов): {anscnt + 2}')
```

![Код и демонстрация работы](/images/lab01/img05.png)

