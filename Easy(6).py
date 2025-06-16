numbers = []
print("Введите 10 чисел:")
for i in range(10):
    user_number = int(input("-> "))
    numbers.append(user_number)
print(f"Среднее значение {(sum(numbers)) / len(numbers)}")