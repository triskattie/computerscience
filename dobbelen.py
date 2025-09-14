import random
from gedeelde_functies import verkrijg_nummer

def rol_dobbelsteen(hoeveelheid_stenen):
    uitslag = []
    for i in range(hoeveelheid_stenen):
        uitslag.append(random.randint(1, 6))
    return uitslag

def main():
    while True:
        print("""Welkom bij mijn dobbelspel!\nMet hoeveel mensen ben je? """)
        spelers = verkrijg_nummer(min_toegestaan=False)
        print("Hoeveel rondes wil je doen?")

        player1_score, player2_score = 0, 0
        for ronde in range(rondes):
            print( "-------SCORES-------")
            print( "Speler 1 -- Speler 2")
            print(f"   {player1_score}     --     {player2_score}")
            print("")

if __name__ == "__main__":
    main()