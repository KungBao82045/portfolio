#Oppgave 1.1 – HELLO WORLD 
#Lag en variabel som inneholder strengen «Hello World!» og skriv den ut til konsollen. 

from ast import operator
from calendar import c
from functools import total_ordering
from turtle import pen


def test():  # Som at jeg hopper over koder som at jeg slipper å


    oppg1 = "Hellow World!"
    print(oppg1)

    #Oppgave 1.2 
    #Lag to variabler og legg sammen to verdier. Skriv passende tekst sammen med utskriften av svaret. 

    a = 55
    b = 10


    #Oppgave 1.3 
    #Gang sammen to tall. Bruk så mange variabler som du tenker kan være lurt, og skriv i kommentarer i koden hvorfor du har gjort det. 

    print(a*b)

    #Oppgave 1.4 
    #Hent inn en streng fra brukeren som du skriver ut tre ganger. 

    print_ut1 = input("Navn: ")
    print_ut2 = int(input("Alder: "))
    print_ut3 = input("Favoritt Farge: ")
    print("Du sier at du heter,", print_ut1 + ".\nDu sier at du er", print_ut2, "år gammel.\nOg til slutt, du sier at favoritt fargen din er", print_ut3)

    #Oppgave 1.5 
    #Hent inn tre temperaturer fra brukeren og finn gjennomsnittet av de. Skriv ut passende tekst og resultat i konsollen. Bruk escape-tegn. 

    temp1 = input("Skriv inn temperatur(Celsius): ")
    print((temp1 * 9/5) + 32, "Fahrenheit") # Formula fra nett
    print(temp1 + 273.15, "Kelvin") # Formula fra nett

    
    #Oppgave 1.6 
    # Hent inn hvor mye brukeren har i timelønn, og hvor mange timer brukeren har jobbet. Lag begge disse variablene på samme linje. 
    # Finn bruttolønnen (lønn før skatt). Hent etterpå inn hvor mye brukeren skatter i prosent. Skriv ut passende informasjon til brukeren, 
    # med forklarende tekst. 

    print("\n")
    timelønn1 = int(input("Hello! Hvor mye har du jobba i timer? \n> "))
    timelønn2 = int(input("Hvor mye tjener du per time? \n> "))
    skatteProsent = 35/100 #prosent
    brutto = timelønn1 * timelønn2 * 30
    skatt = brutto * skatteProsent
    print("Du tjener", brutto, "kr i en måned. Du betaler", skatt, "skatt.")
    netto = brutto - skatt
    print("Nettlønnen din er:", netto)

#Oppgave 1.7 
#Lag en enkel kalkulator som tar inn tall fra brukeren og som legger de sammen. Skriv kommentarer i koden din. La så brukeren bestemme selv 
# om de vil legge til enda et tall, eller ikke. Skriv ut fornuftige ting i konsollen, og bruk den korteste skrivemåten du får til. 

    calc1 = input("Skriv inn ditt første nummer: ")
    calc2 = input("Skriv inn ditt andre nummer: ")
    print(calc1, "+", calc2, "=", int(calc1)+int(calc2))


#Oppgave 1.8 
#Lag et program som spør brukeren om forskjellige datatyper, og som gjør om til den datatypen som blir spurt om. Skriv ut hva brukeren skrev. 

    print("Hei! Si hva som helst og jeg skal konvertere den til en datatype")
    dataInp = input()
    print(type(dataInp))


#Oppgave 1.9 – UTFORDRING 
# Lag en fleksibel kalkulator som kan regne mange forskjellige regnearter, og kan skrive tall ut på vitenskapelig notasjon dersom 
# brukeren ønsker det. Bruk funksjoner dersom du kan det fra før av (funksjoner er et tema som kommer senere, dersom du ikke kan det). 
# Brukeren skal i starten av programmet kunne angi hvor mange siffer de ønsker etter komma, og kalkulatoren skal tilpasse seg. 
# Bruk escape-tegn i utskriftene til brukeren. 

