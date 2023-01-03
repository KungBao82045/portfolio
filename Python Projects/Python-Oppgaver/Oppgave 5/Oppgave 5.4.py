# Oppgave 5.4 

# Ta i bruk følgende dictionary: 
# person = {'name': 'Alex', 'age': 17, 'drivers license': False, 'height': 175, 'sex': 'non-binary'} 
# Skriv ut verdien som er tilknyttet nøkkelen “age”. Skriv ut verdien som er tilknyttet nøkkelen “height”.  
# Spør brukeren hva de ønsker å vite noe om, og skriv ut verdien tilknyttet den nøkkelen. 



person = {'name': 'Alex', 'age': 17, 'drivers license': False, 'height': 175, 'sex': 'non-binary'} 

# print("Age:", person["age"])
# print("Height:", person["height"])


for value, key in person.items():
    print(value + ": ?")


print("Hva vil du vite om personen? Slutt loop ved å skrive ut 'e'")
while True:
    information = input("Skriv inn nøkkel: ").lower()
    if information == "name":
        print("%s: %s" % (information, person["name"]))
    elif information == "age":
        print("%s: %s" % (information, person["age"]))
    elif information == "drivers license":
        print("%s: %s" % (information, person["drivers license"]))
    elif information == "height":
        print("%s: %s" % (information, person["height"]))
    elif information == "sex":
        print("%s: %s" % (information, person["sex"]))
    elif information == "e":
        break