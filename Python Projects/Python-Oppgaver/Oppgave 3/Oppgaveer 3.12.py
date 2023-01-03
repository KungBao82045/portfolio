#  Oppgave 3.12 

# Lag en funksjon som tar inn en streng. Iterer over stringen og returner den første vokalen du finner. 
# Dersom det ikke finnes noen vokal i strengen, returner en beskrivende tekst. 




def vocal_detector(strings):
    x = "aeiouy"
    for looper in strings:
        if looper in x:
            print(looper)
        else:
            print("Ingen vokaler fant!")


lol = input("Skriv inn en streng: ")

print(vocal_detector(lol))



