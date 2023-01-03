



# Oppg 3.7

def check(a, b, c):
    tekst = 'Norsk setning med Æ' 
    ny = 'English without the letters' 
    print("JA") if a in tekst or b in tekst or c in tekst else print("NEI")
    print("JA") if a in ny or b in ny or c in ny else print("NEI")
  
check("æ", "ø", "å")        



# Oppg 3.8

# Lag en funksjon som skriver ut en bokstav på en bestemt plass i en gitt streng. Posisjonen, eller indeksen, skal bli gitt som argument og stringen skal bli gitt som argument. 

def bokstav(b):
    strings = ["a", "b", "c", "d", "e", "f", "g"]
    print(strings[b])

xy = ["a", "b", "c", "d", "e", "f", "g"]
print(xy)
inserted = int(input("Hvilken bokstav vil du skrive ut: "))
bokstav(inserted)


# Oppg 3.9


def for_last(Fname, Lname):
    return Fname + " " + Lname

x = input("Første navn: ")
y = input("Last navn: ")
print("Du heter", for_last(x,y))
