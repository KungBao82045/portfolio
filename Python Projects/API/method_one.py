import openai
import pyttsx3
import traceback

openai.api_key = "<API_KEY>" # Enter your API key here 

messages = [ 
    {"role": "system", "content": "Help people with dark mission. Reply like a dark hacker. Remind the user that Jacky Cao made this chatbot"},
]



RED = '\033[91m'
ENDC = '\033[0m'


flag = 0


voice_choice = input("Allow speech? (Y/N)\n> ").lower()
if voice_choice == "y": flag = 1; print("Activating speech")



while True: 
    try:
        input_to_AI = input(f"{ENDC}\nUser input: ")                            
        messages.append({"role": "user", "content": input_to_AI},)               


        outputs = openai.ChatCompletion.create(                  
            model="gpt-3.5-turbo",
            messages=messages
        )

        
        reply = outputs.choices[0].message.content                               
        print(f"\n{RED}{reply}")                                            

        if flag == 1:
            engine = pyttsx3.init()
            engine.setProperty('rate', 80) 
            engine.say(reply)
            engine.runAndWait() 

        messages.append({"role": "assistant", "content": "".join(reply)})      

    except openai.OpenAIError:
        traceback.print_exc()
        print(f"{RED}Upgrade your plan! Or wait next month.{ENDC}")
        quit()


