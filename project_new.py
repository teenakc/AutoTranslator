# speech to text convertor
import pyttsx3
import speech_recognition as sr
from tkinter import *
from PIL import Image,ImageTk

voice_eng= pyttsx3.init('sapi5') #speechAPI version 5, engine to convert text  to speech
voices = voice_eng.getProperty('voices')
voice_eng.setProperty('voice',voices[1].id)
root = Tk()
root.geometry('1100x680')
root.title("Auto speech translator")
root.configure(bg='LightSkyBlue')
def speak(audio):
    voice_eng.say(audio)
    voice_eng.runAndWait()

def speakSentence():
    user = sr.Recognizer()
    with sr.Microphone() as record:
        speak("Ready to listen, please Speak.. ")
        user.pause_threshold = 1   # 1 for system timeout for recognizing voice(wait)
        recording = user.listen(record,phrase_time_limit=5)
        print(recording)
        print("Recognizing...")
        sentence = str(user.recognize_google(recording,language="en-in"))
        fl = open('speechToText', 'w')
        fl.write(sentence)
        speak("you said:")
        speak(sentence)
        lb = Label(root,text="Great, Your message has been saved to the file successfully!",font="Courier 20 bold",fg="Green",bg="LightSkyBlue")
        lb.place(x=140 , y=600)
        speak("Great, Your message has been saved to the file successfully!")

title= Label(root,text="AUTO TRANSLATOR",padx=20,font=("Courier", 16, "bold"),bg="aquamarine4",fg="white",compound=LEFT,height=50)
title.place(x=0,y=0,height=50,width=1100)

para = Label(root,text="Please click on the button to record your voice and convert to text!",fg="violet red",bg="LightSkyBlue",font= ("Modern", 19, "bold")).place(x=180,y=55)
img = Image.open('img.png').resize((730,390))
pic = ImageTk.PhotoImage(img)

label = Label(image=pic).pack(padx=25,pady=95)
butt = Button(root,text=" Click",bg="aquamarine4",fg="black",font=("Courier",13 ,"bold"),height=2,width=10,command=speakSentence).place(x=450 , y=530)
speak("Please click on the button to record your message...")
print("Please click on the button to record your message...")
root.mainloop()

