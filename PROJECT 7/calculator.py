"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/15/2024
PURPOSE:CALCULATOR GUI
"""

from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("450x500")
root.maxsize(450,500)
root.minsize(450,500)
root.title("KRISTAL CALCULATOR GUI")
root.config(bg="grey")
root.wm_iconbitmap(r"C:\Users\Kristal\Desktop\Python-Tkinter-GUI\PROJECTS\Calculator\calculator.ico")

def click(event):
    global screen_var
    text=event.widget.cget("text") 
    # print(text)
    if text == "=":
        if screen_var.get().isdigit():
            value=int(screen_var.get())
        else:
            try:
                value=eval(screen_var.get())
            except Exception as e:
                print(e)
                screen_var.set("ERROR")
                tmsg.showerror(title="Error",message=f"{e}")

        screen_var.set(value)
        screen_input.update()

    elif text== "C":
        screen_var.set("")
        screen_input.update()
    else:
        screen_var.set(screen_var.get() + text)
        screen_input.update()

screen_var=StringVar()
screen_var.set("")
screen_input=Entry(root,textvar=screen_var,font="lucida 30 bold",fg="red",bg="yellow")
screen_input.pack(fill=X,padx=10,pady=10)

frame1=Frame(root,bg="grey")
#option 1 make seperate indivual buttons and individual variables which is very long code
# button9=Button(frame1,text="9",padx=5,pady=5,font="Lucida 30 bold")
# button9.pack(side=LEFT,anchor="w",padx=15,pady=15)
# button9.bind("<Button-1>",click)
# button8=Button(frame1,text="8",padx=5,pady=5,font="Lucida 30 bold",)
# button8.pack(side=LEFT,anchor="w",padx=15,pady=15)
# button7=Button(frame1,text="7",padx=5,pady=5,font="Lucida 30 bold",)
# button7.pack(side=LEFT,anchor="w",padx=15,pady=15)

#option2 make same variable but seperate individual buttons

# button=Button(frame1,text="9",padx=5,pady=5,font="Lucida 30 bold")
# button.pack(side=LEFT,anchor="w",padx=15,pady=15)
# button.bind("<Button-1>",click)

# button=Button(frame1,text="8",padx=5,pady=5,font="Lucida 30 bold")
# button.pack(side=LEFT,anchor="w",padx=15,pady=15)
# button.bind("<Button-1>",click)

# button=Button(frame1,text="7",padx=5,pady=5,font="Lucida 30 bold")
# button.pack(side=LEFT,anchor="w",padx=15,pady=15)
# button.bind("<Button-1>",click)


#option better to use for loop and same variable
#for this i need 3 frames to have 4 horizontals
frame2=Frame(root,bg="grey")
frame3=Frame(root,bg="grey")
frame4=Frame(root,bg="grey")
buttons=[
        (9,frame1),(8,frame1),(7,frame1),('/',frame1),('C',frame1),
        (6,frame2),(5,frame2),(4,frame2),('*',frame2),('(',frame2),
        (3,frame3),(2,frame3),(1,frame3),('-',frame3),(')',frame3),
        (0,frame4),('00',frame4),('.',frame4),('+',frame4),('=',frame4)
        ]

for (number,frame) in buttons:
    button=Button(frame,text=f"{str(number)}",padx=5,pady=5,font="Lucida 30 bold",bg="grey",fg="blue")
    button.pack(side=LEFT,anchor="w",padx=15,pady=15)
    button.bind("<Button-1>",click)

    
frame1.pack(fill=X)
frame2.pack(fill=X)
frame3.pack(fill=X)
frame4.pack(fill=X)
root.mainloop()