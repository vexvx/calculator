import tkinter as tk
from tkinter import font

# Function to update the display when a button is clicked
def button_click(number):
    current = display_var.get()
    display_var.set(current + number)

# Function to evaluate the expression
def calculate():
    expression = display_var.get()
    try:
        result = str(eval(expression))
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")
        print(f"Error: {e}")

# Function to clear the display
def clear_display():
    display_var.set("")

# Create the main window
root = tk.Tk()
root.title("Stylish Calculator")

# Configure fonts
large_font = font.Font(size=15)
button_font = font.Font(size=12, weight='bold')

# Configure colors
root.configure(bg='#f0f0f0')
button_bg = '#d9d9d9'
button_active_bg = '#bfbfbf'

# Create a display widget
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=large_font, bd=10, bg='#fff', justify='right')
display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

# Define buttons with text, row, column, width, height, and function
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("", 5, 1), ("", 5, 2), ("", 5, 3)
]

# Create buttons in a grid
for (text, row, column) in buttons:
    if text:
        if text == "=":
            button = tk.Button(root, text=text, font=button_font, width=5, height=2,
                               bg=button_bg, activebackground=button_active_bg,
                               command=calculate)
        elif text == "C":
            button = tk.Button(root, text=text, font=button_font, width=5, height=2,
                               bg=button_bg, activebackground=button_active_bg,
                               command=clear_display)
        else:
            button = tk.Button(root, text=text, font=button_font, width=5, height=2,
                               bg=button_bg, activebackground=button_active_bg,
                               command=lambda text=text: button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

# Additional styling
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()