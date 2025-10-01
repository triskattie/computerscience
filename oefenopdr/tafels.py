while True:
    try:
        nummer = int(input("Kies een getal tot 50 en wij geven de tafel."))
    except ValueError:
        print("Verkeerde input")
        continue
    if nummer > 50:
        print("Te hoog")
        continue
    break
for i in range(1, 11):
    print(i * nummer)