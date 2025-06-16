import random

numbers_array = [random.randint(-100, 100) for _ in range(50)]
user_number = int(input("Введите число:\n-> "))

if user_number in numbers_array:
    print(f"Число {user_number} есть в массиве.")
else:
    print(f"Числа {user_number} нет в массиве.")