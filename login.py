from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Sign_up import signup_pg
from Welcome import welcome_screen
import ast

from PIL import Image, ImageTk

# Function to authenticate user login
def login_user():

    username = user_entry.get()
    password = pass_entry.get()

# Check entered credentials against registered users
    try:

        file = open("user_details.txt", "r")

        for line in file:

            data = ast.literal_eval(line.strip())

            if data["username"] == username:

                if data["password"] == password:

                    messagebox.showinfo(
                        "Success",
                        f"Welcome {username}!"
                    )

                    # Open welcome screen after successful login
                    root.withdraw()
                    welcome_screen(
                    root,
                    user_entry,
                    pass_entry,
                    username
                    )
                    return

                else:

                    messagebox.showerror(
                        "Error",
                        "Incorrect Password!"
                    )

                    user_entry.delete(0, END)
                    pass_entry.delete(0, END)

                    return

        messagebox.showerror(
            "Error",
            "Username does not exist!"
        )

        user_entry.delete(0, END)
        pass_entry.delete(0, END)

        file.close()

    except FileNotFoundError:

        messagebox.showerror(
            "Error",
            "No users registered yet!"
        )

# Main Login Window
root = Tk()
root.geometry("1920x1080")
root.title("Login")
root.config(bg="black")

main_frame = Frame(root,
                   bg="skyblue")
main_frame.pack(pady=100)

img = Image.open("Assets/Sign_in_logo.png")
img=img.resize((300,300))
photoimg = ImageTk.PhotoImage(image=img)

label = Label(main_frame, 
              image=photoimg, bg="lavender")
label.pack(pady=10) 

user_frame = Frame(main_frame,
                   bg="skyblue")
user_frame.pack(pady=5)

user_label = Label(user_frame, 
                   text="Username:",
                   width=10,
                   fg='black',
                  bg="skyblue",
                   font=("Arial", 20, 'bold'))
user_label.pack(side=LEFT)

user_entry = Entry(user_frame, font=("Arial", 20, 'bold'), width=25)
user_entry.pack(side=LEFT, padx=10)


pass_frame = Frame(main_frame,
                   bg="skyblue")
pass_frame.pack(pady=5)

pass_label = Label(pass_frame, 
                   text="Password:",
                   width=10,
                   fg='black',
                   bg="skyblue",
                   font=("Arial", 20, 'bold'))
pass_label.pack(side=LEFT)

pass_entry = Entry(pass_frame, 
                font=("Arial", 20, 'bold'),
                width=25,
                show="*")
pass_entry.pack(side=LEFT, padx=10)

# Login and Signup Buttons
btn_frame = Frame(main_frame,
                   bg="skyblue")
btn_frame.pack(pady=10)

btn_login = Button(btn_frame,
                   text="Login",
                   command=login_user,
                   fg='white',
                   bg="seagreen",
                   font=("Arial", 20, 'bold'),
                   bd=4,
                   relief='raised',
                   width=10
                   )
btn_login.pack(side= LEFT)

btn_signup = Button(btn_frame,
                   text="Sign Up",
                   command=signup_pg,
                   fg='white',
                   bg="tomato",
                   font=("Arial", 20, 'bold'),
                   bd=4,
                   relief='raised',
                   width=10
                   )
btn_signup.pack(padx=10)
root.mainloop()