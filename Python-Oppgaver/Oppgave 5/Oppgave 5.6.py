# Oppgave 5.6 
# Ta i bruk følgende dictionary: 
# aksjekurs = {'EQNR': 233.90, 'DNB': 210.50, 'NHY': 71.04, 'PMG': 18.52} 
# Hver nøkkel er her en “ticker” og hver verdi er markedsverdi. Iterer over aksjekurs og skriv ut hver ticker. 

# key : value
# Nøkkel : verdi

aksjekurs = {'EQNR': 233.90, 'DNB': 210.50, 'NHY': 71.04, 'PMG': 18.52} 

for x, y in aksjekurs.items():
    print(x, y)

    
