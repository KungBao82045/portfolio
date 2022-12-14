# Oppgave 2.10 - UTFORDRING 
# Lag et program som skriver ut tallene fra 1 til og med 9 i et 'rutenett':  
# 1	2	3 
# 4	5	6 
# 7	8	9 

for i in range(1,10): # Printer ut tall fra 1 ikke 0, til 10

    print(i, end="\t") # end printer ut i samme linje.     end="" printer ut tall i samme linje. med \t, lager den ekstra mellomrom.
    if i % 3 == 0: # Lag ny linje hvis i % 3 == 0
        print("\n")







# EKSEMPEL PÅ % MODULO
# % skal printe ut som er igjen. Si at du skal regne ut 10 % 3. Du skal plusse 3 helt til du kommer nærme til 10 og fikk 9 som er 
# nærmeste tall. Du mangler 1 for å komme til 10, så svaret er 1
print(10%3)

# MER EKSEMPEL
# La oss regne 50 % 9. Du skal plusse 9+9+9 og gjenta helt til du er på den nærmeste tall. 9+9+9+9+9 = 45. Du kan ikke plusse 9 igjen fordi da er du over 50.
# Du mangler 5 for å få 50 tall, så svaret er 5.
print(50%9)

# SISTE EKSEMPEL
# 30 % 4281. Svaret er jo bare 30. 2 % 40 = 2. Svaret er alltid på venstre så lenge venstre tallet er mindre enn høyre. Med mindre venstre er større enn høyre.
# Bare tenk på venstre taller er riktig. For eksempel: 105 % 20498234092374985439 = 105
print(30 % 4281)
print(2 % 40)
print(105 % 20498234092374985439)