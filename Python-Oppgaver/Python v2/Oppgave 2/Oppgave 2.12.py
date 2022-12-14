# Oppgave 2.12 - UTFORDRING 
# tekst = 'Uten mat og drikke, duger helten ikke' 
# vokaler = 'aeiouyæøå' 

tekst = 'Uten mat og drikke, duger helten ikke' 
vokaler = 'aeiouyæøå' 

print("\n") # Lager ny linje som at teksten skal bli mer leselig.

for i in tekst: # Printer ut hver bokstaver som er konsonanter
    if i not in vokaler:
        print(i, end="") # end="" gjør at hver bokstaver skal printes ut i samme linje

print("\n") 

for i in tekst: # Printer ut hver bokstaver som er vokaler
    if i in vokaler:
        print(i, end="") # end="" gjør at hver bokstaver skal printes ut i samme linje


print("\n")

# Print ut alle vokaler i «tekst»-variabelen. 
# Print ut alle konsonanter i «tekst»-variablenen. 



# Hint: bruk «vokaler»-variabelen og sannhetsuttrykket «in», f.eks.: ‘h’ in vokaler gir False, ‘y’ in vokaler gir True. 