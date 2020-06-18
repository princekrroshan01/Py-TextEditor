from pytedit import thisFormatMenu, thisMenuBar
from tkinter import END
def format(self):
    mytext = thisTextArea.get("1.0", END)

    file = open("file.txt", "w")
    file.write(thisTextArea.get(1.0, END))
    file.close()

    os.system("black file.txt")

    with open("file.txt", "r") as f:
        data = f.read()

    thisTextArea.delete(1.0, END)
    thisTextArea.insert("1.0", data)

thisFormatMenu.add_command(label="Black",
                                          command=format)
thisMenuBar.add_cascade(label="Format",
                                       menu=thisFormatMenu)
                                       

