print("Welkom bij deze even of oneven checker, voer een nummer in of voer stop in om te stoppen.")
while True:
    nummer = input("Welk nummer wil je checken?")
    if nummer.lower() == "stop":
        break
    try:
       nummer = int(nummer)
    except ValueError:
        print("Voer een getal in aub")
        continue
    print(f'{"Even" if nummer % 2 == 0 else "Oneven"}')
print("Tot later!")