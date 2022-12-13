

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