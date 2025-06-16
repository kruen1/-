import random

last = int(input("Введите число, которое является концом диапазона чисел:\n"))

array = [random.randint(1, last) for _ in  range(10)]

array.sort()

propusk_number = []

for i in range(len(array) - 1):
    if array[i + 1] - array[i] > 1:
        for num in range(array[i] + 1, array[i + 1]):
            propusk_number.append(num)

print(f"Исходный массив: {array}\n")
print(f"Пропущенные числа: {propusk_number}")