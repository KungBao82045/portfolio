# Oppgave 3.3 
# Deklarer en global variabel. Lag en funksjon som skal endre på den globale variabelen. Lag også en lokal variabel inni funksjonen. 
# Kall på funksjonen, og prøv å printe de forskjellige variablene etterpå. Skriv en kommentar i koden for hva som skjer. 

globe_x = 5
print(globe_x) # Printer ut 5

def globe_var():
    global globe_x
    globe_x = 10 # Må være etter global globe_x ellers så printer konsolen ut error.
    print(globe_x)
globe_var() # For at globe_x skal endre verdi,skriv inn glove_var()

print(globe_x) # Printes 10 fordi globe_x inn i globe_var funksjon ble deklarert som global.


print("\n") # Ignorer den. Gjør det mer lesbart.


lokal_x = 7
print(lokal_x)
def lokal_var():
    lokal_x = 12
    print(lokal_x)
lokal_var()
print(lokal_x) # Uten global inn i funksjonen, kan ikke lokal_x printe ut 12, så det printes ut