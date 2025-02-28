from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import smtplib

from tkcalendar import DateEntry


class Email:
    def __init__(self,root):
        self.root=root
        self.root.title("Appointments")
        self.root.geometry("1580x800+0+0")

        self.AppntId=IntVar()
        self.DateAppnt=StringVar()
        self.TimeAppnt=StringVar()
        self.EmailId=StringVar()
        self.Emailtext=StringVar()
        self._frame=None

        lbltitle=Label(self.root,text ="Appointment Management",bg="light yellow",font=("times new roman",50,"bold"),relief=RIDGE,bd=20)
        lbltitle.pack(side=TOP,fill=X)
        # Frames
        Dataframe=Frame(self.root,bd=10,relief=RIDGE,bg="light yellow")
        Dataframe.place(x=0,y=120,width=1530,height=350)

        DataframeLeft=LabelFrame(Dataframe,text="Appointments",bd=10,relief=RIDGE,padx=5,font=("times new roman",12,"bold"))
        DataframeLeft.place(x=0,y=5,width=760,height=320)

        DataframeRight = LabelFrame(Dataframe, text="Email text", bd=10, relief=RIDGE, padx=5,font=("times new roman", 12, "bold"))
        DataframeRight.place(x=765, y=5, width=740, height=320)

        Buttonframe = Frame(self.root, bd=10, relief=RIDGE)
        Buttonframe.place(x=0, y=475, width=740, height=80)

        Buttonframe1 = Frame(self.root, bd=10, relief=RIDGE)
        Buttonframe1.place(x=800, y=475, width=690, height=80)

        Detailframe=Frame(self.root,relief=RIDGE,bd=10,bg="light yellow")
        Detailframe.place(x=0,y=560,width=1530,height=220)

        # Entry field
        appntid = Label(DataframeLeft, text="Id", font=("times new roman", 20, "bold"), pady=18)
        appntid.grid(row=0, column=0)
        idtext = Entry(DataframeLeft, textvariable=self.AppntId, font=("ariel", 20), width=35,validate='key',validatecommand=(root.register(self.int_input),"%P"))
        idtext.grid(row=0, column=1)

        dateappnt = Label(DataframeLeft, text="Date", font=("times new roman", 20, "bold"), pady=18)
        dateappnt.grid(row=1, column=0)
        date_of_appnt = DateEntry(DataframeLeft, selectmode="day", date_pattern="yyyy-MM-dd", width=55,textvariable=self.DateAppnt)
        date_of_appnt.grid(row=1, column=1)

        timeappnt = Label(DataframeLeft, text="Time", font=("times new roman", 20, "bold"), pady=18,width=12)
        timeappnt.grid(row=2, column=0)
        timetext = Entry(DataframeLeft, textvariable=self.TimeAppnt, font=("ariel", 20), width=35)
        timetext.grid(row=2, column=1)

        emailid = Label(DataframeLeft, text="Email Id", font=("times new roman", 20, "bold"), pady=18, width=12)
        emailid.grid(row=3, column=0)
        emailid = Entry(DataframeLeft, textvariable=self.EmailId, font=("ariel", 20), width=35)
        emailid.grid(row=3, column=1)

        self.Emailtext=Text(DataframeRight,font=("times new roman", 20),width=50,height=9,padx=2,pady=6)
        self.Emailtext.grid(row=0,column=0)

        # Buttons
        viewapp=Button(Buttonframe,text="View Record",font=("times new roman", 15, "bold"), width=19, height=2, padx=2,pady=2, bg="light yellow",command=self.appnt_fetch)
        viewapp.grid(row=0,column=0)

        updateapp = Button(Buttonframe, text="Update", font=("times new roman", 15, "bold"), width=19,height=2, padx=2, pady=2, bg="light yellow",command=self.appnt_update)
        updateapp.grid(row=0, column=1)

        deleteapp = Button(Buttonframe, text="Delete", font=("times new roman", 15, "bold"), width=19,height=2, padx=2, pady=2, bg="light yellow",command=self.appnt_data_delete)
        deleteapp.grid(row=0, column=2)

        sendemail = Button(Buttonframe1, text="Send Email", font=("times new roman", 15, "bold"), width=27,height=2, padx=2, pady=2, bg="light yellow",command=self.send_mail)
        sendemail.grid(row=0, column=0)

        adminpage = Button(Buttonframe1, text="Back", font=("times new roman", 15, "bold"), width=27, height=2,padx=2, pady=2, bg="light yellow",command=lambda: self.back_adminpage())
        adminpage.grid(row=0, column=1)


        # Table view of appointments

        # scroll bar
        scrlx = ttk.Scrollbar(Detailframe, orient=HORIZONTAL)
        scrly = ttk.Scrollbar(Detailframe, orient=VERTICAL)

        self.appnt_table = ttk.Treeview(Detailframe, columns=("appnt_id", "patient_name", "patient_age","patient_sex","pat_email",
                                                              "doctor_id","date_appnt","time_appnt"),
                                        xscrollcommand=scrlx.set, yscrollcommand=scrly.set)
        scrlx.pack(side=BOTTOM, fill=X)
        scrly.pack(side=RIGHT, fill=Y)

        scrlx = ttk.Scrollbar(command=self.appnt_table.xview)
        scrly = ttk.Scrollbar(command=self.appnt_table.yview)

        self.appnt_table.heading("appnt_id", text="Id")
        self.appnt_table.heading("patient_name", text="Name")
        self.appnt_table.heading("patient_age", text="Age")
        self.appnt_table.heading("patient_sex", text="Gender")
        self.appnt_table.heading("pat_email", text="Email Id")
        self.appnt_table.heading("doctor_id", text="Referring Doctor ID")
        self.appnt_table.heading("date_appnt", text="Date Scheduled")
        self.appnt_table.heading("time_appnt", text="Time Scheduled")

        self.appnt_table["show"] = "headings"
        self.appnt_table.pack(fill=BOTH, expand=1)


    def int_input(self,value):
        try:
            if value.isdigit() or value=="":
                return True
            else:
                raise ValueError("")
        except ValueError:
            messagebox.showinfo("Error","Only integers allowed")
            return False

    def appnt_update(self):
            conn = mysql.connector.connect(host='localhost', username='root', password='Example@2023#',
                                           database='hospital')
            curr = conn.cursor()
            curr.execute("select * from appointment where aid=%s",
                         (self.AppntId.get(),))
            rows=curr.fetchall()
            k=0
            for i in rows:
                k=k+1
            if k!=0:
                curr.execute("update appointment set date_of_appointment=%s,time_of_appointment=%s where aid=%s",
                         (self.DateAppnt.get(), self.TimeAppnt.get(), self.AppntId.get()))
                messagebox.showinfo("Status", "Updated")
                conn.commit()
                conn.close()
                self.AppntId.set("")
                self.DateAppnt.set("")
                self.TimeAppnt.set("")
            else:
                messagebox.showinfo("Error","Incorrect data")
    def appnt_data_delete(self):
            conn = mysql.connector.connect(host='localhost', username='root', password='Example@2023#',
                                           database='hospital')
            curr = conn.cursor()
            curr.execute("select * from appointment where aid=%s",
                         (self.AppntId.get(),))
            rows = curr.fetchall()
            k = 0
            for i in rows:
                k = k + 1
            if k != 0:
                curr.execute("delete from appointment where aid=%s", (self.AppntId.get(),))
                messagebox.showinfo("Status", "Deleted")
                conn.commit()
                conn.close()
                self.AppntId.set("")
            else:
                messagebox.showinfo("Error","Data does not exist")
    def appnt_fetch(self):
            conn = mysql.connector.connect(host='localhost', username='root', password='Example@2023#',
                                           database='hospital')
            curr = conn.cursor()
            curr.execute("select * from appointment")
            rows = curr.fetchall()
            if len(rows) != 0:
                self.appnt_table.delete(*self.appnt_table.get_children())
                for i in rows:
                    self.appnt_table.insert("", END, values=i)
            conn.commit()
            conn.close()

    def send_mail(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Example@2023#",database="hospital")
        curr=conn.cursor()
        curr.execute("select * from appointment where email=%s",(self.EmailId.get(),))
        row=curr.fetchall()
        k=0
        for i in row:
            k=k+1
        if k!=0:
            myemail = "aditisinghvns66@gmail.com"
            pasword="mfshggsnybrasflv"
            connection = smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()  # Making connection secure to prevent illegal reading of email data
            connection.login(user=myemail, password=pasword)
            connection.sendmail(from_addr=myemail, to_addrs=self.EmailId.get(), msg=self.Emailtext.get("1.0", END))
            messagebox.showinfo("Status", "Sent")
            connection.close()
        else:
            messagebox.showinfo("Error","Incorrect email id")
    def back_adminpage(self):
        root.destroy()
        import admin






root = Tk()
obj=Email(root)
root.mainloop()

