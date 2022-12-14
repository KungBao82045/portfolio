# PYTHON X: UTFORDRINGSHJØRNET  
# Oppgave X.1 
# Lag et rutenett av størrelse 5x5. Bruk lister og for-løkker for å gjøre dette. Tallene skal være tilfeldige. 

import random
print("\n" * 10)

for x in range(1, 26):
    # tilfeldig = random.randint(0,100)
    tilfeldig1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,8,19,20,21,22,23,24,25]
    print(random.choice(tilfeldig1), end="\t")
    if x % 5 == 0:
        print("\n")
