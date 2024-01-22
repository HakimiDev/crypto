import tkinter as tk
from tkinter import ttk
import src.ciphers.ciphers as ciphers

# Function to handle the encryption process
ciphertext = ''

def process_text():
    plaintext = plaintext_entry.get().strip()
    algorithm = algorithm_var.get()

    if algorithm == "Caesar":
        key = int(key_entry.get())
        if not encrypt_var.get():
            key = -key
        ciphertext = ciphers.caesarCipher(plaintext, key)
    elif algorithm == "Affine":
        key_a = int(key_a_entry.get())
        key_b = int(key_b_entry.get())
        try:
            ciphertext = ciphers.affineCipher(plaintext, key_a, key_b, not encrypt_var.get())
        except:
            result_label.configure(text="Key A is not a prime number", foreground="#FF0000")
            return
    else:
        result_label.configure(text="Invalid algorithm selected.")
        return

    result_label.configure(text="Result: " + ciphertext)


# Create a Tkinter window
root = tk.Tk()
root.title("Text Encryption")
root.geometry("400x400")
root.configure(bg="#f2f2f2")
root.resizable(False, False)
style = ttk.Style(root)
style.configure("TLabel", background="#f2f2f2")
style.configure("TButton", background="#4caf50", foreground="white")

# Algorithm selection
algorithm_label = ttk.Label(root, text="Select Algorithm:")
algorithm_label.pack(pady=10)

algorithm_var = tk.StringVar(value="Caesar")  # Default selection is set to "Caesar"
algorithm_dropdown = ttk.Combobox(root, textvariable=algorithm_var, values=["Caesar", "Affine"], state="readonly")
algorithm_dropdown.pack()

# Key input for Caesar cipher
key_label = ttk.Label(root, text="Caesar Key:")
key_label.pack()

key_entry = ttk.Entry(root)
key_entry.pack()

# Key inputs for Affine cipher
key_a_label = ttk.Label(root, text="Affine Key A:")
key_a_label.pack()

key_a_entry = ttk.Entry(root)
key_a_entry.pack()

key_b_label = ttk.Label(root, text="Affine Key B:")
key_b_label.pack()

key_b_entry = ttk.Entry(root)
key_b_entry.pack()

# Function to handle algorithm selection
def algorithm_changed(event):
    if algorithm_var.get() == "Caesar":
        key_label.pack()
        key_entry.pack()
        key_a_label.pack_forget()
        key_a_entry.pack_forget()
        key_b_label.pack_forget()
        key_b_entry.pack_forget()
    else:
        key_label.pack_forget()
        key_entry.pack_forget()
        key_a_label.pack()
        key_a_entry.pack()
        key_b_label.pack()
        key_b_entry.pack()

algorithm_dropdown.bind("<<ComboboxSelected>>", algorithm_changed)

# Plaintext input
plaintext_label = ttk.Label(root, text="Plaintext:")
plaintext_label.pack()

plaintext_entry = ttk.Entry(root)
plaintext_entry.pack()

# Result label
result_label = ttk.Label(root, text="", background="#f2f2f2", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Encrypt or Decrypt selection
encrypt_var = tk.BooleanVar(value=True)
encrypt_radio = ttk.Radiobutton(root, text="Encrypt", variable=encrypt_var, value=True)
decrypt_radio = ttk.Radiobutton(root, text="Decrypt", variable=encrypt_var, value=False)
encrypt_radio.pack()
decrypt_radio.pack()

# Process button
process_button = ttk.Button(root, text="Process", command=process_text)
process_button.pack(pady=20)

algorithm_changed(None);

# Start the Tkinter event loop
root.mainloop()