def simpleCal():
    print("\nLitt advansert kalkulator. Nå kan du velge hvilken operatør du ønsker å kalkulere!")
    a = int(input("Skriv in ditt første nummer: ")) # int gjør at brukeren skal bare skrive inn tall. Ellers, så kræsjer koden.
    print("1 = +\n2 = -\n3 = *\n4 = /\n5 = //\n6 = %\n7 = **")
    operator = int(input("Hvilken operatør(Skriv inn nummer øverst): "))
    b = int(input("Skriv inn ditt andre nummer: "))
    print(a*b) if operator == 3 else print(a+b) if operator == 1 else print(a-b) if operator == 2 else print(a/b) if operator == 4 \
    else print(a//b) if operator == 5 else print(a%b) if operator == 6 else print(a**b) if operator == 7 else print("Har du skrevet riktig operatør?")
        





# PYTHON 1.2: Sannhetsuttrykk, if/else, standardfunksjoner 
# Oppgave 2.1 
# Ta inn to tall der du sjekker om det andre er større enn det første i en variabel. Skriv ut resultatet av sjekken. 
def test2():
    oppg21 = 5
    oppg211 = 10

    if oppg21 < oppg211:
        print("Den første variabel er større enn den andre variabel")
    else:
        print("Den første variabel er mindre enn den andre variabel")

# Oppgave 2.2 
# Lag seks variabler med positive og negative verdier. Finn maks med en standardfunksjon. Finn minimum med en standardfunksjon. Finn absoluttverdien av ett av tallene. 
# Avrund ett av tallene. Skriv alt dette ut på et fint og oversiktlig format i konsoll. 

    var1 = -5
    var2 = 24
    var3 = 1
    var4 = -4
    var5 = -10
    var6 = 12

    total_var = var1, var2, var3, var4, var5, var6

    print(max(total_var))
    print(min(total_var))

# Oppgave 2.3 
# Ta inn navnet til brukeren og skriv ut hvor langt det er. 

    lengdeNavn = input("Hva heter du:")
    print("Hei,", lengdeNavn + ". Lengden på navnet ditt er:", len(lengdeNavn))

# Oppgave 2.4 
# Sjekk om 50/3 er større enn 20, og print ut fornuftige resultater. 

    if 50/3 > 20:
        print("50/3 =", int(50/3), "er større enn 20")
    else:
        print("50/3 =", int(50/3), "er mindre enn 20")

# Oppgave 2.5 
# Prøv deg frem med %-operatoren (modulo). 10%3, 17%2, 17%3, 17%6. Skriv i koden din hvordan modulo fungerer. 

    prosento1 = 10%3 # Plusse 3+3 helt til du er nærmest på 10. 3+3+3=9 er nærmest og mangler 1 for å få 10. Så denne variabel printer 1 på konsollen.
    prosento2 = 17%2 
    prosento3 = 17%3
    prosento4 =  17%6 # Plusse 6+6=12 og du kan ikke plusse mer fordi da får du 18 som er mer enn 17. Du mangler 5 for å komme til 17. Så denne variabel printer 5 på konsollen.


    print(prosento1, prosento2, prosento3, prosento4)

    # Oppgave 2.6 
    # Lag en if-setning der du sjekker om en variabel er større enn en annen. 

    if var2 > var5:
        print(var2, "er større enn", var5)
    else:
        print(var2, "er mindre enn", var5)

    # Oppgave 2.7 
    # Ta inn hvor mange biler brukeren har solgt, og gi en bonus på 5000kr dersom det er solgt flere enn 70 biler. Regn så ut hvor mye brukeren 
    # får i lønn, hver bil gir 500kr i lønn. Skriv til konsoll. 

    bilerPrKr = 500
    bilerBonus = 5000 # Hvis solgt flere enn 70 biler
    bilerSolgt = int(input("Hvor mange biler har du solgt: "))
    lønnBiler = bilerSolgt * bilerPrKr
    if bilerSolgt > 70:
        print("Du solgte flere enn 70 biler og fikk 5000kr bonus. Ditt lønn er: " + str(lønnBiler) + "kr +", str(bilerBonus), "=", lønnBiler+bilerBonus, "kr")
    else:
        print("Ditt lønn er:", str(lønnBiler) + "kr")

    # Oppgave 2.8 
    # Test ut de forskjellige betingelsene <, >, <=, >=, == og != på noen variabler.  

    oppg_28_1 = 4
    oppg_28_2 = 5

    print(oppg_28_1 > oppg_28_2) # Større enn
    print(oppg_28_1 < oppg_28_2) # Mindre enn
    print(oppg_28_1 <= oppg_28_2) # Mindre eller like enn
    print(oppg_28_1 >= oppg_28_2) # Større eller like enn
    print(oppg_28_1 == oppg_28_2) # Like enn
    print(oppg_28_1 != oppg_28_2) # Ikke like enn

# Oppgave 2.9 
# Godteri koster 30, og brus koster 20. Ta inn fra brukeren hvor mye penger de har. Skriv ut hva en brukeren kan kjøpe. 

    godteri = 30
    brus = 20

    print("Godteri koster:" + str(godteri) + "kr\nBrus koster:" + str(brus) + "kr")
    oppg_29 = int(input("Hvor mye penger har du: "))

    totalButikk = godteri + brus

    if oppg_29 >= totalButikk:
        print("Du har råd til godteri og brus")
    elif oppg_29 >= godteri and oppg_29 < totalButikk:
        print("Du har råd til godteri, men ikke råd til brus etter du kjøpte godteri")
    elif oppg_29 >= brus and oppg_29 < totalButikk:
        print("Du har råd til brus, men ikke råd til godteri etter du kjøpte brus")
    else:
        print("Du har ikke råd til noe av de")


# Oppgave 2.10 
# Lag en enkel nøstet if-setning. Altså en if-setning inni en if-setning. Den skal først sjekke og en variabel er større enn et tall, 
# og så sjekke om variabelen modulo 1 (%) blir akkurat 1. Dersom det er sant skal det printes «Oddetall!» 
# Dersom det ikke er sant skal det printes «Partall!» 

pengerR = 2 % 11
print(pengerR)
if pengerR > 1:
    print("Større enn 1")
    if pengerR == 1:
        print("Oddetall!")
    else:
        print("Partall!")
else:
    print("Mindre enn 1 eller like")