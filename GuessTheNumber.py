from tkinter import*
import random
import time
window = Tk()
window.title("Guess the number")
window.geometry("400x350")

a = random.randint(0,100)
logo=PhotoImage(file="UpArrow.png")
logo2=PhotoImage(file="DownArrow.png")
logo3=PhotoImage(file="Correct.png")

def start(*args):
    global lbl3, txt,b
    b = txt.get()
    if a>int(b):
        lbl3.configure(image=logo)
        txt.delete(0,END)
    if int(b)>a:
        lbl3.configure(image=logo2)
        txt.delete(0,END)
    if a==int(b):
        lbl3.configure(image=logo3)
        txt.configure(state="disabled")

def restart():
    global lbl3, txt,a,lbl5
    txt.configure(state="normal")
    txt.delete(0,END)
    lbl3.configure(image="")
    a=random.randint(0, 100)
    for i in range(0, 15):
        c = random.randint(0, 100)
        lbl5.configure(text=c)
        lbl5.update()
        time.sleep(0.1)
        lbl5.configure(text="")

def firstwindow():
    global lbl2,btn,btn2,lbl4,lbl3,txt,lbl5
    lbl=Label(window,justify="center",text="Guess the number",font=("Book Antiqua",15),fg="white",bg="blue")
    lbl.grid(column=0,row=0,rowspan=2,columnspan=2,padx=20)
    lbl2=Label(window,text="The computer finds a number from 0 to 100\n and you try to guess it.",font=("Book Antiqua",13),fg="blue")
    lbl2.grid(column=0,row=4,columnspan=2,padx=20)
    lbl4=Label(window,justify="center",text="Write a number, Press Enter and Guess!",font=("Book Antiqua",13),fg="blue")
    lbl4.grid(column=0,row=5,rowspan=2,columnspan=2)
    lbl3=Label(window,text="",font=("Book Antiqua",13),fg="blue")
    lbl3.grid(column=1,row=9)
    txt=Entry(window,justify="center",width=10,font=("Book Antiqua",13),fg="blue")
    txt.grid(column=0,row=9,pady=40)
    btn=Button(window,text="Exit",width=10,font=("Book Antiqua",13),fg="blue",command=exit)
    btn.grid(column=0,row=11,pady=35)
    btn2=Button(window,text="Restart",width=10,font=("Book Antiqua",13),fg="blue",command=restart)
    btn2.grid(column=1,row=11,pady=35)
    lbl5 = Label(window, text="", font=("Book Antiqua", 13), fg="blue")
    lbl5.grid(column=0, row=10, columnspan=2)
    for i in range(0, 15):
        c = random.randint(0, 100)
        lbl5.configure(text=c)
        lbl5.update()
        time.sleep(0.1)
        lbl5.configure(text="")
    window.bind("<Return>",start)




firstwindow()
window.mainloop()