# imports required libraries
from customtkinter import *
import string
import random

set_appearance_mode("Dark")

# Creates a character list
characterList = ""

# Stores the amount of checkboxes are ticked
checkboxes = 3

ERROR_RED = "#f7706a"
ICE_BLUE = "#dce4ee"

# Fills the character list with letters, numbers, and symbols
characterList += string.ascii_letters # letters
characterList += string.digits # numbers
characterList += string.punctuation # symbols
    
""" Defines paramiters for the window """
pwgen = CTk() # Creates windwo
pwgen.geometry("250") # Sets window size
pwgen.title("Password Generator") # Sets window title
pwgen.resizable(False, False) # Makes the window non reslizable
pwgen.iconbitmap("Password_Generator/pwgen.ico") # Sets window icon

""" Creates functions to add each setting to the character list"""
def letters_add():
    global characterList
    characterList += string.ascii_letters
def numbers_add():
    global characterList
    characterList += string.digits
def symbols_add():
    global characterList
    characterList += string.punctuation

""" Creates function to remove each setting from the character list """
def letters_remove():
    global characterList
    # Convert the string to a list to allow item removal
    character_list_as_list = list(characterList)

    # Create a new list containing only the non-ASCII letters
    filtered_list = [char for char in character_list_as_list if char not in string.ascii_letters]

    # Convert the filtered list back to a string
    characterList = "".join(filtered_list)
def numbers_remove():
    global characterList
    # Convert the string to a list to allow item removal
    character_list_as_list = list(characterList)

    # Create a new list containing only the non-ASCII letters
    filtered_list = [char for char in character_list_as_list if char not in string.digits]

    # Convert the filtered list back to a string
    characterList = "".join(filtered_list)
def symbols_remove():
    global characterList
    # Convert the string to a list to allow item removal
    character_list_as_list = list(characterList)

    # Create a new list containing only the non-ASCII letters
    filtered_list = [char for char in character_list_as_list if char not in string.punctuation]

    # Convert the filtered list back to a string
    characterList = "".join(filtered_list)

""" Creates a function to check weather the Checkbox is check or not when toggled """
def letters_check():
    global checkboxes
    if letters.get() == 1: # checks if letters settings in not checked
        letters_add()
        checkboxes = checkboxes + 1 # adds 1 to checkboxes variable to store the amount of checkboxes ticked
    elif letters.get() == 0: # checks if letters settings in checked     
        letters_remove()
        checkboxes = checkboxes - 1 # removes 1 to checkboxes variable to store the amount of checkboxes ticked
        
    print(checkboxes)
def numbers_check():
    global checkboxes
    if numbers.get() == 1: # checks if numbers settings in not checked
        numbers_add()
        checkboxes = checkboxes + 1 # adds 1 to checkboxes variable to store the amount of checkboxes ticked
    elif numbers.get() == 0: # checks if numbers settings in checked
        numbers_remove()
        checkboxes = checkboxes - 1 # removes 1 to checkboxes variable to store the amount of checkboxes ticked
    print(checkboxes)
def symbols_check():
    global checkboxes
    if symbols.get() == 1: # checks if symbols settings in not checked
        symbols_add()
        checkboxes = checkboxes + 1 # adds 1 to checkboxes variable to store the amount of checkboxes ticked
    elif symbols.get() == 0: # checks if symbols settings in checked
        symbols_remove()
        checkboxes = checkboxes - 1 # removes 1 to checkboxes variable to store the amount of checkboxes ticked
    print(checkboxes)

""" Creates a function to generate a password """
def password_generator(event=None):
    global final_password
    if event: # fixes an issue where when the enter key is pressed it throws an error that complains about the funcion getting more paramters than expected
        print(event)
    """ Clears the textbox content show the new password """
    password_display.configure(state=NORMAL, text_color=ICE_BLUE) # makes the textbox editable and sets the text colour
    password_display.delete("0.0", "end") # Clears the textbox
    
    """ If statement to check weather there are any checkboxes ticked """
    if checkboxes == 0: # If no checkboxes are ticked it tells the user to tick atleast one
        password_display.configure(text_color=ERROR_RED)
        password_display.insert("0.0", "Please tick at least one Check Box")
    else: # If checkboxes are tick continue with password creation
        password = [] # clears the old password before making a new one so they don't combind
        length = int(password_length.get()) # gets the password length from the slider
        for i in range(length):
            randomchar = random.choice(characterList) # Picking a random character from the character list
            password.append(randomchar) # appending a random character to password
            final_password = "".join(password)
            
        """ Places the password in the text box """
        password_display.insert("0.0", final_password) # Puts the hashed value in the textbox as character 0 and line 0
        password_display.configure(state=DISABLED) # makes the textbox read only

