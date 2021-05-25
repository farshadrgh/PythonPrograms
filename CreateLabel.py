import tkinter as tk
parent = tk.Tk()
parent.title("MySecondWindow")
my_label = tk.Label(parent, text="Hello World", font=("Arial Bold", 45))
my_label.grid(column=0, row=0)
parent.mainloop()