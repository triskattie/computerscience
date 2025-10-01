cijfer_rekenen = float(input("Je cijfer voor rekenen"))
cijfer_taal = float(input("Je cijfer voor taal"))
cijfer_gym = float(input("Je cijfer voor gym"))
if cijfer_rekenen >= 6 and cijfer_taal >= 6:
    print("Geslaagd")
elif cijfer_rekenen == 10 and cijfer_taal >= 5 and cijfer_gym >= 5:
    print("Geslaagd")
elif cijfer_taal == 10 and cijfer_gym >= 5 and cijfer_rekenen >= 5:
    print("Geslaagd")
elif cijfer_gym == 10 and cijfer_rekenen >= 5 and cijfer_taal >= 5:
    print("Geslaagd")
else:
    print("Niet geslaagd")