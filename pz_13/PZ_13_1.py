# Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и последних строках и столбцах матрицы Matr2 произвольного размера.

Matr2 = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

n_rows = len(Matr2)
n_cols = len(Matr2[0])

Matr1 = []
for i in range(1, n_rows - 1):
    row = []
    for j in range(1, n_cols - 1):
        row.append(Matr2[i][j])
    Matr1.append(row)

print('Исходная матрица:')
for row in Matr2:
    print(row)

print('Новая матрица:')
for row in Matr1:
    print(row)
