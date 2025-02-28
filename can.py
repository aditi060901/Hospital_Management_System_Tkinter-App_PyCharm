from tkinter import *
import mysql.connector
from tkinter import messagebox

root=Tk()
root.geometry("300x300+500+200")
root.title("Cancel Appointment")
root.resizable(0,0)

appnt_id=StringVar()
email_id=StringVar()


def del_appnt():
    if appnt_id.get()=="" or email_id.get()=="":
            messagebox.showinfo("Error","Enter All Fields")
            return
    conn=mysql.connector.connect(host='localhost',username='root',password='Example@2023#',database='hospital')
    curr=conn.cursor()
    curr.execute("select * from appointment where (aid=%s) and (email=%s)",(appnt_id.get(),email_id.get()))
    r=curr.fetchall()
    m=0
    for i in r:
        m=m+1
    if m!=0:
        curr.execute('delete from appointment where (aid=%s) and (email=%s)',(appnt_id.get(),email_id.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Status","Appointment Cancelled")
        appnt_id.set(0)
        email_id.set("")
    else:
        messagebox.showinfo("Error","No appointment scheduled with provided information")


Dataframe=Frame(root,relief=RIDGE,bg='light pink',width=500,height=500)
Dataframe.place(x=0,y=5)

label2=Label(Dataframe,text="Email ID",font=("times new roman",15,"bold"),bg='light pink',bd=10)
label2.place(x=0,y=50)
emailentry=Entry(Dataframe,textvariable=email_id,font=('times new roman',15,'bold'),width=13)
emailentry.place(x=158,y=50)

label1=Label(Dataframe,text="Appointment ID",font=('times new roman',15,'bold'),bd=10,bg='light pink')
label1.place(x=0,y=100)
apntid=Entry(Dataframe,textvariable=appnt_id,font=('times new roman',15,'bold'),width=13)
apntid.place(x=158,y=100)

delappnt=Button(Dataframe,text="Cancel",font=('times new roman',15,'bold'),command=del_appnt)
delappnt.place(x=110,y=160)

root.mainloop()