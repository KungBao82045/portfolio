def Guide_v2():
    # PYTHON 2 del 1: For-løkker, while-løkker 
    # Oppgave 2.1 
    # Skriv en for-løkke som går fem ganger og printer ut stringen «Dette printes!». 

    for i in range(5):
        print("Dette printes!")

    # Oppgave 2.2 
    # Beskriv hva datatypene string, integer, float og boolean er. Prøv å komme med et eksempel på når det kan være lurt å bruke de forskjellige datatypene. 

    string, integer, floater, booler = "Hello!", 1, 5.1, True
    print(type(string)); print(type(integer)); print(type(floater)); print(type(booler)) 
    # str er tekst(bør inneholde "" eller '')
    # int er heltall
    # float er desimaltall
    # boolean er enten sant eller usant. hvis 5 > 4 (True) hvis 5 > 6 (False)

    # Oppgave 2.3 
    # Print ut tallene fra 0 til og med 7 med en while-løkke. Bruk en variabel for å holde styr på om løkken skal forsette å kjøre. 
    thall, thallEND = 0, 8
    while thall < thallEND:
        print(thall)
        thall += 1

    # Oppgave 2.4 
    # Print ut tallene fra 10 til og med 20 med en while-løkke. Bruk en boolsk variabel for å bestemme om løkken skal forsette å kjøre. 

    thall1, thallEND1 = 10, 21
    while thall1 < thallEND1:
        print(thall1)
        thall1 += 1
        

    # Oppgave 2.5 
    # Spør om input fra bruker frem til bruker skriver 'Exit'. Skriv ut det brukeren skrev hver gang. 
    while True:
        user = input("Si Noe: ")
        print(user)
        if user == "exit":
            break
    

    # Oppgave 2.6 
    # Lag en for-løkke som skriver ut tallene fra 0-5. Bruk en f-string til å formatere utskriften. 

    for i in range(6):
        print(f"For-Løkk printer ut: {i}")

# Oppgave 2.7 
# Lag en for-løkke som skriver ut tallene 5-9. 

    for i in range(5, 10):
        print(i)

# Oppgave 2.8 
# Lag en for-løkke som skriver ut partallene mellom 0 og 10. 

    for i in range(0, 11, 2):
        print(i)

# Oppgave 2.9 
# Lag en for-løkke som skriver ut tallene 1-5 i motsatt rekkefølge. 

    for i in range(5, 0, -1):
        print(i)

# Oppgave 2.10 - UTFORDRING 
# Lag et program som skriver ut tallene fra 1 til og med 9 i et 'rutenett':  
# 1	2	3 
# 4	5	6 
# 7	8	9 


# print(1, "\t", 2, "\t", 3)
# print(4, "\t", 5, "\t", 6)
# print(7, "\t", 8, "\t", 9)
    for i in range(1,10):
        print(i, end="\t") # end printer ut i samme linje.
        if i % 3 == 0:
            print("\n")



# PYTHON 2 del 2: in, continue, break  
# Oppgave 2.11 
# Lag en if-setning som sjekker om 'e' er i en string. 
    checkStr = "Hello, World!"
    if "e" in checkStr:
        print("True")
    else:
        print("False")

# Oppgave 2.12 - UTFORDRING 
# tekst = 'Uten mat og drikke, duger helten ikke' 
# vokaler = 'aeiouyæøå' 

tekst = 'Uten mat og drikke, duger helten ikke' 
vokaler = 'aeiouyæøå' 

for i in tekst:
    if i not in vokaler:
        print(i, end="")

print("\n")

for i in tekst:
    if i in vokaler:
        print(i, end="")

print("\n")


# Print ut alle vokaler i «tekst»-variabelen. 
# Print ut alle konsonanter i «tekst»-variablenen. 



# Hint: bruk «vokaler»-variabelen og sannhetsuttrykket «in», f.eks.: ‘h’ in vokaler gir False, ‘y’ in vokaler gir True. 

 

# Oppgave 2.13 - continue 
# Skriv en for-løkke som går over tallene 1 til 10, og printer ut alle tallene utenom 6. Bruk continue på dette tallet. Søk opp hvordan continue fungerer. Skriv til skjermen når det hoppes over. 

for i in range(1, 10):
    if i == 6:
        continue
    print(i)

# Oppgave 2.14 - break 
# Lag en for-løkke som går fra 10 til 20 som legger til ett  og ett av disse tallene frem til totalverdien er over 50. 
# Bryt ut av løkken med break og print ut verdien. 
total = 0
for i in range(10, 21, 1):
    total += i
    print(total)
    if total > 50:
        break





