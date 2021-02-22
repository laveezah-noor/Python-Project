import tkinter as tk
from tkinter import ttk
main = tk.Tk()


class Window:

    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)

    def create_label(self, txt):
        self.label = tk.Label(self.root, text=txt).pack()

    def create_button(self, txt, cmd=None):
        self.btn = tk.Button(self.root, text=txt, command=cmd).pack()

    def create_entry(self, txt, cmd=None):
        self.entrythingy = tk.Entry(self.root)
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        def print_contents(event):
            print("Hi. The current entry content is:",  self.contents.get())

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>', print_contents)


    def create_optmenu(self, lst=None):
        clicked = tk.StringVar()
        clicked.set(lst[0])

        def cmd(event):
            print(clicked.get())
        self.dropBtn = tk.OptionMenu(self.root, clicked, *lst, command=cmd).pack()

    def create_combomenu(self, lst):
        def cmd(event):
            print(self.comboBtn.get())
        self.comboBtn = ttk.Combobox(self.root, value=lst).pack()
        # self.comboBtn.current(0)
        # self.comboBtn.bind('<<ComboboxSelected>>', cmd)


win = Window(main, 'App', '300x300')

win.create_label('Username:')
win.create_entry('Enter Name')
win.create_button('Submit')
options = ['Monday',
           'Tuesday']
win.create_optmenu(options)
win.create_combomenu(options)

main.mainloop()
