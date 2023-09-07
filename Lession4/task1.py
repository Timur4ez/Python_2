# Напишите функцию для транспонирования матрицы

def transp_matrix(matrix):
    transp_matrix = [[matrix[j][i] for j in range(len(matrix))] 
                         for i in range(len(matrix[0]))]
    return transp_matrix

matrix = [[12, 11, 10], [19, 12, 49]]
result = transp_matrix(matrix)
print(result)