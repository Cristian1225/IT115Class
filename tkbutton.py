#  importing tkkinter as tk
import tkinter as tk 


# printing a statement for button 
def button_child():
    print("Button clicked!")

# creating a button example 
root = tk.Tk()
root.title("Button Example!")

# using button to create a click me coommand button
button = tk.Button(root,text="Click Me!", command=button_child)
button.pack()



root.mainloop()