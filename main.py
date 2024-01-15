import random
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    passowrd_letters = [choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols = [choice(symbols) for _ in range(random.randint(2,4))]
    password_list = passowrd_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password1_label.insert(0, password)
    pyperclip.copy(password)



def save():
    website = entry_label.get()
    email = email_label.get()
    password = password1_label.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="please make sure you haven't left any field empty")
    is_okk = messagebox.askokcancel(title="website",
                                    message=f"these are details entered: \nEmail:{email}\nPassword:{password}\nis it okk to save?")
    if is_okk:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            entry_label.delete(0, END)
            password1_label.delete(0, END)


windows = Tk()
windows.title("password manager")
windows.config(padx=20, pady=20, )

canvas = Canvas()
canvas.config(width=200, height=200, highlightthickness=0)
canvas.grid(row=0, column=2)
my_pass = PhotoImage(file="C:\\Users\\rb632\\Downloads\\password-manager-start\\logo.png")
canvas.create_image(100, 100, image=my_pass)
canvas.grid()
website_label = Label(text="Website:", highlightthickness=0)
website_label.grid(row=1, column=1, columnspan=1)

entry_label = Entry(width=35)
entry_label.grid(row=1, column=2, columnspan=2)
entry_label.focus()

username_label = Label(text="Username/Email:", highlightthickness=1)
username_label.grid(row=2, column=1)

email_label = Entry(width=35)
email_label.grid(row=2, column=2, columnspan=2)

password_label = Label(text="Password:", highlightthickness=3)
password_label.grid(row=3, column=1)

password1_label = Entry(width=21)
password1_label.grid(row=3, column=2)

button_label = Button(text="Generate Password", command=generate_password)
button_label.grid(row=3, column=3, columnspan=3)
##generate_entry = Entry(width=30)
# generate_entry.grid(row=3, column=3)
add_label = Button(text="Add", width=36, command=save)
add_label.grid(row=4, column=2, columnspan=5)
windows.mainloop()
