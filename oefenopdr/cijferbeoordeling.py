while True:
    cijfer = input("Geef je cijfer of voer klaar in om te stoppen")
    if cijfer == "klaar":
        break
    try:
        cijfer = float(cijfer)
    except ValueError:
        print("Geef een nummer")
        continue
    if cijfer < 1 or cijfer > 10:
        print("Onjuist cijfer")
        continue
    print(f"Je hebt een {'goed' if cijfer >= 8 else 'voldoende' if cijfer >= 6 else 'onvoldoende'}")
print("Tot later")