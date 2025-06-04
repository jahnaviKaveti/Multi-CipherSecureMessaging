import tkinter as tk
from caesar import *
from vigenere import *
from playfair import *
from transposition import *

def process():
    text = entry_text.get()
    key = entry_key.get()
    method = cipher_var.get()
    mode = mode_var.get()
    
    if method == "Caesar":
        shift = int(key)
        output = caesar_encrypt(text, shift) if mode == "Encrypt" else caesar_decrypt(text, shift)
    elif method == "Vigenere":
        output = vigenere_encrypt(text, key) if mode == "Encrypt" else vigenere_decrypt(text, key)
    elif method == "Playfair":
        output = playfair_encrypt(text, key) if mode == "Encrypt" else playfair_decrypt(text, key)
    elif method == "Transposition":
        output = transposition_encrypt(text, int(key)) if mode == "Encrypt" else transposition_decrypt(text, int(key))
    
    result_label.config(text=f"Result: {output}")

root = tk.Tk()
root.title("Multi-Cipher Secure Messaging")

tk.Label(root, text="Text:").grid(row=0, column=0)
entry_text = tk.Entry(root, width=50)
entry_text.grid(row=0, column=1)

tk.Label(root, text="Key:").grid(row=1, column=0)
entry_key = tk.Entry(root, width=50)
entry_key.grid(row=1, column=1)

cipher_var = tk.StringVar(value="Caesar")
tk.OptionMenu(root, cipher_var, "Caesar", "Vigenere", "Playfair", "Transposition").grid(row=2, column=1)

mode_var = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt").grid(row=3, column=0)
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt").grid(row=3, column=1)

tk.Button(root, text="Process", command=process).grid(row=4, column=1)
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()