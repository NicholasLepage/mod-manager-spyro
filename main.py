import os
import tkinter as tk
from tkinter import filedialog


class App:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.winfo_toplevel().title("Spyro: Reignited Trilogy Mod Manager")
        frame.pack()

        # Listbox
        self.listbox = tk.Listbox(root, width="40", height="30")
        self.listbox.pack(side=tk.LEFT)
        self.import_button = tk.Button(root, text="Add Mod(s)", command=self.openFile)
        self.import_button.pack()
        self.delete_button = tk.Button(root, text="Delete", command=self.deleteFile)
        self.delete_button.pack()

        # Other Buttons
        self.printButton = tk.Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=tk.LEFT)

        self.quitButton = tk.Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=tk.LEFT)

        self.saved_items = []

    def load(self):
        if os.path.isfile('save.txt'):
            with open('save.txt', 'r') as file:
                for line in file:
                    currentMod = line[:-1]
                    self.saved_items.append(currentMod)

        for item in self.saved_items:
            file = os.path.basename(item)
            self.listbox.insert(tk.END, file)

    def save(self):
        with open('save.txt','w') as f:
            f.seek(0)
            f.truncate(0)
            for item in self.saved_items:
                f.write(str('%s\n' % item))

    def printMessage(self):
        print(self.saved_items)

    def openFile(self):
        file_path = filedialog.askopenfilename()
        file = os.path.basename(file_path)
        self.saved_items.append(str(file_path))
        self.listbox.insert(tk.END, file)

    def deleteFile(self):
        self.listbox.delete(tk.ANCHOR)
        self.saved_items.delete(tk.ANCHOR)
        print(self.saved_items)

root = tk.Tk()
img = tk.PhotoImage(file='./assets/spyro.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("1280x720")

# Top Menu

# menu = tk.Menu(root)
# root.config(menu=menu)

# submenu = tk.Menu(menu)
# menu.add_cascade(label="File", menu=submenu)
# submenu.add_command(label="Import mod", command=openFile(listbox))
# submenu.add_command(label="Save", command=doNothing)
# submenu.add_separator()
# submenu.add_command(label="Exit", command=root.quit)

# editmenu = tk.Menu(menu)
# menu.add_cascade(label="Edit", menu=editmenu)
# editmenu.add_command(label="Undo", command=doNothing)

app = App(root)
app.load()
root.mainloop()
app.save()