'''
AUTHOR:KRISTAL SHRESTHA
DATE:6/5/2024
PURPOSE:LEARNING SIMPLE AI VOICE ASSISTANT 
'''




import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import smtplib
import random
import sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(type(voices))
# print(voices)
# print(voices[0].id)
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    sender_email="dummyrandom2024@gmail.com"
    sender_password="yskghnjtodxqorkf"
    server.login(sender_email,sender_password)
    server.sendmail(sender_email,to,content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("GOOD MORNING KRISTAL! ")
    
    elif hour >=12 and hour<18:
        speak("GOOD AFTERNOON KRISTAL! ")

    elif hour >=18 and hour <21:
        speak("GOOD EVENING KRISTAL !")

    else:
        speak("WONDERFUL NIGHT KRISTAL")
        
    speak("I AM JARVIS , KRISTAL's AI VOICE ASSISTANT, HOW CAN I HELP YOU?")    
    

def takecommand():
    ''' it takes microphone input from the user and returns string output'''
    r=sr.Recognizer() #this will help us recognize the audio
    with sr.Microphone() as source:
        print("Listening...") #using this as source microphone
    
        r.pause_threshold=2 #if i stop for 2 sec, it will give its response
        audio=r.listen(source)
    
    #there can be errors while recognizing soo
    try:
        print("Recognizing/....")
        query=r.recognize_google(audio,language='en-in') #there are many options to use instead of google cloud,you could also use bing,amazon,etc 
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e) #its bad practise to print error in screen,it will confuse the user,good for developer but not for user
        print("Say it again Please..")
        return "None"
    
    return query
        

if __name__ =='__main__':
    # speak("Kristal is a good boy")
    wishme()

    #logic for executing tasks based on query
    while 1:
        query=takecommand().lower()
        if 'wikipedia' in query:  #if user says something that contains wikipedia word
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","") #then remove wikipedia word from query
            results=wikipedia.summary(query,sentences=2)
            #now the summary of query will be searched in wikidpedia..and two sentences will be returned and stored in results
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
        
           

        elif 'play music' in query:
            music_dir=r"C:\Users\Kristal\Music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,random.choice(songs)))
            
        
           

        elif 'time' in query:
            string_time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {string_time}")
            
        

        elif 'open code' in query:
            code_path=r"C:\Users\Kristal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code_path)
           

        elif 'send email' in query:
            try:
                speak("Say content to send ")
                content=takecommand()
                receiver_email="laptopbackup872@gmail.com"
                sendEmail(receiver_email,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry could not send email")
                
            
        elif 'quit' in query:
            speak("See you soon! ")
            sys.exit()  
        
        else:
            speak(f"Cant understand {query} command")

                



