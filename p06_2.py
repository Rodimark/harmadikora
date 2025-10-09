import tkinter as tk
from tkinter import messagebox
import random

#def throw(dobasok):
    #num = random.randint(1,6)
    #eredmeny_cimke_szovege.set(str(num))
def throw(dobasok):
    eredmenyek = [0 for _ in range(7)]
    for _ in range(dobasok):
        num = random.randint(1,6)
        eredmenyek[num] += 1
    eredmeny_cimke_szovege.set(
        f"1 - {eredmenyek[1]} \n"
        f"2 - {eredmenyek[2]} \n"
        f"3 - {eredmenyek[3]} \n"
        f"4 - {eredmenyek[4]} \n"
        f"5 - {eredmenyek[5]} \n"
        f"6 - {eredmenyek[6]} "
    )
    #print(eredmenyek)
def on_throw():
    try:
        dobasok_szama = int(dobasok_szama_bemenet.get()) #kulonben typererror
        throw(dobasok_szama)
    except:
        messagebox.showerror("Hiba")

root = tk.Tk()
root.title("Kockadobasok statisztikaja")
root.geometry("450x450")

title = tk.Label(root, text="Press the button", font=("Arial", 16))
title.pack(pady=30)

dobasok_szama_bemenet = tk.StringVar(value='10')
dobasszam = tk.Entry(root, textvariable=dobasok_szama_bemenet, width=10)
dobasszam.pack(pady=10)

button = tk.Button(root,text="Throw",command=on_throw)
button.pack()

eredmeny_cimke_szovege = tk.StringVar(value="......")
eredmeny_cimke = tk.Label(root, textvariable=eredmeny_cimke_szovege,font=("Arial", 20))
eredmeny_cimke.pack(pady=20)

kilepes = tk.Button(root, text="Exit",command=root.destroy, bg="red")
kilepes.pack()
tk.mainloop()