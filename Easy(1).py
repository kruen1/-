user_choice = int(input("Сколько нужно чисел?\n"))
array = []
print(f"Введите {user_choice} чисел:")
for i in range(user_choice):
    user_number = int(input())
    array.append(user_number)
print(array)
print(f"Сумма элементов массива равна {sum(array)}")