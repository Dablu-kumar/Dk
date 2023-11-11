from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Login_Window:
    def __init__(self, root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1360x700+0+0")
        
       # self.bg_photoImage__photo=ImageTk.PhotoImage(file=r"image\image/360_F_123629765_x2OfzT7sQnJFhYVA4K3JQrKvL0tDSeaG.jpg")
       # lbl_bg_photoImage__photo=Label(self.root,image=self.bg)
       # lbl_bg_photoImage__photo.place(x=0, y=0, relwidth=1, relheight=1)
        self.img = ImageTk.PhotoImage(Image.open("image/neon-lights-3d-5120x2880-12485.jpg")) # photoimage attribute error .......
        img = Label(self.root,image = self.img).place(x=0,y=0,relheight=1,relwidth=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=500, y=40, width=400, height=450)
        
        img1=Image.open(r"image/img2.jpg")
        img1=img1.resize((90,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=655,y=50,width=90,height=90)
        
        get_str=Label(frame,text="Welcome",font=("tmimes new roan",20,"bold"),fg="white",bg="black")
        get_str.place(x=140,y=100)
        
        # label
        username=lbl=Label(frame, text="username", font=("tmimes new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70, y=155)
        
        
        self.txtuser=ttk.Entry(frame, font=("tmimes new roman",15,"bold"))
        self.txtuser.place(x=40, y=180, width=310)
        
        password=lbl=Label(frame, text="Password", font=("tmimes new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70, y=255)
        
        
        self.txtuser=ttk.Entry(frame, font=("tmimes new roman",15,"bold"))
        self.txtuser.place(x=40, y=280, width=310)
        #================ICON IMAGE============
        img2=Image.open(r"image/IMG-20231110-WA0004-01.jpeg.jpg")
        img2=img2.resize((20,20),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=550,y=200,width=20,height=20)
        
        img3=Image.open(r"image/IMG-20231110-WA0004-01.jpeg.jpg")
        img3=img3.resize((20,20),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=550,y=300,width=20,height=20)
        
        #====LOGIN BUTTON===#
        loginbtn=Button(frame,command=self.login_function ,text="login", font=("tmimes new roan",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white", activebackground="red")
        loginbtn.place(x=140,y=330,width=120, height=35)
        
         #====REGISTER BUTTON===#
        registerbtn=Button(frame, text="New User Register", font=("tmimes new roan",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white", activebackground="black")
        registerbtn.place(x=20,y=375,width=160)
       
         #====FORGET PASSSWORD===#
        forgetpasswordbtn=Button(frame, text="Forget Password", font=("tmimes new roan",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white", activebackground="black")
        forgetpasswordbtn.place(x=15,y=400,width=160)
       
    
    def login_function(self):
        
        
    # You can add your own validation logic here
        if self.txtuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","all field required",parent=self.root)
        elif self.txtuser.get()!="admin" and self.txtpass.get()!="admi":
           messagebox.showerror("error", "Invalid Username/Password",parent=self.root)
        else:
           messagebox.showeinfo("Welcome",f"Welcome{self.txtuser.get()}\n your Password:{self.textpass.get()}")

      
if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()