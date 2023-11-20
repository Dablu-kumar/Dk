from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class Criminal:
    def __init__(self,root):
      self.root=root
      self.root.geometry('1368x768+0+0')
      self.root.title('VOTING MANAGEMENT SYSTEM')
      
      self.bg = ImageTk.PhotoImage(Image.open("image/neon-lights-3d-5120x2880-12485.jpg")) # photoimage attribute error .......
      self.bg_image = Label(self.root,image = self.bg).place(x=0,y=00,relheight=1,relwidth=1)
       
      lbl_title=Label(self.root,text='VOTING MANAGENENT SYSTEM SOFTWARE',font=('times new roman',40,'bold'),bg='white',fg='gold')
      lbl_title.place(x=0,y=0,width=1368,height=70)
         
     # V.M.S logo.
      img_logo= Image.open('image/EVMs.jpeg')
      img_logo=img_logo.resize((92,65),Image.ANTIALIAS)
      self.photo_logo=ImageTk.PhotoImage(img_logo)
      
      self.logo=Label(self.root,image=self.photo_logo)
      self.logo.place(x=16,y=5,width=92,height=60)
     
      #img_Frame.
      img_frame=Frame(self.root,bd=1,relief=RIDGE,bg='blue')
      img_frame.place(x=0,y=70,width=1368,height=130)
      
      # 1st 
      img1= Image.open('image/EVMs.jpeg')
      img1=img1.resize((500,150),Image.ANTIALIAS)
      self.photo1=ImageTk.PhotoImage(img1)
      
      self.img_1=Label(img_frame,image=self.photo1)
      self.img_1.place(x=2,y=0,width=500,height=150)
      
      # 2nd
      img2= Image.open('image/image5.jpg')
      img2=img2.resize((500,150),Image.ANTIALIAS)
      self.photo2=ImageTk.PhotoImage(img2)
      
      self.img_2=Label(img_frame,image=self.photo2)
      self.img_2.place(x=500,y=0,width=500,height=150)
      
      # 3rd
      img3= Image.open('image/voting_img.jpg')
      img3=img3.resize((500,150),Image.ANTIALIAS)
      self.photo3=ImageTk.PhotoImage(img3)
      
      self.img_3=Label(img_frame,image=self.photo3)
      self.img_3.place(x=1000,y=0,width=390,height=150)
      
      # main_frame.
      
      main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
      main_frame.place(x=2,y=200,width=1368,height=480)
      
      # upper_frame.
      upper_frame=LabelFrame(main_frame, bd=2, relief=RIDGE,text='Party Information',font=('times new roman',9,'bold'),fg='red')
      upper_frame.place(x=1, y=1, width=1345, height=225)
      
      # Background Right Side Image
      img_crime= Image.open('image/blockchain based.jpg')
      img_crime=img_crime.resize((470,200),Image.ANTIALIAS)
      self.photocrime=ImageTk.PhotoImage(img_crime)
      
      self.img_crime=Label(upper_frame,image=self.photocrime)
      self.img_crime.place(x=853,y=0,width=480,height=200)
      
      # Labels Entery.
      
      
      # party ID.
      caseid=Label(upper_frame, text='Party ID:', font=('arial',9,'bold'),bg='gray')
      caseid.grid(row=0, column=0, padx=2, sticky=W)
      
      caseentery=ttk.Entry(upper_frame, width=20, font=('arial',9,'bold'))
      caseentery.grid(row=0, column=1, padx=2, sticky=W)
      
      # Party no.
      lbl_criminal_no=Label(upper_frame, text='Party No:', font=('arial',10,'bold'),bg='gray')
      lbl_criminal_no.grid(row=0, column=2, sticky=W, padx=2, pady=7)
      
      text_criminal_no=ttk.Entry(upper_frame, width=20, font=('arial',10,'bold'))
      text_criminal_no.grid(row=0, column=3, padx=2, pady=7)
      
      #candidate name.
      lbl_Name=Label(upper_frame, text='Candidate Name:', font=('arial',10,'bold'),bg='gray')
      lbl_Name.grid(row=1, column=0, sticky=W, padx=2, pady=7)
      
      text_Name=ttk.Entry(upper_frame, width=20, font=('arial',10,'bold'))
      text_Name.grid(row=1, column=1, sticky=W, padx=2, pady=7)
      
      # NickName.
      lbl_nickname=Label(upper_frame, text='NickName:', font=('arial',10,'bold'),bg='gray')
      lbl_nickname.grid(row=1, column=2, sticky=W, padx=2, pady=7)
      
      text_nickname=ttk.Entry(upper_frame, width=20, font=('arial',10,'bold'))
      text_nickname.grid(row=1, column=3, sticky=W, padx=2, pady=7)
      
      #Membership/Filow No.
      lbl_arrestDate=Label(upper_frame, text='Membership/Fillow NO:', font=('arial',10,'bold'),bg='gray')
      lbl_arrestDate.grid(row=2, column=0, sticky=W, padx=2, pady=7)
      
      text_nickname=ttk.Entry(upper_frame, width=20, font=('arial',10,'bold'))
      text_nickname.grid(row=2, column=1, sticky=W, padx=2, pady=7)
      
      # Date of Voting.
      lbl_dateofcrime=Label(upper_frame, text='Date of Voting:', font=('arial',10,'bold'),bg='gray')
      lbl_dateofcrime.grid(row=2, column=2, sticky=W, padx=2, pady=7)
      
      text_dateofcrime=ttk.Entry(upper_frame, width=20, font=('arial',10,'bold'))
      text_dateofcrime.grid(row=2, column=3, sticky=W, padx=2, pady=7)
      
      
      # ===========REGION===========
            
      lbl_dateofcrime=Label(upper_frame, text='Region :', font=('arial',10,'bold'),bg='gray')
      lbl_dateofcrime.grid(row=2, column=4, sticky=W, padx=2, pady=7)
      
      text_dateofcrime=ttk.Entry(upper_frame, width=20, font=('arial',10,'bold'))
      text_dateofcrime.grid(row=2, column=5, sticky=W, padx=2, pady=7)
      
      
      #Address.
      lbl_address=Label(upper_frame, text='Address:', font=('arial',10,'bold'),bg='gray')
      lbl_address.grid(row=3, column=0, sticky=W, padx=2, pady=7)
      
      text_address=ttk.Entry(upper_frame, width=20, font=('arial',10,'bold'))
      text_address.grid(row=3, column=1, sticky=W, padx=2, pady=7)
      
      # Age
      lbl_age=Label(upper_frame, text='Email:', font=('arial',10,'bold'),bg='gray')
      lbl_age.grid(row=3, column=2, sticky=W, padx=2, pady=7)
      
      text_age=ttk.Entry(upper_frame, width=20, font=('arial',10,'bold'))
      text_age.grid(row=3, column=3, sticky=W, padx=2, pady=7)
      
      # Occuption
      lbl_occuption=Label(upper_frame, text='Occuption:', font=('arial',10,'bold'),bg='gray')
      lbl_occuption.grid(row=4, column=0, sticky=W, padx=2, pady=7)
      
      text_occuption=ttk.Entry(upper_frame, width=20, font=('arial',10,'bold'))
      text_occuption.grid(row=4, column=1, sticky=W, padx=2, pady=7)
      
      # D.O.B.
      lbl_dob=Label(upper_frame, text='D.O.B:', font=('arial',10,'bold'),bg='gray')
      lbl_dob.grid(row=4, column=2, sticky=W, padx=2, pady=7)
      
      text_dob=ttk.Entry(upper_frame, width=20, font=('arial',10,'bold'))
      text_dob.grid(row=4, column=3, sticky=W, padx=2, pady=7)
      
      #Crime Type.
      lbl_CrimeType=Label(upper_frame, text='Vote Type:', font=('arial',10,'bold'),bg='gray')
      lbl_CrimeType.grid(row=0, column=4, sticky=W, padx=2, pady=7)
      
      text_CrimeType=ttk.Entry(upper_frame, width=20, font=('arial',10,'bold'))
      text_CrimeType.grid(row=0, column=5, sticky=W, padx=2, pady=7)
      
      #Sex
      lbl_sex=Label(upper_frame, text='Sex:', font=('arial',10,'bold'),bg='gray')
      lbl_sex.grid(row=1, column=4, sticky=W, padx=2, pady=7)
      
      # Radio Button Sex.
      radio_frame_sex=Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
      radio_frame_sex.place(x=625, y=36, width=155, height=30)
      
      male=Radiobutton(radio_frame_sex, text='Male', value='male', font=('arial',9,'bold'),bg='light blue')
      male.grid(row=0, column=0, pady=1, padx=7, sticky=W)
      
      female=Radiobutton(radio_frame_sex, text='Female', value='female', font=('arial',9,'bold'),bg='light blue')
      female.grid(row=0, column=1, pady=1, padx=7, sticky=W)
      
      
      # Buttons
      button_frame=Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
      button_frame.place(x=1, y=175, width=508, height=30)
      
      # add Buttons
      btn_add=Button(button_frame, text='Record save', font=('arial',9,'bold'), width=16, bg='blue', fg='white')
      btn_add.grid(row=0, column=0, padx=3, pady=0)
      
      # Update Button
      btn_update=Button(button_frame, text='Update', font=('arial',9,'bold'), width=16, bg='blue', fg='white')
      btn_update.grid(row=0, column=1, padx=3, pady=0)
      
      #Delete Button
      btn_delete=Button(button_frame, text='Delete', font=('arial',9,'bold'), width=16, bg='blue', fg='white')
      btn_delete.grid(row=0, column=2, padx=3, pady=0)
      
      #Clear Button
      btn_clear=Button(button_frame, text='Clear', font=('arial',9,'bold'), width=15, bg='blue', fg='white')
      btn_clear.grid(row=0, column=3, padx=3, pady=0)
      
      #down_frame.
      down_frame=LabelFrame(main_frame, bd=2, relief=RIDGE,text='Party Information Tabel',font=('times new roman',9,'bold'),fg='red')
      down_frame.place(x=1, y=250, width=1345, height=220)
      
      # search_frame.
      search_frame=LabelFrame(down_frame, bd=2, relief=RIDGE,text='search Party Record',font=('times new roman',9,'bold'),fg='red')
      search_frame.place(x=0, y=0, width=1338, height=60)
      
      search_by=Label(search_frame, text='Search By:', font=('arial',11,'bold'),bg='blue', fg='white')
      search_by.grid(row=0, column=0, sticky=W, padx=5)
      
      combo_search_box=ttk.Combobox(search_frame, font=('arial',11,'bold'), width=18, state='readonly')
      combo_search_box['value']=('Select Option', 'voter_id', 'Adhar_no','Pan Card')
      combo_search_box.current(0)
      combo_search_box.grid(row=0, column=1, sticky=W, padx=5)
      
      search_text=ttk.Entry(search_frame, width=18, font=('arial',11,'bold'))
      search_text.grid(row=0, column=2, sticky=W, padx=5)
      
      #search Button
      btn_search=Button(search_frame, text='Sarch', font=('arial',10,'bold'), width=16, bg='blue', fg='white')
      btn_search.grid(row=0, column=3, padx=5, sticky=W)
      
      #All Button
      btn_all=Button(search_frame, text='Show All', font=('arial',10,'bold'), width=16, bg='blue', fg='white')
      btn_all.grid(row=0, column=4, padx=5, sticky=W)
      
      
      crimeagency=Label(search_frame, text='BLOCKCHAIN BASED SOFTWARE', font=('arial',20,'bold'),width=33,bg='white',fg='crimson')
      crimeagency.grid(row=0, column=5, sticky=W, padx=15, pady=0)
      
      
      #Table Frame
      table_frame=Frame(down_frame, bd=3, relief=RIDGE)
      table_frame.place(x=0, y=60, width=1338, height=140)
      
      
      # Scrollbar
      scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
      
      self.crimnal_table=ttk.Treeview(table_frame, column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
      
      
      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)
      
      scroll_x.config(command=self.crimnal_table.xview)
      scroll_y.config(command=self.crimnal_table.yview)
      
      self.crimnal_table.heading('1',text="PartyID")
      self.crimnal_table.heading('2',text="Fillow No")
      self.crimnal_table.heading('3',text="Candidate Name")
      self.crimnal_table.heading('4',text="Party Name")
      self.crimnal_table.heading('5',text='Voter Id')
      self.crimnal_table.heading('6',text="Voting Date")
      self.crimnal_table.heading('7',text="Address")
      self.crimnal_table.heading('8',text='Email')
      self.crimnal_table.heading('9',text="Occupation")
      self.crimnal_table.heading('10',text="DOB")
      self.crimnal_table.heading('11',text="Pan No")
      self.crimnal_table.heading('12',text="Adhar No")
      self.crimnal_table.heading('13',text="Sex")
     # self.crimnal_table.heading('14',text="Wanted")
      
      self.crimnal_table['show']='headings'
      
      self.crimnal_table.column("1",width=100)
      self.crimnal_table.column("2",width=100)
      self.crimnal_table.column("3",width=100)
      self.crimnal_table.column("4",width=100)
      self.crimnal_table.column("5",width=100)
      self.crimnal_table.column("6",width=100)
      self.crimnal_table.column("7",width=100)
      self.crimnal_table.column("8",width=100)
      self.crimnal_table.column("9",width=100)
      self.crimnal_table.column("10",width=100)
      self.crimnal_table.column("11",width=100)
      self.crimnal_table.column("12",width=100)
      self.crimnal_table.column("13",width=100)
      self.crimnal_table.column("14",width=100)
      
      self.crimnal_table.pack(fill=BOTH,expand=1)
      
     
      
if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
   