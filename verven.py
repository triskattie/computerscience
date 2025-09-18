"""
Naam: PRIVACY
Programma: verven.py
Werking: Dit stuk code helpt de gebruiker met het beslissen van hoeveel emmers verf ze moeten kopen.
"""

import math
from gedeelde_functies import verkrijg_nummer


def main():
    # Basis variabelen
    oppervlakte_per_liter = 8
    totale_opp = 0

    print("Hoeveel muren wil je schilderen? ")
    hoeveelheid_muren = verkrijg_nummer(min_toegestaan=False, decimalen_toegestaan=False)

    print("Hoe groot is de inhoud van een emmer verf (liters)?")
    inhoud = verkrijg_nummer(min_toegestaan=False)

    # Elke muur langs gaan om de oppervlakte te verkrijgen
    for muur in range(hoeveelheid_muren):
        print(f"Wat is de breedte van muur {muur + 1}? ")
        b = verkrijg_nummer(min_toegestaan=False)
        print(f"Wat is de hoogte van muur {muur + 1}? ")
        h = verkrijg_nummer(min_toegestaan=False)
        opp = b * h
        totale_opp += opp

    # Berekenen van benodigdheden
    benodigde_l = round(totale_opp / oppervlakte_per_liter, 1)
    hoeveelheid_potten = math.ceil(benodigde_l / inhoud)
    # Resultaat
    print(f"Het totale oppervlak van jouw muren is {round(totale_opp, 2)} m2")
    print(f"Met 1 liter kun je {oppervlakte_per_liter} m2 verven")
    print(f"Voor jouw kamer hebt je {benodigde_l} liter verf nodig")
    print(f"Je moet dus {hoeveelheid_potten} pot{'' if hoeveelheid_potten == 1 else 'ten'} verf kopen")


if __name__ == "__main__":
    main()
