import tkinter as tk


main_window = tk.Tk()
main_window.geometry('400x600')
entry_var = tk.StringVar()
label_var = tk.StringVar()
screen_entry = tk.Entry(main_window,textvariable=entry_var,bd=2,relief="ridge",font=("Arial", 20))
screen_entry.pack(fill="both",padx=5,pady=5)
main_window.columnconfigure(0, weight=1)

buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", ".", "=", "/"],
    ["sin", "cos", "tan", "sqrt"],
    ["asin", "acos", "atan", "square"],
    ["DEL","C"]
]

button_frame = tk.Frame(main_window)
button_frame.pack()

text_lst = []

def button_input(button_text):
    current_text = entry_var.get()
    if button_text in ["sin","cos","tan","sqrt","asin","acos","atan","square"]:
        num = float(current_text)
        if button_text == "sin":
            pass
        elif button_text == "cos":
            pass
        elif button_text == "tan":
            pass
        elif button_text == "sqrt":
            show_result(num**0.5)
        elif button_text == "asin":
            pass
        elif button_text == "acos":
            pass
        elif button_text == "atan":
            pass
        elif button_text == "square":
            show_result(num**2)
    elif button_text == "=":
        show_result(entry_var.get())
    elif button_text == "C":
        entry_var.set("")
        show_result("")
    elif button_text == "DEL":
        if len(text_lst) == 1:
            entry_var.set("")
            return
        entry_var.set(text_lst[-2])
        text_lst.pop()

    else:
        entry_var.set(current_text+button_text)
        text_lst.append(current_text+button_text)



def show_result(result):
    label_var.set(f"{result}")

for button_row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack()
    for button in button_row:
        tk.Button(row_frame,text=button,font=("Arial", 16),command=lambda b=button:button_input(b)).pack(side="left",fill="both",expand=True)

result_label = tk.Label(main_window,font=("Arial", 16),bd=2, relief="ridge",textvariable=label_var).pack()
if __name__ == '__main__':
    main_window.mainloop()