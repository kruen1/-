def calculate_sum_of_matrix_numbers(matrix):
    sum = 0
    for row in matrix:
        for nums in row:
            sum += nums
    return f"Сумма всех чисел в матрице равна {sum}"

m = [[1,1,1,],[1,1,1],[1,1,1]]
print(calculate_sum_of_matrix_numbers(m))