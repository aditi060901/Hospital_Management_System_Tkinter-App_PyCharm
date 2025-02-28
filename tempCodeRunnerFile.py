from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk
import pymysql


#Function
def forget_pass():
    window = Toplevel()
    window.title("Change Password")
    
    bgPic= ImageTk.PhotoImage(file='bg.png')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()
    


    heading=Label(window,text='RESET PASSWORD',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',
              fg='firebrick1')
    heading.place(x=593,y=120)

    
    usernameLabel=Label(window, text="Username", font=('Microsoft Yahei UI Light',12,'bold'),bg='white',bd=0,
                            fg='firebrick1')
    usernameLabel.place(x=574,y=180)
    usernameEntry=Entry(window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,
                            fg='firebrick1')
    usernameEntry.place(x=574, y=205)
    
    frame1=Frame(window, width=250,height=2,bg='firebrick1').place(x=574,y=225)
    

    passwordLabel=Label(window, text="Password", font=('Microsoft Yahei UI Light',12,'bold'),bg='white',
                            fg='firebrick1')
    passwordLabel.place(x=574,y=250)

    passwordEntry=Entry(window,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bd=0,
                            fg='white')
    passwordEntry.place(x=574,y=275)
    frame2=Frame(window, width=250,height=2,bg='firebrick1').place(x=574,y=295)