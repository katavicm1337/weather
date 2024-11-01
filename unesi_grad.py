import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb 
from tkinter import filedialog as fd
import os           

window = tk.Tk()
window.title(f'Unesi ime grada')
window.geometry('500x500')
window.configure(bg='#B4B4B4')

title = tk.Label(master = window, text = 'Unesi ime grada za koji želiš pregledati prognozu', font = 'Calibri 18', bg="#909090")
title.pack()   

def napravi_file():
    gradinput = entry_str.get()
    f = open("ime_grada.txt", "w")
    f.write(gradinput)
    f.close()
    window.destroy()
    os.startfile(os.path.abspath("main.py"))

input_frame = tk.Frame(master = window, bg='#B4B4B4', width= 700, height=50, pady= 100)
entry_str = tk.StringVar()
entry = tk.Entry(master = input_frame, textvariable = entry_str, bg='#B4B4B4')
button = tk.Button(master = input_frame, text = 'Unesi', bg='#B4B4B4', width= 10, command = napravi_file)

entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

output_string = tk.StringVar()
output_label = tk.Label(
    master = window,
    text = 'Output',
    font = 'Calibri 20',
    bg='#B4B4B4',
    textvariable = output_string)
output_label.pack(pady = 5)

window.mainloop()
