import tkinter as tk
import math

# Create a variable to track the current calculator mode
basic_mode = True

def toggle_scientific_mode():
    global basic_mode
    basic_mode = not basic_mode
    if basic_mode:
        sin_button.grid_remove()
        cos_button.grid_remove()
        tan_button.grid_remove()
        log_button.grid_remove()
        exp_button.grid_remove()
        left_parenthesis_button.grid_remove()
        right_parenthesis_button.grid_remove()
        toggle_mode_button.config(text="Scientific Mode")
    else:
        sin_button.grid(row=1, column=6, sticky="nsew")
        cos_button.grid(row=2, column=6, sticky="nsew")
        tan_button.grid(row=3, column=6, sticky="nsew")
        log_button.grid(row=4, column=6, sticky="nsew")
        exp_button.grid(row=5, column=6, sticky="nsew")
        left_parenthesis_button.grid(row=4, column=5, sticky="nsew")
        right_parenthesis_button.grid(row=5, column=5, sticky="nsew")
        toggle_mode_button.config(text="Basic Mode")

def on_digit_click(digit):
    current_text = display_var.get()
    if current_text == "Error":
        clear_display()
        current_text = ""
    new_text = current_text + str(digit)
    display_var.set(new_text)

def on_operator_click(operator):
    current_text = display_var.get()
    if current_text and current_text[-1] not in '+-*/':
        new_text = current_text + operator
        display_var.set(new_text)

def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")
        print(e)

def clear_display():
    display_var.set("")

def add_decimal():
    current_text = display_var.get()
    if "." not in current_text:
        new_text = current_text + "."
        display_var.set(new_text)

def backspace():
    current_text = display_var.get()
    new_text = current_text[:-1]
    display_var.set(new_text)

def memory_store():
    memory_var.set(display_var.get())

def memory_recall():
    display_var.set(memory_var.get())

def memory_clear():
    memory_var.set("")

def calculate_square_root():
    current_text = display_var.get()
    try:
        result = math.sqrt(float(current_text))
        display_var.set(result)
    except ValueError:
        display_var.set("Error")

def calculate_percentage():
    current_text = display_var.get()
    try:
        result = eval(current_text) / 100
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")
        print(e)

def calculate_sin():
    current_text = display_var.get()
    try:
        result = math.sin(float(current_text))
        display_var.set(result)
    except ValueError:
        display_var.set("Error")

def calculate_cos():
    current_text = display_var.get()
    try:
        result = math.cos(float(current_text))
        display_var.set(result)
    except ValueError:
        display_var.set("Error")

def calculate_tan():
    current_text = display_var.get()
    try:
        result = math.tan(float(current_text))
        display_var.set(result)
    except ValueError:
        display_var.set("Error")

def calculate_log():
    current_text = display_var.get()
    try:
        result = math.log(float(current_text))
        display_var.set(result)
    except ValueError:
        display_var.set("Error")

def calculate_exp():
    current_text = display_var.get()
    try:
        result = math.exp(float(current_text))
        display_var.set(result)
    except ValueError:
        display_var.set("Error")

# Create the main window
window = tk.Tk()
window.title("Advanced Calculator")
window.minsize(400, 500)

# Configure rows and columns for responsiveness
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Create a display label
display_var = tk.StringVar()
display_label = tk.Label(window, textvariable=display_var, font=("Arial", 24), anchor="e")
display_label.grid(row=0, column=0, columnspan=6, sticky="nsew")

# Create digit buttons
for i in range(1, 10):
    row = (9 - i) // 3 + 1
    col = (i - 1) % 3
    digit_button = tk.Button(window, text=str(i), command=lambda i=i: on_digit_click(i), font=("Arial", 18))
    digit_button.grid(row=row, column=col, sticky="nsew")

# Other buttons
zero_button = tk.Button(window, text="0", command=lambda: on_digit_click(0), font=("Arial", 18))
zero_button.grid(row=4, column=1, sticky="nsew")

decimal_button = tk.Button(window, text=".", command=add_decimal, font=("Arial", 18))
decimal_button.grid(row=4, column=2, sticky="nsew")

clear_button = tk.Button(window, text="C", command=clear_display, font=("Arial", 18))
clear_button.grid(row=1, column=3, sticky="nsew")

backspace_button = tk.Button(window, text="←", command=backspace, font=("Arial", 18))
backspace_button.grid(row=2, column=3, sticky="nsew")

equal_button = tk.Button(window, text="=", command=calculate_result, font=("Arial", 18))
equal_button.grid(row=3, column=3, rowspan=2, sticky="nsew")

operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    operator_button = tk.Button(window, text=operator, command=lambda operator=operator: on_operator_click(operator), font=("Arial", 18))
    operator_button.grid(row=i+1, column=4, sticky="nsew")

# Memory buttons
memory_var = tk.StringVar()
memory_label = tk.Label(window, textvariable=memory_var, font=("Arial", 18), anchor="e")
memory_label.grid(row=0, column=5, sticky="nsew")

memory_store_button = tk.Button(window, text="M+", command=memory_store, font=("Arial", 18))
memory_store_button.grid(row=1, column=5, sticky="nsew")

memory_recall_button = tk.Button(window, text="MR", command=memory_recall, font=("Arial", 18))
memory_recall_button.grid(row=2, column=5, sticky="nsew")

memory_clear_button = tk.Button(window, text="MC", command=memory_clear, font=("Arial", 18))
memory_clear_button.grid(row=3, column=5, sticky="nsew")

# Square root and percentage buttons
sqrt_button = tk.Button(window, text="√", command=calculate_square_root, font=("Arial", 18))
sqrt_button.grid(row=4, column=4, sticky="nsew")

percent_button = tk.Button(window, text="%", command=calculate_percentage, font=("Arial", 18))
percent_button.grid(row=4, column=5, sticky="nsew")

# Scientific mode toggle button
toggle_mode_button = tk.Button(window, text="Scientific Mode", command=toggle_scientific_mode, font=("Arial", 14))
toggle_mode_button.grid(row=0, column=6, columnspan=2, sticky="nsew")

# Scientific buttons
sin_button = tk.Button(window, text="sin", command=calculate_sin, font=("Arial", 18))
cos_button = tk.Button(window, text="cos", command=calculate_cos, font=("Arial", 18))
tan_button = tk.Button(window, text="tan", command=calculate_tan, font=("Arial", 18))
log_button = tk.Button(window, text="log", command=calculate_log, font=("Arial", 18))
exp_button = tk.Button(window, text="exp", command=calculate_exp, font=("Arial", 18))

# Parentheses buttons
left_parenthesis_button = tk.Button(window, text="(", command=lambda: on_digit_click("("), font=("Arial", 18))
right_parenthesis_button = tk.Button(window, text=")", command=lambda: on_digit_click(")"), font=("Arial", 18))

# Initially hide scientific buttons
if basic_mode:
    sin_button.grid_remove()
    cos_button.grid_remove()
    tan_button.grid_remove()
    log_button.grid_remove()
    exp_button.grid_remove()
    left_parenthesis_button.grid_remove()
    right_parenthesis_button.grid_remove()

# Run the GUI loop
window.mainloop()
