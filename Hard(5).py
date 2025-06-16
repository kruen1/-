import random

array_numbers = [random.randint(1, 100) for _ in range(15)]
array_numbers.sort()

print(array_numbers)
print(f"Второе наибольшее число в массиве - это число {array_numbers[-2]}")