# Oppgave 4.8 

# Finn det største tallet, men du skal nå gjøre det manuelt (ikke bruke maks/min). Du skal iterere over listen, og lagre den største verdi i en variabel. 
# Du skal sammen ligne to og to elementer fra listen, som du så skal finne den største av før den da lagres og du itererer videre. Skriv ut for hver 
# iterasjon hvilke to tall som blir sammenlignet og hva som er lagret i variabelen. 


x = [2345, 93249, 39024, 578329, 293045, 459234, 938452, 2389520, 23940, 432903]
maks = x[0]
print(maks)

for element in x:
    empty = []
    if maks < element:
        maks = element
    else:
        
        print(maks)
