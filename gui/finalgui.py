# python3
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
#import requests
from login import testuserinput
# from tkvideo import tkvideo

from datetime import datetime
import time

fen = tk.Tk()

def movement(direction):
  #url = "http://192.168.1.25:5000"
  #requests.post(url, json={'command': direction})
  time = datetime.now()
  current_time = time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
  with open('logText.txt', 'at') as f:
    f.write(f"{direction} at " + current_time + "\n")
    f.close()


def logout(testuserinput):
  fen.destroy()
  time = datetime.now()
  current_time = time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
  with open('logText.txt', 'at') as f:
    f.write(f"{testuserinput} has logged out at " + current_time + "\n")
    f.close()


#TOP LEFT
left = tk.Frame(fen, bg="grey", width=200, height=200)
left.pack_propagate(False)
tk.Label(left,text="Raw Video",fg="white",bg="black",anchor="center",justify="center").pack()
left.grid(column=0, row=0, pady=5, padx=10, sticky="n")
sep = Separator(fen, orient="vertical")
sep.grid(column=1, row=0, sticky="ns")

#line
sty = Style(fen)
sty.configure("TSeparator", background="black")

#TOP RIGHT
right = tk.Frame(fen, width=200, height=200, bg="grey")
right.pack_propagate(False)
tk.Label(right, text="Movement Controls", fg="white", bg="black").pack()
right.grid(column=2, row=0, pady=5, padx=10, sticky="n")

forwardbutton = Button(right,text="↑",width=3,command=lambda: movement("forward"))
forwardbutton.grid(row=4, column=6, pady=(30, 3))
# a button for moving backward
backbutton = Button(right,text="↓",width=3,command=lambda: movement("backward"))
backbutton.grid(row=6, column=6, pady=3)
# a button for turning right
rightbutton = Button(right,text="→",width=3,command=lambda: movement("right"))
rightbutton.grid(row=5, column=7, pady=3, padx=3)
# a button for turning left
leftbutton = Button(right, text="←", width=3, command=lambda: movement("left"))
leftbutton.grid(row=5, column=5, pady=3, padx=3)
# a custom button
stopbutton = Button(right,text="STOP",width=5,command=lambda: movement("stop"))
stopbutton.grid(row=5, column=6, padx=3, pady=3)
logoutbutton = Button(right, text="Logout", width=5, command=lambda: logout(testuserinput))
logoutbutton.grid(row=7, column=6, pady=27)

#BOTTOM LEFT
bleft = tk.Frame(fen, bg="grey", width=200, height=200)
bleft.pack_propagate(False)
tk.Label(bleft,text="Video With Line Detection",fg="white",bg="black",anchor="center",justify="center").pack()
bleft.grid(column=0, row=1, pady=5, padx=10, sticky="n")
sep = Separator(fen, orient="vertical")
sep.grid(column=1, row=1, sticky="ns")

import tkinter as tk

def update_log_label():
    try:
        with open("logText.txt", "r") as file:
            log_content = file.read()
            log_label.config(text=log_content)
    except FileNotFoundError:
        log_label.config(text="Log file not found.")

# BOTTOM RIGHT
bright = tk.Frame(fen, bg="grey", width=200, height=200)
bright.pack_propagate(False)
tk.Label(bright, text="Log", fg="white", bg="black").pack()

log_label = tk.Label(bright, text="", fg="white", bg="black")
log_label.grid(column=1, row=1, pady=5, padx=10, sticky="n")

update_log_label()

update_button = tk.Button(bright, text="Update Log", command=update_log_label)
update_button.grid(column=2, row=1, pady=5, padx=10, sticky="n")



bright.grid(column=2, row=1, pady=5, padx=10, sticky="n")

fen.mainloop()