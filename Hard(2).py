inputStr = input("Введите сроку:\n")
listStr = list(inputStr)
length = len(listStr)

for i in range(length // 2):
    listStr[i], listStr[length - 1 - i] = listStr[length - 1 - i], listStr[i]

print(''. join(listStr))