# Напишите функцию для транспонирования матрицы

def matrix_trans():
    matrix_a = [[5, 4, 3], [2, 4, 6], [4, 7, 9], [8, 1, 3]]
    trans_result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for a in range(len(matrix_a)):
        for b in range(len(matrix_a[0])):
            trans_result[b][a] = matrix_a[a][b]
    print("The matrix A is: ")
    for res in matrix_a:
        print(res)
    print("The transpose of matrix A is: ")
    for res in trans_result:
        print(res)


if __name__ == '__main__':
    matrix_trans()