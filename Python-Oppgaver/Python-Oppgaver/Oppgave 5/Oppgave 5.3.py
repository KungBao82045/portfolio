# Oppgave 5.3 
# Utvid forrige oppgave til å spørre brukeren om de ønsker å legge til en ny temperatur for en annen by. Skriv ut fornuftige ting til brukeren. 

dictionary = {
    "Oslo" : 13, 
    "Stavanger": 9, 
    "Tromsø" : 1
}

bruker1 = input("Skriv inn bydel: ")
bruker2 = int(input("Skriv inn temperatur (Celsius): "))

dictionary[bruker1] = bruker2


for key, value in dictionary.items():
    print(key, str(value) + "°C")

