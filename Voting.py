from tkinter import *
import  PhoneLib
window=Tk()
window.geometry("1100x300");
L1=Label(text='Live Voting')
L1.place(x=600,y=20)



P1=PhotoImage(file='rr.gif')
B1 = Button(window, image=P1,text ="RR")
B1.place(x=50,y=50)
L2=Label(text='0')
L2.place(x=200,y=250)


P2=PhotoImage(file='rk.gif')
B2 = Button(window, text ="RK",image=P2)
B2.place(x=400,y=50)
L3=Label(text='0')
L3.place(x=550,y=250)

P3=PhotoImage(file='sk.gif')
B3 = Button(window, text ="SK" ,image=P3)
B3.place(x=750,y=50)
L4=Label(text='0')
L4.place(x=900,y=250)


window.mainloop()