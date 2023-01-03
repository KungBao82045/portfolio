# Lag en funksjon som tar inn to parametre, timelønn og antall_timer. Funksjonen skal returnere lønn gitt antall timer. 
# Lag så en funksjon som tar inn timelønn og antall timer fra brukeren og returnerer det. 
# Gjør et nøstet funksjonskall (funksjonskall INNI funksjonskall) der den første funksjonen blir kalt først, og den andre etterpå. 
# Print ut resultatet. 

def func(timelonn, antall_timer):
    
    def func1():
        return timelonn * antall_timer

    return func1()

x = func(150, 7)
print(x)