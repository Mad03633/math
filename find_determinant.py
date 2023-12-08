from copy import deepcopy


def smaller_matrix(original_matrix, row, column):
    new_matrix = deepcopy(original_matrix)
    new_matrix.remove(original_matrix[row])
    for i in range(len(new_matrix)):
        new_matrix[i].remove(new_matrix[i][column])
    return new_matrix

def determinant(matrix):
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            print("Not a square matrix")
            return None
    if len(matrix) == 2:
        simple_determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return simple_determinant
    else:
        answer = 0
        num_columns = num_rows
        for j in range(num_columns):
            cofactor = (-1) ** (0+j) * matrix[0][j] * determinant(smaller_matrix(matrix, 0, j))
            answer += cofactor
        return answer

a_matrix = [[9, 7], 
            [8], 
            [6, 2]]
print(determinant(a_matrix))

a_matrix = [[2, 3], 
            [7, 1]]
print(determinant(a_matrix))

a_matrix = [[2, 3, 7, 1], 
            [7, 1, 9, 8],
            [8, 6, 1, 4],
            [0, 1, 4, 2]]
print(determinant(a_matrix))

