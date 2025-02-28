from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
import mysql.connector
from tkcalendar import DateEntry
from tktimepicker import AnalogPicker, constants
from datetime import datetime,date,timedelta
from fpdf import FPDF
from tkinter.filedialog import asksaveasfile


"""class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message"""

class Appoint:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1580x800+0+0")
        self.root.title("Appointment Booking")
        self.patient=StringVar()
        self.age=IntVar()
        self.sex=StringVar()
        self.patient_email=StringVar()
        self.doctor_id=IntVar()
        self.dateof=StringVar()


        lbltitle = Label(self.root, text="Appointment Booking", bg="light blue",font=("times new roman", 50, "bold"), relief=RIDGE, bd=20)
        lbltitle.pack(side=TOP, fill=X)

        Dataframe = Frame(self.root, bd=10, relief=RIDGE, bg="light blue")
        Dataframe.place(x=0, y=120, width=1530, height=680)
        DataframeLeft = LabelFrame(Dataframe, bd=5, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),
                                     text="Patient Details")
        DataframeLeft.place(x=0, y=3, width=765, height=650)
        DataframeRight = LabelFrame(Dataframe, bd=5, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),
                                      text="Doctors")
        DataframeRight.place(x=770, y=5, width=738, height=300)

        Buttonframe=Frame(Dataframe,bd=5, relief=RIDGE)
        Buttonframe.place(x=800,y=310,width=300,height=100)

        Buttonframe1=Frame(Dataframe,bd=5, relief=RIDGE)
        Buttonframe1.place(x=1200,y=310,width=300,height=100)

        Buttonframe3 = Frame(Dataframe, bd=5, relief=RIDGE)
        Buttonframe3.place(x=800, y=430, width=300, height=100)

        Buttonframe4 = Frame(Dataframe, bd=5, relief=RIDGE)
        Buttonframe4.place(x=1200, y=430, width=300, height=100)

        Buttonframe2=Frame(Dataframe,bd=5, relief=RIDGE)
        Buttonframe2.place(x=1000,y=540,width=300,height=100)




        patientname = Label(DataframeLeft, text="Name", font=("times new roman", 25, "bold"), pady=4,width=15)
        patientname.grid(row=0, column=0)
        nametext = Entry(DataframeLeft, font=("ariel", 25),textvariable=self.patient, width=15,validate='key',validatecommand=(root.register(self.name_input),"%P"))
        nametext.grid(row=0, column=1)

        patientage = Label(DataframeLeft, text="Age", font=("times new roman", 25, "bold"), pady=4, width=15)
        patientage.grid(row=1, column=0)
        agetext = Entry(DataframeLeft, textvariable=self.age, font=("ariel", 25), width=15,validate='key',validatecommand=(root.register(self.int_input),"%P"))
        agetext.grid(row=1, column=1)

        patientsex = Label(DataframeLeft, text="Gender", font=("times new roman", 25, "bold"), pady=4, width=15)
        patientsex.grid(row=2, column=0)
        sextext = Entry(DataframeLeft, textvariable=self.sex, font=("ariel", 25), width=15,validate='key',validatecommand=(root.register(self.name_input),"%P"))
        sextext.grid(row=2, column=1)

        patientemail = Label(DataframeLeft, text="Email Id", font=("times new roman", 25, "bold"), pady=4, width=15)
        patientemail.grid(row=3, column=0)
        emailtxt = Entry(DataframeLeft, textvariable=self.patient_email, font=("ariel", 25), width=15)
        emailtxt.grid(row=3, column=1)

        docid = Label(DataframeLeft, text="Doctor Id", font=("times new roman", 25, "bold"), pady=4, width=15)
        docid.grid(row=4, column=0)
        doctext = Entry(DataframeLeft, textvariable=self.doctor_id, font=("ariel", 25), width=15,validate='key',validatecommand=(root.register(self.int_input),"%P"))
        doctext.grid(row=4, column=1)

        dateappnt=Label(DataframeLeft, text="Appointment Date", font=("times new roman",25,"bold"), width=15, pady=4)
        dateappnt.grid(row=5,column=0)

        min_date=date.today()+timedelta(days=2)
        max_date=date.today()+timedelta(days=15)

        self.date_of_appnt=DateEntry(DataframeLeft,selectmode="day", date_pattern="yyyy-MM-dd",width=48,textvariable=self.dateof,mindate=min_date,maxdate=max_date)
        self.date_of_appnt.grid(row=5, column=1)

        timeappnt = Label(DataframeLeft, text="Appointment Time", font=("times new roman", 25, "bold"), width=15,pady=4)
        timeappnt.grid(row=6, column=0)
        self.time_of_appnt = AnalogPicker(DataframeLeft)
        self.time_of_appnt.grid(row=6, column=1)

        viewdoc = Button(Buttonframe, text="View Doctors", font=("times new roman", 15, "bold"), width=30, height=4,padx=2, pady=6, bg="light pink",command=self.doctor_fetch)
        viewdoc.pack()
        bookapp = Button(Buttonframe1, text="Book Appointment", font=("times new roman", 15, "bold"), width=30, height=4,padx=2, pady=6, bg="light pink",command=self.book_appnt)
        bookapp.pack()
        logout = Button(Buttonframe2, text="Logout", font=("times new roman", 15, "bold"), width=30, height=4,padx=2, pady=6, bg="light pink",command=self.log)
        logout.pack()
        delappnt = Button(Buttonframe3, text="Cancel Appointment", font=("times new roman", 15, "bold"), width=30, height=4, padx=2,
                        pady=6, bg="light pink", command=self.cancel)
        delappnt.pack()
        printrec = Button(Buttonframe4, text="Download receipt", font=("times new roman", 15, "bold"), width=30, height=4, padx=2,
                        pady=6, bg="light pink", command=self.download)
        printrec.pack()
        # Doctor Table

        scrlx = ttk.Scrollbar(DataframeRight, orient=HORIZONTAL)
        scrly = ttk.Scrollbar(DataframeRight, orient=VERTICAL)

        self.doctor_table = ttk.Treeview(DataframeRight, columns=("doctor_id", "doctor_name", "doctor_spec","doctor_work"),
                                         xscrollcommand=scrlx.set, yscrollcommand=scrly.set)
        scrlx.pack(side=BOTTOM, fill=X)
        scrly.pack(side=RIGHT, fill=Y)

        scrlx = ttk.Scrollbar(command=self.doctor_table.xview)
        scrly = ttk.Scrollbar(command=self.doctor_table.yview)

        self.doctor_table.heading("doctor_id", text="Doctor Id")
        self.doctor_table.heading("doctor_name", text="Name")
        self.doctor_table.heading("doctor_spec", text="Specialisation")
        self.doctor_table.heading("doctor_work", text="Working Hours")

        self.doctor_table["show"] = "headings"
        self.doctor_table.pack(fill=BOTH, expand=1)


    def download(self):
        pdf=FPDF('P','mm','A4')
        pdf.add_page()
        pdf.set_font("times",'',16)


        conn=mysql.connector.connect(host='localhost',username='root',password='Example@2023#',database='hospital')
        curr=conn.cursor()
        f = self.time_of_appnt.time()
        times = ""

        if f[2] == "AM" and f[0] == 12:
            if 0 <= f[1] <= 9:
                times = "00:0" + str(f[1]) + ":00"
            else:
                times = "00:" + str(f[1]) + ":00"
        elif f[2] == "AM":
            if 0 <= f[1] <= 9:
                times = str(f[0]) + ":0" + str(f[1]) + ":00"
            else:
                times = str(f[0]) + ":" + str(f[1]) + ":00"

        elif f[2] == "PM" and f[0] == 12:
            if 0 <= f[1] <= 9:
                times = str(f[0]) + ":0" + str(f[1]) + ":00"
            else:
                times = str(f[0]) + ":" + str(f[1]) + ":00"
        else:
            if 0 <= f[1] <= 9:
                times = str(f[0] + 12) + ":0" + str(f[1]) + ":00"
            else:
                times = str(f[0] + 12) + ":" + str(f[1]) + ":00"

        curr.execute('select * from appointment where (date_of_appointment=%s) and (time_of_appointment=%s)', (self.dateof.get(),times))
        r= curr.fetchall()
        k=0
        for i in r:
            k=k+1
        if k!=0:
            e = self.time_of_appnt.time()
            timee = str(e[0]) + ":" + str(e[1]) + " " + e[2]
            curr.execute("select aid from appointment where (date_of_appointment=%s) and (time_of_appointment=%s) and (did=%s)",(self.dateof.get(),times,self.doctor_id.get()))
            res=curr.fetchall()
            apntid=res[0][0]
            curr.execute('select dname,spec from doctor where did=%s', (self.doctor_id.get(),))
            row = curr.fetchall()
            doc_name = row[0][0]
            doc_spec = row[0][1]
            pdf.cell(40,10,"Appointment Details",align='center',ln=True)
            pdf.cell(40, 10, "Appointment ID : ")
            pdf.cell(40, 10, str(apntid), ln=True)
            pdf.cell(40,10,"Name : ")
            pdf.cell(40,10,self.patient.get(),ln=True)
            pdf.cell(40,10,"Age : ")
            pdf.cell(40, 10, str(self.age.get()),ln=True)
            pdf.cell(40, 10, "Gender : ")
            pdf.cell(40, 10,self.sex.get(),ln=True)
            pdf.cell(40, 10, "Email ID : ")
            pdf.cell(40, 10, self.patient_email.get(),ln=True)
            pdf.cell(40, 10, "Doctor Name : ")
            pdf.cell(40, 10, doc_name,ln=True)
            pdf.cell(70, 10, "Doctor Specialisation")
            pdf.cell(40, 10, doc_spec, ln=True)
            pdf.cell(70, 10, "Date Of Appointment : ")
            pdf.cell(40, 10, str(self.dateof.get()),ln=True)
            pdf.cell(70, 10, "Time Of Appointment : ")
            pdf.cell(40, 10, timee,ln=True)

            pdf.cell(40,10,"Thank You for booking!!",align='center')
            pdf.output(filedialog.asksaveasfilename(defaultextension="*.pdf", filetypes=(("PDF Files", "*.pdf"),)))
            # pdf.output(r'C:\Users\Appointment_Receipt.pdf')
            conn.commit()
            conn.close()
            self.patient.set("")
            self.sex.set("")
            self.doctor_id.set(0)
            self.patient_email.set("")
            self.age.set(0)
        else:
            messagebox.showinfo("Error","Appointment not booked yet...Book first")


    def log(self):
        root.destroy()
        import mainscreen

    def doctor_fetch(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Example@2023#', database='hospital')
        curr = conn.cursor()
        curr.execute("select * from doctor")
        rows = curr.fetchall()
        if len(rows) != 0:
            self.doctor_table.delete(*self.doctor_table.get_children())
            for i in rows:
                self.doctor_table.insert("", END, values=i)
        conn.commit()
        conn.close()

    def name_input(self,value):
            try:

                if value.isalpha() or value==" ":
                    return True
                else:
                    raise ValueError("")
            except ValueError:

                messagebox.showinfo("Error","Only characters allowed")

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

    def book_appnt(self):



        """exception_handled=0
        while exception_handled==0:

            
            try:
        """
        conn = mysql.connector.connect(host='localhost', username='root', password='Example@2023#',database='hospital')
        curr = conn.cursor()
        a = self.patient.get()
        b = self.sex.get()
        c = self.age.get()
        d = self.doctor_id.get()
        e = self.time_of_appnt.time()
        timee = ""


        if e[2] == "AM" and e[0] == 12:
                    if 0<=e[1]<=9:
                        timee = "00:0" + str(e[1]) + ":00"
                    else:
                        timee = "00:" + str(e[1]) + ":00"
        elif e[2] == "AM":
                    if 0 <= e[1] <= 9:
                        timee = str(e[0]) + ":0" + str(e[1]) + ":00"
                    else:
                        timee = str(e[0]) + ":" + str(e[1]) + ":00"

        elif e[2] == "PM" and e[0] == 12:
                    if 0 <= e[1] <= 9:
                        timee = str(e[0]) + ":0" + str(e[1]) + ":00"
                    else:
                        timee = str(e[0]) + ":" + str(e[1]) + ":00"
        else:
                    if 0 <= e[1] <= 9:
                        timee = str(e[0] + 12) + ":0" + str(e[1]) + ":00"
                    else:
                        timee = str(e[0] + 12) + ":" + str(e[1]) + ":00"

        f = self.dateof.get()
                

        query="select did,date_of_appointment,time_of_appointment from appointment where (did=%s) and (date_of_appointment=%s) and (time_of_appointment=%s)"
        curr.execute(query,(d, f, timee))
        row= curr.fetchall()
        q="select * from schedules where (did=%s) and (date_of_appointment=%s) and (time_of_appointment=%s)"
        curr.execute(q,(d, f, timee))
        r=curr.fetchall()
        j=0
        k=0
        for i in row:
            j=j+1
        for m in r:
            k=k+1


        if j==0 and k!=0:


                    curr.execute("insert into appointment (pname , age , gender, email , did , date_of_appointment , time_of_appointment) values(%s,%s,%s,%s,%s,%s,%s)",
                                 (self.patient.get(), self.age.get(), self.sex.get(), self.patient_email.get(), self.doctor_id.get(),self.dateof.get(), timee))
                    messagebox.showinfo("Status", "Booked")
                    conn.commit()
                    conn.close()




        elif k!=0:
                messagebox.showerror('Error', 'Appointment Already booked...Choose new one')

        else:
                    messagebox.showinfo("Error","Appointment not available")


    def cancel(self):
        import can



root=Tk()
obj=Appoint(root)
root.mainloop()

