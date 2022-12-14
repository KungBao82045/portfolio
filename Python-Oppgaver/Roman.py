# 1 = I, 5 = V, 10 = X, L = 50, C = 100, D = 500, M = 1000
# IV = 4, IX = 9, XC = 90, 


def write_a_number():
    num = int(input("Skriv inn num: "))
    return num

def num_to_roman(number):
    roman = " "
    while number > 0:
        if number >= 1000:
            roman += "M"
            number -= 1000
        elif number >= 900:
            roman += "CM"
            number -= 900
        elif number >= 500:
            roman += "D"
            number -= 500
        elif number >= 100:
            roman += "C"
            number -= 100
        elif number >= 50:
            roman += "L"
            number -= 50
        elif number >= 10:
            roman += "X"
            number -= 10
        elif number >= 9:
            roman += "IX"
            number -= 9
        elif number >= 5:
            roman += "V"
            number -= 5
        elif number >= 4:
            roman += "IV"
            number -= 4
        elif number >= 1:
            roman += "I"
            number -= 1
        
    print(roman)

# num_to_roman(write_a_number())
    
def write_roman():
    roman1 = input("Type inn roman: ").upper()
    roman = tuple(roman1)
    print(roman)
    return roman

def roman_to_num(roman):
    numCount = 0, 
    for x in roman:
        if roman[0] == "M":
            numCount += 1000
            roman = slice()
        elif roman[0] == "D":
            numCount += 500
        else:
            print("You typed non-roman character(s)")
            quit()

    print(roman)
    print(numCount)


roman_to_num(write_roman())
