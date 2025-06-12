import tkinter as tk
from tkinter import messagebox
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift_val = shift if mode == "encrypt" else -shift
            result += chr((ord(char) - base + shift_val) % 26 + base)
        else:
            result += char
    return result
def process():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")
        return

    mode = var_mode.get()
    output = caesar_cipher(text, shift, mode)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, output)
root = tk.Tk()
root.title("Caesar Cipher")
tk.Label(root, text="Message:").grid(row=0, column=0)
entry_text = tk.Entry(root, width=50)
entry_text.grid(row=0, column=1)
tk.Label(root, text="Shift:").grid(row=1, column=0)
entry_shift = tk.Entry(root, width=10)
entry_shift.grid(row=1, column=1, sticky="w")
var_mode = tk.StringVar(value="encrypt")
tk.Radiobutton(root, text="Encrypt", variable=var_mode, value="encrypt").grid(row=2, column=0)
tk.Radiobutton(root, text="Decrypt", variable=var_mode, value="decrypt").grid(row=2, column=1, sticky="w")
tk.Button(root, text="Process", command=process).grid(row=3, column=0, columnspan=2)
tk.Label(root, text="Result:").grid(row=4, column=0)
entry_result = tk.Entry(root, width=50)
entry_result.grid(row=4, column=1)
root.mainloop()
