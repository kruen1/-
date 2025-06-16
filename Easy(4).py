user_word = list(input("Введите слово:\n"))
while len((user_word)) > 0 and user_word[0] == user_word[-1]:
    user_word.pop(0)
    user_word.pop(-1)
if len(user_word) == 0:
    print("Слово является палиндромом.")
else:
    print("Слово не является палиндромом.")
