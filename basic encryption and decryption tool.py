import tkinter as tk
from tkinter import messagebox

# Encryption and Decryption functions (Vigenère Cipher)
def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(text, key):
    cipher_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i]) - ord('A') if text[i].isupper() else ord(key[i].lower()) - ord('a')
            base = ord('A') if text[i].isupper() else ord('a')
            cipher_text.append(chr((ord(text[i]) + shift - base) % 26 + base))
        else:
            cipher_text.append(text[i])
    return "".join(cipher_text)

def decrypt_vigenere(cipher_text, key):
    original_text = []
    key = generate_key(cipher_text, key)
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = ord(key[i]) - ord('A') if cipher_text[i].isupper() else ord(key[i].lower()) - ord('a')
            base = ord('A') if cipher_text[i].isupper() else ord('a')
            original_text.append(chr((ord(cipher_text[i]) - shift - base) % 26 + base))
        else:
            original_text.append(cipher_text[i])
    return "".join(original_text)

# GUI Setup
def process_text(action):
    text = text_entry.get("1.0", "end-1c")
    key = key_entry.get()
    if not text or not key:
        messagebox.showerror("Error", "Please enter both text and a key.")
        return
    if action == "encrypt":
        result = encrypt_vigenere(text, key)
    else:
        result = decrypt_vigenere(text, key)
    result_label.config(text=f"Result: {result}")

# Main window
root = tk.Tk()
root.title("Encryption and Decryption Tool")

# Text input
tk.Label(root, text="Enter Text:").pack(pady=5)
text_entry = tk.Text(root, height=5, width=40)
text_entry.pack(pady=5)

# Key input
tk.Label(root, text="Enter Key:").pack(pady=5)
key_entry = tk.Entry(root, width=20)
key_entry.pack(pady=5)

# Buttons for Encryption and Decryption
encrypt_button = tk.Button(root, text="Encrypt", command=lambda: process_text("encrypt"))
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=lambda: process_text("decrypt"))
decrypt_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result:", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
