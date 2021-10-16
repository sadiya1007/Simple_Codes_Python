from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *

def add():
    temp = (cmp_entry.get(),)
    cmpChosen['values'] = cmpChosen['values'] + temp
    f = open('wordlist.txt', 'w')
    for i in cmpChosen['values']:
        print(i, file=f)
    f.close()
    lines = [line.strip() for line in open('wordlist.txt')]
    for i in lines:
        f=open(i+'.txt','a+')
    f.close()


def money():
    Amount_txt.delete(1.0,END)
    Q=eval(Quantity_entry.get())
    if((color.get() == 1) and Q<=99): #black
        Amount_txt.insert(END,str(Q*1)+' Rs')
        f=open(str(cmp.get())+'.txt','a+')
        print('Quantity'+str(Q)+'Amount ='+str(Q*1)+' Rs',file=f)
    elif((color.get() == 1) and Q>=100):
        Amount_txt.insert(END,str(Q*0.6)+' Rs')
        f=open(str(cmp.get())+'.txt','a+')
        print('Quantity'+str(Q)+'Amount ='+str(Q*0.6)+' Rs',file=f)
    elif ((color.get() == 2) and Q<=99):
        Amount_txt.insert(END,str(Q*10)+' Rs')
        f=open(str(cmp.get())+'.txt','a+')
        print('Quantity'+str(Q)+'Amount ='+str(Q*10)+' Rs',file=f)
    elif((color.get() == 2) and Q>=100):
        Amount_txt.insert(END,str(Q*7)+' Rs')
        f=open(str(cmp.get())+'.txt','a+')
        print('Quantity'+str(Q)+'Amount ='+str(Q*7)+' Rs',file=f)
    pastbill()

def pastbill():
    f=open(str(cmp.get())+'.txt','r')
    history_bill_txt.delete(1.0,END)
    history_bill_txt.insert(END,f.read())
    


root=Tk()




lines = [line.strip() for line in open('wordlist.txt')]
for i in lines:
    f=open(i+'.txt','a+')
    f.close()

cmp = StringVar()                         
cmpChosen = Combobox(width=12, textvariable=cmp) 
cmpChosen['values'] = tuple(lines)    
cmpChosen.grid(row=0,column=0)

cmp_entry=Entry()  
cmp_entry.grid(row=0,column=1)

addcmp=Button(text='ADD',command=add)
addcmp.grid(row=0,column=2)

history_bill_txt = ScrolledText(height=6,width=20)
history_bill_txt.grid(row=0,column=3,rowspan=4,sticky='NSEW')




Xtype_lbl = Label(text='Xerox Type')
Xtype_lbl.grid(row=1,column=0)
color = IntVar()
bw_rb = Radiobutton(text='B/W',var=color,value=1)
bw_rb.grid(row=1,column=1)
color_rb = Radiobutton(text='COLOR',var=color,value=2)
color_rb.grid(row=1,column=2)

Quantity_lbl = Label(text='Quantity')
Quantity_lbl.grid(row=2,column=0)
Quantity_entry = Entry()
Quantity_entry.grid(row=2,column=1,columnspan=2,sticky='NSEW')

bill_button = Button(text='Generate Bill',command=money)
bill_button.grid(row=3,column=0,columnspan='2',sticky='NSEW')

History_bill_button = Button(text='Bill History',command=pastbill)
History_bill_button.grid(row=3,column=2,sticky='NSEW')




Amount_lbl = Label(text='Amount')
Amount_lbl.grid(row=4,column=0)
Amount_txt = Text(height=1,width=5)
Amount_txt.grid(row=4,column=1,columnspan=2,sticky='NSEW')

mainloop()
