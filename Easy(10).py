numbers = []
print("Введите 3 числа:")
for i in range (3):
    n = int(input("->"))
    numbers.append(n)
print(f"Максимальное из 3 чисел -> {max(numbers)}")