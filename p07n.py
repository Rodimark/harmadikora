import csv
import sqlite3
import tkinter as tk
from tkinter import messagebox

import p07

class SaveDiceThrow(p07.DiceThrow):
    def __init__(self, master):  # <-- itt volt a Error
        super().__init__(master)
        self.txt_save = tk.Button(master, text="Save to txt file", command=self.save_to_txt)
        self.txt_save.grid(row=3, column=0, pady=10)

        self.csv_save = tk.Button(master, text="Save to csv file", command=self.save_to_csv)
        self.csv_save.grid(row=3, column=1)

        self.sql_save = tk.Button(master, text="Save to SQL", command=self.sql_save)
        self.sql_save.grid(row=3, column=2)



    def sql_save(self):
        try:
            conn = sqlite3.connect("kokadobas.db")
            db = conn.currow()
            db.execute("CREATE TABLE IF NOT EXISTS dice (throws INT, one INT, two INT, three INT, four INT,  five INT, six INT)")

            db.execute("INSERT INTO dice VALUES (?, ?, ?, ?, ?, ?, ?)", (self.thrownum,
                                                                          self.results[1],
                                                                          self.results[2],
                                                                          self.results[3],
                                                                          self.results[4],
                                                                          self.results[5],
                                                                          self.results[6])
                       )
            conn.commit()
            conn.close()
        except:
            messagebox.showerror("Error", "Saving to SQL failed!")


    def save_to_csv(self):
        filename = "mentes.csv"
        try:
            with open(filename, mode="a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([self.thrownum] + [self.results[i] for i in range(1, 7)])
                messagebox.showinfo("Saving", "Successfully saved!")
        except:
            messagebox.showerror("Error", "Saving error!")

    def save_to_txt(self):
        row= (f"{self.thrownum}, "
              f"{self.results[1]}, {self.results[2]}, {self.results[3]}, "
              f"{self.results[4]}, {self.results[5]}, {self.results[6]}\n")
        try:
            with open("mentes.txt", "a", encoding="utf-8") as file:
                file.write(row)
            messagebox.showinfo("Saving","Successfully saved!")
        except:
            messagebox.showerror("Error", "Saving error!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SaveDiceThrow(root)
    root.mainloop()