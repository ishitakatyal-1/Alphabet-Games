# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:44:48 2019

@author: Ishita
"""
def write_a():
    output1["text"] = "a"
    
def write_b():
    output1["text"] = "b"

def write_c():
    output1["text"] = "c"

def write_d():
    output1["text"] = "d"

def write_e():
    output1["text"] = "e"

def write_f():
    output1["text"] = "f"
    
def write_g():
    output1["text"] = "g"

def write_h():
    output1["text"] = "h"

def write_i():
    output1["text"] = "i"

def write_j():
    output1["text"] = "j"

def write_k():
    output1["text"] = "k"
    
def write_l():
    output1["text"] = "l"

def write_m():
    output1["text"] = "m"

def write_n():
    output1["text"] = "n"

def write_o():
    output1["text"] = "o"

def write_p():
    output1["text"] = "p"
    
def write_q():
    output1["text"] = "q"

def write_r():
    output1["text"] = "r"

def write_s():
    output1["text"] = "s"

def write_t():
    output1["text"] = "t"

def write_u():
    output1["text"] = "u"
    
def write_v():
    output1["text"] = "v"

def write_w():
    output1["text"] = "w"

def write_x():
    output1["text"] = "x"

def write_y():
    output1["text"] = "y"

def write_z():
    output1["text"] = "z"


import sys
import tkinter as tk
from tkinter import *

color = tk.Tk()
color.title("a2z`")
color.geometry("250x750")
color.config(background="white")

mainframe1 = tk.Frame(color)
mainframe1.pack()

button1 = tk.Button(mainframe1, height=3, width=10, background="red", text="a", command=write_a)
button2 = tk.Button(mainframe1, height=3, width=10, background="blue",text="b", command=write_b)
button3 = tk.Button(mainframe1, height=3, width=10, background="yellow", text="c", command=write_c)
button4 = tk.Button(mainframe1, height=3, width=10, background="lightgreen", text="d", command=write_d)
button5 = tk.Button(mainframe1, height=3, width=10, background="pink", text="e", command=write_e)

button6 = tk.Button(mainframe1, height=3, width=10, background="red", text="f", command=write_f)
button7 = tk.Button(mainframe1, height=3, width=10, background="blue", text="g", command=write_g)
button8 = tk.Button(mainframe1, height=3, width=10, background="yellow", text="h", command=write_h)
button9 = tk.Button(mainframe1, height=3, width=10, background="lightgreen", text="i", command=write_i)
button10 = tk.Button(mainframe1, height=3, width=10, background="pink", text="j", command=write_j)

button11 = tk.Button(mainframe1, height=3, width=10, background="red", text="k", command=write_k)
button12 = tk.Button(mainframe1, height=3, width=10, background="blue", text="l", command=write_l)
button13 = tk.Button(mainframe1, height=3, width=10, background="yellow", text="m", command=write_m)
button14 = tk.Button(mainframe1, height=3, width=10, background="lightgreen", text="n", command=write_n)
button15 = tk.Button(mainframe1, height=3, width=10, background="pink", text="o", command=write_o)

button16 = tk.Button(mainframe1, height=3, width=10, background="red", text="p", command=write_p)
button17 = tk.Button(mainframe1, height=3, width=10, background="blue", text="q", command=write_q)
button18 = tk.Button(mainframe1, height=3, width=10, background="yellow", text="r", command=write_r)
button19 = tk.Button(mainframe1, height=3, width=10, background="lightgreen", text="s", command=write_s)
button20 = tk.Button(mainframe1, height=3, width=10, background="pink", text="t", command=write_t)

button21 = tk.Button(mainframe1, height=3, width=10, background="red", text="u", command=write_u)
button22 = tk.Button(mainframe1, height=3, width=10, background="blue", text="v", command=write_v)
button23 = tk.Button(mainframe1, height=3, width=10, background="yellow", text="w", command=write_w)
button24 = tk.Button(mainframe1, height=3, width=10, background="lightgreen", text="x", command=write_x)
button25 = tk.Button(mainframe1, height=3, width=10, background="pink", text="y", command=write_y)
button26 = tk.Button(mainframe1, height=3, width=10, background="red", text="z", command=write_z)

output1 = tk.Label(mainframe1, height=2, width=5, background="white", font="Times 20")
     
label00 = tk.Label(mainframe1, text="Copyright\n@Myra-IK")              

button = tk.Button(mainframe1, height=3, width=10, text="Close", font=("Times 10"),command=color.destroy)

button1.grid(row=0, column=0, columnspan=1, sticky=tk.W, pady=5)
button2.grid(row=0, column=1, columnspan=1, sticky=tk.W, pady=5)
button3.grid(row=0, column=2, columnspan=1, sticky=tk.W, pady=5)
button4.grid(row=1, column=0, columnspan=1, sticky=tk.W, pady=5)
button5.grid(row=1, column=1, columnspan=1, sticky=tk.W, pady=5)

button6.grid(row=1, column=2, columnspan=1, sticky=tk.W, pady=5)
button7.grid(row=2, column=0, columnspan=1, sticky=tk.W, pady=5)
button8.grid(row=2, column=1, columnspan=1, sticky=tk.W, pady=5)
button9.grid(row=2, column=2, columnspan=1, sticky=tk.W, pady=5)
button10.grid(row=3, column=0, columnspan=1, sticky=tk.W, pady=5)

button11.grid(row=3, column=1, columnspan=1, sticky=tk.W, pady=5)
button12.grid(row=3, column=2, columnspan=1, sticky=tk.W, pady=5)
button13.grid(row=4, column=0, columnspan=1, sticky=tk.W, pady=5)
button14.grid(row=4, column=1, columnspan=1, sticky=tk.W, pady=5)
button15.grid(row=4, column=2, columnspan=1, sticky=tk.W, pady=5)

button16.grid(row=5, column=0, columnspan=1, sticky=tk.W, pady=5)
button17.grid(row=5, column=1, columnspan=1, sticky=tk.W, pady=5)
button18.grid(row=5, column=2, columnspan=1, sticky=tk.W, pady=5)
button19.grid(row=6, column=0, columnspan=1, sticky=tk.W, pady=5)
button20.grid(row=6, column=1, columnspan=1, sticky=tk.W, pady=5)

button21.grid(row=6, column=2, columnspan=1, sticky=tk.W, pady=5)
button22.grid(row=7, column=0, columnspan=1, sticky=tk.W, pady=5)
button23.grid(row=7, column=1, columnspan=1, sticky=tk.W, pady=5)
button24.grid(row=7, column=2, columnspan=1, sticky=tk.W, pady=5)
button25.grid(row=8, column=0, columnspan=1, sticky=tk.W, pady=5)
button26.grid(row=8, column=2, columnspan=1, sticky=tk.W, pady=5)

output1.grid(row=9, column=0, columnspan=3, sticky=tk.EW)
label00.grid(row=10, column=0, columnspan=1, sticky=tk.W, pady=5)
button.grid(row=10, column=2, columnspan=1, sticky=tk.W, pady=5)

color.mainloop()