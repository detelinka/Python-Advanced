text = input()
symbols = set(input())

for symbol in sorted(symbols):
    print(f"{symbol}: {text.count(symbol)} time/s")