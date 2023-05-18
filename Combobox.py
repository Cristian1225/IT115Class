# we imported tk kinter 
import tkinter as tk    
from tkinter import ttk


# Here we are stting an event to select an event 
def on_select(event):

    selected_item = event.widget.get()
    print("Selected items:", selected_item)

#  Here we created a title for the combobox 
root = tk.Tk()
root.title("Combobox Exampple!")

