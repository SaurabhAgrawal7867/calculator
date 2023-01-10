from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

#Defining the geometry of our windows
root=Tk()
root.title("Untitled-Notepad")
root.iconbitmap('notepad.ico')
root.geometry("649x427")

#Defining all the function here

def newFile():
    global file
    file=None
    root.title("Untitled-Notepad")
    textarea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

def saveasFile():
        global file
        if file == None :
            file = asksaveasfilename ( initialfile='Untitled.txt', defaultextension=".txt",
                                       filetypes=[("All Files", "*.*"),
                                                  ("Text Documents", "*.txt")] )
            if file == "" :
                file = None

            else :
                f = open ( file, "w" )
                f.write ( textarea.get ( 1.0, END ) )
                f.close ()

                root.title ( os.path.basename ( file ) + " - Notepad" )
                print ( "File Saved" )
        else :
            f = open ( file, "w" )
            f.write ( textarea.get ( 1.0, END ) )
            f.close ()
def quitApp():
    root.destroy()
def cutFile():
    textarea.event_generate(("<<Cut>>"))
def copyFile():
    textarea.event_generate(("<<Copy>>"))
def pasteFile():
    textarea.event_generate(("<<Paste>>"))
def font():
    textarea.config()
#Defining the text area

textarea=Text(root,font="Arial 12",undo=True)
textarea.pack(expand=True,fill=BOTH)
file=None

#Defining Menubar

mainMenu=Menu(root)

#First nested menu bar

fileMenu=Menu(mainMenu,tearoff=0)
fileMenu.add_command(label="New",command=newFile)
fileMenu.add_command(label="open",command=openFile)
fileMenu.add_command(label="Save as",command=saveasFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quitApp)

#Second nested menu
editMenu=Menu(mainMenu,tearoff=0)
editMenu.add_command(label="Cut       Ctrl+X",command=cutFile)
editMenu.add_command(label="Paste     Ctrl+V",command=pasteFile)
editMenu.add_command(label="Copy      Ctrl+C",command=copyFile)
editMenu.add_command(label="Undo      Ctrl+Z",command=textarea.edit_undo)
editMenu.add_command(label="Redo      Ctrl+Y",command=textarea.edit_redo)

#Third nested menu
'''
formatMenu=Menu(mainMenu,tearoff=0)
formatMenu.add_command(label="Font",command=)
'''

mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_cascade(label="Edit",menu=editMenu)
#mainMenu.add_cascade(label="Format",menu=formatMenu)

#Creating Scrollbar

scroll=Scrollbar(textarea)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)

root.config(menu=mainMenu)





root.mainloop()