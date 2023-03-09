from tkinter import *

aken=Tk()
aken.geometry("800x600")
aken.title("Ruutvõrrandi lahendus")

lbl=Label(aken,text="Ruutvõrrandi lahendus",bg="gold",fg="#AA4A44",font="Arial 20",height=5,width=20)
ent1=Entry(aken,fg="blue",bg="lightblue",width=3,font="Arial 20",justify=LEFT)
lbl1=Label(aken,text="x**2+",font="Arial 20",height=5,width=10)
ent2=Entry(aken,fg="blue",bg="lightblue",width=3,font="Arial 20",justify=LEFT)
lbl2=Label(aken,text="x+",font="Arial 20",height=5,width=10)
ent3=Entry(aken,fg="blue",bg="lightblue",width=3,font="Arial 20",justify=LEFT)
lbl3=Label(aken,text="=0",font="Arial 20",height=5,width=10)
ent4=Button(aken,text="Lahenda",fg="blue",bg="lightblue",width=10,font="Arial 20",justify=LEFT)
lbl0=Label(aken,text="Ruutvõrrandi lahendus",bg="gold",fg="#AA4A44",font="Arial 20",height=5,width=20)


lbl.pack()
ent1.pack(side=LEFT)
lbl1.pack(side=LEFT)
ent2.pack(side=LEFT)
lbl2.pack(side=LEFT)
ent3.pack(side=LEFT)
lbl3.pack(side=LEFT)
ent4.pack(side=LEFT)
lbl0.pack(side=BOTTOM)
aken.mainloop()