#creating a functional temperature convector
from tkinter import *
root = Tk()
root.title('Temperature Convector')
root.minsize(width=500, height=500)



l1=LabelFrame(root,text='Celcius To Fahrenheit',padx=20, pady=20)
l1.grid(row=2, column=0)
E1=Entry(l1,state='disable')
E1.grid(row=4, column=0)

def Cel_Active():
    E1.configure(state='normal')

btn_active=Button(root,text='Activate -Celcius to Fahrenheit', command=Cel_Active)
btn_active.grid(row=6, column=0)

l2=LabelFrame(root, text='Fahrenheit to Celcius',padx=20, pady=20)
l2.grid(row=2, column=5)
E2=Entry(l2,state='disable')
E2.grid(row=4, column=5)

def Far_Active():
    E2.configure(state='normal')

btn_active1=Button(root,text='Activate -Fahrenheit to Celcius', command=Far_Active)
btn_active1.grid(row=6, column=5)



def exit():
    root.destroy()

exit_btn = Button(text = "Quit", command=exit)
exit_btn.grid(row=15, column=9)

def convert2fah():
    if E1:
        celcius= float(E1.get())
        fah = (celcius * 9/5) + 32
        result_entry.insert(0, fah)

def convert():
    if E2:
        fahrenheit = float(E2.get())
        celcius = (fahrenheit-32)*5/9
        result_entry.insert(0, celcius)


result_bnt=Button(root, text='C-F', command=convert2fah)
result_bnt.grid(row=6, column=3)
result_bnt.place(x = 100, y = 200)


result_bnt1=Button(root, text='F-C',command=convert)
result_bnt1.grid(row=10, column=10)
result_bnt1.place(x = 100, y = 250)

result_entry=Entry(root, bg='light green')
result_entry.grid(row=7, column=3)

def Clear():
    E1.delete(0, END)
    E2.delete(0, END)

root.mainloop()
