from tkinter import *


# function for profile
def Click():
    emailCheck ='abhie@gmail.com'
    pasCheck = '123456'
    if emailCheck == EmailEntry.get() and pasCheck == PasswordEntry.get():
        Profile = Tk()
        Profile.geometry('300x300')
        Profile.title('User Profile')
        Profile.mainloop()

        # UserName = Label(Profile,text='Name: ')
        # user = Label(Profile,text='Abhishek Pandey')
        # age = Label(Profile,text='Age: ')
        # userAge = Label(Profile,text='20 yrs')
        # tech = Label(Profile,text='Tech Stack: ')
        # userTech = Label(Profile,text='Python , Java')
        #
        # UserName.grid(column=0,row=0)
        # age.grid(column=0,row=1)
        # tech.grid(column=0,row=2)
        #
        # user.grid(column=1,row=0)
        # userAge.grid(column=1,row=1)
        # userTech.grid(column=1,row=2)

        # l1= Label(Profile,text=name)
        # l2= Label(Profile,text = pas)
        #
        # l1.grid(column=0,row=0)
        # l2.grid(column=0,row=1)


frame = Tk()
frame.geometry('600x500')
frame.title('Login page')
# frame.config(bg='sky blue')

Email = Label(frame,text='Email: ')
Password = Label(frame, text='Password: ')

Password.grid(column=0,row=1)
Email.grid(column=0, row=0)

EmailEntry = Entry(frame,width=20)
PasswordEntry = Entry(frame,width=20)

EmailEntry.grid(column=4,row=0)
PasswordEntry.grid(column=4,row=1)

btn = Button(frame,text='Log In',command=Click)

btn.grid(column=1,row=3)

frame.mainloop()
