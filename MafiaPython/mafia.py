# NOTE: This code is not finished. 

import random

health = 100
money = 0
strenght = 24

def actions():
    global health, money, strenght

    rob = random.randint(0, 20)
    risk_of_damage = random.randint(0, 50)
    rob_success = random.randint(0, 10)
    damage_taken = random.randint(1, 10)


    command = input("\n(R)ob - To rob someone\n(S)hop - Buy something goods\n(st)tat - Check your stats\n> ").upper()
    print("\n")

    if command == "ST":
        print("Here Is Your following Stats:\nMoney: %d\nhealth: %d\nstrenght: %d\n" % (money,health,strenght))




    if command == "R":

        if rob > 10 and risk_of_damage < strenght:
            print("You've managed to rob a person and gave you $%d! No damage taken from the person" % rob_success)
            money = money + rob_success

        

        elif rob > 10 and risk_of_damage > strenght:
            health = health - damage_taken
            print("You've managed to rob a person and gave you $%d! You are hurt and need some treatments." % rob_success)
            money = money + rob_success
            print("Damage Taken: %d" % damage_taken)


        elif rob < 10 and risk_of_damage > strenght:
            health = health - damage_taken
            print("You've failed to rob the person. You are hurt, but managed to escape")
            print("Damage Taken: %d" % damage_taken)


        else:
            print("The person got no money, so you left the area before the police came")
    
    if command == "S":
        pass
    
    
    # END CODE
    
    if health <= 0:
        print("You Are Dead. Gave Over")
        quit(0)
    


while True:
    action_return = actions()
    print(action_return)
