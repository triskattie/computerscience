"""
Naam: PRIVACY
Programma: sps.py
Werking: Steen papier schaar tegen de computer in 3 rondes
"""

import random

# Beslist wie heeft gewonnen
def winnaar_script(speler_keuze, computer_keuze):
    if speler_keuze == computer_keuze:
        return "gelijk"
    elif (speler_keuze == "steen" and computer_keuze == "schaar") or \
            (speler_keuze == "papier" and computer_keuze == "steen") or \
            (speler_keuze == "schaar" and computer_keuze == "papier"):
        return "gewonnen"
    else:
        return "verloren"

def main():
    keuzes = ['steen', 'papier', 'schaar']
    print("Welkom bij steen papier schaar!")
    print("In dit spel doe je steen papier schaar tegen een computer in 3 rondes")
    speler_score = 0
    computer_score = 0
    for i in range(3): # 3 rondes
        print(f"Computer - Speler")
        print(f"{computer_score} - {speler_score}")
        computer_keuze = random.choice(keuzes)

        # while True loop om ervoor te zorgen dat de gebruiker een correcte input geeft
        while True:
            speler_keuze = input("steen, papier, schaar? ").lower()
            if speler_keuze not in keuzes:
                print("Kies steen, papier, of schaar ajb")
                continue
            break
        resultaat = winnaar_script(speler_keuze, computer_keuze)
        print(f"De computer koos {computer_keuze}")
        print(f"Je hebt {resultaat}")

        # Punten toekennen
        if resultaat == "gewonnen":
            speler_score += 1
        elif resultaat == "verloren":
            computer_score += 1
        else:
            pass

    # Uiteindelijke resultaat
    print(f"Computer - Speler")
    print(f"{computer_score} - {speler_score}")
    if speler_score > computer_score:
        print("Je hebt gewonnen!")
    elif speler_score < computer_score:
        print("Je hebt verloren...")
    else:
        print("Het is gelijkspel")




if __name__ == '__main__':
    main()