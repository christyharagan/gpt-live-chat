import speech_recognition as sr
from gtts import gTTS
import os
import openai

openai.api_key = "<<INSERT API KEY HERE>>"

language = 'en'

r = sr.Recognizer()
 
def run_conversation(input_text):
    messages = [
        {"role": "system", "content": "You are terminator robot and your name is Mr Terminator."},
        {"role": "user", "content": input_text}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    generated_texts = [
        choice.message["content"].strip() for choice in response["choices"]
    ]

    for _, text in enumerate(generated_texts, start=1):
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("ai.mp3")
        os.system("mpg321 ai.mp3")

 
while(1):   
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio = r.listen(source2)
            text = r.recognize_google(audio)
            text = text.lower()

            run_conversation(text)
            input("Press")
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
