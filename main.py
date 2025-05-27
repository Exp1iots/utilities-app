# imports required libraries
from customtkinter import *
from PIL import Image
import subprocess

set_appearance_mode("Dark")

""" Defines paramiters for the window """
root = CTk() # creates the window
root.geometry("336x319") # sets the window size (in px)
root.title("Python Utility App") # sets the windows title
root.resizable(False, False) # makes the windows not resiable
root.iconbitmap("main.ico") # Sets window icon

""" Creates functions to run the apps """
def launch_calc():
    root.withdraw() # closes the main app
    print("calc opened")

    process = subprocess.Popen(["pythonw", "Calc/calc.py"]) # creates a subprocess of hasher.py

    def check_calc_closed():
        if process.poll() is not None:  # poll() returns the exit code if the process has finished
            print("calc closed")
            root.deiconify() # reopens the main app
        else:
            root.after(100, check_calc_closed)  # Check again after 100 milliseconds

    check_calc_closed()

def launch_hasher():
    root.withdraw() # closes the main app
    print("hasher opened")

    process = subprocess.Popen(["pythonw", "Hasher/hasher.py"]) # creates a subprocess of hasher.py

    def check_hasher_closed():
        if process.poll() is not None:  # poll() returns the exit code if the process has finished
            print("hasher closed")
            root.deiconify() # reopens the main app
        else:
            root.after(100, check_hasher_closed)  # Check again after 100 milliseconds

    check_hasher_closed()

def launch_pwgen():
    root.withdraw() # closes the main app
    print("pwgen opened")

    process = subprocess.Popen(["pythonw", "Password_Generator/password_generator.py"]) # creates a subprocess of password_generator.py

    def check_pwgen_closed():
        if process.poll() is not None:  # poll() returns the exit code if the process has finished
            print("pwgen closed")
            root.deiconify() # reopens the main app
        else:
            root.after(100, check_pwgen_closed)  # Check again after 100 milliseconds

    check_pwgen_closed()

def launch_txtedit():
    root.withdraw() # closes the main app
    print("txtedit opened")

    process = subprocess.Popen(["pythonw", "TextEditor/txtedit.py"]) # creates a subprocess of txtedit.py

    def check_txtedit_closed():
        if process.poll() is not None:  # poll() returns the exit code if the process has finished
            print("txtedit closed")
            root.deiconify() # reopens the main app
        else:
            root.after(100, check_txtedit_closed)  # Check again after 100 milliseconds

    check_txtedit_closed()

""" Creates a function to format the buttons in a grid """
def app_layout(target_row, target_col, text, app_open, app_image):
    if target_row and target_col and text and app_open and app_image:
        app_icon = CTkImage( # creates an image
            dark_image=Image.open(app_image),
            size=(100, 100) # sets image size
        )
        
        app_image_label = CTkLabel( # creates a label to hold the image
            root,
            image=app_icon,
            text="" # sets text to nothing so it doesn't disrupt the image
        )
        app_image_label.grid(row=target_row, column=target_col, padx=13.5, pady=7)
        
        app_name = CTkButton( # creates a button to open the app
            root,
            text=text,
            command=app_open
        )
        app_name.grid(row=target_row+1, column=target_col, padx=13.5, pady=7)

""" Creates a grid with the desired buttons """
for row in range(4): # 4 rows
    for col in range(2): # 2 columns
        app_layout(1, 1, "Calculator", launch_calc, "Calc/calc.png")
        app_layout(1, 2, "Hasher", launch_hasher, "Hasher/hasher.png")
        app_layout(3, 1, "Password Generator", launch_pwgen, "Password_Generator/pwgen.png")
        app_layout(3, 2, "Text Editor", launch_txtedit, "TextEditor/txtedit.png")

root.mainloop()
