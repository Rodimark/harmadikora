import tkinter as tk
from tkinter import messagebox
import random

class DiceThrow:
    def __init__(self, master):
        self.master = master
        self.master.title("Kockadobások statisztikája")
        self.master.geometry("600x500")

        self.throws_num = 10
        self.results = [0 for _ in range(7)]

        self.title = tk.Label(self.master, text="Kattints a gombra!", font=("Ariel", 16))
        self.title.grid(row=0, column=1, pady=20)

        self.throws_num_input = tk.StringVar(value="10")
        self.thrownum = tk.Entry(self.master, textvariable=self.throws_num_input, width=10)
        self.thrownum.grid(row=1, column=0, pady=20, padx=50)

        self.gomb = tk.Button(self.master, text="Throw", command=self.on_throw)
        self.gomb.grid(row=1, column=2, pady=20)

        self.throws_num_text = tk.StringVar(value="......")
        self.result_label = tk.Label(self.master, textvariable=self.throws_num_text, font=("Ariel", 16))
        self.result_label.grid(row=2, column=1, pady=20)

        self.exit = tk.Button(self.master, text="Kilépés", command=self.master.destroy, bg="red")
        self.exit.grid(row=1, column=3, pady=20, padx=40)

        self.on_throw()

        # self.master.mainloop()

    def throw(self, throws):
        """A dobások elvégzése és az eredmény frissítése"""
        #results = [0 for _ in range(7)]
        for _ in range(throws):
            num = random.randint(1, 6)
            self.results[num] += 1

        self.throws_num_text.set(
            f"1 - {self.results[1]} \n"
            f"2 - {self.results[2]} \n"
            f"3 - {self.results[3]} \n"
            f"4 - {self.results[4]} \n"
            f"5 - {self.results[5]} \n"
            f"6 - {self.results[6]}"
        )

    def on_throw(self):
        """A dobás gomb eseménykezelője"""
        try:
            self.throws_num = int(self.throws_num_input.get())
            self.throw(self.throws_num)
        except ValueError:
            messagebox.showerror("Hiba", "Rossz értéket adott meg!")


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceThrow(root)
    root.mainloop()