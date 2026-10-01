from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

class student :
    def __init__(self, root):
        self.root = root
        self.root.title("face recognition system")
        self.root.geometry("1550x800+0+0")

        # Background Image
        self.original_bg = Image.open(r"E:\loging\image\tt.jpg")
        self.bg = ImageTk.PhotoImage(self.original_bg.resize((1550,800), Image.LANCZOS))
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=127, relwidth=1, relheight=1)

        # first image
        img1 = Image.open(r"E:\loging\image\a.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img2 = Image.open(r"E:\loging\image\b.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image
        img3 = Image.open(r"E:\loging\image\c.jpg")
        img3 = img3.resize((550, 130), Image.LANCZOS)
        self.photoimage3= ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimage3)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        title_lbl=Label(bg_lbl,text=" Student Management System ", font=("times new roman", 30, "bold"), fg="green", bg="white")
        title_lbl.place(x=0,y=0,width=1550,height=45)

        main_frame=Frame(bg_lbl,bd=2)
        main_frame.place(x=20,y=50,width=1480,height=600)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman", 18, "bold"))
        left_frame.place(x=10,y=10,width=740,height=580)

        # first image in left
        img_left= Image.open(r"E:\loging\image\a.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimage_left = ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimage_left)
        f_lbl.place(x=5,y=5,width=720,height=130)

        # student current
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="current Student Information ",font=("times new roman", 18, "bold"))
        left_frame.place(x=15,y=180,width=720,height=100)

        # department
        dep_Label=Label(left_frame,text="department:",font=("times new roman", 10, "bold"),bg="white")
        dep_Label.grid(row=0,column=0,padx=10,sticky='w')
        dep_combo=ttk.Combobox(left_frame,font=("times new roman", 10, "bold"),state="read only")
        dep_combo["values"]=("select department","computer","IT","Civil","Mechhnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky='w')

        # semester
        dep_Label=Label(left_frame,text="semester:",font=("times new roman", 10, "bold"))
        dep_Label.grid(row=1,column=0,padx=10,sticky='w')
        dep_combo=ttk.Combobox(left_frame,font=("times new roman", 10, "bold"),state="read only")
        dep_combo["values"]=("select semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky='w')

        # year
        dep_Label=Label(left_frame,text="year:",font=("times new roman", 10, "bold"))
        dep_Label.grid(row=0,column=2,padx=10,sticky='w')
        dep_combo=ttk.Combobox(left_frame,font=("times new roman", 10, "bold"),state="read only")
        dep_combo["values"]=("select year","2020","21","22","23","24")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=10)

        # course
        dep_Label=Label(left_frame,text="course:",font=("times new roman", 10, "bold"))
        dep_Label.grid(row=1,column=2,padx=10,sticky='w')
        dep_combo=ttk.Combobox(left_frame,font=("times new roman", 10, "bold"),state="read only")
        dep_combo["values"]=("select course","Java","python","OOP ","C ++","C #")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=10)

        # student information
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information ",font=("times new roman", 18, "bold"))
        left_frame.place(x=15,y=290,width=720,height=290)

        dep_Label=Label(left_frame,text="department:",font=("times new roman", 10, "bold"),bg="white")
        dep_Label.grid(row=0,column=0,padx=10,sticky='w')
        dep_combo=ttk.Combobox(left_frame,font=("times new roman", 10, "bold"),state="read only")
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky='w')

        # semester
        dep_Label=Label(left_frame,text="semester:",font=("times new roman", 10, "bold"))
        dep_Label.grid(row=1,column=0,padx=10,sticky='w')
        dep_combo=ttk.Combobox(left_frame,font=("times new roman", 10, "bold"),state="read only")
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky='w')

        # phone
        dep_Label=Label(left_frame,text="phnoe:",font=("times new roman", 10, "bold"))
        dep_Label.grid(row=2,column=0,padx=10,sticky='w')
        dep_combo=ttk.Combobox(left_frame,font=("times new roman", 10, "bold"),state="read only")
        dep_combo.grid(row=2,column=1,padx=2,pady=10,sticky='w')

        # address
        dep_Label=Label(left_frame,text="address:",font=("times new roman", 10, "bold"))
        dep_Label.grid(row=3,column=0,padx=10,sticky='w')
        dep_combo=ttk.Combobox(left_frame,font=("times new roman", 10, "bold"),state="read only")
        dep_combo.grid(row=3,column=1,padx=2,pady=10,sticky='w')

        # year
        dep_Label=Label(left_frame,text="year:",font=("times new roman", 10, "bold"))
        dep_Label.grid(row=0,column=2,padx=10,sticky='w')
        dep_combo=ttk.Combobox(left_frame,font=("times new roman", 10, "bold"),state="read only")
        dep_combo["values"]=("select year","2020","21","22","23","24")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=10)

        # course
        dep_Label=Label(left_frame,text="course:",font=("times new roman", 10, "bold"))
        dep_Label.grid(row=1,column=2,padx=10,sticky='w')
        dep_combo=ttk.Combobox(left_frame,font=("times new roman", 10, "bold"),state="read only")
        dep_combo["values"]=("select course","Java","python","OOP ","C ++","C #")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=10)

        # radio button
      
        # radio button

        self.photo_var = StringVar()
        self.photo_var.set("No")

        radiobtn1=ttk.Radiobutton(left_frame,text="Take Photo Sample",variable=self.photo_var,value="Yes")
        radiobtn1.grid(row=4,column=0,padx=10,pady=10)

        radiobtn2=ttk.Radiobutton(left_frame,text="Don't Take Photo Sample",variable=self.photo_var,value="No")
        radiobtn2.grid(row=4,column=1,padx=10,pady=10)
        
       #Button frame
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        Save_btn=Button(btn_frame,text="Save",width =15 ,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        Save_btn.grid(row=0,column=0)

        delete_btn=Button(btn_frame,text="Delete",width =15 ,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=1)

        updat_btn=Button(btn_frame,text="Update",width =15 ,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        updat_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width =15 ,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame_1=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame_1.place(x=0,y=230,width=715,height=35)

        takeph_btn=Button(btn_frame_1,text="Take Photo Sample ",width =31 ,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        takeph_btn.grid(row=0,column=0)

        takeup_btn=Button(btn_frame_1,text="Take Photo update ",width =31 ,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        takeup_btn.grid(row=0,column=1)

        
          
        


        

     
        # Right label frame

        
        # Right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" STUDENT Details",font=("times new roman", 18, "bold"))
        Right_frame.place(x=750,y=10,width=690,height=580)

        # image

        img_right= Image.open(r"E:\loging\image\a.jpg")
        img_right = img_right.resize((680, 130), Image.LANCZOS)
        self.photoimage_right = ImageTk.PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=self.photoimage_right)
        f_lbl.place(x=5,y=5,width=680,height=130)

        # search system

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman", 12, "bold"))
        search_frame.place(x=5,y=140,width=680,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman", 12, "bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5)

        search_combo=ttk.Combobox(search_frame,font=("times new roman", 12, "bold"),state="read only",width=12)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=5)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman", 12, "bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5)

        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5,pady=5)

        showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5,pady=5)

        # student table

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=220,width=680,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,
                                        columns=("dep","semester","year","course","id","name","gender","dob","phone","address","photo"),
                                        xscrollcommand=scroll_x.set,
                                        yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSample")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("year",width=80)
        self.student_table.column("course",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)





if __name__ == "__main__":
    root = Tk()
    app = student(root)
    root.mainloop()