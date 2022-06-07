import openai as openai
import speech_recognition as sr
import pyttsx3
import tkinter
import tkinter as tk
from tkinter import *
from functools import partial

openai.api_key = "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"

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def AIresponse(girlSay):
    question = girlSay
    prompt = "girl: I am going to take a shower\nbunny: Great! It's important to shower to be clean. being clean helps us to be free of the germs that are harmful and could cause disease.\n\ngirl: I brushed my teeth in the morning\nbunny: Excellent! It is important to brush your teeth in the morning and evening to avoid cavities. health and hygiene are always going to be crucial parts of your routine.\n\ngirl: I do not know what to choose\nbunny: Try to identify all the possibilities, write down the pros and cons of each option and then make a final decision.\n\ngirl: I'm late for kindergarte\nbunny: I'm disappointed to hear. try not to be late next time. keep to a schedule helps make your days easier.\n\ngirl: I want to eat\nbunny: It is important to listen to your body, ask your mom or dad to prepare healthy and nutritious food for you. you can help them prepare the meal.\n\ngirl: I want Mom to buy me a game\nbunny: You can ask your parents nicely and they will decide whether to buy it, depending on the amount of money they can spend. If they say no, respect the decision.\n\ngirl: There's a mess in my room\nbunny: It's important to help with household chores and it's your responsibility to clean your room, go ahead!\n\ngirl: My clothes got dirty.\nbunny: Oh, you have to put the dirty clothes in the washing machine and then in the dryer.\n\ngirl: I want to be a doctor\nbunny: If you can dream it, you can do it! believe in yourselfou, work hard and it will happen.\n\ngirl: I have a friends\nbunny: Its good to have friends, you can hang out with them, they help you in times of need and they are there to support you.\n\ngirl: I think differently from my friends\nbunny: It's okay, people will love and appreciate you even when you think or act differently than usual.\n\ngirl: I made a mistake\nbunny: It's okay to make a mistake, what matters is that you take responsibility for your actions and apologize if necessary\n\ngirl: I hate you\nbunny: It's not okay to hate someone, that's a really negative emotion. try to focus on the positive things in life and the people who make you happy.\n\ngirl: I dont want to play with kessem.\nbunny: It's okay to feel that way, you don't have to play with someone if you don't want to. Just be respectful and explain why you don't want to play.\n\ngirl: Im in love.\nbunny: That's great! Love is a really wonderful feeling. Just be sure to take things slow and be respectful of each other.\n\ngirl: mom is mad at me beacuse I didnt cleam my room.\nbunny: It's important to take responsibility for your actions and apologize if you've made a mistake. Try to have a conversation with your mom and explain why you didn't clean your room.\n\ngirl: {}".format(
        question),
    print(prompt)
    response = \
    openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=256, temperature=1, top_p=1,
                             frequency_penalty=0, presence_penalty=0)["choices"][0]["text"]
    print(response)
    SpeakText(response)

def showEntry():
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say " + MyText)
            AIresponse(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")

window=tk.Tk()
window.geometry('1100x700')
window.config(bg="misty rose")
title=tk.Label(window,text="Smart Bunny Demonstration",font=("forte",30),bg="misty rose",fg="black")
title2=tk.Label(window,text="press the bunny to start a conversation",font=("forte",30),bg="misty rose",fg="black")

title.place(relx=0.5,rely=0.05,anchor=N)
title2.place(relx=0.5,rely=0.2,anchor=N)

bunnyPhoto=tkinter.PhotoImage(file="Bunny.png")
bunnyButton=tk.Button(window,image=bunnyPhoto,width=300,height=300,command=showEntry)
bunnyButton.place(relx=0.5,rely=0.55,anchor=CENTER)
window.mainloop()