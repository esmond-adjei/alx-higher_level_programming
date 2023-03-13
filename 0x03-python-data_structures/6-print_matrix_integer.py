#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_len = len(matrix)
    col_len = len(matrix[0])
    if row_len == 1 and col_len == 0:
        print()
    else:
        for i in range(row_len):
            for j in range(col_len):
                if j == col_len - 1:
                    print("{:d}".format(matrix[i][j]), end='\n')
                else:
                    print("{:d}".format(matrix[i][j]), end=' ')
