import random
doel = random.randint(1,20)
print("Welkom bij dit getal raad spelletje.")
while True:
    try:
        nummer = int(input("Raad een nummer"))
    except ValueError:
        print("Geef een nummer aub")
    if nummer == doel:
        break
    print(f"{'Te hoog' if nummer > doel else 'Te laag'}")
print("Correct!")
