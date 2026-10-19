"""
Matrix exponentiation for logarithmic Fibonacci calculation.
"""
def matrix_mult_2x2(A, B):
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

def matrix_pow(M, p):
    res = [[1, 0], [0, 1]]
    base = M
    while p > 0:
        if p % 2 == 1: res = matrix_mult_2x2(res, base)
        base = matrix_mult_2x2(base, base)
        p //= 2
    return res
