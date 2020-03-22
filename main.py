import os
import tkinter as tk
from tkinter import filedialog

class App:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.winfo_toplevel().title("Spyro: Reignited Trilogy Mod Manager")
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
    file = os.path.basename(filedialog.askopenfilename())
    listbox.insert(tk.END, file)



root = tk.Tk()
img = tk.PhotoImage(file='/home/nicholas/Desktop/Code/mod-manager-spyro/assets/spyro.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("1280x720")

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

# Listbox

listbox = tk.Listbox(root, width="40", height="30")
listbox.pack(side=tk.LEFT)
import_button = tk.Button(root, text="Add Mod(s)", command=openFile)
import_button.pack()
delete_button = tk.Button(root, text="Delete", command=lambda lb=listbox: lb.delete(tk.ANCHOR))
delete_button.pack()



app = App(root)
root.mainloop()