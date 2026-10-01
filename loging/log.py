from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")  # window size

        # ==== Background Image ====
        self.original_bg = Image.open(r"E:\loging\image\tt.jpg")
        self.bg = ImageTk.PhotoImage(self.original_bg.resize((1900, 1080), Image.LANCZOS))

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ==== Login Frame ====
        frame = Frame(self.root, bg="black")
        frame.place(x=500, y=180, width=380, height=450)

        # ==== Login Icon ====
        img1 = Image.open(r"E:\loging\image\f.jpeg")
        img1 = img1.resize((150, 150), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(frame, image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=140, y=1, width=100, height=100)

        # ==== Username ====
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="black", fg="white")
        username_lbl.place(x=80, y=120)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=50, y=150, width=300)

        # ==== Password ====
        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
        password_lbl.place(x=80, y=210)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txtpass.place(x=50, y=240, width=300)

        # ==== Show / Hide Password ====
        self.show_var = tk.BooleanVar(value=False)
        show_btn = tk.Checkbutton(frame, text="Show password", variable=self.show_var,
                                  command=self.toggle_password,
                                  bg="black", fg="white", selectcolor="black", activebackground="black")
        show_btn.place(x=50, y=270)

        # ==== Icons ====
        img2 = Image.open(r"E:\loging\image\ss.jpeg")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(frame, image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=50, y=120, width=25, height=25)

        img3 = Image.open(r"E:\loging\image\gg.jpeg")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(frame, image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=50, y=210, width=25, height=25)

        # ==== Login Button ====
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"),
                          bd=3, relief=RIDGE, fg="white", bg="red",
                          activebackground="white", activeforeground="red")
        loginbtn.place(x=110, y=320, width=120, height=35)

        # ==== Register Button ====
        registerbtn = Button(frame, text="New Register", font=("times new roman", 10, "bold"),
                             borderwidth=0, fg="white", bg="black",
                             activebackground="white", activeforeground="red")
        registerbtn.place(x=20, y=370, width=100)

        # ==== Forgot Button ====
        forgatebtn = Button(frame, text="Forgot", font=("times new roman", 10, "bold"),
                            borderwidth=0, fg="white", bg="black",
                            activebackground="white", activeforeground="red")
        forgatebtn.place(x=20, y=400, width=100)

    # ==== Toggle Show Password ====
    def toggle_password(self):
        if self.show_var.get():
            self.txtpass.config(show="")
        else:
            self.txtpass.config(show="*")

    # ==== Login Function ====
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        elif self.txtuser.get() == "rumon" and self.txtpass.get() == "1234":
            messagebox.showinfo("Success", "Welcome Rumon!")
        else:
            messagebox.showerror("Invalid", "Invalid Username or Password")


if __name__ == "__main__":
    root = Tk()
    app = login_window(root)
    root.mainloop()
