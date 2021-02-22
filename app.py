# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:55:30 2021

@author: Allan
"""

#imports
import tkinter as tk
from tkinter import filedialog, Text
import os
from PIL import ImageTk, Image

# Main Screen
root = tk.Tk()
root.title('Python App')

#  Image import
img = Image.open('secure.png')
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

#Register Screen
register_screen = Toplevel(root)
register_screen.title("Register")

# Canvas
canvas = tk.Canvas(root, height=200, width=200, bg="#263D42")
canvas.pack()

# Frame
frame = tk.Frame(root, bg="#ccc")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Button
button = tk.Button(frame, text="Button", bg="#cccccc2")
button.grid(row=0, column=0)

# Label
label = tk.Label(frame, text="Custom Label", )
label.grid(row=1, column=1)

# Input
entry = tk.Entry(frame, bg="yellow") 
entry.grid(row=2, column=2)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42")
openFile.pack()
# Code to add widgets will go here...
root.mainloop()
