wachtwoord = input("Geef een wachtwoord")
if len(wachtwoord) > 8 and " " not in wachtwoord:
    print("Wachtwoord goedgekeurd")
else:
    print("Wachtwoord niet goedgekeurd")