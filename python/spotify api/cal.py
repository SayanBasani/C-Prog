import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("600x600")
root.resizable(0, 0)

# Create the entry widget for displaying the input/output
entry = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Global variable to store the current expression
expression = ""

# Define functions for calculator operations
def button_click(number):
    global expression
    expression += str(number)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def button_clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

def button_delete():
    global expression
    expression = expression[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def button_equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

def button_function(func):
    global expression
    try:
        result = str(eval(f"{func}({expression})"))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Define button functions for trigonometric and other math functions
def button_sin(): button_function("math.sin")
def button_cos(): button_function("math.cos")
def button_tan(): button_function("math.tan")
def button_log(): button_function("math.log10")
def button_ln(): button_function("math.log")
def button_sqrt(): button_function("math.sqrt")
def button_exp(): button_function("math.exp")
def button_pi(): button_click(math.pi)
def button_e(): button_click(math.e)
def button_deg(): button_function("math.degrees")
def button_rad(): button_function("math.radians")

# Define the layout of buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('Del', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('=', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('(', 4, 3), (')', 4, 4),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3), ('ln', 5, 4),
    ('sqrt', 6, 0), ('exp', 6, 1), ('pi', 6, 2), ('e', 6, 3), ('^', 6, 4),
    ('deg', 7, 0), ('rad', 7, 1)
]

# Create and place buttons in the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_equal, bg='lightblue')
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_clear, bg='lightcoral')
    elif text == 'Del':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_delete, bg='lightyellow')
    elif text == 'sin':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_sin, bg='lightgreen')
    elif text == 'cos':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_cos, bg='lightgreen')
    elif text == 'tan':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_tan, bg='lightgreen')
    elif text == 'log':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_log, bg='lightgreen')
    elif text == 'ln':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_ln, bg='lightgreen')
    elif text == 'sqrt':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_sqrt, bg='lightgreen')
    elif text == 'exp':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_exp, bg='lightgreen')
    elif text == 'pi':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_pi, bg='lightgreen')
    elif text == 'e':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_e, bg='lightgreen')
    elif text == 'deg':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_deg, bg='lightgreen')
    elif text == 'rad':
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_rad, bg='lightgreen')
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda text=text: button_click(text))
    
    button.grid(row=row, column=col, sticky="nsew")

# Make the buttons resize with the window
for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

# Start the main event loop
root.mainloop()