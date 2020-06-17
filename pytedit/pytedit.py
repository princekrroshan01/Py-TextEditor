"""

"""


from gtts import gTTS
#from google import *
from PyDictionary import PyDictionary
import goslate
from numpy.distutils.fcompiler import none

dictionary = PyDictionary()
gl = goslate.Goslate()


from pytedit import thisreadoutMenu, thistranslateMenu, thisMenuBar, thismeaningMenu, thismorseMenu, thisHelpMenu

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }


CODE_REVERSED = {value: key for key, value in CODE.items()}


def meaning():

    mytext = thisTextArea.get("1.0", END)

    mset = mytext.split(" ")
    mean = []
    for x in mset:
        mean.append(dictionary.meaning(x))

    for j in mean:
        showinfo("Dictionary Meaning", j)

def translatetoeng():
    mytext = thisTextArea.get("1.0", END)
    englishText = gl.translate(mytext, 'en')
    showinfo("Translated to English", englishText)

def translatetoit():
    mytext = thisTextArea.get("1.0", END)
    italianText = gl.translate(mytext, 'it')
    showinfo("Translated to italian", italianText)

def translatetoch():
    mytext = thisTextArea.get("1.0", END)
    chineseText = gl.translate(mytext, 'zh')
    showinfo("Translated to Chinese", chineseText)

def translatetode():
    mytext = thisTextArea.get("1.0", END)
    germanText = gl.translate(mytext, 'de')
    showinfo("Translated to English", germanText)

def translatetohi():
    mytext = thisTextArea.get("1.0", END)
    hindiText = gl.translate(mytext, 'hi')
    showinfo("Translated to hindi", hindiText)


def frommorse():
    mytext = thisTextArea.get("1.0", END)
    tr = ''.join(CODE_REVERSED.get(i) for i in mytext.split())
    showinfo("Translated to english from morse", tr)


def readouten():
    mytext = thisTextArea.get("1.0", END)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("eng.mp3")
    os.system("eng.mp3")

def readoutit():

    mytext = thisTextArea.get("1.0", END)
    language = 'it'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("ita.mp3")
    os.system("ita.mp3")

def readoutch():

    mytext = thisTextArea.get("1.0", END)
    language = 'zh'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("chi.mp3")
    os.system("chi.mp3")

def readoutde():

    mytext = thisTextArea.get("1.0", END)
    language = 'de'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("ger.mp3")
    os.system("ger.mp3")

def readoutes():

    mytext = thisTextArea.get("1.0", END)
    language = 'es'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("spa.mp3")
    os.system("spa.mp3")

def readouthi():

    mytext = thisTextArea.get("1.0", END)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("hin.mp3")
    os.system("hin.mp3")

def showAbout():
    showinfo("Notepad", "Notepad V1.0")
    
thisreadoutMenu.add_command(label="Read out in English",
                                   command=readouten)

thisreadoutMenu.add_separator()

thisreadoutMenu.add_command(label="Read out in Italian",
                                   command=readoutit)
thisreadoutMenu.add_separator()

thisreadoutMenu.add_command(label="Read out in Chinese",
                                   command=readoutch)
thisreadoutMenu.add_separator()

thisreadoutMenu.add_command(label="Read out in German",
                                   command=readoutde)
thisreadoutMenu.add_separator()

thisreadoutMenu.add_command(label="Read out in Spanish",
                                   command=readoutes)
thisreadoutMenu.add_separator()

thisreadoutMenu.add_command(label="Read out in hindi",
                                   command=readouthi)
thisreadoutMenu.add_separator()

thisMenuBar.add_cascade(label="Text to Speech",
                               menu=thisreadoutMenu)

thismeaningMenu.add_command(label="Find Meaning",
                                   command=meaning)

thisMenuBar.add_cascade(label="Dictionary",
                               menu=thismeaningMenu)

thistranslateMenu.add_command(label="Translate to English",
                                     command=translatetoeng)

thistranslateMenu.add_separator()

thistranslateMenu.add_command(label="Translate to Italian",
                                     command=translatetoit)
thistranslateMenu.add_separator()
thistranslateMenu.add_command(label="Translate to Chinese",
                                     command=translatetoch)
thistranslateMenu.add_separator()
thistranslateMenu.add_command(label="Translate to German",
                                     command=translatetode)
thistranslateMenu.add_separator()
thistranslateMenu.add_command(label="Translate to Hindi",
                                     command=translatetohi)
thistranslateMenu.add_separator()
thisMenuBar.add_cascade(label="Translate",
                               menu=thistranslateMenu)



                                
thismorseMenu.add_command(label="Translate from Morse",
                                 command=frommorse)

thisMenuBar.add_cascade(label="Morse",
                               menu=thismorseMenu)

thisHelpMenu.add_command(label="About Notepad",
                                command=showAbout)
thisMenuBar.add_cascade(label="Help",
                               menu=thisHelpMenu)











