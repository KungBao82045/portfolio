# Lag en funksjon som tar inn navn som parameter. Spør brukeren (med navn) om alder og bosted. 
# Returner alder og bosted. Kall på funksjonen og lagre returverdiene i variabler. 

def navn_alder(navn, alder):
    return navn + " " + alder

x = input("Hva heter du:")
y = input("Hvor gammel er du: ")

a = navn_alder(x, y)
print(a)