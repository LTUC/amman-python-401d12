import tkinter as tk # python pkg to create GUI
from tkinter import ttk # submodule fro (tkinter)

# 1- creating the main window
root = tk.Tk() # Tk() create tha main window of the application

# 2- start creating & packing the elements
# create a label
ttk.Label(root, text="Hello from 401d12!", padding=(30,10)).pack()

# 3- Running the main event loop (run the app using the root window)
root.mainloop()
