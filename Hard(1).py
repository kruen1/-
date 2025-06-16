import random

def bubble(array):
    print(f"Вот неотсортированный массив: {array}")
    count = 1
    while count < len(array):
        for i in range(len(array) - count):
            if array[i] > array[i+1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        count += 1
    return f"Вот отсортированный массив: {array}"

array_number = [random.randint(-10, 10) for _ in range(10)]
result = bubble(array_number)
print(result)
