# Oppgave 5.5 
# Bruk samme dictionary som forrige oppgave. Fjern nøkkelen “sex” med metoden pop(). 
# Sjekk om nøkkelen “height” finnes i dictionaryen. Skriv ut alle nøklene til dictionaryen med metoden keys(). Skriv ut alle verdiene med metoden values(). 

person = {'name': 'Alex', 'age': 17, 'drivers license': False, 'height': 175, 'sex': 'non-binary'} 

person.pop("sex")

if person["height"]:
    print("Height Exist!")

print(person.keys())
print(person.values())




