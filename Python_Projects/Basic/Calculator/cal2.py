#Project Name: Basic Calculator
#Project Category: Basic
#Day: 24th August-2023
#programming language: Python
#Programer: Amna Amjid

import tkinter
from tkinter import *
import tkinter as tk

root=Tk()
root.title("Simple Calculator")
root.geometry("418x445+300+200")
root.config(bg="#17161b")
root.resizable(False,False)


equation= " "

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation = " "
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result= eval(equation)
        except:
            result="error"
            equation=""
            
    label_result.config(text=result)

            
label_result= Label(root, width=27, height=2, text=" ",font=("arial",25,"bold"))
label_result.pack()

Button(root, width= 4, height=1, text="C",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=0,y=58)
Button(root, width= 4, height=1, text="/",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("/")).place(x=105,y=58)
Button(root, width= 4, height=1, text="%",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("%")).place(x=210,y=58)
Button(root, width= 4, height=1, text="*",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("*")).place(x=315,y=58)

Button(root, width= 4, height=1, text="7",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("7")).place(x=0,y=135)
Button(root, width= 4, height=1, text="8",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("8")).place(x=105,y=135)
Button(root, width= 4, height=1, text="9",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("9")).place(x=210,y=135)
Button(root, width= 4, height=1, text="-",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("-")).place(x=315,y=135)

Button(root, width= 4, height=1, text="4",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("4")).place(x=0,y=210)
Button(root, width= 4, height=1, text="5",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("5")).place(x=105,y=210)
Button(root, width= 4, height=1, text="6",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("6")).place(x=210,y=210)
Button(root, width= 4, height=1, text="+",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("+")).place(x=315,y=210)

Button(root, width= 4, height=1, text="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("1")).place(x=0,y=290)
Button(root, width= 4, height=1, text="2",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("2")).place(x=105,y=290)
Button(root, width= 4, height=1, text="3",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("3")).place(x=210,y=290)
Button(root, width= 9, height=1, text="0",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show("0")).place(x=0,y=370)

Button(root, width= 4, height=1, text=".",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#212d36",command=lambda:show(".")).place(x=210,y=370)
Button(root, width= 4, height=3, text="=",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda:calculate()).place(x=315,y=290)

root.mainloop()