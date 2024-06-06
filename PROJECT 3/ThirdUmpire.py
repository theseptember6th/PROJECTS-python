"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/6/2024
PURPOSE:THIRD UMPIRE DECISION MAKING
"""

import tkinter
import PIL.Image,PIL.ImageTk #install pillow
import cv2  #you have to install opencv-python
from functools import partial
import imutils
import time
import threading
''' Threading allows you to have different parts of your process run concurrently. These different parts are usually individual and have a separate unit of execution belonging to the same process. The process is nothing but a running program that has individual units that can be run concurrently. For example, A web-browser could be a process, an application running multiple cameras simultaneously could be a process; a video game is another example of a process.

example could be a video game in which the process has to run the tasks in parallel like the graphics, user interaction, and networking (while playing multiplayer games) because it has to be responsive at all times. And to accomplish this, it has to make use of the concept of multi-threading, where each thread would be responsible for running each independent and individual task.'''
#width and height for our application screen
SET_WIDTH=650
SET_HEIGHT=368

#it will store my video
stream=cv2.VideoCapture(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 3\images\clip.mp4')
flag=True
def play(speed):
    global flag
    print(f"you clicked on play,the speed is {speed}")
    
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES) #it takes the frame number
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    try:   
        grabbed,frame=stream.read()
        frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image=frame
        canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
        if flag:
            canvas.create_text(134,26,fill="orange",font="Times 26  bold",text="Decision Pending")
        flag=not flag

    except Exception as e:
        print("end of the video")
    
   
    

def pending(decision):
    # step 1 display decision pending image
    frame=cv2.cvtColor(cv2.imread(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 3\images\pending.png'),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    # step 2 wait for 5 seconds
    time.sleep(5)
    # step 3 Dispaly sponsor image
    frame=cv2.cvtColor(cv2.imread(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 3\images\sponsor.png'),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    # step 4 wait for 5 seconds
    time.sleep(5)
    # step 5 Display Out/not out image
    if decision=='out':
        decisionImg=r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 3\images\out.png'
    else:
        decisionImg=r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 3\images\not_out.png'
    frame=cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #step 6 wait for 5 second
    time.sleep(10)
  

def out():
    thread =threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("Player is out")

def not_out():
    thread =threading.Thread(target=pending,args=("not out",))
    thread.daemon=1
    thread.start()
    print("Player is not out")
    
#Tkinter GUI starts here
window=tkinter.Tk() #Construct a toplevel Tk widget, which is usually the main window of an application
window.title("KRISTAL'S THIRD EMPIRE DECISION REVIEW KIT")


'''The canvas widget is the most flexible widget in Tkinter. The Canvas widget allows you to build anything from custom widgets to complete user interfaces.
The canvas widget is a blank area on which you can draw figures, create text, and place images.'''
cv_img=cv2.cvtColor(cv2.imread(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 3\images\welcome.png'),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)

photo =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()


#Buttons to control playback
btn=tkinter.Button(window,text="<< Previous (fast)",width=50,command=partial(play,-25))
btn.pack()

btn=tkinter.Button(window,text="<< Previous (slow)",width=50,command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window,text="Next (fast) >>",width=50,command=partial(play,25))
btn.pack()

btn=tkinter.Button(window,text="Next (slow) >>",width=50,command=partial(play,2))
btn.pack()

btn=tkinter.Button(window,text="GIVE OUT",width=50,command=out)
btn.pack()

btn=tkinter.Button(window,text="GIVE NOT OUT",width=50,command=not_out)
btn.pack()

window.mainloop() #tells Python to run the Tkinter event loop.
