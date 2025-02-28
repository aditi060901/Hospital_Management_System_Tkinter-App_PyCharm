from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


# Function

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

def forget_pass():
    def change_password():
        if userEntry.get() == "" or newpassEntry.get() == '' or cpassEntry.get()=='' or newpassEntry.get()=='':
            messagebox.showerror("Error", 'All Fields are required!', parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='Example@2023#', database='hospital')
            mycursor = con.cursor()
            mycursor.execute("select * from data where (username=%s) and (email=%s)", (userEntry.get(),emailuserEntry.get()))
            r1 = mycursor.fetchall()
            r1no=0
            for i in r1:
                r1no=r1no+1
            if r1no==0:
                messagebox.showerror('Error', 'Incorrect Email Address or Username ', parent=window)
            else:
                if validate_password(newpassEntry.get()):
                    if newpassEntry.get() != cpassEntry.get():
                        messagebox.showerror("Error", 'Password Mismatch!', parent=window)
                    else:
                        query = 'update data set password=%s where username=%s'
                        mycursor.execute(query, (newpassEntry.get(), userEntry.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo('Success', 'Password is Reset\nPlease Login with the New Password!', parent=window)
                        window.destroy()
                else:
                    messagebox.showerror('Error',
                                         'Password is weak.\n1. Password should have atleast one lowercase,one uppercase and one special character i.e. %,#,@,$.\n2.Password length should be atleast 8 characters upto 20.')
    window = Toplevel()
    window.title("Change Password")

    bgPic = ImageTk.PhotoImage(file='bg.png')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    heading = Label(window, text='RESET PASSWORD', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white',
                    fg='firebrick1')
    heading.place(x=593, y=120)

    emailuserLabel = Label(window, text="Email Address", font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white',
                           bd=0,
                           fg='firebrick1')
    emailuserLabel.place(x=574, y=180)
    emailuserEntry = Entry(window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0,
                           fg='firebrick4')
    emailuserEntry.place(x=574, y=205)

    frame1 = Frame(window, width=250, height=2, bg='firebrick1').place(x=574, y=227)

    userLabel = Label(window, text="Username", font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white',
                      fg='firebrick1')
    userLabel.place(x=574, y=255)

    userEntry = Entry(window, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bd=0,
                      fg='firebrick4')
    userEntry.place(x=574, y=280)
    frame2 = Frame(window, width=250, height=2, bg='firebrick1').place(x=574, y=302)

    newpassLabel = Label(window, text="Password", font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white',
                         fg='firebrick1')
    newpassLabel.place(x=574, y=330)

    newpassEntry = Entry(window, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', bd=0,
                         fg='firebrick4')
    newpassEntry.place(x=574, y=355)
    frame3 = Frame(window, width=250, height=2, bg='firebrick1').place(x=574, y=377)

    cpassLabel = Label(window, text="Confirm Password", font=('Microsoft Yahei UI Light', 12, 'bold'), bg='white',
                       fg='firebrick1')
    cpassLabel.place(x=574, y=405)

    cpassEntry = Entry(window, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', bd=0,
                       fg='firebrick4')
    cpassEntry.place(x=574, y=430)
    frame4 = Frame(window, width=250, height=2, bg='firebrick1').place(x=574, y=452)

    signupButton = Button(window, text="Change Password", font=('Microsoft Yahei UI Light', 13, 'bold'),
                          bg='firebrick1', fg='white',
                          activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=22,
                          command=change_password)
    signupButton.place(x=574, y=477)
    window.mainloop()


def login_user():
    if usernameEntry.get() == '' or passwordEntry.get == '':
        messagebox.showerror('Error', 'All Fields are Required!')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Example@2023#',database='hospital')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection Not Established...\nPlease Try Again')
            return
        mycursor.execute('select * from data where username=%s and password=%s', (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchall()
        k=0
        for i in row:
            k=k+1
        if k==0:
            messagebox.showerror('Error', 'Invalid Username or Password!')
        else:
            login_window.destroy()
            import appnt


def signup_page():
    login_window.destroy()
    import signup




def user_entry(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def password_entry(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

    # GUI Part


def main_screen():
    login_window.destroy()
    import mainscreen


login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')

bgImage = PhotoImage(file='bg.png')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white',
                fg='firebrick1')
heading.place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                      bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_entry)

frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),
                      bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_entry)

frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=580, y=282)


forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white',
                      cursor='hand2', font=('Microsoft Yahei UI Light', 9, 'bold'), fg='firebrick1',
                      activeforeground='firebrick1', command=forget_pass)
forgetButton.place(x=715, y=295)

loginButton = Button(login_window, text="Login", font=('Microsoft Yahei UI Light', 13, 'bold'), bg='firebrick1',
                     fg='white',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=23,
                     command=login_user)

loginButton.place(x=578, y=350)


backButton = Button(login_window, text="Logout", font=('Microsoft Yahei UI Light', 13, 'bold'), bg='firebrick1',
                     fg='white',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=23,
                     command=main_screen)

backButton.place(x=578, y=450)


orLabel = Label(login_window, text='------------- OR --------------',
                font=('Microsoft Yahei UI Light', 13, 'bold'),
                fg='firebrick1', bg='white')
orLabel.place(x=575, y=395)


signupLabel = Label(login_window, text="Don't have an account?",
                    font=('Microsoft Yahei UI Light', 9, 'bold'),
                    fg='firebrick1', bg='white')
signupLabel.place(x=553, y=490)

AccountButton = Button(login_window, text="Create New Account", font=('Microsoft Yahei UI Light', 9, 'bold underline'),
                       bg='white', fg='blue',
                       activeforeground='blue', activebackground='white', cursor='hand2', bd=0, command=signup_page)

AccountButton.place(x=710, y=489)

login_window.mainloop()


