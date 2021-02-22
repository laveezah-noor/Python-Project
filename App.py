import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=500)
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.create_btn('Button', cmd=None)
        self.create_label('Label', cmd=None)
        # self.create_entry()
        self.pack()

    def create_btn(self, txt, cmd):
        self.btn = tk.Button(self)
        self.btn["text"] = txt
        self.btn["command"] = cmd
        self.btn.pack()

    def create_label(self, txt, cmd):
        self.label = tk.Label(self)
        self.label["text"] = txt
        self.label["command"] = cmd
        self.label.pack()

    def create_entry(self):
        self.entry = tk.Entry(self, width=50, borderwidth=5)
        # self.entry.grid(row=0, column=0)
        self.entry.insert(0, 'Enter Shitty Name:')
        self.entry.pack()


root = tk.Tk()
root.title('Application')
root.iconbitmap('')
app = Application(master=root)
app.mainloop()
