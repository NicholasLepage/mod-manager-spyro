import os
import tkinter as tk
from tkinter import filedialog
import sqlite3 as lite

from db import initiate_db
# **TODO: implement mod deletion


class App:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.winfo_toplevel().title("Spyro: Reignited Trilogy Mod Manager")
        frame.pack()

        # Listbox
        self.listbox = tk.Listbox(root, width="40", height="30")
        self.listbox.pack(side=tk.LEFT)
        self.import_button = tk.Button(
            root, text="Add Mod(s)", command=self.open_file)
        self.import_button.pack()
        self.delete_button = tk.Button(
            root, text="Delete", command=self.delete_file)
        self.delete_button.pack()

        # Other Buttons
        self.locate_spyro_button = tk.Button(
            frame, text="Locate Spyro.exe", command=self.locate_spyro)
        self.locate_spyro_button.pack()

        self.quit_button = tk.Button(frame, text="Quit", command=frame.quit)
        self.quit_button.pack(side=tk.LEFT)

        self.saved_items = []
        self.spyro_install_path = ""

    def delete_file(self):
        selection = self.listbox.curselection()
        self.cur.execute()
        self.listbox.delete(tk.ANCHOR)
        self.saved_items.delete(tk.ANCHOR)
        print(self.saved_items)

    # Runs on startup to fetch added mods and spyro.exe location
    def load(self):
        if not os.path.isfile('info.db'):
            initiate_db()

        self.conn = lite.connect("info.db")
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT * FROM mods_location")
        mod_list = self.cur.fetchall()
        for item in mod_list:
            self.saved_items.append(item[0])
            file = os.path.basename(item[0])
            self.listbox.insert(tk.END, file)

        self.cur.execute("SELECT * FROM spyro_location")
        tmp_spyro_path = self.cur.fetchall()
        if tmp_spyro_path:
            self.spyro_install_path = tmp_spyro_path[0]

    def locate_spyro(self):
        self.spyro_install_path = filedialog.askopenfilename(
            title="Select Spyro.exe", filetypes=[("Spyro.exe", "*.exe")])

        self.cur.execute(f"INSERT INTO spyro_location VALUES('{self.spyro_install_path}')")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        file = os.path.basename(file_path)

        self.cur.execute(f"INSERT INTO mods_location VALUES('{file_path}', {1})")
        self.conn.commit()

        self.listbox.insert(tk.END, file)

    def save(self):
        self.conn.commit()
        self.conn.close()


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
