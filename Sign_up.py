from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ast

# Function to validate and save new user details
def register_details(username, password, confirm_password, Email, Phone_No):

    username = username.strip()
    Email = Email.strip()
    Phone_No = Phone_No.strip()

    # Blank validation
    if not all([username, password, confirm_password, Email, Phone_No]):
        messagebox.showwarning(
            "Blank Detected",
            "Please fill all details!"
        )
        return

    # Password match
    if password != confirm_password:
        messagebox.showerror(
            "Error",
            "Passwords do not match!"
        )
        return

    # Password length
    if len(password) < 6:
        messagebox.showerror(
            "Error",
            "Password must be at least 6 characters!"
        )
        return

    # Email validation
    if "@" not in Email or "." not in Email:
        messagebox.showerror(
            "Error",
            "Enter a valid email!"
        )
        return

    # Phone validation
    if not Phone_No.isdigit() or len(Phone_No) != 10:
        messagebox.showerror(
            "Error",
            "Enter a valid 10-digit phone number!"
        )
        return

    # Check whether username or email already exists
    try:

        with open("user_details.txt", "r") as file:

            for line in file:

                data = ast.literal_eval(line.strip())

                if data["username"] == username:
                    messagebox.showerror(
                        "Error",
                        "Username already exists!"
                    )
                    return

                if data["Email"] == Email:
                    messagebox.showerror(
                        "Error",
                        "Email already registered!"
                    )
                    return

    except FileNotFoundError:
        pass

    with open("user_details.txt", "a") as file:
        
        # Store user information in text file
        file.write(
            str({
                "username": username,
                "password": password,
                "Email": Email,
                "Phone_No": Phone_No
            }) + "\n"
        )

    messagebox.showinfo(
        "Success",
        "Registration Successful!"
    )

    signup_root.destroy()

# Create Signup Window
def signup_pg():

    global signup_root

    signup_root = Toplevel()
    signup_root.title("Sign Up")
    signup_root.geometry("900x850")
    signup_root.config(bg="black")

    main_frame = Frame(
        signup_root,
        bg="beige",
        padx=30,
        pady=20
    )

    main_frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )


    img = Image.open("Assets/Sign_up_logo.png")
    img = img.resize((300, 300))

    photoimg = ImageTk.PhotoImage(img)

    logo = Label(
        main_frame,
        image=photoimg,
        bg="lavender"
    )
    logo.image = photoimg

    logo.grid(
        row=0,
        column=0,
        columnspan=3,
        pady=20
    )

    LABEL_FONT = ("Arial", 20, "bold")
    ENTRY_FONT = ("Arial", 18)


    Label(
        main_frame,
        text="Username:",
        font=LABEL_FONT,
        bg="beige"
    ).grid(row=1, column=0, padx=10, pady=10, sticky="e")

    user_entry = Entry(
        main_frame,
        font=ENTRY_FONT,
        width=25
    )

    user_entry.grid(row=1, column=1, pady=10)


    Label(
        main_frame,
        text="Password:",
        font=LABEL_FONT,
        bg="beige"
    ).grid(row=2, column=0, padx=10, pady=10, sticky="e")

    pass_entry = Entry(
        main_frame,
        font=ENTRY_FONT,
        width=25,
        show="*"
    )

    pass_entry.grid(row=2, column=1, pady=10)

   
    Label(
        main_frame,
        text="Confirm Password:",
        font=LABEL_FONT,
        bg="beige"
    ).grid(row=3, column=0, padx=10, pady=10, sticky="e")

    confirm_entry = Entry(
        main_frame,
        font=ENTRY_FONT,
        width=25,
        show="*"
    )

    confirm_entry.grid(row=3, column=1, pady=10)


    show_pass = BooleanVar()

    # Toggle password visibility
    def toggle_password():

        if show_pass.get():

            pass_entry.config(show="")
            confirm_entry.config(show="")

        else:

            pass_entry.config(show="*")
            confirm_entry.config(show="*")

    Checkbutton(
        main_frame,
        text="Show",
        variable=show_pass,
        command=toggle_password,
        bg="beige"
    ).grid(row=2, column=2, padx=10)

  
    Label(
        main_frame,
        text="E-Mail ID:",
        font=LABEL_FONT,
        bg="beige"
    ).grid(row=4, column=0, padx=10, pady=10, sticky="e")

    mail_entry = Entry(
        main_frame,
        font=ENTRY_FONT,
        width=25
    )

    mail_entry.grid(row=4, column=1, pady=10)


    Label(
        main_frame,
        text="Phone No:",
        font=LABEL_FONT,
        bg="beige"
    ).grid(row=5, column=0, padx=10, pady=10, sticky="e")

    phone_entry = Entry(
        main_frame,
        font=ENTRY_FONT,
        width=25
    )

    phone_entry.grid(row=5, column=1, pady=10)


    Button(
        main_frame,
        text="Sign Up",
        fg="white",
        bg="tomato",
        font=("Arial", 20, "bold"),
        width=10,
        bd=4,
        relief="raised",
        command=lambda: register_details(
            user_entry.get(),
            pass_entry.get(),
            confirm_entry.get(),
            mail_entry.get(),
            phone_entry.get()
        )
    ).grid(
        row=6,
        column=0,
        columnspan=3,
        pady=30
    )