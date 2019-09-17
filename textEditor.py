#Author: Nawal Ahmed
#The program is a simple, lightweight text editor specifically made for creating, saving, and loading lists.

from tkinter.filedialog import* #Open and save file dialouges
# The maybe not so quick brown fox jumped over the lazy dog
filename = None

#Four functions used in the file menu and in the context menu
def newFile(): #New file function
    global filename
    filename = "Untitled"
    text.delete(0.0, END) #Number on the left place of the decimal is the line number and the right is the column number

def saveAs(): #Save as file function
    f = asksaveasfile() #Inside the tk file dialouge
    t = text.get(0.0, END) #Gets all the text
    try: #If able to save then it will include all whitespace in the text file
        f.write(t.rstrip())
    except: #If unable to save, then do nothing
        pass

def openFile(): #Open file function
    f = askopenfile(mode='r')
    t = f.read() #Read all the text inside
    text.delete(0.0, END) #Clear the text in the text box
    text.insert(0.0, t)

def onclickEnter(event): #Bullet creator function
    text.insert(END, "• ")

root = Tk() #Beginning of Tkinter program
root.title("Nawal's QuickList Creator") #Title of program
#Size of the window
root.minsize(width=600, height=400)
root.maxsize(width=600, height=400)

#Context Menu
popup = Menu(root, tearoff=0)
#Use built-in commands from Tkinter
popup.add_command(label="New", command=newFile)
popup.add_command(label="Open", command=openFile)
popup.add_separator() #Separate for clairity
popup.add_command(label="Save As", command=saveAs)
popup.add_command(label="Quit", command=root.quit)

def do_popup(event):
    # display the popup menu
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup.grab_release()

root.bind("<Button-3>", do_popup) #Right click will open the popup function which opens the context menu
root.bind('<Return>', onclickEnter) #When pressing the enter key, activate the oneclickEnter function which makes a new bullet on a new line

text = Text(root, width=600, height=400) #Text box same as window size
text.pack()
#Begin the file with some instructions on what the program can do
text.insert(END, "                    "
                 "--This is a quicklist creator.--\n"
                 "         "
                 "--Everytime you press enter, a new bullet is created.--\n"
                 "              "
                 "--Right-click to save and make a new file.--"
                 "                               "
                 "--Remember to save your text files as .txt--\n"
                 "--------------------------------------------------------------------------\n• ")
#Menubar that's below the title but above the textbox
menubar = Menu(root)
filemenu = Menu(menubar)
#Typical menubar functions built-into Tkinter
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu) #Cascading dialouge

root.config(menu=menubar)
root.mainloop() #mainloop
