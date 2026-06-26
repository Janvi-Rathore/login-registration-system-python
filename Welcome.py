from tkinter import *
from PIL import Image, ImageTk

# Display welcome screen after successful login
def welcome_screen(root, user_entry, pass_entry, username):

    # Welcome Window
    welcome_root = Toplevel()

    # Logout user and return to login page
    def logout():
        welcome_root.destroy()

        user_entry.delete(0, END)
        pass_entry.delete(0, END)
        root.deiconify()

    welcome_root.geometry("1000x700")
    welcome_root.title("Welcome")
    welcome_root.config(bg="midnightblue")

    card = Frame(
        welcome_root,
        bg="white",
        bd=4,
        relief="raised"
    )
    card.pack(pady=40, padx=60, fill="both", expand=True)

    img = Image.open("Assets/Welcome_logo.png")
    img = img.resize((250, 250))

    photo = ImageTk.PhotoImage(img)

    logo = Label(
        card,
        image=photo,
        bg="white"
    )
    logo.image = photo
    logo.pack(pady=15)

    Label(
        card,
        text="LOGIN SUCCESSFUL",
        font=("Arial", 28, "bold"),
        fg="mediumvioletred",
        bg="white"
    ).pack(pady=10)

    Label(
        card,
        text="Welcome Back,",
        font=("Arial", 20),
        fg="navy",
        bg="white"
    ).pack(pady=(20, 5))

    Label(
        card,
        text=username,
        font=("Arial", 32, "bold"),
        fg="black",
        bg="white"
    ).pack()

    Label(
        card,
        text="We're glad to see you again!",
        font=("Arial", 16),
        fg="slateblue",
        bg="white"
    ).pack(pady=15)

    # Logout Button
    Button(
        card,
        text="Logout",
        font=("Arial", 16, "bold"),
        bg="tomato",
        fg="white",
        width=10,
        command=logout
    ).pack(pady=20)
