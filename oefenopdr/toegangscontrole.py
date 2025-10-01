while True:
    try:
        leeftijd = int(input("Geef je leeftijd"))
    except ValueError:
        print("Onjuiste leeftijd")
        continue
    break
vip_kaart = input("Heb je een VIP-kaart? y/n")
if vip_kaart.lower() == "y" or leeftijd >= 18:
    print("Toegang toegestaan")
else:
    print("Toegang geweigerd")