import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext,lang=language,slow=True)
    myobj.save(filename)

#this function returns pydubs audio segment
def mergeAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio=AudioSegment.from_mp3(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\Railways_Announcement.mp3')

    #1(Starting Sound)
    start=0000
    finish=1550
    audioProcessed=audio[start:finish]
    audioProcessed.export(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\1.mp3',format="mp3")

    #2 (may i have your attention please...train no)
    start=36950
    finish=39800
    audioProcessed=audio[start:finish]
    audioProcessed.export(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\2.mp3',format="mp3")

    #3 (train no and name)

    #4 from
    start=44200
    finish=44750
    audioProcessed=audio[start:finish]
    audioProcessed.export(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\4.mp3',format="mp3")

    #5 (from city)


    #6 (to)
    start=45600
    finish=46150
    audioProcessed=audio[start:finish]
    audioProcessed.export(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\6.mp3',format="mp3")

    #7 (to city)

    #8 (via)
    start=47100
    finish=47650
    audioProcessed=audio[start:finish]
    audioProcessed.export(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\8.mp3',format="mp3")

    #9 (via city)

    #10 (is arriving shortly on platform no)
    start=49000
    finish=52100
    audioProcessed=audio[start:finish]
    audioProcessed.export(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\10.mp3',format="mp3")

    #11 (platform no)

    #12 (thankyou end music)
    start=52800
    finish=54800
    audioProcessed=audio[start:finish]
    audioProcessed.export(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\12.mp3',format="mp3")


def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
        #3 (train no and name)
        textToSpeech(f"{item['Train_No']} {item['Train_Name']}",r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\3.mp3')

        #5 (from city)
        textToSpeech(item['From'],r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\5.mp3')

        #7 (to city)
        textToSpeech(item['To'],r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\7.mp3')

        #9 (via city)
        textToSpeech(item['Via'],r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\9.mp3')
        
        #11 (platform no)
        textToSpeech(item['Platform_No'],r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios\11.mp3')


        #merging all audios
        basedirectory=r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\audios'
        audios=[f"{basedirectory}/{i}.mp3" for i in range(1,13)]
        announcement=mergeAudios(audios)
        announcement.export(f"{basedirectory}/Announcement_{item['Train_No']}_{index+1}.mp3",format="mp3")

if __name__=='__main__':
    print("Generating skeleton")
    generateSkeleton()
    print("Now Generating Announcement")
    generateAnnouncement(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 4\Train-Announcement_List.xlsx')