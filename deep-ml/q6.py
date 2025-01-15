def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    ''' specifically 2x2
    Eigenvals satisfy: Av=λv
    found by solving: det(A−λI)=0
    for a 2x2 this is a quadratic eqn: λ^2−tr(A)λ+det(A)=0

    find lambda values that satisfy the quadratic
    where a is 1, b is tr(A), and c is det(A)

    trace (tr): a+d
    determinant (det): ad-bc
    '''
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    tr = -(a+d) # negated since quadratic eqn assums ax^2 + bx... but eigen val eqn has -
    det = a*d - b*c

    discrim = tr**2 - 4*det

    soln1 = (-tr + discrim**0.5) / 2
    soln2 = (-tr - discrim**0.5) / 2

    eigenvalues = sorted([soln1, soln2], reverse=True)

    return eigenvalues

if __name__ == '__main__':
    matrix = [[2, 1], [1, 2]]
    '''
    [[2, 1]
    [1, 2]]
    '''
    print(calculate_eigenvalues(matrix))