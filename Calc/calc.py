# imports required libraries
from tkinter import *
from customtkinter import *

""" Formating Variables """
# Default Colours
WHITE = "#FFFFFF"
TURQUOISE = "#1e7887"
PURPLE_BLUE = "#456cce"
INIDGO = "#3c339a"
LIGHT_BLUE = "#4192e8"
LIGHT_GREY = "#eeeeee"
GREY = "#2b2b2b"

# Font Styles
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 20, "bold")
DIGIT_FONT_STYLE = ("Arial", 26, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

# Button Styles
BORDER = 0

# creates a class called Calculator
class Calculator:
    def __init__(self):
        self.calc = CTk() # creates the calc
        self.calc.geometry("260x450") # sets calc size (in px)
        self.calc.resizable(False,False) # make the calc not resizable
        self.calc.title("Calculator") # sets the calc title
        self.calc.iconbitmap("Calc/calc.ico") # sets the calc icon

        print (self.calc)
        # Creates variables for the equations to be stored
        self.total_expression = "" # total expression is the previously typed part of an equation
        self.current_expression = "" # current expression is the current equation text as you type this will update
        
        # Assigns the display frame and it's labels
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
                
        # Creates a dictionary to store the location values of each digit
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,1), ".":(4,2)
        }
                
        self.operations = {
            "/":"\u00F7", "*":"\u00D7",
            "-":"-", "+":"+"
        }
        
        # Assigns the buttons frame
        self.buttons_frame = self.create_buttons_frame()
        
        # Makes the buttons fill there frame
        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)
        
        # Runs the functions to create the buttons
        self.create_digit_butons()
        self.create_operator_buttons()
        self.bind_keys()
        self.create_clear_button()
        self.create_clear_all_button()
        self.create_equals_button()
        self.create_backspace_button()
        
    """ creates a function to bind keyboard keys to calcualtor buttons """
    def bind_keys(self):
        self.calc.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.calc.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
            
        for key in self.operations:
            self.calc.bind(key, lambda event, operator=key: self.append_operator(operator))
        
        self.calc.bind("<BackSpace>", self.backspace)
            
        
    """ Creates a function to create the display labels """
    def create_display_labels(self):
        """ Creates label for the total expression """
        total_label = Label(
                    self.display_frame,
                    text=self.total_expression,
                    anchor=E,
                    bg=GREY,
                    fg=WHITE,
                    padx=24,
                    font=SMALL_FONT_STYLE
                    )
        total_label.pack(expand=True, fill="both")
        
        """ Creates a label for the current expression """
        label = Label(
                    self.display_frame,
                    text=self.current_expression,
                    anchor=E,
                    bg=GREY,
                    fg=WHITE,
                    padx=24,
                    font=LARGE_FONT_STYLE
                    )
        label.pack(expand=True, fill="both")
            
        return total_label, label
    
    """ Creates a function for frame of the display """
    def create_display_frame(self):
        frame = CTkFrame(self.calc, height=22)
        frame.pack(expand=True, fill="both")
        return frame
    
    """ Creates a function to add value to the current expression """
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    
    """ Creates a function to create the digit buttons """
    def create_digit_butons(self):
        for digit, grid_value in self.digits.items():
            button = CTkButton(
                self.buttons_frame,
                text=str(digit),
                fg_color=PURPLE_BLUE,
                text_color=LIGHT_GREY,
                border_spacing=BORDER,
                font=DIGIT_FONT_STYLE,
                command=lambda x=digit:self.add_to_expression(x)
            )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW, padx=1, pady=1)
    
    """ Creates a function to append the operators to make sure they are placed and movied correctly """
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()
    
    """ Creates a function to create the operator buttons """
    def create_operator_buttons(self):
        i = 0
        for operator,symbol in self.operations.items():
            button = CTkButton(
                            self.buttons_frame,
                            text=symbol,
                            fg_color=INIDGO,
                            text_color=LIGHT_GREY,
                            border_spacing=BORDER,
                            font=DEFAULT_FONT_STYLE,
                            command=lambda x=operator:self.append_operator(x)
                            )
            button.grid(row=i, column=4, sticky=NSEW, padx=1, pady=1)
            i += 1
    
    """ Creates a function to clear the current and total expressions """
    def clear_all(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()
    
    """ Creates a function to clear the current expression """
    def clear(self):
        self.current_expression = ""
        self.update_label()
    
    """ Creates a function to delete the most reacent character in the current expression """
    def backspace(self, event=None):
        if event:
            print(event)
        
        self.current_expression = self.current_expression[:-1]
        self.update_label()
    
    """ Creates a function to create the clear button """
    def create_clear_all_button(self):
            button = CTkButton(
                            self.buttons_frame,
                            text="C",
                            fg_color=TURQUOISE,
                            text_color=LIGHT_GREY,
                            border_spacing=BORDER,
                            font=DEFAULT_FONT_STYLE,
                            command=self.clear_all
                            )
            button.grid(row=0, column=2, sticky=NSEW, padx=1, pady=2)
    
    """ Creates a function to create the clear button """
    def create_clear_button(self):
            button = CTkButton(
                            self.buttons_frame,
                            text="CE",
                            fg_color=TURQUOISE,
                            text_color=LIGHT_GREY,
                            border_spacing=BORDER,
                            font=DEFAULT_FONT_STYLE,
                            command=self.clear
                            )
            button.grid(row=0, column=1, sticky=NSEW, padx=1, pady=2)
    
    """ Creates a function to create the backspace button """
    def create_backspace_button(self):
            button = CTkButton(
                            self.buttons_frame,
                            text="⌦",
                            fg_color=TURQUOISE,
                            text_color=LIGHT_GREY,
                            border_spacing=BORDER,
                            font=DEFAULT_FONT_STYLE,
                            command=self.backspace
                            )
            button.grid(row=0, column=3, sticky=NSEW, padx=1, pady=2)
    
    """ Creates a function to evaluate the expressions """
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        
        self.current_expression = str(eval(self.total_expression))
        
        self.total_expression = ""
        self.update_label()
           
    """ Creates a function to create the equals button """
    def create_equals_button(self):
            button = CTkButton(
                            self.buttons_frame,
                            text="=",
                            fg_color=LIGHT_BLUE,
                            text_color=LIGHT_GREY,
                            border_spacing=BORDER,
                            font=DEFAULT_FONT_STYLE,
                            command=self.evaluate
                            )
            button.grid(row=4, column=3, columnspan=2, sticky=NSEW, padx=1, pady=1)
    
    """ Creates a function for frame of the buttons """
    def create_buttons_frame(self):
        frame = CTkFrame(self.calc)
        frame.pack(expand=True, fill="both")
        return frame
    
    """ Creates a function to update the total label with the value of total expression """
    def update_total_label(self):
        self.total_label.config(text=self.total_expression)
    
    """ Creates a function to update the label with the value of current expression """
    def update_label(self):
        self.label.config(text=self.current_expression)
    
    """ Creates a function to run the Calculator """
    def run(self):
        self.calc.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()