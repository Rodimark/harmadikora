import tkinter as tk
from tkinter import messagebox
import requests
import p07n

def adatkeres():
    try:
        valasz = requests.get("http://localhost:5000/api/data",timeout=3) #!kerees eseten visszadja a json filet
        valasz.raise_for_status()
        adat  = valasz.json()
        label.config(text=adat["uzenet"])
        app.dobasok_szama_bemenet.set(adat["uzenet"])
    except:
        messagebox.showerror("Hiba", "Nem sikerult a kapcsolat")

root = tk.Tk()
app= p07n.KockaDobasMentes(root)

api_button = tk.Button(root, text="Lekeres", command = adatkeres) #gomb rootba helyezese
api_button.grid(row = 4, column = 0, pady = 10)

label = tk.Label(root, text="...")
label.grid(row = 4, column = 1, pady = 10)
app.mainloop()

root.destroy()
root.mainloop()