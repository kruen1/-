numbers = []
print("Напишите 10 чисел:")
for i in range(10):
    k = int(input("-> "))
    numbers.append(k)
print(f"Максимальное число {min(numbers)}. Максимальное число {max(numbers)}")