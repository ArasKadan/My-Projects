#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
import os

def get_unique_filename(base_name, extension, directory):
    filename = os.path.join(directory, f"{base_name}{extension}")
    counter = 1

    while os.path.exists(filename):
        filename = os.path.join(directory, f"{base_name}({counter}){extension}")
        counter += 1

    return filename

def on_button_click_create_htmlfile():
    directory = filedialog.askdirectory(title="Select Directory")
    if not directory:  
        return
    filename = get_unique_filename("htmlfile", ".html", directory)
    with open(filename, "w") as file:
        file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>HTML File</title>\n</head>\n<body>\n<h1>This file was created by a button click!</h1>\n</body>\n</html>")
    print(f"Html file created: {filename}")

def on_button_click_create_pythonfile():
    directory = filedialog.askdirectory(title="Select Directory")
    if not directory:  
        return
    filename = get_unique_filename("pythonfile", ".py", directory)
    with open(filename, "w") as file:
        file.write("print('This file was created by a button click!')")
    print(f"Python file created: {filename}")

def on_button_click_create_scalafile():
    directory = filedialog.askdirectory(title="Select Directory")
    if not directory:  
        return
    filename = get_unique_filename("scalafile", ".scala", directory)
    with open(filename, "w") as file:
        file.write("object scalafile extends App {}")
    print(f"Scala file created: {filename}")

def on_button_click_create_csharpfile():
    directory = filedialog.askdirectory(title="Select Directory")
    if not directory:  
        return
    filename = get_unique_filename("csharpfile", ".cs", directory)
    with open(filename, "w") as file:
        file.write("using System;")
    print(f"C# file created: {filename}")

root = tk.Tk()
root.title("File Creator")
root.configure(bg="black")
canvas = tk.Canvas(root, width=500, height=1)
canvas.pack()

btn0 = tk.Button(
    root,
    text="Create Html File",
    command=on_button_click_create_htmlfile,
    font=("JetBrainsMono Nerd Font", 12),
    bg="#444444",  
    fg="white",    
    activebackground="#666666",  
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10
)
btn1 = tk.Button(
    root,
    text="Create Python File",
    command=on_button_click_create_pythonfile,
    font=("JetBrainsMono Nerd Font", 12),
    bg="#444444",
    fg="white",
    activebackground="#666666",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10
)
btn2 = tk.Button(
    root,
    text="Create Scala File",
    command=on_button_click_create_scalafile,
    font=("JetBrainsMono Nerd Font", 12),
    bg="#444444",
    fg="white",
    activebackground="#666666",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10
)

btn3 = tk.Button(

    root,
    text="Create C# File",
    command=on_button_click_create_csharpfile,
    font=("JetBrainsMono Nerd Font", 12),
    bg="#444444",
    fg="white",
    activebackground="#666666",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10
)

btn0.pack(pady=10)
btn1.pack(pady=10)
btn2.pack(pady=10)
btn3.pack(pady=10)

root.mainloop()
