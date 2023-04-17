from django.shortcuts import render
import openai

def chatbot(request):
  
  user_input = request.POST.get('user_input')                                   # Hent input fra yourbot.html

  openai.api_key = "API_KEY"
  
  messages = [ # Dette er til å lagre chat logs.
    {"role": "system", "content": "Help people with dark mission. Reply like a dark hacker."},
  ]

  messages.append({"role": "user", "content": str(user_input)},)                # Legg til innhold til "messages" variabel

  try:
    outputs = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        )
    
    reply = outputs.choices[0].message.content                                    # Så kun tekst svar fra AI.
    
    messages.append({"role": "assistant", "content": "".join(reply)})
    
    context = {'user_input': user_input, "reply_user": reply}                     # context brukes til å lagre og sende data mellom templates og views.py


  except openai.OpenAIError as e:
    context = {'user_input': user_input, "reply_user": e}
    
  return render(request, 'yourbot.html', context)
  
