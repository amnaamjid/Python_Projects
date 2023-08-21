#Project Name:Langauge translator App
#project No :2
#Caregory:Basic
#Day:2
#20-08-2023
#Programmer: Amna Amjid
#Programming language: Python


from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title("Language Translator")
root.geometry('592x370')

frame1= Frame(root, width=592, height=370, relief = RIDGE, borderwidth=5, bg='#F7DC6F')
frame1.place(x=0,y=0)
lab_txt = Label(root, text="Language Translator", font=("Helvetica 20 bold"), fg="black", bg='#F7DC6F').pack(pady=10)

lab_txt = Label(root, text="Source Text", font=("Helvetica 10 bold"), fg="black", bg='#F7DC6F')
lab_txt.place(x=10,y=50,width=100,height=50)

list_txt = [1,2,3,4]
comb_sor = ttk.Combobox(frame1, value = list_txt)
lab_txt.place(x=10,y=50,width=100,height=50)

sou_txt= Text(frame1, width=20, height=7, borderwidth =5, relief=RIDGE, font=("verdana",15))
sou_txt.place(x=10,y=100)

dest_txt= Text(frame1, width= 20, height=7, borderwidth=5, relief= RIDGE, font=("Verdana", 15))
dest_txt.place(x=300, y=100)

btn1= Button(frame1, text="Translate", relief= RAISED, borderwidth=2,font=("verdana", 10, "bold"),bg='#248aa2', fg="White",cursor="hand2" )
btn1.place(x=185,y=300)

btn2= Button(frame1, text="Clear", relief= RAISED, borderwidth=2,font=("verdana", 10, "bold"),bg='#248aa2', fg="White",cursor="hand2" )
btn2.place(x=300,y=300)

root.mainloop()