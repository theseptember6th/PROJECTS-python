"""
AUTHOR: KRISTAL SHRESTHA
DATE: 6/15/2024
PURPOSE: Notepad
"""
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        with open(file, "r") as f:
            textArea.insert(1.0, f.read())

def saveFile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt',
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            with open(file, "w") as f:
                f.write(textArea.get(1.0, END))
            root.title(os.path.basename(file) + " - Notepad")
            statusvar.set("Saved")
    else:
        with open(file, "w") as f:
            f.write(textArea.get(1.0, END))
        statusvar.set("Saved")

def quitApp():
    root.destroy()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("Info", "Welcome to Notepad by Kristal")

def on_mouse_wheel(event):
    textArea.yview_scroll(int(-1*(event.delta/120)), "units")

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

if __name__ == "__main__":
    root = Tk()
    root.geometry("600x400")
    root.title("Kristal Notepad")
    root.wm_iconbitmap(r"C:\Users\Kristal\Desktop\Python-Tkinter-GUI\PROJECTS\Notepad\notes.ico")

    # textarea
    textArea = Text(root, font="lucida 13")
    file = None
    textArea.pack(fill='both', expand=True)

    # Adding Scrollbar
    scroll = Scrollbar(textArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll.set)

    # Bind mouse wheel event
    textArea.bind("<MouseWheel>", on_mouse_wheel)

    # Context menu
    context_menu = Menu(root, tearoff=0)
    context_menu.add_command(label="Cut", command=cut)
    context_menu.add_command(label="Copy", command=copy)
    context_menu.add_command(label="Paste", command=paste)

    textArea.bind("<Button-3>", show_context_menu)

    # Menu bar
    mainMenu = Menu(root)

    # File menu
    fileMenu = Menu(mainMenu, tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quitApp)
    mainMenu.add_cascade(label="File", menu=fileMenu)

    # Edit menu
    editMenu = Menu(mainMenu, tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    mainMenu.add_cascade(label="Edit", menu=editMenu)

    # Help menu
    helpMenu = Menu(mainMenu, tearoff=0)
    helpMenu.add_command(label="About", command=about)
    mainMenu.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=mainMenu)

    # Adding status bar
    statusvar = StringVar()
    statusvar.set("Welcome to Notepad")
    sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor='w')
    sbar.pack(side=BOTTOM, fill=X)

    # Keyboard shortcuts
    textArea.bind("<Control-x>", lambda e: cut())
    textArea.bind("<Control-c>", lambda e: copy())
    textArea.bind("<Control-v>", lambda e: paste())

    root.mainloop()
