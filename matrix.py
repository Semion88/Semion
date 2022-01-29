def fill_matrix(rows, cols):
    try:
        matrix = []
        print("Введите значения матрицы:")
        for row_idx in range(rows):
            matrix.append([])
            user_input = input()
            matrix_values = user_input.split(" ")
            for col_idx in range(cols):
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


def matrix_multiple_on_const(a_size, matrix_a):
    const = int(input("Введите константу: "))
    final_matrix = []
    for row_idx in range(int(a_size.split(' ')[0])):
        final_matrix.append([])
        for col_idx in range(int(a_size.split(' ')[1])):
            final_matrix[row_idx].append(matrix_a[row_idx][col_idx] * const)

    return final_matrix


def matrix_multiple(a_size, matrix_a, b_size, matrix_b):
    if a_size.split(' ')[1] == b_size.split(' ')[0]:
        final_matrix = []
        for row_a_idx in range(int(a_size.split(' ')[0])):
            final_matrix.append([])
            for col_b_idx in range(int(b_size.split(' ')[1])):
                multiplied_value = 0
                for col_a_idx in range(int(a_size.split(' ')[1])):  # 1
                    multiplied_value += matrix_a[row_a_idx][col_a_idx] * matrix_b[col_a_idx][col_b_idx]
                final_matrix[row_a_idx].append(multiplied_value)
        return final_matrix
    else:
        print("Error: count of cols in first matrix must be equal to count of rows in second matrix")


def matrix_transpose(a_size, matrix_a):
    print("Chose option: \n"
          "1. Main diagonal \n"
          "2. Side diagonal \n"
          "3. Vertical line \n"
          "4. Horizontal line\n")
    user_input = int(input())
    if user_input == 1:
        transposed_matrix = []
        for col_idx in range(int(a_size.split(' ')[1])):
            transposed_matrix.append([])
            for row_idx in range(int(a_size.split(' ')[0])):
                transposed_matrix[col_idx].append(matrix_a[row_idx][col_idx])
        return transposed_matrix
    elif user_input == 2:
        transposed_matrix = []
        for col_idx in range(int(a_size.split(' ')[1])):
            transposed_matrix.append([])
            for row_idx in range(int(a_size.split(' ')[0])):
                transposed_matrix[col_idx].append(
                    matrix_a
                    [abs(row_idx - (int(a_size.split(' ')[0]) - 1))]
                    [abs(col_idx - (int(a_size.split(' ')[1]) - 1))]
                )
        return transposed_matrix
    elif user_input == 3:
        transposed_matrix = []
        for row_idx in range(int(a_size.split(' ')[0])):
            transposed_matrix.append([])
            for col_idx in range(int(a_size.split(' ')[1])):
                transposed_matrix[row_idx].append(
                    matrix_a
                    [row_idx]
                    [abs(col_idx - (int(a_size.split(' ')[1]) - 1))]
                )
        return transposed_matrix
    elif user_input == 4:
        transposed_matrix = []
        for row_idx in range(int(a_size.split(' ')[0])):
            transposed_matrix.append([])
            for col_idx in range(int(a_size.split(' ')[1])):
                transposed_matrix[row_idx].append(
                    matrix_a
                    [abs(row_idx - (int(a_size.split(' ')[0]) - 1))]
                    [col_idx]
                )
        return transposed_matrix
    else:
        print("Incorrect input")


def main():
    try:
        size_a = input("Enter size of first matrix: ")  # 4 4
        matrix_a = fill_matrix(int(size_a.split(" ")[0]), int(size_a.split(" ")[1]))

        size_b = input("Enter size of second matrix: ")
        matrix_b = fill_matrix(int(size_b.split(" ")[0]), int(size_b.split(" ")[1]))

        while True:
            print(
                "Chose option \n"
                "1. Add matrices \n"
                "2. Multiply matrix by a constant \n"
                "3. Multiply matrices \n"
                "4. Transpose matrix  \n"
                "0. Exit"
            )
            user_input = int(input(""))

            if user_input == 1:
                summed_matrix = matrix_sum(size_a, matrix_a, size_b, matrix_b)
                print(summed_matrix)
            elif user_input == 2:
                multiplied_on_const_matrix = matrix_multiple_on_const(size_a, matrix_a)
                print(multiplied_on_const_matrix)
            elif user_input == 3:
                multiplied = matrix_multiple(size_a, matrix_a, size_b, matrix_b)
                print(multiplied)
            elif user_input == 4:
                transposed = matrix_transpose(size_a, matrix_a)
                print(transposed)
            elif user_input == 0:
                break
            else:
                print("Incorrect input try one's more")
    except:
        print("Ошибка: Неправельно введён размер матрицы")
