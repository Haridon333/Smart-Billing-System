class node():
    def __init__(self,data):
        self.data=data
        self.children=[]
    def add_child(self,child):
        self.children.append(child)
def disp(root,y):
    print(root.children)
    for i in root.children:
        print(" ",i.data)
        for i in root.children[y].children:
            print("  ",i.data)
            y=y+1
def BILLCAL(data):
    bill=200
    if(data>100):
        temp=data-100
        if temp in range(1,100):
            bill=bill+(temp*1)
        elif temp in range(100,200):
            bill=bill+(temp*2)
        elif temp in range(200,400):
            bill=bill+(temp*3.5)
        elif temp in range(400,600):
            bill=bill+(temp*5)
        else:
            bill=bill+(temp*6.5)
    return(bill)
y=0;M=0
print("enter the city name:")
a=input();k=1
root=node(a);d=[];e=[];t=[];data1=[];names=[];HOUSES=[];BILLS=[]
print("enter number of areas :")
b=int(input())
for i in range(1,b+1):
    print("enter the name of area {n}:".format(n=i))
    c=input()
    d.append(c)
for i in d:
    root.add_child(node(i))
for i in range(len(d)):
    print("enter house numbers of area {n1} :".format(n1=k))
    k=k+1
    mM=list(input().split())
    HOUSES.append(mM)
    L=0; sM=[]; BM=[]
    for j in mM:
        lL=[]; sL=[]
        t.append(j)
        print("enter the owner name of house",j)
        name=input()
        names.append(name) ; lL.append(name)
        print("enter the data used by",name)
        data=int(input())
        BILL=BILLCAL(data)
        BM.append(BILL); lL.append(BILL); sL.append(lL)
        sM.append(dict(zip(t,sL)))
        L=L+1; t.clear()
    e.append(sM)
    BILLS.append(BM)
    M=M+1
for i in range(b):
    x=node(e[i])
    root.children[i].add_child(x)
disp(root,y)
from tkinter import *
root5=Tk()
root5.iconbitmap(r"C:\Users\Hari Subramaniam\Downloads\dsalogo.ico")
root5.geometry('500x500')
root5.title("DIGITAL INDIA")
main=[root.data]
z=d
k=HOUSES
m=BILLS
q=[i for j in k for i in j]
l=sum(m,[])
total=sum(l);jk=[]
for i in m:
    x=sum(i)
    jk.append(x)
def staff():
        global flag 
        if (flag==0):
            root5.destroy()
            flag=1
        root1=Tk()
        root1.iconbitmap(r"C:\Users\Hari Subramaniam\Downloads\dsalogo.ico")
        root1.geometry('500x500')
        root1.title('staff portal')
        button=Button(root1,text='Back',font='bold',command=cos).place(relx=0.9,rely=0.1,anchor=CENTER)
        mylabel1=Label(root1,text="We welcome the pillars of our nation ",font='bold').place(relx=0.5,rely=0.2,anchor=CENTER)
        cost1=Label(root1,text='CITY : '+ str(dict(zip(main,[total]))),font='bold').place(relx=0.5,rely=0.3,anchor=CENTER)
        cost2=Label(root1,text='AREAS : '+ str(dict(zip(z,jk))),font='bold').place(relx=0.5,rely=0.4,anchor=CENTER)
        cost3=Label(root1,text='HOUSES : '+ str(dict(zip(q,l))),font='bold').place(relx=0.5,rely=0.5,anchor=CENTER)
def cos():
        global flag
        if (flag==0):
            root5.destroy()
            flag=1
        root1= Tk()
        root1.iconbitmap(r"C:\Users\Hari Subramaniam\Downloads\dsalogo.ico")
        button=Button(root1,text='Back',font='bold',command=staff).place(relx=0.9,rely=0.1,anchor=CENTER)
        fm=dict(zip(q,l))
        cd=dict(zip(q,names))
        root1.geometry('500x500')
        root1.title('costumer portal')
        mylabel1=Label(root1,text= "We welcome you humbly !!!!",font='bold').place(relx=0.5,rely=0.1,anchor=CENTER)
        e1=Entry(root1,width=40,font='bold')
        e1.place(relx=0.5,rely=0.2,anchor=CENTER)
        def val():
                a=e1.get()
                if a in q:
                        mylabel6=Label(root1,text="Hi  "+str(cd[a]),font='bold').place(relx=0.5,rely=0.4,anchor=CENTER)
                        mylabel7=Label(root1,text="     Your bill is Rs."+str(fm[a]),font='bold').place(relx=0.5,rely=0.5,anchor=CENTER)
                else:
                        mylabel6=Label(root1,text='                                             ',height='4').place(relx=0.5,rely=0.4,anchor=CENTER)
                        mylabel1=Label(root1,text="    USER NOT FOUND     ",font='bold').place(relx=0.5,rely=0.5,anchor=CENTER)
        button1=Button(root1,text="submit",font='bold',command=val)
        button1.place(relx=0.5,rely=0.3,anchor=CENTER)
flag=0
mylabel9=Label(root5,text='USER PORTAL',height='4',width='20',font='title').place(relx=0.5,rely=0.1,anchor=CENTER)
button1=Button(root5,text="staff login",command=staff,font='bold')
button1.place(relx=0.5,rely=0.4,anchor=CENTER)
button2=Button(root5,text="costumer login",command=cos,font='bold')
button2.place(relx=0.5,rely=0.5,anchor=CENTER)
root5.mainloop()
