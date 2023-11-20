from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1360x700+0+0")
        
        # *************VARIABLE***********
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        # ====Background Image===========
        self.img = ImageTk.PhotoImage(Image.open(r"image/neon-lights-3d-5120x2880-12485.jpg")) # photoimage attribute error .......
        img = Label(self.root,image = self.img).place(x=0,y=0,relheight=1,relwidth=1)
        
        
        #======left image===========
        self.bg1=ImageTk.PhotoImage(file=r"image/image5.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=482)
        
        #=======main frame=============
        frame=Frame(self.root,bg="white")
        frame.place(x=520, y=100, width=780, height=482)

        #========REGISTER HERE========
        register_lbl=Label(frame,text="REGISTER HERE",font=("tmimes new roan",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=300,y=15)
       
        #==============label and entry=======
        
        #----------FIRST AND LAST NAME----------
        
        fname=Label(frame,text="Party Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        self.frmae_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.frmae_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Candidate Name",font=("tmimes new roan",15,"bold"),fg="black",bg="white")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
       
       #------CONTACT NUMBER ---------------
       
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
       #----------EMAIL ID--------------
       
        email=Label(frame,text="Email Id",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        #---------SELECT SECURITY QUESTION---------------
        
        security_Q=Label(frame,text="Select security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","your birth place","your party name","your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
       
       #-----SECURITY ANSWER----
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
       #------PASSWORD------
       
        pswd=Label(frame,text="password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
       
       #-----CONFERM POSWORD-----
       
        conferm_pswd=Label(frame,text="Conferm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        conferm_pswd.place(x=370,y=310)
        
        self.txt_conferm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_conferm_pswd.place(x=370,y=340,width=250)
       
       #-----CHECK BUTTON----
       
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,text="I Agree The Terms & conditions",variable=self.var_check,font=("times new roan",10,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=370)
        
        ############# BUTTON ##############
        
        #++++++++++++REGISTER BUTTON***************
        
        img=Image.open(r"image/image7.jpeg")
        img=img.resize((250,60),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roan",10,"bold"),fg="white")
        b1.place(x=10,y=400,width=300)
        
        #------------LOGIN BUTTON-------
        
        img1=Image.open(r"image/image8.jpeg")
        img1=img1.resize((250,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roan",10,"bold"),fg="white")
        b1.place(x=310,y=400,width=300)
        
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="select" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & cnfirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree our terms & condition")
        else:
            messagebox.showinfo("seccess","welcome to election commisionar")
       
       




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()       
    
        