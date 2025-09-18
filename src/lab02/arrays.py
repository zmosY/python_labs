
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    return min(nums), max(nums)

#test min_max
# print('1:',min_max([3, -1, 5, 5, 0]))
# print('2:',min_max([42]))
# print('3:',min_max([-5, -2, -9]))
# try: print('4:',min_max([]))
# except Exception as e: print('4:',type(e).__name__)
# print('5:',min_max([1.5, 2, 2.0, -3.1]))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(sorted((set(nums))))

#test unique_sorted
# print('1:', unique_sorted([3, 1, 2, 1, 3]))
# print('2:', unique_sorted([]))
# print('3:', unique_sorted([-1, -1, 0, 2, 2]))
# print('4:', unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(nums : list[list | tuple]) -> list:
    ans = []
    for num in nums:
        if not isinstance(num, (list, tuple)):
            raise TypeError()
        for item in num:
            ans.append(item)
    return ans

#test flatten
# print('1:',flatten([[1, 2], [3, 4]]))
# print('2:',flatten(([1, 2], (3, 4, 5))))
# print('3:',flatten([[1], [], [2, 3]]))
# try: print('4:',flatten([[1, 2], "ab"]))
# except Exception as e: print('4:',type(e).__name__)

