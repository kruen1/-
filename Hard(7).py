def calculate_max_number_in_matrix(matrix):
    max_number = float('-inf')
    for rows in matrix:
        for nums in rows:
            if nums > max_number:
                max_number = nums
    return f"Максимальное число в массиве это {max_number}"

m = [[1,2,3],[4,5,6],[7,8,9]]
print(calculate_max_number_in_matrix(m))