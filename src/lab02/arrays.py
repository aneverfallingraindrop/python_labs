def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError
    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(sorted(set(nums)))


def flatten(mat: list[list | tuple]) -> list:
    res = []
    for i in mat:
        if type(i) in (list, tuple):
            for j in i:
                res.append(j)
        else:
            raise TypeError
    return res


print("min_max test cases")
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
# print(min_max([])) skipped: raises ValueError, thus interrupting the code flow but it does work
print(min_max([1.5, 2, 2.0, -3.1]))

print("unique_sorted test cases")
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print("flatten test cases")
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
# print(flatten([[1, 2], "ab"])) again, skipped since raising an error interrupts flow, is functional
