import os
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

import click

root = Tk()


thisWidth = 300
thisHeight = 300

root.title("Untitled - Notepad")

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

left = (screenWidth / 2) - (thisWidth / 2)

top = (screenHeight / 2) - (thisHeight / 2)

root.geometry('%dx%d+%d+%d' % (thisWidth,
                                      thisHeight,
                                      left, top))

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
thisTextArea = Text(root)
thisTextArea.grid(sticky=N + E + S + W)


thisMenuBar = Menu(root)
thisFileMenu = Menu(thisMenuBar, tearoff=0)
thisFormatMenu = Menu(thisMenuBar, tearoff=0)
thisEditMenu = Menu(thisMenuBar, tearoff=0)

thisreadoutMenu = Menu(thisMenuBar, tearoff=0)

thismeaningMenu = Menu(thisMenuBar, tearoff=0)

thistranslateMenu = Menu(thisMenuBar, tearoff=0)

thisgsearchMenu = Menu(thisMenuBar, tearoff=0)

thismorseMenu = Menu(thisMenuBar, tearoff=0)

thisHelpMenu = Menu(thisMenuBar, tearoff=0)

thisScrollBar = Scrollbar(thisTextArea)
file = None

root.config(menu=thisMenuBar)

thisScrollBar.pack(side=RIGHT, fill=Y)

thisScrollBar.config(command=thisTextArea.yview)
thisTextArea.config(yscrollcommand=thisScrollBar.set)



@click.command()
@click.option("--coading", default='yes', help='coading mode')
@click.option("--reading", default='yes', help='reading mode you can translate text from one language to another and their is text to speech facility also')
def run(coading,reading):
    if coading == 'yes':
        import pytedit.pytcore
        import pytedit.pytcode
    else:
        import pytedit.pytcore
        import pytedit.pytedit 
    root.mainloop()

