"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/15/2024
PURPOSE:Notepad
"""
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    textArea.delete(1.0,END)

def openFile():
    global file
    file=askopenfilename(
                        defaultextension=".txt",
                         filetypes=[("All Files","*.*"),
                        ("Text Documents","*.txt")]
                        )
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0,END)
        f=open(file,"r")
        textArea.insert(1.0,f.read())
        f.close()
def saveFile():
   global file
   if file==None:
       file=asksaveasfilename(
                            initialfile='Untitled.txt',
                            defaultextension=".txt",
                            filetypes=[("All Files","*.*"),
                            ("Text Documents","*.txt")])
       if file=="":
           file=None
       else:
           #save as new file
           f=open(file,"w")
           f.write(textArea.get(1.0,END))
           f.close()

           root.title(os.path.basename(file) + "- Notepad")
           print("file saved")

   else:
       #save the file
       f=open(file,"w")
       f.write(textArea.get(1.0,END))
       f.close()


def quitApp():
    root.destroy()

def Cut():
    textArea.event_generate(("<<Cut>>"))

def Copy():
    textArea.event_generate(("<<Copy>>"))

def Paste():
    textArea.event_generate(("<<Paste>>"))

def About():
    tmsg.showinfo("Info","Welcome to Notepad by Kristal")


if __name__=="__main__":
    root=Tk()
    root.geometry("600x400")
    root.title("Kristal Notepad")
    root.wm_iconbitmap(r"C:\Users\Kristal\Desktop\Python-Tkinter-GUI\PROJECTS\Notepad\notes.ico")

    # textarea

    textArea=Text(root,font="lucida 13")
    file=None
    textArea.pack(fill='both',expand=True)

    #menu bar
    mainMenu=Menu(root)

    #fileMenu starts
    fileMenu=Menu(mainMenu,tearoff=0)
    #to open new file
    fileMenu.add_command(label="New",command=newFile)
    #to open already existing file
    fileMenu.add_command(label="Open",command=openFile)
    #to save the current file
    fileMenu.add_command(label="Save",command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=quitApp)
    mainMenu.add_cascade(label="File",menu=fileMenu)
    #fileMenu ends

    #editMenu starts
    editMenu=Menu(mainMenu,tearoff=0)
    #cut,copy,pastefeature
    editMenu.add_command(label="Cut",command=Cut)
    editMenu.add_command(label="Copy",command=Copy)
    editMenu.add_command(label="Paste",command=Paste)
    mainMenu.add_cascade(label="Edit",menu=editMenu)
    #editMenu ends

    #helpMenu starts
    helpMenu=Menu(mainMenu,tearoff=0)
    helpMenu.add_command(label="About",command=About)
    mainMenu.add_cascade(label="Help",menu=helpMenu)


    root.config(menu=mainMenu)

    #Adding scroll bar

    scroll=Scrollbar(textArea)
    scroll.pack(side=RIGHT,fill=Y)

    #linking scrollbar
    scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll.set)


    root.mainloop()