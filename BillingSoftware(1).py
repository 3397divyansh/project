from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random# random bill generating
import os
import tempfile #print
from tkinter import messagebox #to show message while saving
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        
        # Variables===============
        self.c_name=StringVar()
        self.c_phon = StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email = StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        
        
        
        # Product categories List
        self.Category=["Select Option" , "Clothing" ,"LifeStyle", "Mobiles"]
        self.SubCatCloathing = ["Pant","T_Shirt","IShirt"]
        self.pant = ["Levis","Raymond","Mufti","Sparky","RedTape"]
        self.price_levis = 5000
        self.price_Raymond = 7000
        self.price_Mufti = 1500
        self.price_Sparky= 8000
        self.price_Redtape= 800
        
        self.T_Shirt = ["Polo","Roadster","Jack&Jones"]
        self.price_polo = 1500
        self.price_Roadster= 1800
        self.price_JackJones= 3800
        
        self.IShirt=["Peter_England","Louis_Phillips","Park_Avenue"]
        self.price_Peter = 2100
        self.price_Louis = 2700
        self.price_Park = 1740
        
        # SubCatLife
        
        self.SubCatLife = ["Bath_Shop","Hair_oil","Face_cream"]
        
        self.Bath_Shop = ["LifeBuy","Lux","Santoor","Pearl"]
        self.price_LifeBuy = float(20)
        self.price_Lux=float(50)
        self.price_Santoor = float(40)
        self.price_Pearl=float(450)
        
        self.Hair_oil = ["ParaChute" , "Jashmin" , "Bajaj"]
        self.price_Para = 25
        self.price_Jashmin = 22
        self.price_bajaj = 30
        
        self.Face_cream = ["Fair&Lovely", "Ponds" , "Olay","Garnier"]
        self.price_fair = 25
        self.price_ponds = 80
        self.price_olay = 50
        self.price_garnier = 45
        
        # Mobils
        self.SubMobil= ["Iphone","Samsung","Xiome","RealMe","One+"]
        self.Iphone = ["Iphone_X","Iphone_11","Iphone_12","Iphone_13","Iphone_14"]
        self.price_ix = 40000
        self.price_i11 = 45000
        self.price_i12 = 50000
        self.price_i13 = 85000
        self.price_i14 = 114000
        
        self.Samsung = ["Samsung_M16" , "Samsung_M12","Samsung_M21"]
        self.price_sm16 = 20000
        self.price_sm12 = 25000
        self.price_sm21 = 18000
        
        self.Xiome = ["Red11" , "Redme-12","RedmePro"]
        self.price_r11 = 10000
        self.price_r12 = 22000
        self.price_rpro = 17000
        
        self.RealMe = ["RealMe_12" , "RealMe_13","RealMe_Pro"]
        self.price_rel12 = 25000
        self.price_rel13 = 22000
        self.price_relpro = 11000
        
        
        self.OnePlus = ["OnePlus1" , "OnePlus2","OnePlus3"]
        self.price_one1 = 55000
        self.price_one2 = 32050
        self.price_one3 = 21000
        
        
        
        
        

        
        # Image = 1
        img = Image.open("image/a5.jpg")
        img = img.resize((500,200))#converts hight level imag eto low level
        self.pic = ImageTk.PhotoImage(img)
        
        lbl_img = Label(self.root,image=self.pic)
        lbl_img.place(x=0,y=0,width=500,height=200)
        
        # Image = 2
        img1 = Image.open("image/a4.jpg")
        img1 = img1.resize((500,200),Image.ANTIALIAS)
        self.pic1 = ImageTk.PhotoImage(img1)
        
        lbl_img1 = Label(self.root,image=self.pic1)
        lbl_img1.place(x=500,y=0,width=500,height=200)
        
        # Image = 3
        img2 = Image.open("image/a1.jpg")
        img2 = img2.resize((540,200),Image.ANTIALIAS)
        self.pic2 = ImageTk.PhotoImage(img2)
        
        lbl_img2 = Label(self.root,image=self.pic2)
        lbl_img2.place(x=1000,y=0,width=520,height=200)
        
        lbl_title = Label(self.root , text="Billing Software" , font=("times new roman",35,"bold"),bg = "white",fg="red")
        lbl_title.place(x=0,y=180,width=1530,height=60)
        
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
        
        lbl = Label(lbl_title,font=('times new roman',16,'bold'),background='white',fg='blue')
        lbl.place(x=0,y = 0,width=120,height=45)
        time()
            
        
        Main_Frame = Frame(self.root,bd=5,relief=GROOVE,bg="white",)
        Main_Frame.place(x=0, y=240,width=1530,height=620)
        
        # Customer leval Frem
        Cust_Frame = LabelFrame(Main_Frame , text="Customer",font=("times new roman",12,"bold"),bg = "white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)
        
        
        self.lbl_mob = Label(Cust_Frame,text="Mobile No .",font=("times new roman",12,"bold"),bg = "white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_mob = ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)
        
        self.lblCustName = Label(Cust_Frame,text="Customer Name .",font=("times new roman",12,"bold"),bg="white",bd=6)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.txtCus = ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=24)
        self.txtCus.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.lblem = Label(Cust_Frame,text="Email ",font=("times new roman",12,"bold"),bg = "white",bd=4)
        self.lblem.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.txtiml = ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=24)
        self.txtiml.grid(row=2,column=1)
        
        # Product leval Frem
        Pro_Frame = LabelFrame(Main_Frame , text="Product",font=("times new roman",12,"bold"),bg = "white",fg="red")
        Pro_Frame.place(x=400,y=5,width=600,height=140)
        
        # Select Categories
        self.lblCa = Label(Pro_Frame,text="Select Categories ",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblCa.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.ComboCa = ttk.Combobox(Pro_Frame,value=self.Category,font=("arial" ,12, "bold"),width=18,state="readonly")
        self.ComboCa.current(0)
        self.ComboCa.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.ComboCa.bind("<<ComboboxSelected>>",self.Categories)
        
        # Subcategory
        self.lblCa = Label(Pro_Frame,text="Subcategory ",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblCa.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.ComboCa1 = ttk.Combobox(Pro_Frame,value=[""],font=("arial" ,12, "bold"),width=18,state="readonly")
        self.ComboCa1.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboCa1.bind("<<ComboboxSelected>>",self.ProductAdd)
        
        # Product Name 
        self.lblCa = Label(Pro_Frame,text="Product Name ",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblCa.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.ComboCa2 = ttk.Combobox(Pro_Frame,textvariable=self.product,font=("arial" ,12, "bold"),width=18,state="readonly")
        self.ComboCa2.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboCa2.bind("<<ComboboxSelected>>",self.price)
        
        # Price
        self.lblPr = Label(Pro_Frame,text="Price ",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblPr.grid(row=0,column=2,sticky=W,padx=5,pady=2)
        self.ComboPr = ttk.Combobox(Pro_Frame,textvariable=self.prices,font=("arial" ,12, "bold"),width=18,state="readonly")
        self.ComboPr.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        
        # Qty
        self.lblQu = Label(Pro_Frame,text="Qty ",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblQu.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        self.ComboQu = ttk.Combobox(Pro_Frame,textvariable=self.qty,font=("arial" ,12, "bold"),width=18,state="readonly")
        self.ComboQu.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        
        # Search Bar
        Srch_Frem = Frame(Main_Frame,bd=2,bg="white")
        Srch_Frem.place(x=1120,y=10,width=500,height=40)
        
        self.lblBil = Label(Main_Frame,text="Bill Number ",font=("times new roman",12,"bold"),bg="red",fg="white")
        self.lblBil.grid(row=0,column=0,sticky=W,padx=1032,pady=16)
        
        self.ComboBil = ttk.Entry(Srch_Frem,textvariable=self.search_bill,font=("times new roman",12,"bold"),width=30)
        self.ComboBil.grid(row=0,column=1,sticky=W,padx=2,pady=2)
        
        self.Search = Button(Srch_Frem,command=self.find_bill,text="Search",font=("times new roman",9,"bold"),bg="red",fg="white",width=9,cursor="hand2")
        self.Search.grid(row = 0,column=2)
        
        # Image in middle
        
        # Image = 1
        imge = Image.open("image/a2.jpg")
        imge = imge.resize((500,400),Image.ANTIALIAS)
        self.pick = ImageTk.PhotoImage(imge)
        
        lbl_imge = Label(self.root,image=self.pick)
        lbl_imge.place(x=11,y=400,width=500,height=270)
        
        # Image = 2
        imge1 = Image.open("image/a3.jpg")
        imge1 = imge1.resize((500,400),Image.ANTIALIAS)
        self.pick1 = ImageTk.PhotoImage(imge1)
        
        lbl_imge1 = Label(self.root,image=self.pick1)
        lbl_imge1.place(x=520,y=400,width=490,height=270)
        
        # Right Side Bill Area
        RightLableFrem = LabelFrame(Main_Frame , text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLableFrem.place(x=1030,y=45,width=450,height=380)
        
        Scrollbar_y=Scrollbar(RightLableFrem,orient=VERTICAL)
        self.textarea = Text(RightLableFrem,yscrollcommand=Scrollbar_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        # Bill Counter  Frem
        Bottem_Frame = LabelFrame(Main_Frame , text="Bill Counter",font=("times new roman",12,"bold"),bg = "white",fg="red")
        Bottem_Frame.place(x=0,y=425,width=1500,height=115)
        
        # Sub total
        self.lblSubTotal = Label(Bottem_Frame,text="Sub Total ",font=("times new roman",12,"bold"),bg="white")
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.ComboSubtotal = ttk.Entry(Bottem_Frame,textvariable=self.sub_total,font=("arial" ,12, "bold"),width=23)
        self.ComboSubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        # Tax
        self.lbltax = Label(Bottem_Frame,text="Gov Tax ",font=("times new roman",12,"bold"),bg="white")
        self.lbltax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.Combotax = ttk.Entry(Bottem_Frame,textvariable=self.tax_input,font=("times new roman",12,"bold"),width=26)
        self.Combotax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        # Total Amount
        self.lblTa = Label(Bottem_Frame,text="TotalAmount ",font=("times new roman",12,"bold"),bg="white")
        self.lblTa.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.ComboTa = ttk.Entry(Bottem_Frame,textvariable=self.total,font=("arial" ,12, "bold"),width=23)
        self.ComboTa.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        # Buttons
        Btn_Frem = Frame(Bottem_Frame,bd=2,bg="white")
        Btn_Frem.place(x=360,y=10)
        
        self.BtnAddToCard = Button(Btn_Frem,command=self.AddItems,height = 2,text="Add To Cart",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCard.grid(row = 0,column=0)
        
        self.Bill = Button(Btn_Frem,command=self.gen_bill,height = 2,text="Generate Bill",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Bill.grid(row = 0,column=1)
        
        self.Save = Button(Btn_Frem,command=self.save_bill,height = 2,text="Save Bill",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Save.grid(row = 0,column=2)
        
        self.PrintBill = Button(Btn_Frem,command=self.Print_Bill,height = 2,text="Print",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.PrintBill.grid(row = 0,column=3)
        
        self.Clear = Button(Btn_Frem,command=self.clear,height = 2,text="Clear",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Clear.grid(row = 0,column=4)
        
        self.Exit = Button(Btn_Frem,command=self.root.destroy,height = 2,text="Exit",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Exit.grid(row = 0,column=5)        
        self.welcome()
        self.l=[]
    # =====================Function Declearation
    
    
    
    def AddItems(self):
        Tax = 1
        self.n=self.prices.get()
        self.m = self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select The Product")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))
    
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add Items")
        else:
            text = self.textarea.get(10.0,(10.0+float(len(self.l)))) 
            self.welcome() 
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n===============================================") 
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n===============================================") 
    
    def save_bill(self):
        op = messagebox.askyesno("Save Bill" , "Do You Want to Save Bill")
        if op > 0:
            self.bill_data = self.textarea.get(1.0,END)
            f1 = open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            f1.close()
        op = messagebox.showinfo("Saved" , f"Bill No : {self.bill_no.get()} Saved Successfully")
    
    def Print_Bill(self):
        q = self.textarea.get(1.0,"end-1c")
        filename = tempfile.mktemp(".txt")
        open(filename,'w').write(q)
        os.startfile(filename,"print")
    
    def find_bill(self):
        found = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found = "yes"
        if found == "no":
            messagebox.showerror("Error","Invalid Bill No")
                
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        z=random.randint(1000,9999)
        self.bill_no.set(str(z))
        self.c_email.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set('')
        self.total.set("")
        self.welcome()
                       
                
    
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t Welcome CSR Mini Mall")
        self.textarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Mobile Number : {self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email : {self.c_email.get()}")
        
        self.textarea.insert(END , "\n===============================================")
        self.textarea.insert(END,f"\n Product\t\t\tQTY\t\tPrice")
        self.textarea.insert(END , "\n===============================================")
        
        
    def Categories(self,event="") :
        if self.ComboCa.get()=="Clothing":
            self.ComboCa1.config(value = self.SubCatCloathing)
            self.ComboCa1.current(0)
        
        if self.ComboCa.get()=="LifeStyle":
            self.ComboCa1.config(value = self.SubCatLife)
            self.ComboCa1.current(0)
            
        if self.ComboCa.get()=="Mobiles":
            self.ComboCa1.config(value = self.SubMobil)
            self.ComboCa1.current(0)
    
    def ProductAdd(self,event=""):
        if self.ComboCa1.get()=="Pant":
            self.ComboCa2.config(value=self.pant)
            self.ComboCa2.current(0)
        
        if self.ComboCa1.get()=="T_Shirt":
            self.ComboCa2.config(value=self.T_Shirt)
            self.ComboCa2.current(0)
        
        if self.ComboCa1.get()=="IShirt":
            self.ComboCa2.config(value=self.IShirt)
            self.ComboCa2.current(0)
            
        if self.ComboCa1.get()=="Bath_Shop":
            self.ComboCa2.config(value=self.Bath_Shop)
            self.ComboCa2.current(0)
            
        if self.ComboCa1.get()=="Hair_oil":
            self.ComboCa2.config(value=self.Hair_oil)
            self.ComboCa2.current(0)
            
        if self.ComboCa1.get()=="Face_cream":
            self.ComboCa2.config(value=self.Face_cream)
            self.ComboCa2.current(0)
            
        if self.ComboCa1.get()=="Iphone":
            self.ComboCa2.config(value=self.Iphone)
            self.ComboCa2.current(0)
            
        if self.ComboCa1.get()=="Samsung":
            self.ComboCa2.config(value=self.Samsung)
            self.ComboCa2.current(0)
            
        if self.ComboCa1.get()=="Xiome":
            self.ComboCa2.config(value=self.Xiome)
            self.ComboCa2.current(0)
        
        if self.ComboCa1.get()=="RealMe":
            self.ComboCa2.config(value=self.RealMe)
            self.ComboCa2.current(0)
            
    def price(self,event=""):
        if self.ComboCa2.get()=="Levis":
            self.ComboPr.config(value=self.price_levis)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Raymond":
            self.ComboPr.config(value=self.price_Raymond)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Mufti":
            self.ComboPr.config(value=self.price_Mufti)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="Sparky":
            self.ComboPr.config(value=self.price_Sparky)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="RedTape":
            self.ComboPr.config(value=self.price_Redtape)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="Polo":
            self.ComboPr.config(value=self.price_polo)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Roadster":
            self.ComboPr.config(value=self.price_Roadster)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Jack&Jones":
            self.ComboPr.config(value=self.price_JackJones)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="Peter_England":
            self.ComboPr.config(value=self.price_Peter)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Louis_Phillips":
            self.ComboPr.config(value=self.price_Peter)
            self.ComboPr.current(0)
            self.qty.set(1)
        if self.ComboCa2.get()=="Park_Avenue":
            self.ComboPr.config(value=self.price_Park)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        
        if self.ComboCa2.get()=="LifeBuy":
            self.ComboPr.config(value=self.price_LifeBuy)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Santoor":
            self.ComboPr.config(value=self.price_Santoor)
            self.ComboPr.current(0)
            self.qty.set(1)
                
        if self.ComboCa2.get()=="Lux":
            self.ComboPr.config(value=self.price_Lux)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Pearl":
            self.ComboPr.config(value=self.price_Pearl)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="ParaChute":
            self.ComboPr.config(value=self.price_Para)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Jashmin":
            self.ComboPr.config(value=self.price_Jashmin)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Bajaj":
            self.ComboPr.config(value=self.price_bajaj)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="Fair&Lovely":
            self.ComboPr.config(value=self.price_fair)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Ponds":
            self.ComboPr.config(value=self.price_ponds)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="Olay":
            self.ComboPr.config(value=self.price_olay)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="Garnier":
            self.ComboPr.config(value=self.price_ix)
            self.ComboPr.current(0)
            self.qty.set(1)
        
            
        if self.ComboCa2.get()=="Iphone_X":
            self.ComboPr.config(value=self.price_i11)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="Iphone_12":
            self.ComboPr.config(value=self.price_i12)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Iphone_13":
            self.ComboPr.config(value=self.price_i13)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="Iphone_14":
            self.ComboPr.config(value=self.price_i14)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        
        if self.ComboCa2.get()=="Samsung_M16":
            self.ComboPr.config(value=self.price_sm16)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="Samsung_M12":
            self.ComboPr.config(value=self.price_sm12)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="Red11":
            self.ComboPr.config(value=self.price_r11)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="Redme-12":
            self.ComboPr.config(value=self.price_r12)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="RedmePro":
            self.ComboPr.config(value=self.price_rpro)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="RealMe_12":
            self.ComboPr.config(value=self.price_rel12)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="RealMe_13":
            self.ComboPr.config(value=self.price_rel13)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="RealMe_Pro":
            self.ComboPr.config(value=self.price_relpro)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="OnePlus1":
            self.ComboPr.config(value=self.price_one1)
            self.ComboPr.current(0)
            self.qty.set(1)
            
        if self.ComboCa2.get()=="OnePlus2":
            self.ComboPr.config(value=self.price_one2)
            self.ComboPr.current(0)
            self.qty.set(1)
        
        if self.ComboCa2.get()=="OnePlus3":
            self.ComboPr.config(value=self.price_one3)
            self.ComboPr.current(0)
            self.qty.set(1)
    
    
if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
    