import tkinter as tk
import trigonometric_math as tm

# Create the main application window
main_window = tk.Tk()
main_window.geometry('400x600')

# Variable to store the input and display text
entry_var = tk.StringVar()

# Create an entry widget for the calculator screen
screen_entry = tk.Entry(main_window, textvariable=entry_var, bd=2, relief="ridge", font=("Arial", 20))
screen_entry.pack(fill="both", padx=5, pady=5)

# Configure the main window's column to expand
main_window.columnconfigure(0, weight=1)

# Define the buttons layout for the calculator
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", ".", "=", "/"],
    ["sin", "cos", "tan", "sqrt"],
    ["asin", "acos", "atan", "square"],
    ["DEL", "C"]
]

# Create a frame to hold the buttons
button_frame = tk.Frame(main_window)
button_frame.pack()

# List to keep track of the input history
text_lst = []

# Function to handle button clicks
def button_input(button_text):
    current_text = entry_var.get()
    if button_text in ["+", "-", "*", "/"]:
        # Append the operator to the current text
        entry_var.set(current_text + button_text)
        text_lst.append(current_text + button_text)
    elif button_text in ["sin", "cos", "tan", "sqrt", "asin", "acos", "atan", "square"]:
        # Perform trigonometric or mathematical operations
        num = float(current_text)
        if button_text == "sin":
            show_result(tm.cal_sin(num))
        elif button_text == "cos":
            show_result(tm.cal_cos(num))
        elif button_text == "tan":
            show_result(tm.cal_tan(num))
        elif button_text == "sqrt":
            show_result(num**0.5)
        elif button_text == "asin":
            show_result(tm.cal_asin(num))
        elif button_text == "acos":
            show_result(tm.cal_acos(num))
        elif button_text == "atan":
            show_result(tm.cal_atan(num))
        elif button_text == "square":
            show_result(num**2)
    elif button_text == "=":
        # Evaluate the expression and show the result
        show_result(str(eval(current_text)))
    elif button_text == "C":
        # Clear the entry
        entry_var.set("")
        show_result("")
    elif button_text == "DEL":
        # Delete the last character or operation
        if len(text_lst) == 1:
            entry_var.set("")
            return
        entry_var.set(text_lst[-2])
        text_lst.pop()
    else:
        # Append the number or decimal point to the current text
        entry_var.set(current_text + button_text)
        text_lst.append(current_text + button_text)

# Function to display the result in the entry widget
def show_result(result):
    entry_var.set(result)

# Create and pack the buttons in the button frame
for button_row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack()
    for button in button_row:
        tk.Button(row_frame, text=button, font=("Arial", 16), command=lambda b=button: button_input(b)).pack(side="left", fill="both", expand=True)

# Run the main application loop
if __name__ == '__main__':
    main_window.mainloop()