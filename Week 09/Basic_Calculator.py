import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main Window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Display
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=8, height=3,
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=8, height=3,
                  command=lambda b=button: click(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear Button
tk.Button(root, text="C", width=35, height=2,
          command=clear).grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()