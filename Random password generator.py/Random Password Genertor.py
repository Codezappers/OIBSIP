import tkinter as tk
import random
import string
import pyperclip
from PIL import Image, ImageTk

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        return "Please select at least one character type"
    return ''.join(random.choice(characters) for _ in range(length))

def generate():
    length_str = length_entry.get()
    if not length_str.isdigit():
        password_label.config(text="Please enter the length of the password")
        return
    length = int(length_str)
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    password_label.config(text=f"Generated password: {password}")

def copy_to_clipboard():
    password = password_label.cget("text")
    if password.startswith("Generated password: "):
        password = password[len("Generated password: "):]
        pyperclip.copy(password)
        password_label.config(text="Password copied to clipboard!")
    else:
        password_label.config(text="No password to copy")

root = tk.Tk()
root.title('Password Generator')
root.geometry('500x600')

bg_image = Image.open("C:\\Users\\Aden\\OneDrive\\Desktop\\Personal coding\\Internship - info\\Random password generator.py\\Make-your-password-strong-1024x576.jpg")
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

entry_label = tk.Label(root, text='Please enter the length of the password', font=('Helvetica', 20), bg='gray')
entry_label.pack(side=tk.TOP, pady=10, anchor='center')

length_entry = tk.Entry(root, width=20, font=('Helvetica', 20), bg='gray')
length_entry.pack(side=tk.TOP, pady=10, anchor='center')

letters_var = tk.BooleanVar()
letters_check = tk.Checkbutton(root, text="Letters", variable=letters_var, font=('Helvetica', 15), bg='gray', selectcolor='gray')
letters_check.pack(anchor='center')

numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text="Numbers", variable=numbers_var, font=('Helvetica', 15), bg='gray', selectcolor='gray')
numbers_check.pack(anchor='center')

symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(root, text="Symbols", variable=symbols_var, font=('Helvetica', 15), bg='gray', selectcolor='gray')
symbols_check.pack(anchor='center')

generate_button = tk.Button(root, text="Generate Password", font=('Helvetica', 20), bg='gray', command=generate)
generate_button.pack(side=tk.TOP, pady=10, anchor='center')

password_label = tk.Label(root, text="", font=('Helvetica', 20), bg='gray', wraplength=350)
password_label.pack(side=tk.TOP, pady=10, anchor='center')

copy_button = tk.Button(root, text="Copy to Clipboard", font=('Helvetica', 20), bg='gray', command=copy_to_clipboard)
copy_button.pack(side=tk.TOP, pady=10, anchor='center')

root.mainloop() 
