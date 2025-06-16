import  random

numbers_array = [random.randint(-100, 100) for _ in range (50)]

counter_for_even_numbers = 0
counter_for_not_even_numbers = 0

for i in numbers_array:
    if i % 2 == 0:
        counter_for_even_numbers += 1
    else:
        counter_for_not_even_numbers += 1

print(f"Количество чётных чисел равно {counter_for_even_numbers},"
      f"Количество нечётных чисел равно {counter_for_not_even_numbers}")