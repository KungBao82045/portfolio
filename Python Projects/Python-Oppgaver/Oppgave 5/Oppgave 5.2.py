# Oppgave 5.2 
# Lag en dictionary temperaturer. Nøklene skal være bynavn med små bokstaver, og så skal du skriv inn forskjellige temperaturer som verdier. 
# Skriv nå ut hvert bynavn og temperatur sammen. Hint: bruk “for key in dictionary” og “dictionary[key]”. 

dictionary = {"Oslo" : 13, "Stavanger": 9, "Tromsø" : 1}

for key, value in dictionary.items():
    print(key, str(value) + "C")