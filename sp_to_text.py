# Author: Abolfazl Zarghani


import speech_recognition as sr
import pyttsx3
import pyaudio
import openai

openai.api_key  = "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"

r = sr.Recognizer()

def SpeakText(command):
     
   
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()




def call_gpt3(prompt):
    
    response = openai.Completion.create(engine = "text-davinci-001", 
                                        prompt = prompt, max_tokens = 50)
    return response["choices"][0]["text"]
    
mic = sr.Microphone()
    
while(1):   
     

    try:
         
        with sr.Microphone() as source2:
             
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            audio2 = r.listen(source2)
             
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            a = MyText
            print("Did you say ",MyText)
            gpt_output = call_gpt3(MyText)
            print(gpt_output)
            SpeakText(gpt_output)
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
