

# Oppgave 3.2 
# Beskriv begrepene mtp. funksjoner i Python (gjerne kopier fra et internettsøk, så lenge du er enig i det som står der og forstår det): 

# 1.Deklarere en funksjon 
# 2.Funksjonskall 
# 3.Parametre 
# 4.Argumenter 
# 5.Returverdi 
# 6.Global variabel 
# 7.Lokal variabel 


# mtp er en forkortelse (med tanke på)



# 1. Deklarere en funksjon
def deklarere_func(fname): # 3. parameter er variabel inn i def
    print("Jeg heter:", fname)

deklarere_func("Jacky") # 2,4. Funksjonskall med argunemt "Jacky". Argument er verdi som ble sent til funksjon når den ble kalt.


def return_funk(x):
    return x * 52

print(return_funk(2)) # 5. For at returnverdi skal skrive ut, bruk funksjonen inn i print.



globe_x = 5
print("printer før func:", globe_x)

def global_vs_lokal():
    global globe_x
    globe_x = 10
    print("Inn i func:", globe_x)
global_vs_lokal()

print("Etter func,", globe_x) # Printes 10 fordi globe_x inn i global_vs_lokal funk ble deklarert som global. Ellers print 5



def lokal_vs_global():
    globe_x = 20
    print("Inn i func", globe_x)

lokal_vs_global()
print(globe_x) # Fortsatt 10 fordi globe_x inn i lokal_vS_global funk er ikke globalt variabel.