array = list(range(1, 101))

userInput = int(input("Введите число:\n"))

arr = []

for i in range(len(array) - 1):
    if userInput % array[i] == 0:
        arr.append(array[i])

arr.remove(userInput)

if sum(arr) == userInput:
    print(f"Число {userInput} совершенно.")
else:
    print(f"Число {userInput} не совершенно.")