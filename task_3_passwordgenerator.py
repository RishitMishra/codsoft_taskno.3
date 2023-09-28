from tkinter import *
import string
import random

r = Tk(className="Password generator by RM")
r.geometry("200x320")
r.resizable(0,0)

password = ""
I = StringVar()
ch = ""
o1 = IntVar()
o1.set(0)
o2 = IntVar()
o2.set(0)
o3 = IntVar()
o3.set(0)
o4 = IntVar()
o4.set(0)
length_of_pwd = IntVar()

def opt():
    global ch
    ch = ""
    if o1.get() == 1:
        ch += string.ascii_lowercase
    if o2.get() == 1:
        ch += string.ascii_uppercase
    if o3.get() == 1:
        ch += string.digits
    if o4.get() == 1:
        ch += string.punctuation
 
def reset():
    global password
    global ch
    global opt
    global length_of_pwd
    password = ""
    ch = ""
    o1.set(0)
    o2.set(0)
    o3.set(0)
    o4.set(0)
    length_of_pwd.set(0)
    I.set("")

def gen():
    global length_of_pwd
    global ch
    global password
    try:
        for i in range(length_of_pwd.get()):
            password += random.choice(ch)
        I.set(password)
    except:
        I.set("Invalid choice")

heading = Label(r,text="Password Generator",font=("arial black",12,"bold"))
heading.pack()

label_length = Label(r,text="Length:",font=("arial",10))
label_length.pack()

length = Entry(r,textvariable=length_of_pwd)
length.pack()

c1 = Checkbutton(r,text="Use lowercase letters",variable=o1,command=lambda:opt(),onvalue=1,offvalue=0)
c1.pack()

c2 = Checkbutton(r,text="Use uppercase letters",variable=o2,command=lambda:opt(),onvalue=1,offvalue=0)
c2.pack()

c3 = Checkbutton(r,text="Use digits",variable=o3,command=lambda:opt(),onvalue=1,offvalue=0)
c3.pack()

c4 = Checkbutton(r,text="Use special symbols",variable=o4,command=lambda:opt(),onvalue=1,offvalue=0)
c4.pack()

b2 = Button(r,text="Generate",command=lambda:gen(),width=8,height=2)
b2.pack()

b2 = Button(r,text="Reset",command=lambda:reset(),width=8,height=2)
b2.pack()

t1 = Label(r,text="Password:",font=("arial black",10,"bold"))
t1.pack()

display = Entry(bg="light grey",font=("arial black",10,"bold"),textvariable=I)
display.pack()

r.mainloop()