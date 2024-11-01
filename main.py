import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from urllib.request import urlopen

f = open("ime_grada.txt", "r")
BASE_URL = "http://api.weatherapi.com/v1/current.json?key="
API = ""
GRAD = f.read()
TAGS = "&aqi=yes"

url = BASE_URL + API + GRAD + TAGS 

response = requests.get(url)
data = response.json()
main = data['current']
temp = main['temp_c']
vjetar = main['wind_kph']
osjecaj = main['feelslike_c']
vjetar_smjer = main['wind_dir']


window = tk.Tk()
window.title(f'Prognoza za {GRAD.capitalize()}')
window.geometry('500x500')
window.configure(bg='#B4B4B4')

title = tk.Label(window, text = f'Prognoza za grad {GRAD.capitalize()}', font = 'Calibri 24',bg ="#909090")
title.pack()

nepoznati_vjetrovi = ['NNE','ENE','ESE','SE','SSE','SSW','SW','WSW','WNW','NNW']

sjevernjak = ['N','NE']
bura = ['NE','ENE']
istocnjak = ['E','ESE','SE']
jugo = ['S','SSE','SSW']
zapadnjak = ['W','SW','WSW']
maestral = ['NW','WNW','NNW']


if vjetar_smjer == sjevernjak:
     vjetar_smjer = "Sjevernjak"
     

elif vjetar_smjer == bura:
    vjetar_smjer = "Bura"


elif vjetar_smjer == istocnjak:
    vjetar_smjer = "Istočnjak"


elif vjetar_smjer == jugo:
    vjetar_smjer = "Jugo"

elif vjetar_smjer == zapadnjak:
    vjetar_smjer = "Zapadnjak"

elif vjetar_smjer == maestral:
    vjetar_smjer = "Maestral"


temperatura = tk.Label(master = window, text = f'Temperatura - {temp}°C', font = 'Calibri 12', bg='#B4B4B4', pady = 25)
temperatura.pack()

osjecaj_temp = tk.Label(master = window, text = f'Stvarni osjećaj - {osjecaj}°C', font = 'Calibri 12', bg='#B4B4B4', pady = 25)
osjecaj_temp.pack()

vjetar_brzina = tk.Label(master = window, text = f'Vjetar - {vjetar}km/h', font = 'Calibri 12', bg='#B4B4B4', pady = 25)
vjetar_brzina.pack()

vjetar_smjer2 = tk.Label(master = window, text = f'Smjer vjetra - {vjetar_smjer}', font = 'Calibri 12', bg='#B4B4B4', pady = 25)
vjetar_smjer2.pack()

     

window.mainloop()
