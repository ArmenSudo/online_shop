#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox
from Tkinter import *
import webbrowser
top = Tkinter.Tk()
top["bg"] = "#33CCFF"
top.title("Խոխմա")
ent=StringVar()
p1=StringVar()
p2=StringVar()
p1.set("1")
p2.set("0")
E1= Entry(top, bg = '#33CCFF',width=29,bd = 5, textvariable=ent).grid(row=1,column=3)
def about():
	tkMessageBox.showinfo( "Մեր մասին", "This program creators are:\nMihran Sargsyan\nArmen Harutyunyan" )
andu=""
andu = StringVar()
a=0
u=0
var = StringVar()
colour = StringVar()
andu.set("yellow")
colour.set("#33CCFF")
def cu():
    colour.set('#33CCFF' if colour.get()!='#33CCFF' else 'red')
    Q = str(colour.get())
    print Q
    print "1"
l = Label(top,height=3,width=30,bg = colour.get(), textvariable=var ).grid(row=2,column=3)
var.set("Դուք գտնվում եք Խոխմա ծրագրում\nՆերմուծեք բառը և ընտրեք լեզուն")	
def stug():
	qrt =ent.get()
	qr=qrt.strip( ' ' )
	qr=qr.lower()
	q= qr.isalpha()
	if(str(q) ==("True")):
		if str(q)<=1:
			var.set("Դա բառ չե")		
		else:
			tarq()
	elif (str(q) == ("False")):
		var.set("Դա բառ չէ\nԵղեք ուշադիր")    
		cu()
def tarq():
	b = bu.get()
	if (str(b)=="hx"):
		tarqhx()
	elif (str(b)=="xh"):
		tarqxh()	
def tarqxh():
        var.set("Այդ բառը չկա \nՑանկանու՞մ եք ավելացնել")
        q = 0
        p1.set("0")
        h= ent.get()
        p2.set(str(h))
        h=h.lower()
        h=h.strip( ' ' )
        fha = open('/home/mihran/Desktop/gradaran/2.txt')
        for li in fha:
                li = li.rstrip()
                if li.find(str(h)) == -1 :
                        l =li[:4]
                        a =li[4:]
                        continue
                l = li[:4]
                a = li[4:]
                if (str(a) == str(h)):
                        fhandi = open('/home/mihran/Desktop/gradaran/1.txt')
                        for line in fhandi:
                                line = line.rstrip()
                                if line.find(str(l)) == -1 :
                                        continue
                                lin = line[4:]
                                if line[:4]!=li[:4]:
                                        var.set("Չկա")
                                var.set(str(lin))
                                q=1
                                p1.set("1")
                        fhandi.close()
        l=0
        fha.close

def stu():
	if (str(p1.get())=="1"):
		stug()
def tarqhx():
	var.set("Այդ բառը չկա \nՑանկանու՞մ եք ավելացնել")
	q = 0
	p1.set("0")
	h= ent.get()
	p2.set(str(h))
        h=h.lower()
        h=h.strip( ' ' )
	fha = open('/home/mihran/Desktop/gradaran/1.txt')
	for li in fha:
		li = li.rstrip()
		if li.find(str(h)) == -1 :
			l =li[:4]
			a =li[4:]
			continue
		l = li[:4]
		a = li[4:]
		if (str(a) == str(h)):
			fhandi = open('/home/mihran/Desktop/gradaran/2.txt')
			for line in fhandi:
				line = line.rstrip()
				if line.find(str(l)) == -1 :
					continue
				lin = line[4:]
				if line[:4]!=li[:4]:
					var.set("Չկա")
				var.set(str(lin))
				q=1
				p1.set("1")
			fhandi.close()
	l=0
	fha.close
def exi():
	if (p1.get()=="1"): 
		exit()
	else:
		p1.set("1")
		var.set("Ներմուծեք բառը և ընտրեք լեզուն")
		ent.set("")
def mzo():
	ent.set("")
	var.set("Ներմուծեք թարգմանությունը\nԴադարեցնելու համար սեխմեք ոչ")
	p1.set("2")
def ozo():
	n=p2.get()	
	m=ent.get()
	f=open('/home/mihran/Desktop/gradaran/3.txt', 'a')
	e=str(n)+"-"+str(m)+"\n"
	f.write(str(e))
	f.close()
	p1.set("1")
	var.set("Ներմուծեք բառը և ընտրեք լեզուն")
	ent.set("")
def sozo():
	qrt =ent.get()
        qr=qrt.strip( ' ' )
        qr=qr.lower()
        q= qr.isalpha()
        if(str(q) ==("True")):
                if str(q)<=1:
                        var.set("Դա բառ չէ")
                else:
                        ozo()
        elif (str(q) == ("False")):
                var.set("Դա բառ չէ\nԵղեք ուշադիր")

def maqrel():
	if (str(p1.get())=="1"):
		var.set("")
		ent.set("")
	if (str(p1.get())=="2"):
		sozo()
	if (str(p1.get())=="0"):
		mzo()
mi= StringVar()
mi.set("Հայ-Ղափ")
B = Tkinter.Button(width=9, height=4,bd =4,  text ="Թարքմանել",bg = '#33CCFF',activebackground = '#FFFFFF', command =stu ).grid(row=1,rowspan=2,column=5)
u=1
bu = StringVar()
bu.set("hx")
def pox():
	l = p1.get()
	if (l=="1"):
		b =  bu.get()
		if (str(b)== "hx"):
	               mi.set("Ղափ-Հայ")
		       bu.set("xh")
		elif (str(b) == "xh"):
	               mi.set("Հայ-Ղափ")
		       bu.set("hx")
l2 = Label(top,height=1,width=12,bd=5, bg = '#33CCFF', textvariable=mi,relief=RAISED ).grid(row=1,column=1)
w = Tkinter.Button(width=9, height=2,bd = 5,  text ="Փոխել լեզուն", bg = '#33CCFF', activebackground = '#FFFFFF', command = pox).grid(row=2,column=1,)
top.minsize(width=465,height=133)
top.maxsize(width=465,height=133)
A = Tkinter.Button(width=9, height=2, bd = 5,  text ="Մեր մասին",bg = '#33CCFF',activebackground = '#FFFFFF', command = about).grid(row=4,column=1)
D = Tkinter.Button(width=9, height=2, bd = 5,  text ="Դուրս գալ(Ոչ) ",bg = '#33CCFF',activebackground = '#FFFFFF', command = exi).grid(row=4,column=5)
I = Tkinter.Button(width=26, height=2, bd = 5, text ="Մաքրել(Այո)",bg = '#33CCFF',activebackground = '#FFFFFF', command = maqrel).grid(row=4,column=3)
top.mainloop()
