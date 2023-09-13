import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())

    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on user choices
    character_set = ""
    if use_lowercase.get():
        character_set += lowercase_letters
    if use_uppercase.get():
        character_set += uppercase_letters
    if use_digits.get():
        character_set += digits
    if use_special.get():
        character_set += special_characters

    # Check if at least one character set is selected
    if len(character_set) == 0:
        result_label.config(text="Please select at least one character set.")
        return

    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(password_length))
    result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(root, text="Password Length:",width=40)
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes for character sets
use_lowercase = tk.BooleanVar()
lowercase_check = tk.Checkbutton(root, text="Lowercase Letters", variable=use_lowercase)
lowercase_check.pack()

use_uppercase = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Uppercase Letters", variable=use_uppercase)
uppercase_check.pack()

use_digits = tk.BooleanVar()
digits_check = tk.Checkbutton(root, text="Digits (0-9)", variable=use_digits)
digits_check.pack()

use_special = tk.BooleanVar()
special_check = tk.Checkbutton(root, text="Special Characters", variable=use_special)
special_check.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
