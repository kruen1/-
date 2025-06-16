number = int(input("Введите число:\n-> "))
result = sum(map(int, str(number)))
print(f"Сумма цифр числа {number} равна {result}")