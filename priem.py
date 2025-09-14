"""

"""
import math
from gedeelde_functies import verkrijg_nummer

def main():
  while True:
    priem = True
    print("Welk nummer wil je testen?")
    n = verkrijg_nummer(min_toegestaan=True)
    if n <= 1:
      print("Geen priem")
      continue 
    max_deelbaar = math.floor(math.sqrt(n)) + 1 # Omdat een van de twee nummers die gebruikt worden wel kleiner dan de wortel moet zijn is dit efficienter
    for i in range(2, max_deelbaar):
      if n % i == 0:
        priem = False
    print(f"{'Priem' if priem else 'Niet priem'}")
    continue

if __name__ == "__main__":
  main()