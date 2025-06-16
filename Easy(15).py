def year(y):
    if y % 400 == 0:
        return  True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

user_year = int(input("Введите год -> "))

if year(user_year):
    print(f"Год {user_year} - високосный.")
else:
    print(f"Год {user_year} - не високосный.")