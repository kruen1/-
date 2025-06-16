def calculate_factorial(n):
    if n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)
number = int(input("Введите число, факториал которого хотите найти:\n-> "))
result = calculate_factorial(number)
print(result)