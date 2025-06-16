n = int(input("Сколько нужно чисел?\n"))
number = []
for i in range(n):
    if i % 2 == 0:
        number.append(i)
print(f"Вот все чётные числа в заданном диапазоне: {number},\nИх количество -> {len(number)}")