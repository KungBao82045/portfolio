import os
os.system("clear")
# Oppgave 4.4 

# Lag en liste som inneholder 10 elementer. Skriv ut listen. Endre på det femte elementet (hvilken indeks blir det?), og skriv ut listen på nytt. 
# Legg til ett tall på slutten av listen og skriv ut listen. Legg til ett tall med insert på indeks 4 i listen. Fjern ett tall fra listen med del. 
# Fjern det siste elementet fra listen med pop. Skriv ut resultatet.   

x = ["Black", "White", "Red", "Blue", "Green", "Yellow", "Pink", "Purple", "Brown", "Orange"]

print(x)

x[4] = "GREEN"
print(x)

x.append("1")
print(x)

x.insert(4, "22")
print(x)

del x[-1]
print(x)

x.pop()
print(x)