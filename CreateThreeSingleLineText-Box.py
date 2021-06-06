import tkinter as tk

parent = Text-Box.Tk()
parent.geometry("400x250")

name = Text-Box.Label(parent, text = "Name").place(x = 30, y = 50)
email = Text-Box.Label(parent, text = "User ID").place(x = 30, y = 90)
password =  Text-Box.Label(parent, text = "Password").place(x = 30, y = 130)

sbmitbtn = Text-Box.Button(parent, text = "Submit", activebackground = "green", activeforeground = "blue").place(x = 120, y = 170)

entry1 = Text-Box.Entry(parent).place(x = 85, y = 50)
entry2 = Text-Box.Entry(parent).place(x = 85, y = 90)
entry3 = Text-Box.Entry(parent).place(x = 90, y = 130)

parent.mainloop()
