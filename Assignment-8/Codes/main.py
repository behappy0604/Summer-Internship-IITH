import numpy as np
def matrix_cofactor(matrix):
    C = np.zeros(matrix.shape)
    nrows, ncols = C.shape
    for row in range(nrows):
        for col in range(ncols):
            minor = matrix[np.array(list(range(row))+list(range(row+1,nrows)))[:,np.newaxis],
                           np.array(list(range(col))+list(range(col+1,ncols)))]
            C[row, col] = (-1)**(row+col) * np.linalg.det(minor)
    return C
M = np.array([5, 3, 8, 2, 0, 1, 1, 2, 3]).reshape((3, 3))
print(M)
cofactors = matrix_cofactor(M)
print("Cofator of Matrix", M, "are", cofactors)