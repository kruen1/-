userInput = input("Введите строку:\n")
listStr = list(userInput)

print(f"Вот исходный массив: {listStr}")

for i in range(len(listStr) // 2):
    listStr[i], listStr[len(listStr) - 1 - i] = listStr[len(listStr) - 1 - i], listStr[i]

print(f"А вот перевёрнутый массив: {''. join(listStr)}")