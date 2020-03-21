import tkinter as tk
from tkinter import filedialog

class App:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.printButton = tk.Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=tk.LEFT)

        self.quitButton = tk.Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=tk.LEFT)

    def printMessage(self):
        print("Wow, this works.")


def doNothing():
    print("I do nothing")

def openFile():
    file_path = filedialog.askopenfilename()
    print(file_path)

root = tk.Tk()
root.geometry("500x300")

# Top Menu

menu = tk.Menu(root)
root.config(menu=menu)

submenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Import mod", command=openFile)
submenu.add_command(label="Save", command=doNothing)
submenu.add_separator()
submenu.add_command(label="Exit", command=root.quit)

editmenu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", command=doNothing)

# Toolbar



app = App(root)
root.mainloop()