from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Login_Window:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1360x700+0+0")
        self.root.resizable(False,False)
       
        self.bg = ImageTk.PhotoImage(Image.open("image/neon-lights-3d-5120x2880-12485.jpg")) # photoimage attribute error .......
        self.bg_image = Label(self.root,image = self.bg).place(x=0,y=0,relheight=1,relwidth=1)
        
        #======= LOGIN FRAME =========#
        
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=500, y=40, width=450, height=450)
        
        #=====LOGIN ICON =======#
        
        img1=Image.open(r"image/image9.jpg")
        img1=img1.resize((90,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=655,y=43,width=90,height=90)
        
        #===== TITLE ======#
        
        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=80)
        desc=Label(Frame_login,text="Accountant Party Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=140)
       
       
        label_user=Label(Frame_login,text="Username",font=("Goudy old style",20,"bold"),fg="gray",bg="white").place(x=90,y=165)
        self.text_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.text_user.place(x=90,y=205,width=300,height=35)
       

        label_pass=Label(Frame_login,text="password",font=("Goudy old style",20,"bold"),fg="gray",bg="white").place(x=90,y=240)
        self.text_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.text_pass.place(x=90,y=275,width=300,height=35)
       
       
        #====LOGIN BUTTON===#
        
        login_btn=Button(Frame_login,command=self.login_function,text="Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=90,y=330,width=120,height=35)
        
         #====REGISTER BUTTON===#
        
        register_btn=Button(Frame_login,text="New Register Button?",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=375,width=160)
       
         #====FORGET PASSSWORD===#
         
        forget_btn=Button(Frame_login,text="Forget Password?",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=410,width=160)
       
    def login_function(self):
        if self.text_pass.get()=="" or self.text_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.text_pass.get()!="123456789" or self.text_user.get()!="Dablu":
            messagebox.showerror("Error","Invalid User name & password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome{self.text_user.get()}\n your password: {self.text_pass.get()}",parent=self.root)
            
         
       
       
       

root=Tk()
app=Login_Window(root)
root.mainloop()