import tkinter as tk
from tkinter import messagebox

current_user = ""

# ------------------ Utility ------------------

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# ------------------ Sign Up ------------------

def save_credentials():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == "" or pwd == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    with open("credentials.txt", "a") as f:
        f.write(f"{user},{pwd}\n")

    messagebox.showinfo("Success", "Account Created!")
    show_signin()

def show_signup():
    clear_window()

    global username_entry, password_entry

    tk.Label(root, text="Sign Up", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Create Account",
              command=save_credentials).pack(pady=10)

    tk.Button(root, text="Back",
              command=show_home).pack()

# ------------------ Sign In ------------------

def check_credentials():
    global current_user

    user = username_entry.get()
    pwd = password_entry.get()

    try:
        with open("credentials.txt", "r") as f:
            for line in f:
                saved_user, saved_pwd = line.strip().split(",")

                if user == saved_user and pwd == saved_pwd:
                    current_user = user
                    show_menu()
                    return

        messagebox.showerror("Error", "Invalid Credentials")

    except FileNotFoundError:
        messagebox.showerror("Error", "No Users Found")

def show_signin():
    clear_window()

    global username_entry, password_entry

    tk.Label(root, text="Sign In", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Login",
              command=check_credentials).pack(pady=10)

    tk.Button(root, text="Back",
              command=show_home).pack()

# ------------------ Menu ------------------

def dummy1():
    messagebox.showinfo("Button 1", "Dummy Button 1")

def dummy2():
    messagebox.showinfo("Button 2", "Dummy Button 2")

def sign_out():
    global current_user
    current_user = ""
    show_home()

def show_menu():
    clear_window()

    tk.Label(
        root,
        text=f"Welcome, {current_user}",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    tk.Button(root,
              text="Dummy Button 1",
              command=dummy1,
              width=20).pack(pady=5)

    tk.Button(root,
              text="Dummy Button 2",
              command=dummy2,
              width=20).pack(pady=5)

    tk.Button(root,
              text="Sign Out",
              command=sign_out,
              width=20).pack(pady=15)

# ------------------ Home Screen ------------------

def show_home():
    clear_window()

    tk.Label(root,
             text="Welcome",
             font=("Arial", 18, "bold")).pack(pady=20)

    tk.Button(root,
              text="Sign In",
              command=show_signin,
              width=20).pack(pady=5)

    tk.Button(root,
              text="Sign Up",
              command=show_signup,
              width=20).pack(pady=5)

# ------------------ Main ------------------

root = tk.Tk()
root.title("Login System")
root.geometry("350x300")

show_home()

root.mainloop()