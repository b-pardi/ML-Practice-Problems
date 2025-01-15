# 1 easy
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    n_mat_rows, n_mat_cols = len(a), len(a[0])

    # check if can be dotted
    if n_mat_cols != len(b):
        return -1

    c = []
    for i in range(n_mat_rows):
        elem = 0
        for j in range(n_mat_cols):
            elem += a[i][j] * b[j]
        c.append(elem)

    return c

if __name__ == '__main__':
    a = [[1,2],[2,4]]
    b = [1,2]
    '''
    [[1, 2]  [1
    [2, 4]]   2]
    '''
    print(matrix_dot_vector(a, b))