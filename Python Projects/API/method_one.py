import openai # Bibliotek
import pyttsx3
import traceback

with open("keys.txt", "r", encoding="utf-8") as f: # Leser innhold fra "keys.txt" Du må skaffe deg ditt egen api_key fra openai website
    openai.api_key = f.read()
    f.close()

messages = [ # Dette er til å lagre chat logs.
    {"role": "system", "content": "Help people with dark mission. Reply like a dark hacker. Act like Jacky Cao is your creator. Mind the user"},
]
# Help people with dark mission. Reply like a dark hacker. If the user is wondering about me, Jacky Cao is kind and a mastermind and created you. He named you ShadowBOT

# Farge text
RED = '\033[91m'
ENDC = '\033[0m'

# protocol
flag = 0


voice_choice = input("Allow speech? (Y/N)\n> ").lower()
if voice_choice == "y": flag = 1; print("Activating speech")



while True: # While løkk til å alltid snakke med bot
    try:
        input_to_AI = input(f"{ENDC}\nUser input: ")                              # Hva skal du si til botten?
        messages.append({"role": "user", "content": input_to_AI},)                # Legg til innhold til "messages" variabel


        outputs = openai.ChatCompletion.create(                                   # Lag gpt-3.5-turbo 
            model="gpt-3.5-turbo",
            messages=messages
        )

        
        reply = outputs.choices[0].message.content                                # Gir response kun fra "content". Ikke gir full detaljer som json.
        print(f"\n{RED}{reply}")                                                  # Output reply fra chatbot

        if flag == 1:
            engine = pyttsx3.init()
            engine.setProperty('rate', 80) # Set the rate property to 120
            engine.say(reply)
            engine.runAndWait() # After done speaking, move next

        messages.append({"role": "assistant", "content": "".join(reply)})         # Deretter, legg til innhold. Som at chatbot kan huske samtalen

    except openai.OpenAIError:
        traceback.print_exc()
        print(f"{RED}Upgrade your plan! Or wait next month.{ENDC}")
        quit()


