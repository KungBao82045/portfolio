# Du skal nå lage et terningspill som kombinerer alt du har lært hittil. Husk: Google er din venn! 

# Importer random-modulen (du trenger kun randint). 
# Lag en info()-funksjon som skriver ut info om spillet, samt hvordan man avslutter. 
# Ta inn navnet til en bruker i en funksjon. Returner navnet. Bruk funksjonen til å lage to spilleret.

# Lag en funksjon som heter trill_terninger. De to brukerne skal trille terninger om og om igjen så lenge brukeren vil. 
# Hold styr på hvor mange poeng de har. Gi ett poeng til den som får høyest terningkast, ingen poeng dersom de får samme terningkast. 
# Returner hvor mange poeng spillerene har etter funksjonen er ferdig. 

# Lag en funksjon som heter start_spill() og som er ansvarlig for å kalle på alle de andre funksjonene. 
# Lag en funksjon som tar inn to parametre, score_en og score_to. Funksjonen skal skrive ut poengscore og hvem som vinner. 





from random import randint

def info(user1, user2): # skriver ut info om spillet, samt hvordan man avslutter. 
    return user1, user2

def trill_terninger(): # to brukerne skal trille terninger om og om igjen så lenge brukeren vil. 
    pass

def start_spill(): # ansvarlig for å kalle på alle de andre funksjonene. 
    pass





# print("Velkommen til terningspill! Opp")
bruker1 = input("Skriv inn første bruker: ")
bruker2 = input("Skrivv inn andre bruker: ")

