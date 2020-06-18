import os

from pytedit import thisFileMenu,thisMenuBar, thisEditMenu, thisTextArea,root 
from tkinter import END
from tkinter import filedialog as fd



def openFile():

    file = fd.askopenfilename(defaultextension=".txt",
                                  filetypes=[("All Files", "*.*"),
                                             ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:

        root.title(os.path.basename(file) + " - Notepad")
        thisTextArea.delete(1.0, END)

        file = open(file, "r")

        thisTextArea.insert(1.0, file.read())

        file.close()

def newFile():
    root.title("Untitled - Notepad")
    file = None
    thisTextArea.delete(1.0, END)
    


def saveFile():
    file=None    
    if file == None:
        file = fd.asksaveasfilename(initialfile='Untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:

            with open(file, "w") as f:
                f.write(thisTextArea.get(1.0, END))
            

            root.title(os.path.basename(file) + " - Notepad")

    else:
        file = open(file, "w")
        file.write(thisTextArea.get(1.0, END))
        file.close()

def cut():
    thisTextArea.event_generate("<<Cut>>")

def copy():
    thisTextArea.event_generate("<<Copy>>")

def paste():
    thisTextArea.event_generate("<<Paste>>")

def quitApplication():
    root.destroy()
    
thisFileMenu.add_command(label="New",
                                command=newFile)

thisFileMenu.add_command(label="Open",
                                command=openFile)

thisFileMenu.add_command(label="Save",
                                command=saveFile)

thisFileMenu.add_separator()
thisFileMenu.add_command(label="Exit",
                                command=quitApplication)
thisMenuBar.add_cascade(label="File",
                               menu=thisFileMenu)

thisEditMenu.add_command(label="Cut",
                                command=cut)

thisEditMenu.add_command(label="Copy",
                                command=copy)

thisEditMenu.add_command(label="Paste",
                                command=paste)

thisMenuBar.add_cascade(label="Edit",
                               menu=thisEditMenu)




