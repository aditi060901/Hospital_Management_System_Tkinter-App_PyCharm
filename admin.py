
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import mysql.connector
from tkcalendar import DateEntry
from datetime import datetime, date, timedelta
import keyboard


class Admin:

    def __init__(self,rooot):
        self.rooot = rooot
        self.rooot.title("Admin Page")
        self.rooot.geometry("1540x800+0+0")

        self.DoctorId=IntVar()
        self.DoctorName=StringVar()
        self.DoctorSpec = StringVar()
        self.ScheDate = StringVar()
        self.ScheTime = StringVar()
        self.DoctorId_Sche = IntVar()
        self.DoctorWorkhr=StringVar()



        # Heading
        lbltitle=Label(self.rooot,bd=10,relief=RIDGE,text="Administrator",font=("times new roman",50,"bold"),bg='light green')
        lbltitle.pack(side=TOP,fill=X)

        # First frame
        Dataframe=Frame(self.rooot,bd=20,relief=RIDGE,bg="light green")

        Dataframe.place(x=0,y=110,width=1530,height=300)
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10, font=("times new roman",12,"bold"),text="Doctor Details")
        DataframeLeft.place(x=0,y=5,width=765,height=250)
        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),text="Schedule Appointment")
        DataframeRight.place(x=768, y=5, width=720, height=250)

        # Button Frame
        Buttonframe = Frame(self.rooot, bd=10, relief=RIDGE)
        Buttonframe.place(x=0, y=420, width=1530, height=100)

        # Details frame
        Detailframe = Frame(self.rooot, bd=20, relief=RIDGE,bg="light green")
        Detailframe.place(x=0, y=525, width=1530, height=250)
        DetailframeLeft = LabelFrame(Detailframe, bd=5, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),text="Doctor Details")
        DetailframeLeft.place(x=0, y=5, width=765, height=200)
        DetailframeRight = LabelFrame(Detailframe, bd=5, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),text="Schedules")
        DetailframeRight.place(x=768, y=5, width=720, height=200)


        # Labels and entry fields

        docid=Label(DataframeLeft, text="Id", font=("times new roman", 20, "bold"),pady=5)
        docid.grid(row=0,column=0)
        idtext=Entry(DataframeLeft,textvariable=self.DoctorId,font=("ariel",20),width=35,validate='key',validatecommand=(rooot.register(self.int_input),"%P"))
        idtext.grid(row=0,column=1)

        docname=Label(DataframeLeft,text="Name",font=("times new roman", 20, "bold"),pady=7)
        docname.grid(row=1,column=0)
        docnametxt=Entry(DataframeLeft,textvariable=self.DoctorName,font=("ariel",20),width=35,validate='key',validatecommand=(rooot.register(self.str_input),"%P"))
        docnametxt.grid(row=1,column=1)

        docspec = Label(DataframeLeft, text="Specialisation", font=("times new roman", 20, "bold"), pady=7)
        docspec.grid(row=2,column=0)
        docspectxt = Entry(DataframeLeft,textvariable=self.DoctorSpec, font=("ariel", 20), width=35,validate='key',validatecommand=(rooot.register(self.str_input),"%P"))
        docspectxt.grid(row=2, column=1)

        docworkhr=Label(DataframeLeft, text="Working Hour", font=("times new roman", 20, "bold"), pady=7)
        docworkhr.grid(row=3,column=0)
        docworkhrtxt = Entry(DataframeLeft,textvariable=self.DoctorWorkhr, font=("ariel", 20), width=35)
        docworkhrtxt.grid(row=3, column=1)

        dateofappnt=Label(DataframeRight,text="Date",font=("times new roman", 20, "bold"),pady=15)
        dateofappnt.grid(row=1,column=0)
        datee=date.today()+timedelta(days=2)
        date_of_appnt = DateEntry(DataframeRight, selectmode="day", date_pattern="yyyy-MM-dd", width=55,textvariable=self.ScheDate,mindate=datee)
        date_of_appnt.grid(row=1, column=1)


        timeofappnt=Label(DataframeRight,text="Time",font=("times new roman", 20, "bold"),pady=15)
        timeofappnt.grid(row=2,column=0)

        timetxt = Entry(DataframeRight,textvariable=self.ScheTime, font=("ariel", 20), width=35)
        timetxt.grid(row=2, column=1)

        did= Label(DataframeRight, text="Doctor Id", font=("times new roman", 20, "bold"), pady=15)
        did.grid(row=0,column=0)
        didtxt = Entry(DataframeRight,textvariable=self.DoctorId_Sche,font=("ariel", 20), width=35,validate='key',validatecommand=(rooot.register(self.int_input),"%P"))
        didtxt.grid(row=0, column=1)

        # Buttons code
        addoc = Button(Buttonframe, text="Add", font=("times new roman", 15, "bold"), width=15, height=2, padx=2,pady=6, bg="light green", command=self.doctor_data)
        addoc.grid(row=0, column=0)
        updoc = Button(Buttonframe, text="Delete", font=("times new roman", 15, "bold"), width=15, height=2, padx=2,pady=6, bg="light green",command=self.doctor_data_delete)
        updoc.grid(row=0, column=1)
        viewdoc = Button(Buttonframe, text="View Doctors", font=("times new roman", 15, "bold"), width=15, height=2, padx=2, pady=6, bg="light green",command=self.doctor_fetch)
        viewdoc.grid(row=0, column=2)

        viewappnt = Button(Buttonframe, text="View Appointments", font=("times new roman", 15, "bold"), width=15, height=2, padx=2,pady=6, bg="light green",command=lambda: self.email_page())
        viewappnt.grid(row=0, column=3)


        addsch = Button(Buttonframe, text="Add", font=("times new roman", 15, "bold"), width=15, height=2, padx=2,pady=6, bg="light green",command=self.schedule_data)
        addsch.grid(row=0, column=4)
        upsch = Button(Buttonframe, text="Delete", font=("times new roman", 15, "bold"), width=15, height=2, padx=2,pady=6, bg="light green",command=self.schedule_data_delete)
        upsch.grid(row=0, column=5)
        viewsch = Button(Buttonframe, text="View Schedules", font=("times new roman", 15, "bold"), width=15, height=2, padx=2,pady=6, bg="light green",command=self.schedule_fetch)
        viewsch.grid(row=0, column=6)

        logout = Button(Buttonframe, text="Logout", font=("times new roman", 15, "bold"), width=13, height=2, padx=2,pady=6, bg="light green",command=self.main_screen)
        logout.grid(row=0, column=7)

        # Table view of doctors and schedules

        #scroll bar
        scrlx=ttk.Scrollbar(DetailframeLeft,orient=HORIZONTAL)
        scrly=ttk.Scrollbar(DetailframeLeft,orient=VERTICAL)
        scrl_x = ttk.Scrollbar(DetailframeRight, orient=HORIZONTAL)
        scrl_y = ttk.Scrollbar(DetailframeRight, orient=VERTICAL)

        # Doctor Table

        self.doctor_table=ttk.Treeview(DetailframeLeft,columns=("doctor_id","doctor_name","doctor_spec","doctor_work"),xscrollcommand=scrlx.set,yscrollcommand=scrly.set)
        scrlx.pack(side=BOTTOM,fill=X)
        scrly.pack(side=RIGHT,fill=Y)

        scrlx=ttk.Scrollbar(command=self.doctor_table.xview)
        scrly = ttk.Scrollbar(command=self.doctor_table.yview)

        self.doctor_table.heading("doctor_id",text="Doctor Id")
        self.doctor_table.heading("doctor_name", text="Name")
        self.doctor_table.heading("doctor_spec", text="Specialisation")
        self.doctor_table.heading("doctor_work", text="Work Hour")

        self.doctor_table["show"]="headings"
        self.doctor_table.pack(fill=BOTH,expand=1)

        # Schedule table

        self.schedules_table = ttk.Treeview(DetailframeRight, columns=("doc_id", "sch_date", "sch_time"), xscrollcommand=scrl_x.set, yscrollcommand=scrl_y.set)
        scrl_x.pack(side=BOTTOM, fill=X)
        scrl_y.pack(side=RIGHT, fill=Y)

        scrl_x = ttk.Scrollbar(command=self.schedules_table.xview)
        scrl_y = ttk.Scrollbar(command=self.schedules_table.yview)

        self.schedules_table.heading("doc_id", text="Doctor Id")
        self.schedules_table.heading("sch_date", text="Scheduled Date")
        self.schedules_table.heading("sch_time", text="Scheduled Time")

        self.schedules_table["show"] = "headings"
        self.schedules_table.pack(fill=BOTH, expand=1)

        # Functionality declaration

    def str_input(self,value):
        try:
            if value.isalpha():
                return True
            else:
                raise ValueError("")

        except ValueError:

            messagebox.showinfo("Error", "Only characters allowed")

            return False

    def int_input(self,value):
        try:
            if value.isdigit() or value=="":
                return True

            else:
                raise ValueError("")
        except ValueError:
            messagebox.showinfo("Error","Only integers allowed")
            return False

    def doctor_data(self):

        conn = mysql.connector.connect(host='localhost', username='root', password='Example@2023#', database='hospital')
        curr = conn.cursor()
        try:
            curr.execute("insert into doctor values(%s,%s,%s,%s)",( self.DoctorId.get(),self.DoctorName.get(),self.DoctorSpec.get(),self.DoctorWorkhr.get()))
            messagebox.showinfo("Status","Saved")
            conn.commit()
            conn.close()
            self.DoctorId.set(0)
            self.DoctorName.set("")
            self.DoctorSpec.set("")
            self.DoctorWorkhr.set("")
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Error","Data exists")

    def doctor_data_delete(self):

        conn = mysql.connector.connect(host='localhost', username='root', password='Example@2023#', database='hospital')
        curr = conn.cursor()
        curr.execute("select  * from doctor where did=(%s)", (self.DoctorId.get(),))
        row=curr.fetchall()
        p=0
        for i in row:
            p=p+1
        if p!=0:
            curr.execute("delete from appointment where did=(%s)", (self.DoctorId.get(),))
            curr.execute("delete from schedules where did=(%s)", (self.DoctorId.get(),))
            curr.execute("delete from doctor where did=(%s)", (self.DoctorId.get(),))
            messagebox.showinfo("Status","Deleted")
            conn.commit()
            conn.close()
            self.DoctorId.set(0)
        else:
            messagebox.showinfo("Error","Data does not exist")

    def doctor_fetch(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Example@2023#', database='hospital')
        curr = conn.cursor()
        curr.execute("select * from doctor")
        rows=curr.fetchall()
        if len(rows)!=0:
            self.doctor_table.delete(*self.doctor_table.get_children())
            for i in rows:
                self.doctor_table.insert("", END, values=i)
        conn.commit()
        conn.close()

    def schedule_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Example@2023#', database='hospital')
        curr = conn.cursor()
        try:
            curr.execute("insert into schedules values(%s,%s,%s)",(self.DoctorId_Sche.get(),self.ScheDate.get(),self.ScheTime.get()))
            messagebox.showinfo("Status","Saved")
            conn.commit()
            conn.close()
            self.ScheTime.set("")
            self.DoctorId_Sche.set(0)
        except mysql.connector.IntegrityError:
            messagebox.showinfo("Error","Data already exists")

    def schedule_data_delete(self):

        conn = mysql.connector.connect(host='localhost', username='root', password='Example@2023#', database='hospital')
        curr = conn.cursor()
        b=self.ScheDate.get()
        c=self.ScheTime.get()
        curr.execute("select * from schedules where (date_of_appointment=%s) and (time_of_appointment=%s) and (did=%s)",
                     (b, c, self.DoctorId_Sche.get()))
        row=curr.fetchall()
        p=0
        for i in row:
            p=p+1
        if p!=0:

            curr.execute("delete from appointment where (date_of_appointment=%s) and (time_of_appointment=%s) and (did=%s)",
                     (b, c, self.DoctorId_Sche.get()))
            curr.execute("delete from schedules where (date_of_appointment=%s) and (time_of_appointment=%s) and (did=%s)",
                     (b, c, self.DoctorId_Sche.get()))
            messagebox.showinfo("Status", "Deleted")
            conn.commit()
            conn.close()
            self.ScheDate.set("")
            self.ScheTime.set("")
            self.DoctorId_Sche.set("")
        else:
            messagebox.showinfo("Error","Data does not exist")

    def schedule_fetch(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Example@2023#', database='hospital')
        curr = conn.cursor()
        """curr.execute("delete from appointment where (date_of_appointment<%s) or (date_of_appointment=%s and time_of_appointment<%s)",(date.today(),date.today(),datetime.now().strftime("%H:%M:%S")))
        curr.execute("delete from schedules where (date_of_appointment<%s) or (date_of_appointment=%s and time_of_appointment<%s)",(date.today(),date.today(),datetime.now().strftime("%H:%M:%S")))"""
        curr.execute("select * from schedules ")
        rows=curr.fetchall()
        if len(rows)!=0:
            self.schedules_table.delete(*self.schedules_table.get_children())
            for i in rows:
                self.schedules_table.insert("", END, values=i)
        conn.commit()
        conn.close()


    def email_page(self):
        rooot.destroy()
        import sendingemail

    def main_screen(self):
        rooot.destroy()
        import mainscreen


rooot = Tk()



obj = Admin(rooot)
rooot.mainloop()








