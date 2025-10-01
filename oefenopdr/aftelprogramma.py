while True:
    try:
        oorspronkelijk_nummer = int(input("Geef een positief nummer"))
    except ValueError:
        print("Verkeerde input")
        continue
    if oorspronkelijk_nummer < 0:
        print("Geef een positief nummer")
        continue
    break
nummer = oorspronkelijk_nummer
while nummer > 0:
    print(nummer)
    nummer -= 1
print("Tijd om te starten!")
for i in range(1, oorspronkelijk_nummer):
    print(i)