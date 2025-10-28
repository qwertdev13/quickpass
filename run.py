import tkinter as tk
import random

def generate_password():
    try:
        length = int(entry.get())
        if length < 1:
            output_entry.config(state='normal')
            output_entry.delete(0, tk.END)
            output_entry.insert(0, "You cannot enter 0, please try again")
            output_entry.config(state='readonly')
        else:
            char = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()[]{}~-_?"
            if length > len(char):
                output_entry.config(state='normal')
                output_entry.delete(0, tk.END)
                output_entry.insert(0, "Length too long, max is {}".format(len(char)))
                output_entry.config(state='readonly')
            else:
                password = "".join(random.sample(char, length))
                output_entry.config(state='normal')
                output_entry.delete(0, tk.END)
                output_entry.insert(0, password)
                output_entry.config(state='readonly')
    except ValueError:
        output_entry.config(state='normal')
        output_entry.delete(0, tk.END)
        output_entry.insert(0, "Please enter a valid integer")
        output_entry.config(state='readonly')

root = tk.Tk()
root.title("Simple Password Gen")
root.geometry("500x200")
root.iconbitmap('./as.ico')               # Set window icon


tk.Label(root, text="Password Length:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generate", command=generate_password).pack(pady=5)

output_entry = tk.Entry(root, state="readonly", width=50)
output_entry.pack(pady=10)

root.mainloop()
