userInput = input("Введите строку:\n").lower()
unique_symbols = set(userInput)
for symbol in unique_symbols:
    count_symbols = userInput.count(symbol)
    print(f"Буква {symbol} встречается {count_symbols} раз.")