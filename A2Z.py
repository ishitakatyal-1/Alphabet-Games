# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:44:48 2019

@author: Ishita
"""
def write_A():
    output1["text"] = "A"
    
def write_B():
    output1["text"] = "B"

def write_C():
    output1["text"] = "C"

def write_D():
    output1["text"] = "D"

def write_E():
    output1["text"] = "E"

def write_F():
    output1["text"] = "F"
    
def write_G():
    output1["text"] = "G"

def write_H():
    output1["text"] = "H"

def write_I():
    output1["text"] = "I"

def write_J():
    output1["text"] = "J"

def write_K():
    output1["text"] = "K"
    
def write_L():
    output1["text"] = "L"

def write_M():
    output1["text"] = "M"

def write_N():
    output1["text"] = "N"

def write_O():
    output1["text"] = "O"

def write_P():
    output1["text"] = "P"
    
def write_Q():
    output1["text"] = "Q"

def write_R():
    output1["text"] = "R"

def write_S():
    output1["text"] = "S"

def write_T():
    output1["text"] = "T"

def write_U():
    output1["text"] = "U"
    
def write_V():
    output1["text"] = "V"

def write_W():
    output1["text"] = "W"

def write_X():
    output1["text"] = "X"

def write_Y():
    output1["text"] = "Y"

def write_Z():
    output1["text"] = "Z"


import sys
import tkinter as tk
from tkinter import *

color = tk.Tk()
color.title("A2Z`")
color.geometry("250x750")
color.config(background="white")

mainframe1 = tk.Frame(color)
mainframe1.pack()

button1 = tk.Button(mainframe1, height=3, width=10, background="red", text="A", command=write_A)
button2 = tk.Button(mainframe1, height=3, width=10, background="blue",text="B", command=write_B)
button3 = tk.Button(mainframe1, height=3, width=10, background="yellow", text="C", command=write_C)
button4 = tk.Button(mainframe1, height=3, width=10, background="green", text="D", command=write_D)
button5 = tk.Button(mainframe1, height=3, width=10, background="orange", text="E", command=write_E)

button6 = tk.Button(mainframe1, height=3, width=10, background="red", text="F", command=write_F)
button7 = tk.Button(mainframe1, height=3, width=10, background="blue", text="G", command=write_G)
button8 = tk.Button(mainframe1, height=3, width=10, background="yellow", text="H", command=write_H)
button9 = tk.Button(mainframe1, height=3, width=10, background="green", text="I", command=write_I)
button10 = tk.Button(mainframe1, height=3, width=10, background="purple", text="J", command=write_J)

button11 = tk.Button(mainframe1, height=3, width=10, background="red", text="K", command=write_K)
button12 = tk.Button(mainframe1, height=3, width=10, background="blue", text="L", command=write_L)
button13 = tk.Button(mainframe1, height=3, width=10, background="yellow", text="M", command=write_M)
button14 = tk.Button(mainframe1, height=3, width=10, background="green", text="N", command=write_N)
button15 = tk.Button(mainframe1, height=3, width=10, background="orange", text="O", command=write_O)

button16 = tk.Button(mainframe1, height=3, width=10, background="red", text="P", command=write_P)
button17 = tk.Button(mainframe1, height=3, width=10, background="blue", text="Q", command=write_Q)
button18 = tk.Button(mainframe1, height=3, width=10, background="yellow", text="R", command=write_R)
button19 = tk.Button(mainframe1, height=3, width=10, background="green", text="S", command=write_S)
button20 = tk.Button(mainframe1, height=3, width=10, background="pink", text="T", command=write_T)

button21 = tk.Button(mainframe1, height=3, width=10, background="red", text="U", command=write_U)
button22 = tk.Button(mainframe1, height=3, width=10, background="blue", text="V", command=write_V)
button23 = tk.Button(mainframe1, height=3, width=10, background="yellow", text="W", command=write_W)
button24 = tk.Button(mainframe1, height=3, width=10, background="green", text="X", command=write_X)
button25 = tk.Button(mainframe1, height=3, width=10, background="orange", text="Y", command=write_Y)
button26 = tk.Button(mainframe1, height=3, width=10, background="purple", text="Z", command=write_Z)

output1 = tk.Label(mainframe1, height=2, background="white", width=5, font="Times 20")

label00 = tk.Label(mainframe1, text="Copyright\n@Myra-IK")  

button = tk.Button(mainframe1, height=3, width=10, text="Close", font=("Times 10"),command=color.destroy)
                 
button1.grid(row=0, column=0, sticky=tk.W, pady=5)
button2.grid(row=0, column=1, sticky=tk.W, pady=5)
button3.grid(row=0, column=2, sticky=tk.W, pady=5)
button4.grid(row=1, column=0, sticky=tk.W, pady=5)
button5.grid(row=1, column=1, sticky=tk.W, pady=5)

button6.grid(row=1, column=2, sticky=tk.W, pady=5)
button7.grid(row=2, column=0, sticky=tk.W, pady=5)
button8.grid(row=2, column=1, sticky=tk.W, pady=5)
button9.grid(row=2, column=2, sticky=tk.W, pady=5)
button10.grid(row=3, column=0, sticky=tk.W, pady=5)

button11.grid(row=3, column=1, sticky=tk.W, pady=5)
button12.grid(row=3, column=2, sticky=tk.W, pady=5)
button13.grid(row=4, column=0, sticky=tk.W, pady=5)
button14.grid(row=4, column=1, sticky=tk.W, pady=5)
button15.grid(row=4, column=2, sticky=tk.W, pady=5)

button16.grid(row=5, column=0, sticky=tk.W, pady=5)
button17.grid(row=5, column=1, sticky=tk.W, pady=5)
button18.grid(row=5, column=2, sticky=tk.W, pady=5)
button19.grid(row=6, column=0, sticky=tk.W, pady=5)
button20.grid(row=6, column=1, sticky=tk.W, pady=5)

button21.grid(row=6, column=2, sticky=tk.W, pady=5)
button22.grid(row=7, column=0, sticky=tk.W, pady=5)
button23.grid(row=7, column=1, sticky=tk.W, pady=5)
button24.grid(row=7, column=2, sticky=tk.W, pady=5)
button25.grid(row=8, column=0, sticky=tk.W, pady=5)
button26.grid(row=8, column=2, sticky=tk.W, pady=5)

output1.grid(row=9, column=0, columnspan=3, sticky=tk.EW)
label00.grid(row=10, column=0, columnspan=1, sticky=tk.W, pady=5)
button.grid(row=10, column=2, columnspan=1, sticky=tk.W, pady=5)


color.mainloop()