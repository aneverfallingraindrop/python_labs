def is_rectangular(mat: list[list]) -> bool:
    if not mat:
        return True
    rectangle_length = len(mat[0])
    for i in mat:
        if len(i) != rectangle_length:
            return False
    return True



def transpose(mat: list[list[float | int]]) -> list[list]:
    res = []
    if not is_rectangular(mat):
        raise ValueError
    if not mat:
        return mat
    for i in range(len(mat[0])):
        prog = []
        for j in range(len(mat)):
            prog.append(mat[j][i])
        res.append(prog)
    
    return res

def row_sums(mat: list[list[float | int]]) -> list[float]:
    res = []
    if not is_rectangular(mat):
        raise ValueError
    for i in mat:
        res.append(sum(i))
    return res

def col_sums(mat: list[list[float | int]]) -> list[float]:
    res = []
    mat = transpose(mat)
    if not is_rectangular(mat):
        raise ValueError
    for i in mat:
        res.append(sum(i))
    return res

print("transpose test cases")
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))

print("row_sums test cases")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))

print("col_sums test cases")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
