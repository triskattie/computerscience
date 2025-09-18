"""
Naam: PRIVACY
Programma: gedeelde_functies.py
Werking: In dit bestand staan alle functies die meerdere keren worden gebruikt in de verschillende opdrachten.
"""


# Functie voor het verkrijgen van een nummer van een gebruiker met typfout detectie
def verkrijg_nummer(min_toegestaan: bool = True,
                    decimalen_toegestaan: bool = True):  # Min-getallen en komma-getallen zijn standaard toegestaan, behalve als ze expliciet worden verboden
    while True:
        n = input("")  # Ontvangt een combinatie van tekens van de gebruiker
        n = n.replace(",", ".")  # Verander een komma in een punt
        if not n:  # Als er niks wordt ingevuld
            print("Vul iets in")
            continue

        if decimalen_toegestaan == False and "." in n:
            print("Komma-getallen zijn niet toegestaan")
            continue

        # Gaat elk apart teken door en haalt de nummers eruit
        punt = False
        finished_letters = ""
        for letter in n:
            if letter.isdigit():
                finished_letters += letter
            elif letter == "." and not punt:
                finished_letters += letter
                punt = True
            elif letter == "-" and finished_letters == "":  # Alleen een min-teken toestaan aan het begin
                finished_letters += "-"

        if finished_letters in ["", "-", ".", "-."]:
            print("Geen nummers gedetecteerd, probeer opnieuw")
            continue

        try:
            getal = int(finished_letters)
        except ValueError:
            try:
                getal = float(finished_letters)
            except ValueError:
                print("Geen geldig nummer, probeer opnieuw.")
                continue

        if not min_toegestaan and getal < 0:
            print("Het kan helaas geen negatief getal zijn.")
            continue

        if getal == 0:
            print("Haha leuk geprobeerd")
            continue

        return getal
