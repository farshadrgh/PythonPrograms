import tkinter as tk

parent = tk.Tk()
parent.geometry("250x200")
label1 = tk.Label(parent,text = "A list of favourite languages...")
listbox = tk.Listbox(parent)

listbox.insert(1,"C++")
listbox.insert(2, "Python")
listbox.insert(3, "Java")
listbox.insert(4, "C#")

label1.pack()
listbox.pack()
parent.mainloop()
