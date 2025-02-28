from tkinter import *
from PIL import ImageTk


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


def login_attempt():
    username = usernameEntry.get()
    password = passwordEntry.get()

    # Check if username and password are correct
    if username == 'admin' and password == 'admin':
        login_window.destroy()
        import admin

    else:
        invalid_label = Label(login_window, text='Invalid username or password', font=('Microsoft Yahei UI Light', 12, 'bold'), fg='red')
        invalid_label.place(x=500, y=400)

def back_main():
    login_window.destroy()
    import mainscreen



# GUI part
login_window = Tk()
login_window.geometry("1540x800+0+0")

login_window.title('Login Page')

bgImage = ImageTk.PhotoImage(file='bgg.jpg')

bgLabel = Label(login_window, image=bgImage)
# Centering the background image
bgLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

heading = Label(login_window, text='ADMIN LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white', fg='blue')
heading.place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 23, 'bold'), bd=0, fg='blue')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width=250, height=2)
frame1.place(x=500, y=222)

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 23, 'bold'), bd=0, fg='blue')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(login_window, width=250, height=2)
frame2.place(x=500, y=282)

loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1', cursor='hand2', bd=0, width=10, command=login_attempt)
loginButton.place(x=600, y=350)

backbutton=Button(login_window, text='Logout', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1', cursor='hand2', bd=0, width=10, command=back_main)
backbutton.place(x=800, y=350)

login_window.mainloop()