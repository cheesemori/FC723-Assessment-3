for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack()
    for button in row:
        tk.Button(row_frame, text=button, font=("Arial", 16), command=lambda b=button: on_click(b)).pack(side='left', expand=True, fill='both', padx=5, pady=5)

root.mainloop()
