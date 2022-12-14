# Lag en funksjon som tar inn to tall som parametre. 
# Ta inn input fra bruker i form av '/', '*', '//' eller '%'. 
# Funksjonen skal returnere resultatet av den typen matematisk operasjon gjort på de to tallene. Skriv ut resultatet. 

def twoNum(num, num1):
    x_x = input("Skriv inn operatør (+ - * / // ** %): ")
    if x_x == "*":
        return num * num1
    elif x_x == "-":
        return num - num1
    elif x_x == "+":
        return num + num1
    elif x_x == "/":
        return num / num1
    elif x_x == "//":
        return num // num1
    elif x_x == "**":
        return num ** num1
    elif x_x == "%":
        return num % num1
    
        

a = int(input("Skriv inn første num: "))
b = int(input("Skriv inn siste num: "))

print(twoNum(a, b))
