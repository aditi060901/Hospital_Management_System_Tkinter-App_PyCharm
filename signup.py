from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import re


def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    cpasswordEntry.delete(0, END)
    check.set(0)


def login_page():
    signup_window.destroy()
    import loginpage


def validate_password(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        #print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        #print('length should be not be greater than 20')
        val = False

    if not any(char.isdigit() for char in passwd):
        #print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        #print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        #print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        #print('Password should have at least one of the symbols $@#')
        val = False
    return val

def gmail(emaill):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9-.]+$)"
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", emaill):
        return True
    else:
        return False

def connect_database():
    u = usernameEntry.get()
    p = passwordEntry.get()
    e = emailEntry.get()

    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or cpasswordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are Required!')
    elif passwordEntry.get() != cpasswordEntry.get():
        messagebox.showerror('Error', 'Password Mismatch!')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept Terms And Conditions!')
    else:

        try:
            con = pymysql.connect(host='localhost', user='root', password='Example@2023#',database='hospital')
            mycursor = con.cursor()

        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return

        mycursor.execute('select * from data where username=%s', (usernameEntry.get(),))
        row = mycursor.fetchall()
        k=0
        for i in row:
            k=k+1

        if k!=0:
            messagebox.showerror('Error', 'Username Already Exists')

        elif (gmail(e)==False):
            messagebox.showerror('Error', 'Incorrect email address')

        elif (validate_password(p) == False):
            messagebox.showerror('Error',
                                 'Password is weak.\n1. Password should have atleast one lowercase,one uppercase and one special character i.e. %,#,@,$.\n2.Password length should be atleast 8 characters upto 20.')

        else:
            query = 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration  Is Successful!')
            clear()
            signup_window.destroy()
            import loginpage


signup_window = Tk()
signup_window.title('Sign Up Page')
signup_window.resizable(0, 0)
bgImage = PhotoImage(file='bg.png')
bgLabel = Label(signup_window, image=bgImage)

bgLabel.grid()

frame = Frame(signup_window, bg='white')
frame.place(x=554, y=100)

heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white',
                fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = Label(frame, text="Email", font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                   fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='IndianRed1',
                   fg='white')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text="Username", font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                      fg='firebrick1')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='IndianRed1',
                      fg='white')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text="Password", font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                      fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))

passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='IndianRed1',
                      fg='white')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

cpasswordLabel = Label(frame, text="Confirm Password", font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                       fg='firebrick1')
cpasswordLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))

cpasswordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='IndianRed1',
                       fg='white')
cpasswordEntry.grid(row=8, column=0, sticky='w', padx=25)

check = IntVar()
tandc = Checkbutton(frame, text='I agree to the Terms and Conditions', font=('Microsoft Yahei UI Light', 9, 'bold'),
                    bg='white',
                    fg='firebrick1', activebackground='white', activeforeground='firebrick1',
                    cursor='hand2', variable=check)
tandc.grid(row=9, column=0, pady=10, padx=15)

signupButton = Button(frame, text="Signup", font=('Microsoft Yahei UI Light', 13, 'bold'), bg='firebrick1', fg='white',
                      activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=22,
                      command=connect_database)
signupButton.grid(row=10, column=0)

logLabel = Label(frame, text="Already have an account?",
                 font=('Microsoft Yahei UI Light', 9, 'bold'),
                 fg='firebrick1', bg='white')
logLabel.grid(row=11, column=0, sticky='w', padx=15)

alreadyaccountButton = Button(frame, text="Login", font=('Microsoft Yahei UI Light', 9, 'bold underline'), bg='white',
                              fg='blue',
                              activeforeground='blue', activebackground='white', cursor='hand2', bd=0,
                              command=login_page)
alreadyaccountButton.place(x=185, y=372)

signup_window.mainloop()