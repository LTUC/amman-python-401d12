import tkinter as tk # python pkg to create GUI
from tkinter import ttk # submodule fro (tkinter)
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x200")

text = tk.Label(root, text="Enter your age", height=2, font=("Arial",20))
text.pack()

age = tk.StringVar()

age.set("0")

# create input for tha age
age_input = ttk.Entry(root, width=2, font=("Arial",30), textvariable=age)
age_input.pack()

def calculate():
    age_value = age.get()

    months = int(age_value) * 12
    weeks = months * 4
    days = int(age_value) * 365

    line_one = f"in months = {months}"
    line_two = f"in weeks = {weeks}"
    line_three = f"in days = {days}"

    all_lines = [line_one, line_two, line_three]
    messagebox.showinfo("Your Age", "\n".join(all_lines))

btn = tk.Button(root, text="Calculate", width=20, height=2, bg="#0087f4", borderwidth=0, command=calculate)
btn.pack()

root.mainloop()