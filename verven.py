"""
Naam: PRIVACY
Programma: verven.py
Werking: Dit stuk code helpt de gebruiker met het beslissen van hoeveel emmers verf ze moeten kopen.
"""

import math
from gedeelde_functies import verkrijg_nummer


def main():
  # Basis variabelen
  OPPERVLAKTE_PER_LITER = 8
  totaleOpp = 0

  print("Hoeveel muren wil je schilderen? ")
  hoeveelheidMuren = verkrijg_nummer(min_toegestaan=False, decimalen_toegestaan=False)

  print("Hoe groot is de inhoud van een emmer verf (liters)?")
  inhoud = verkrijg_nummer(min_toegestaan=False)

  # Elke muur langs gaan om de oppervlakte te verkrijgen
  for muur in range(hoeveelheidMuren):
    print(f"Wat is de breedte van muur {muur + 1}? ")
    b = verkrijg_nummer(min_toegestaan=False)
    print(f"Wat is de hoogte van muur {muur + 1}? ")
    h = verkrijg_nummer(min_toegestaan=False)
    opp = b * h
    totaleOpp += opp

  # Berekenen van benodigdheden
  benodigdeL = round(totaleOpp / OPPERVLAKTE_PER_LITER, 1)
  hoeveelheidPotten = math.ceil(benodigdeL / inhoud)
  # Resultaat
  print(f"Het totale oppervlak van jouw muren is {round(totaleOpp, 2)} m2")
  print(f"Met 1 liter kun je {OPPERVLAKTE_PER_LITER} m2 verven")
  print(f"Voor jouw kamer hebt je {benodigdeL} liter verf nodig")
  print(f"Je moet dus {hoeveelheidPotten} pot{'' if hoeveelheidPotten == 1 else 'ten'} verf kopen")

if __name__ == "__main__":
  main()