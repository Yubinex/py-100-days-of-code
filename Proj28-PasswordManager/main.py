from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered:\nEmail: {email_username}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("Proj28-PasswordManager/data.txt", "a") as f:
                f.write(f"{website} | {email_username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ---------------------------- CANVAS ---------------------------- #

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="Proj28-PasswordManager/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# ---------------------------- LABELS ---------------------------- #

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# ---------------------------- ENTRIES ---------------------------- #

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=50)
email_username_entry.insert(0, "janhauck99@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

# ---------------------------- BUTTONS ---------------------------- #

password_button = Button(text="Generate Password", command=generate_password,
                         highlightthickness=0, padx=0, pady=0)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=47, command=save)
add_button.grid(column=1, row=4, columnspan=2)

mainloop()
