k = int(input("Напишите число, что которого вывести таблицу умножения\n"))
default = 1
for i in range(10):
    print(f"{k} x {default} = {k * default}")
    default += 1