""" Creates a function to set the textbox to the value of the slider """
def display_password_length(value):
    value_rounded = round(value)
    password_length_textBox.configure(state=NORMAL)
    password_length_textBox.delete("0.0", "end") # Clears the textbox
    password_length_textBox.insert("0.0", value_rounded) # Inserts the slider value
    password_length_textBox.insert("0.1", "Characters: ") # Inserts "Characters: " at the start
    password_length_textBox.configure(state=DISABLED)

""" Creates a function to increase the slider value of the password length """
def increaseSlider_value(value):
    global password_length
    print(value) # fixes an issue where when the enter key is pressed it throws an error that complains about the funcion getting more paramters than expected
    length = password_length.get() # Gets the password slider length and assigns it to a variable
    password_length.set(length + 1) # Increases the password length slider by 1
    display_password_length(password_length.get()) # Calls the display_password_length function to display the current password length

""" Creates a function to decrease the slider value of the password length """
def decreaseSlider_value(value):
    global password_length
    print(value) # fixes an issue where when the enter key is pressed it throws an error that complains about the funcion getting more paramters than expected
    length = password_length.get() # Gets the password slider length and assigns it to a variable
    password_length.set(length - 1) # Decreases the password length slider by 1
    display_password_length(password_length.get()) # Calls the display_password_length function to display the current password length

# Creates a Title Bar
title = CTkLabel(pwgen, text="Password Generator", font=("Arial", 30,))
title.pack(anchor=N, pady=3)

# Creates a frame to hold the generated password
password_area = CTkFrame(pwgen, height=65)
password_area.pack(anchor=N, fill=X)

# Creates a label to display the password
password_display = CTkTextbox(password_area, height=65)
password_display.configure(state=DISABLED, corner_radius=0)
password_display.pack(anchor=N, fill=X)

# Create a frame for the settings
settings_frame = CTkFrame(pwgen, fg_color="#242424")
settings_frame.pack(fill="both", expand=True, pady=3)

# Configure grid layout for the frame
settings_frame.grid_columnconfigure(0, weight=1)
settings_frame.grid_columnconfigure(1, weight=1)

""" Creates check boxes for letters, numbers, and symbols """
letters = CTkCheckBox(settings_frame, text="Letters", command=letters_check)
letters.select() # ticks the check box
letters.grid(row=0, column=0, padx=10, pady=1, sticky="w")
numbers = CTkCheckBox(settings_frame, text="Numbers", command=numbers_check)
numbers.select() # ticks the check box
numbers.grid(row=1, column=0, padx=10, pady=1, sticky="w")
symbols = CTkCheckBox(settings_frame, text="Symbols", command=symbols_check)
symbols.select() # ticks the check box
symbols.grid(row=2, column=0, padx=10, pady=2, sticky="w")

# Creates a button to generate a password
generate = CTkButton(settings_frame, text="Generate Password", command=password_generator)
generate.grid(row=0, column=1, padx=10, pady=1, sticky=E) # Using 'E' to align to right of cell

# Creates a textbox to display the password length
password_length_textBox = CTkTextbox(settings_frame, height=20, width=110)
password_length_textBox.grid(row=1, column=1, padx=10, pady=2, sticky=E) # Using 'E' to align to right of cell

# Creates a slider to choose the password length
password_length = CTkSlider(settings_frame, from_=1, to=100, number_of_steps=99, command=display_password_length, width=300)
password_length.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew") # columnspan to span both columns
password_length.set(20)
display_password_length(password_length.get()) # Calls the display_password_length function to display the current password length

""" Binds keys to functions """
pwgen.bind("<Return>", password_generator) # Binds the Enter key to the password generator function
pwgen.bind("<Right>", increaseSlider_value) # Binds the Right Arrow key to the increase slider function
pwgen.bind("<Left>", decreaseSlider_value) # Binds the Left Arrow key to the decrease slider function

pwgen.mainloop()