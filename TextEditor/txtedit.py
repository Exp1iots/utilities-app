# imports required libraries
from customtkinter import *
from tkinter import *
from tkinter import messagebox # that should import with the first tkinter import (I don't know why it doesn't)
import os

""" Defines paramiters for the window """
txtedit = CTk() # Creates window
txtedit.geometry("1300x720") # Sets window size
txtedit.title("Text Editor") # Sets window title
txtedit.iconbitmap("TextEditor/txtedit.ico")  # Sets window icon

def new_file(event=None):
    if event:
        print(event)
    
    """ Asks the user if they want to create a new file """
    newFile_message = messagebox.askquestion("New File?",
"""Are you sure you want to start a new file?
This will delete any unsaved changes made to the current file."""
        )
    if newFile_message == "yes": # if yes was clicked
        textbox.delete("0.0", "end") # clears the textbox to make a new file
    else: # if no was click
        pass

def open_file(event=None):
    global file, fileObject
    if event:
        print(event)
    
    
    file = filedialog.askopenfilename() # opens a dialog menu to choose the file to open
    
    print(file)
    
    """ Checks if the file open dialog has been closed without a path to a file selected """
    if file != "": # if the dialog has closed with a path open the file
        fileObject = open(file, "r+") # opens the file to show the user
        print(fileObject)
        """ Finds the name of the file and changes to title accordinly """
        filePath = fileObject.name # gets the file path
        fileName = os.path.basename(filePath).split("/")[-1] # gets the file name from the file path
        txtedit.title(f"Text Editor: {fileName}")
        """ Adds content from file """
        textbox.delete("0.0", "end") # clears the textbox to display the new content
        textbox.insert("0.0", fileObject.read()) # adds the content from the file to the user
    else: # if the dialog has closed without a path exit the function to avoid error
        pass

def save_file(event=None):
    if event:
        print(event)
    
    filePath = ""
    
    try:
        editedContent = textbox.get("0.0", "end-1c") # gets all the content from the textbox
        filePath = fileObject.name  # Get the file path from the initially opened file
    
        with open(filePath, 'w') as file:
            file.write(editedContent) # writes content to the file
    except Exception as e:
        errorMessage(filePath=filePath) # displays an error message to the user

def saveFile_as(event=None):
    if event:
        print(event)
       
    filePath = ""   
    
    try:
        editedContent = textbox.get("0.0", "end-1c") # gets all the content from the textbox
    
        saveAs_dir = filedialog.asksaveasfile(
            defaultextension=".txt",
            filetypes=[
                ("Text file",".txt"),
                ("HTML file",".html"),
                ("All files",".*")
                ]
            )
        
        """ Finds the name of the file and changes to title accordinly """
        filePath = saveAs_dir.name # gets the file path
        fileName = os.path.basename(filePath).split("/")[-1] # gets the file name from the file path
        txtedit.title(f"Text Editor: {fileName}")
        
        saveAs_dir.write(editedContent) # writes content to the file
    except Exception as e:
        errorMessage(filePath=filePath) # displays an error message to the user

def errorMessage(filePath):
    messagebox.showerror("Save Error", f"An error occurred while saving file: {filePath}") # creates a message box to alart the user of an error

def wordWrap_word():
    textbox.configure(wrap=WORD)

def wordWrap_char():
    textbox.configure(wrap=CHAR)

def create_menu():
    """ Create Menu """
    mainMenu = Menu(txtedit)
    txtedit.config(menu=mainMenu)

    """ Create File Menu """
    file_menu = Menu(mainMenu, tearoff=0) # Create files menu item
    mainMenu.add_cascade(label="File", menu=file_menu) # Places the File menu in the main menu
    # Add File Menu Items
    file_menu.add_command(label="New         Ctrl + N", command=new_file)
    file_menu.add_command(label="Open       Ctrl + O", command=open_file)
    file_menu.add_command(label="Save         Ctrl + S", command=save_file)
    file_menu.add_command(label="Save As    Alt + S", command=saveFile_as)
    
    
    """ Create View Menu """
    view_menu = Menu(mainMenu, tearoff=0) # Creates view menu item
    mainMenu.add_cascade(label="View", menu=view_menu) # Places the view menu in the main menu
    # Create the Word Wrap submenu
    wordWrap_menu = Menu(view_menu, tearoff=0)
    view_menu.add_cascade(label="Word Wrap", menu=wordWrap_menu)
    # Add options to the Word Wrap submenu
    wordWrap_menu.add_command(label="Word", command=wordWrap_word)
    wordWrap_menu.add_command(label="Character", command=wordWrap_char)

create_menu()

""" Create a place to type/editor text """
textbox = CTkTextbox(txtedit, wrap=WORD)
textbox.pack(expand=TRUE, fill=BOTH)

""" Binds keys to functions """
txtedit.bind("<Control-n>", new_file) # Binds the key comboination Ctrl + N to the new file function
txtedit.bind("<Control-o>", open_file) # Binds the key comboination Ctrl + O to the open file function
txtedit.bind("<Control-s>", save_file) # Binds the key comboination Ctrl + S to the save file function
txtedit.bind("<Alt-s>", saveFile_as) # Binds the key comboination Alt + S to the save file as function (Ctrl + Shift + S didn't work)

txtedit.mainloop()