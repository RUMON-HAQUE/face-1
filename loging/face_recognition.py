from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


class face_RecognitioN_System :
    def __init__(self, root):
        self.root = root
        self.root.title("face recognition system")
        self.root.geometry("1550x800+0+0")  # window size 

         # ==== Background Image ====
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
     #second image
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
 
 # title for 
        title_lbl=Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 30, "bold"), fg="red", bg="white")
        title_lbl.place(x=0,y=0,width=1550,height=45)
         
      #body image

        img4 = Image.open(r"E:\loging\image\1.jpg")
        img4 = img4.resize((200,200), Image.LANCZOS)
        self.photoimage4= ImageTk.PhotoImage(img4)
     
        b1=Button(bg_lbl,image=self.photoimage4,cursor="hand2")
        b1.place(x=100,y=100,width=200,height=200)

        b1_1=Button(bg_lbl,text="Student Details",cursor="hand2", font=("times new roman", 15, "bold"), fg="red", bg="blue")
        b1_1.place(x=100,y=300,width=200,height=40)

        img5 = Image.open(r"E:\loging\image\2.jpeg")
        img5 = img5.resize((200,200), Image.LANCZOS)
        self.photoimage5= ImageTk.PhotoImage(img5)
     
        b1=Button(bg_lbl,image=self.photoimage5,cursor="hand2")
        b1.place(x=400,y=100,width=200,height=200)

        b1_1=Button(bg_lbl,text="Face Detector",cursor="hand2", font=("times new roman", 15, "bold"), fg="red", bg="blue")
        b1_1.place(x=400,y=300,width=200,height=40)  

        img6 = Image.open(r"E:\loging\image\3.jpeg")
        img6 = img6.resize((200,200), Image.LANCZOS)
        self.photoimage6= ImageTk.PhotoImage(img6)
     
        b1=Button(bg_lbl,image=self.photoimage6,cursor="hand2")
        b1.place(x=700,y=100,width=200,height=200)

        b1_1=Button(bg_lbl,text="Attendance",cursor="hand2", font=("times new roman", 15, "bold"), fg="red", bg="blue")
        b1_1.place(x=700,y=300,width=200,height=40)

        img7 = Image.open(r"E:\loging\image\4.jpeg")
        img7= img7.resize((200,200), Image.LANCZOS)
        self.photoimage7= ImageTk.PhotoImage(img7)
     
        b1=Button(bg_lbl,image=self.photoimage7,cursor="hand2")
        b1.place(x=1000,y=100,width=200,height=200)

        b1_1=Button(bg_lbl,text="Help Desk",cursor="hand2", font=("times new roman", 15, "bold"), fg="red", bg="blue")
        b1_1.place(x=1000,y=300,width=200,height=40)  

        # down image

        img8 = Image.open(r"E:\loging\image\5.jpg")
        img8= img8.resize((200,200), Image.LANCZOS)
        self.photoimage8= ImageTk.PhotoImage(img8)
     
        b1=Button(bg_lbl,image=self.photoimage8,cursor="hand2")
        b1.place(x=100,y=400,width=200,height=200) 

        b1_1=Button(bg_lbl,text="Train Data",cursor="hand2", font=("times new roman", 15, "bold"), fg="red", bg="blue")
        b1_1.place(x=100,y=600,width=200,height=40)


        img9 = Image.open(r"E:\loging\image\6.jpeg")
        img9= img9.resize((200,200), Image.LANCZOS)
        self.photoimage9= ImageTk.PhotoImage(img9)
     
        b1=Button(bg_lbl,image=self.photoimage9,cursor="hand2")
        b1.place(x=400,y=400,width=200,height=200) 

        b1_1=Button(bg_lbl,text="Photos",cursor="hand2", font=("times new roman", 15, "bold"), fg="red", bg="blue")
        b1_1.place(x=400,y=600,width=200,height=40)

        img10= Image.open(r"E:\loging\image\7.jpeg")
        img10= img10.resize((200,200), Image.LANCZOS)
        self.photoimage10= ImageTk.PhotoImage(img10)
     
        b1=Button(bg_lbl,image=self.photoimage10,cursor="hand2")
        b1.place(x=700,y=400,width=200,height=200) 

        b1_1=Button(bg_lbl,text="Developer",cursor="hand2", font=("times new roman", 15, "bold"), fg="red", bg="blue")
        b1_1.place(x=700,y=600,width=200,height=40)

        img11= Image.open(r"E:\loging\image\8.jpeg")
        img11= img11.resize((200,200), Image.LANCZOS)
        self.photoimage11= ImageTk.PhotoImage(img11)
     
        b1=Button(bg_lbl,image=self.photoimage11,cursor="hand2")
        b1.place(x=1000,y=400,width=200,height=200) 

        b1_1=Button(bg_lbl,text="Exit",cursor="hand2", font=("times new roman", 15, "bold"), fg="red", bg="blue")
        b1_1.place(x=1000,y=600,width=200,height=40)



        
        
 
        
        
if __name__ == "__main__":
    root = Tk()
    app =face_RecognitioN_System (root)
    root.mainloop()