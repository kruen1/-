import random

arr = list(set([random.randint(1, 20) for _ in range(20)]))

print(f"Массив: {arr}")
target = int(input("Введите target:\n"))
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if target == arr[i] + arr[j]:
            print(f"{arr[i]} + {arr[j]} = {target}")