# Oppgave 5.7 
# Bruk samme dictionary som forrige oppgave. Skriv ut en oversikt over hvilken nøkkel som peker på hvilken verdi, bruk for-løkke. 

aksjekurs = {'EQNR': 233.90, 'DNB': 210.50, 'NHY': 71.04, 'PMG': 18.52} 


for verdi, nokkel in aksjekurs.items():
    print("%s: %s" % (verdi, nokkel))