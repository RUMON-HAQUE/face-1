from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox 


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1900x1080+0+0")  # window size
        
        # ==== Variables ====
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.show_var = tk.BooleanVar(value=False)

        # ==== Background Image ====
        self.original_bg = Image.open(r"E:\loging\image\tt.jpg")
        self.bg = ImageTk.PhotoImage(self.original_bg.resize((1900, 1080), Image.LANCZOS))
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ==== Left Side Image ====
        img = Image.open(r"E:\loging\image\uu.jpg")
        img = img.resize((470, 550), Image.LANCZOS)   # resize
        self.bg1 = ImageTk.PhotoImage(img)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # ==== Main Frame ====
        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=100, width=800, height=550)

        title = Label(frame, text="Register Here", font=("times new roman", 25, "bold"), fg="green", bg="white")
        title.place(x=20, y=20)

        # ==== First Name ====
        firstname_lbl = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        firstname_lbl.place(x=20, y=100)
        self.txt_fname = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        self.txt_fname.place(x=20, y=130, width=230)

        # ==== Last Name ====
        lastname_lbl = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lastname_lbl.place(x=350, y=100)
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=350, y=130, width=230)

        # ==== Contact ====
        contact_lbl = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        contact_lbl.place(x=20, y=160)
        self.txt_contact = ttk.Entry(frame, textvariable =self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=20, y=190, width=230)

        # ==== Email ====
        gmail_lbl = Label(frame, text="Gmail", font=("times new roman", 15, "bold"), bg="white")
        gmail_lbl.place(x=350, y=160)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=350, y=190, width=230)

        # ==== Security Question ====
        secuirty_Q = Label(frame, text="Select Security", font=("times new roman", 15, "bold"), bg="white")
        secuirty_Q.place(x=20, y=220)
        self.combo_secuirty_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,
                                             font=("times new roman", 15, "bold"), state="readonly")
        self.combo_secuirty_Q["values"] = ("Select", "Your Birth place", "Married", "Unmarried")
        self.combo_secuirty_Q.place(x=20, y=250, width=230)
        self.combo_secuirty_Q.current(0)

        # ==== Security Answer ====
        secuirty_lbl = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        secuirty_lbl.place(x=350, y=220)
        self.txt_SecurityA = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new roman", 15))
        self.txt_SecurityA.place(x=350, y=250, width=230)

        # ==== Password ====
        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password_lbl.place(x=20, y=280)
        self.txt_pass = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.txt_pass.place(x=20, y=310, width=230)

        # ==== Confirm Password ====
        confirm_lbl = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_lbl.place(x=350, y=280)
        self.txt_confpass = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        self.txt_confpass.place(x=350, y=310, width=230)

        # ==== Show / Hide Password ====
        
        show_btn = tk.Checkbutton(frame, text="Show password", variable=self.show_var,
                                  command=self.toggle_password,
                                  bg="white", fg="black",font=("times new roman", 8, "bold"), selectcolor="white", activebackground="white")
        show_btn.place(x=20, y=340)

        # ==== Terms & Condition ====
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Condition",
                               font=("times new roman", 10, "bold"), onvalue=1, offvalue=0, bg="white")
        checkbtn.place(x=20, y=370)

        # ==== Register Button ====
        RegistaionNowbtn = Button(frame, command=self.RegistaionNow, text="Register Now",
                                  font=("times new roman", 15, "bold"), bd=3, relief=RIDGE,
                                  fg="white", bg="red", activebackground="white", activeforeground="red")
        RegistaionNowbtn.place(x=250, y=420, width=200, height=50)

    # ==== Toggle Password Show/Hide ====
    def toggle_password(self):
        if self.show_var.get():
            self.txt_pass.config(show="")
            self.txt_confpass.config(show="")
        else:
            self.txt_pass.config(show="*")
            self.txt_confpass.config(show="*")

    # ==== Registration Validation ====
    def RegistaionNow(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select" or self.var_pass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our Terms & Condition")
        else:
            messagebox.showinfo("Success", "Welcome to the Registration!")


if __name__ == "__main__":
    root = Tk()
    app = login_window(root)
    root.mainloop()
