class games:
    STOOPID = True

    def People_Who_Loves_To_Simp(count):

        while True:
            x = int(input("\nEnter Seconds: "))

            while count < x:
                for day in range(60):
                    for hour in range(24):
                        for min in range(60):
                            for sec in range(60):
                                if count == x:
                                    return f"{day} day, {hour} hour, {min} minute, {sec} second." # Fatso
                                    
                                count += 1

    while STOOPID:
        x = People_Who_Loves_To_Simp(count=0)
        print(x)



    def guessTheNumberGame():
        import random

        count = 0
        limit = 5

        secret = random.randint(0,10)

        while count < limit:
            guess = int(input("Guess The Number: "))
            count += 1
            if guess == secret: print("CORRECT!"); break
            print("Must Be Higher") if guess < secret else print("must be lower")

        else:
            print("You loser")

    def math_game():
        pass

gamemodes = games.People_Who_Loves_To_Simp()
gamemodes1 = games.guessTheNumberGame()

print(gamemodes1)