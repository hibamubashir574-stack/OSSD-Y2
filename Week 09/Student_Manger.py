import tkinter as tk
from tkinter import messagebox

# Add Student
def add_student():
    name = entry.get()

    if name == "":
        messagebox.showwarning("Warning", "Enter Student Name")
        return

    with open("students.txt", "a") as file:
        file.write(name + "\n")

    messagebox.showinfo("Success", "Student Added")
    entry.delete(0, tk.END)

# View Students
def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.read()

        if data == "":
            messagebox.showinfo("Students", "No Students Found")
        else:
            messagebox.showinfo("Student List", data)

    except FileNotFoundError:
        messagebox.showerror("Error", "File Not Found")

# Delete Student
def delete_student():
    name = entry.get()

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        found = False

        with open("students.txt", "w") as file:
            for student in students:
                if student.strip() != name:
                    file.write(student)
                else:
                    found = True

        if found:
            messagebox.showinfo("Success", "Student Deleted")
        else:
            messagebox.showwarning("Not Found", "Student Not Found")

        entry.delete(0, tk.END)

    except FileNotFoundError:
        messagebox.showerror("Error", "File Not Found")

# Clear Entry
def clear_entry():
    entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("Student Manager")
root.geometry("350x300")

# Heading
tk.Label(root,
         text="Student Manager System",
         font=("Arial", 14, "bold")).pack(pady=10)

# Input
tk.Label(root, text="Student Name").pack()

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Buttons
tk.Button(root,
          text="Add Student",
          width=20,
          command=add_student).pack(pady=5)

tk.Button(root,
          text="View Students",
          width=20,
          command=view_students).pack(pady=5)

tk.Button(root,
          text="Delete Student",
          width=20,
          command=delete_student).pack(pady=5)

tk.Button(root,
          text="Clear",
          width=20,
          command=clear_entry).pack(pady=5)

tk.Button(root,
          text="Exit",
          width=20,
          command=root.destroy).pack(pady=5)

root.mainloop()