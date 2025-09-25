#  lab02

### Задание 1

```py
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    minv = 10 ** 100
    maxv = -10 ** 100
    for num in nums:
        if num < minv:
            minv = num
        if num > maxv:
            maxv = num
    return minv, maxv

#test min_max
print('1:',min_max([3, -1, 5, 5, 0]))
print('2:',min_max([42]))
print('3:',min_max([-5, -2, -9]))
try: print('4:',min_max([]))
except Exception as e: print('4:',type(e).__name__)
print('5:',min_max([1.5, 2, 2.0, -3.1]))
```

![Код и демонстрация работы](/images/lab02/img01_1.png)

```py
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    ans = []
    for i in range(len(nums)):
        if nums[i] not in ans:
            ans.append(nums[i])
    for i in range(len(ans) - 1):
        for j in range(len(ans) - 1 - i):
            if ans[j] > ans[j + 1]:
                ans[j], ans[j + 1] = ans[j + 1], ans[j]
    return ans

#test unique_sorted
print('1:', unique_sorted([3, 1, 2, 1, 3]))
print('2:', unique_sorted([]))
print('3:', unique_sorted([-1, -1, 0, 2, 2]))
print('4:', unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```

![Код и демонстрация работы](/images/lab02/img01_2.png)

```py
def flatten(nums : list[list | tuple]) -> list:
    ans = []
    for num in nums:
        if not isinstance(num, (list, tuple)):
            raise TypeError()
        for item in num:
            ans.append(item)
    return ans

#test flatten
print('1:',flatten([[1, 2], [3, 4]]))
print('2:',flatten(([1, 2], (3, 4, 5))))
print('3:',flatten([[1], [], [2, 3]]))
try: print('4:',flatten([[1, 2], "ab"]))
except Exception as e: print('4:',type(e).__name__)
```

![Код и демонстрация работы](/images/lab02/img01_3.png)

---

### Задание 2 (B)

```py
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    ans = [[0] * len(mat) for _ in range(len(mat[0]))]
    temp_list = []
    for row in mat:
        temp_list.append(len(row))
    if len(set(temp_list)) != 1:
        raise ValueError()
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            ans[j][i] = mat[i][j]
    return ans

#test transpose
print('1:', transpose([[1, 2, 3]]))
print('2:', transpose([[1], [2], [3]]))
print('3:', transpose([[1, 2], [3, 4]]))
print('4:', transpose([]))
try: print('5:', transpose([[1, 2], [3]]))
except Exception as e: print('5:',type(e).__name__)
```

![Код и демонстрация работы](/images/lab02/img02_1.png)

```py
def row_sums(mat: list[list[float | int]]) -> list[float]:
    temp_list = []
    for row in mat:
        temp_list.append(len(row))
    if len(set(temp_list)) != 1:
        raise ValueError()
    ans = [sum(row) for row in mat]
    return ans

#test row_sums
print('1:', row_sums([[1, 2, 3], [4, 5, 6]]))
print('2:', row_sums([[-1, 1], [10, -10]]))
print('3:', row_sums([[0, 0], [0, 0]]))
try: print('4:', row_sums([[1, 2], [3]]))
except Exception as e: print('4:',type(e).__name__)
```

![Код и демонстрация работы](/images/lab02/img02_2.png)

```py
def col_sums(mat: list[list[float | int]]) -> list[float]:
    temp_list = []
    for row in mat:
        temp_list.append(len(row))
    if len(set(temp_list)) != 1:
        raise ValueError()
    ans = [0 for _ in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            ans[j] += mat[i][j]
    return ans

#test col_sums
print('1:', col_sums([[1, 2, 3], [4, 5, 6]]))
print('2:', col_sums([[-1, 1], [10, -10]]))
print('3:', col_sums([[0, 0], [0, 0]]))
try: print('4:', col_sums([[1, 2], [3]]))
except Exception as e: print('4:',type(e).__name__)
```

![Код и демонстрация работы](/images/lab02/img02_3.png)

---

### Задание 3 (C)

```py
def format_record(rec: tuple[str, str, float]) -> str:
    fio_parts = rec[0].split()
    fam = fio_parts[0].capitalize()
    name_init = fio_parts[1][0].upper()
    otch_init = [p[0].upper() for p in fio_parts[2:]]
    initials = name_init + ''.join('.' + i for i in otch_init) + '.'
    gpa_str = f"{rec[2]:.2f}"
    return f"{fam} {initials}, гр. {rec[1]}, GPA {gpa_str}"

#test format_record
print('1:', format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print('2:', format_record(("Петров Пётр", "IKBO-12", 5.0)))
print('3:', format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print('4:', format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```

![Код и демонстрация работы](/images/lab02/img03.png)





