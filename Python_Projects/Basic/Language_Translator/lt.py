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
from googletrans import Translator, LANGUAGES
from tkinter import messagebox
import textblob

root = tk.Tk()
root.title("Language Translator")
root.geometry('592x370')

def label_change():
    c = comb_sor.get()
    c1 = comb_dest.get()
    lab_txt2.configure(text=c)
    lab_txt3.configure(text=c1)
    root.after(1000,label_change)
    

def change(text = "Type", src = "English", dest = "Urdu"):
    
    text1= text
    src1= src
    dest1= dest
    trans = Translator()
    trans1 = trans.translate(text, src = src1, dest = dest1)
    return trans1.text
    
    
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sou_txt.get(1.0, END)
    text_get = change(text = msg, src = s, dest= d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, text_get)
    
def clear():
    sou_txt.delete(1.0, END)
    dest_txt.delete(1.0, END)
    
#icon
image_icon = PhotoImage(file = "translator.png")
root.iconphoto(False, image_icon )

root.minsize(592, 370)
root.maxsize(592, 370)


frame1= Frame(root, width=592, height=370, relief = RIDGE, borderwidth=5, bg='#F7DC6F')
frame1.place(x=0,y=0)

lab_txt1 = Label(root, text="Language Translator", font=("Times New Roman", 20 ,"bold"), fg="black", bg='#F7DC6F').pack(pady=10)

lab_txt2 = Label(root, text= " Source Text ", font=("Times New Roman", 14, "bold"), fg="black", bg='#F7DC6F')
lab_txt2.place(x=100,y=70,width=100,height=20)

list_txt = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame1, value = list_txt)
comb_sor.place(x=11,y=98,width=270,height=22)
comb_sor.set("English")

sou_txt= Text(frame1, width=26, height=7, borderwidth =5, relief=RIDGE, font=("Times New Roman",15))
sou_txt.place(x=10,y=120)

lab_txt3 = Label(root, text="Destination Text", font=("Times New Roman", 14 ,"bold"), fg="black", bg='#F7DC6F')
lab_txt3.place(x=370,y=70,width=150,height=20)

comb_dest = ttk.Combobox(frame1, value = list_txt)
comb_dest.place(x=300,y=98,width=272,height=22)
comb_dest.set("Select Language")

dest_txt= Text(frame1, width= 26, height=7, borderwidth=5, relief= RIDGE, font=("Times New Roman", 15))
dest_txt.place(x=300, y=120)

trans_btn= Button(frame1, text="TRANSLATE", relief= RAISED, borderwidth=4,font=("Times New Roman", 11, "bold"),bg='#248aa2', fg="White",cursor="hand2", activebackground = "purple" , command= data )
trans_btn.place(x=175,y=315)

clear_btn= Button(frame1, text="CLEAR", relief= RAISED, borderwidth=4,font=("Times New Roman", 11, "bold"),bg='#248aa2', fg="White",cursor="hand2", activebackground = "purple", command=clear )
clear_btn.place(x=300,y=315)

label_change()

root.mainloop()