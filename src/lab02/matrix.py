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
# print('1:', transpose([[1, 2, 3]]))
# print('2:', transpose([[1], [2], [3]]))
# print('3:', transpose([[1, 2], [3, 4]]))
# print('4:', transpose([]))
# try: print('5:', transpose([[1, 2], [3]]))
# except Exception as e: print('5:',type(e).__name__)

def row_sums(mat: list[list[float | int]]) -> list[float]:
    temp_list = []
    for row in mat:
        temp_list.append(len(row))
    if len(set(temp_list)) != 1:
        raise ValueError()
    ans = [sum(row) for row in mat]
    return ans

#test row_sums
# print('1:', row_sums([[1, 2, 3], [4, 5, 6]]))
# print('2:', row_sums([[-1, 1], [10, -10]]))
# print('3:', row_sums([[0, 0], [0, 0]]))
# try: print('4:', row_sums([[1, 2], [3]]))
# except Exception as e: print('4:',type(e).__name__)

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
# print('1:', col_sums([[1, 2, 3], [4, 5, 6]]))
# print('2:', col_sums([[-1, 1], [10, -10]]))
# print('3:', col_sums([[0, 0], [0, 0]]))
# try: print('4:', col_sums([[1, 2], [3]]))
# except Exception as e: print('4:',type(e).__name__)
