# Imports required libraires
from customtkinter import *
import hashlib

set_appearance_mode("Dark")


ERROR_RED = "#f7706a"
ICE_BLUE = "#dce4ee"

""" Defines paramiters for the window """
hasher = CTk() # Creates the window
hasher.geometry("400x300") # Sets window size
hasher.title("Hashing Tool") # Sets window title
hasher.resizable(False, False) # Makes the window non resizable
hasher.iconbitmap("Hasher/hasher.ico") # Sets window icon

""" Creates a function to hash the provided text """
def hash(event=None):
    if event: # fixes an issue where when the enter key is pressed it throws an error that complains about the funcion getting more paramters than expected
        print(event)
    """ Clears the textbox content show the new hash """
    hashed_value.configure(state=NORMAL, text_color=ICE_BLUE) # makes the textbox editable and sets the text colour
    hashed_value.delete("0.0", "end") # Clears the textbox
    hash_format = hashing_format_dropdown_box.get() # gets hashing formate chosen by user
    if hash_format == "Hashing Format":
        hashed_value.configure(text_color=ERROR_RED) # sets text colour to ERROR_RED to indicate an error message
        hashed_value.insert("0.0", "Please select a hashing format.") # displays an error message
    else:
        pass
    
    
    data = entry.get() # gets valie given by user
    hash_object = hashlib.new(hash_format) # performs hash
    hash_object.update(data.encode()) # performs hash
    
    hexdigest = hash_object.hexdigest() # convert hash to readable text
    
    """ Places the hashed value in the text box """
    hashed_value.insert("0.0", hexdigest) # Puts the hashed value in the textbox as character 0 and line 0
    hashed_value.configure(state=DISABLED) # makes the textbox read only

# Creates a Title Bar
title = CTkLabel(hasher, text="Hasher", font=("Arial", 30,))
title.pack(anchor=N, pady=3)

# Creates an entry widget for users to enter what they want to hash
entry = CTkEntry(hasher, placeholder_text="Enter here...")
entry.place(x=30, y=60)

# Creates a button to hash the provided text
button = CTkButton(hasher, text="Hash", command=hash)
button.place(x=30, y=90)

""" Creates a Textbox to display hashed value to user """
hashed_value = CTkTextbox(
    hasher,
    width=222,
    height=125,
    border_color="#FFFFFF",
    border_width=3,
    font=("Arial", 14)
)
hashed_value.configure(state=DISABLED) # makes the textbox read only
hashed_value.place(x=100, y=150)

# Creates a dropdown box to choose the hashing algorithm to use
hashing_format_dropdown_box = CTkOptionMenu(hasher, values=['blake2b', 'blake2s', 'sha1', 'sha224', 'sha384', 'sha512', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'md5'])
hashing_format_dropdown_box.set("Hashing Format")
hashing_format_dropdown_box.place(x=230, y=60)

# Binds the Enter key to the hash function
hasher.bind("<Return>", hash)

hasher.mainloop()