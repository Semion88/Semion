def fill_matrix(r, c):
    try:
        matrix = []
        print("Введите значения матрицы:")
        for row_idx in range(r):
            matrix.append([])
            user_input = input()
            matrix_values = user_input.split(" ")
            for col_idx in range(c):
                matrix[row_idx].append(int(matrix_values[col_idx]))
        return matrix
    except:
        print("Ошибка: неправильно введены значения матрицы")


def matrix_sum(a_size, matrix_a, b_size, matrix_b):
    if a_size.split(' ')[0] == b_size.split(' ')[0] and a_size.split(' ')[1] == b_size.split(' ')[1]:
        final_matrix = []
        for row_idx in range(int(a_size.split(' ')[0])):
            final_matrix.append([])
            for col_idx in range(int(a_size.split(' ')[1])):
                final_matrix[row_idx].append(matrix_a[row_idx][col_idx] + matrix_b[row_idx][col_idx])

        return final_matrix
    else:
        print("Error: matrices arent equal")


def matrix_multiple(a_size, matrix_a):
    const = int(input("Введите константу"))
    final_matrix = []
    for row_idx in range(int(a_size.split(' ')[0])):
        final_matrix.append([])
        for col_idx in range(int(a_size.split(' ')[1])):
            final_matrix[row_idx].append(matrix_a[row_idx][col_idx] * const)

    return final_matrix

def main():
    try:
        size_a = input("Введите размер матрицы A: ") # 4 4
        matrix_a = fill_matrix(int(size_a.split(" ")[0]), int(size_a.split(" ")[1]))

        size_b = input("Введите размер матрицы B: ")
        matrix_b = fill_matrix(int(size_b.split(" ")[0]), int(size_b.split(" ")[1]))

        summed_matrix = matrix_sum(size_a, matrix_a, size_b, matrix_b)
        print(summed_matrix)
        multiplied_matrix = matrix_multiple(size_a, matrix_a)
        print(multiplied_matrix)
    except:
        print("Ошибка: Неправельно введён размер матрицы")