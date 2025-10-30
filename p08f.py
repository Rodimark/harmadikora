import tkinter as tk
from tkinter import messagebox
import requests
import p07n

def datakeres():
    try:
        response = requests.get("http://localhost:5000/api/data",timeout=3) #!kerees eseten visszadja a json filet
        response.raise_for_status()
        data  = response.json()
        label.config(text=data["uzenet"])
        app.throws_num_input.set(data["uzenet"])
    except:
        messagebox.showerror("Error", "Nem sikerult a kapcsolat")

root = tk.Tk()
app= p07n.SaveDiceThrow(root)

api_button = tk.Button(root, text="Lekeres", command = datakeres) #gomb rootba helyezese
api_button.grid(row = 4, column = 0, pady = 10)

label = tk.Label(root, text="...")
label.grid(row = 4, column = 1, pady = 10)
app.mainloop()

root.destroy()
root.mainloop()