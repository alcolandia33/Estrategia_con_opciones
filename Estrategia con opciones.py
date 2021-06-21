
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pylab as plt
import pandas as pd


def option(t,p,x1,x2):
	if t==1 or t==2 :
		if x1>x2:
			b=x1-x2
		else:
			b=0
		if t==1:
			v=-p+b
		else:
			v=p-b
	elif t==3 or t==4 :
		if x2>x1:
			b=x2-x1
		else:
			b=0
		if t==3:
			v=-p+b
		else:
			v=p-b
	return v
def futuro (t, f,s):
	if t==1:
		v=s-f
	else:
		v=f-s
	return v

p=1.1
e=19
s=30
t=1
#(tipo opcion, prima,spot, ejercicio)
#tipo 1= Long call 2: short call  3: long put 4: short put
r=option(4,p,s,e)


# futuro= tipo 1: long 2: short
# futuro(tipo,futuro,spot)
r= futuro(2,e,s)


spot=[0,5,10,15,19,25,30]
lista=[]
for i in spot:
	pyg=option(1,p,i,e)
	lista.append(pyg)
print(lista)
def grafica():

	plt.plot(SPOT, ejex,'k')
	plt.plot(SPOT,act1,'b')
	plt.plot(SPOT, act2,'g')
	if len(act3)>2:
		plt.plot(SPOT, act3,'c')
	if len(act4)>2:
		plt.plot(SPOT, act4,'c')
	plt.plot(SPOT, act5,'r')
	plt.title("________ "+nlista,color='r')
	plt.show()


	

pr1=0; pr2=0; pr3=0; ej1=0; ej2=0; ej3=0; tend=0; vol=0; ivin=0; Maxben=0; Maxper=0; b_p=0
lsinteticas=["Call sintético comprado","Call sintético vendido","Put sintético comprado","Put sintético vendido","Futuro sintético comprado","Futuro sintético vendido"]
lcombinadas=["Cono comprado","Cono vendido","Cuna comprada","Cuna vendida","Tunel alcista","Tunel bajista"]
lspread= ["Bull Call","Bull PUT", "Bear Call","Bear Put", "Mariposa CALL Comprada","Mariposa Call Vendida","Mariposa Put Comprada","Mariposa Put Vendida"]
lratio=["Ratio Call Spread","Ratio Call back Spread", "Ratio Put Spread","Ratio Put Back Spread"]
nlista=""
ind=""
lestra=["Call sintético comprado","Call sintético vendido","Put sintético comprado","Put sintético vendido","Futuro sintético comprado","Futuro sintético vendido","Cono comprado","Cono vendido","Cuna comprada","Cuna vendida","Tunel alcista","Tunel bajista","Bull Call","Bull PUT", "Bear Call","Bear Put", "Mariposa CALL Comprada","Mariposa Call Vendida","Mariposa Put Comprada","Mariposa Put Vendida","Ratio Call Spread","Ratio Call back Spread", "Ratio Put Spread","Ratio Put Back Spread"]
# listas
SPOT=[]; act1=[] ; act2=[]; act3=[]; act4=[]; act5=[]; ejex=[]
nn1=0
def ventana2():
	v2=Toplevel(raiz)
	v2.title("Simulador Mejor Estrategia")
	v2.resizable(0,0)
	Label(v2, text="Aqui podras colocar diferentes precios de ejercicios con sus respectivas\n primas de la Call y Put, Seleccionar una estrategia y poder mirar\n  las posibles combinaciones que se pueden realizar y bajo un criterio\n( Flujo de caja inicial, Max perdida, Min perdida, Beneficio/Perdida)\n poder mirar la mejor combinacion\n\n", fg="gray6",font=("Loma",12)).grid(row=0,column=2,columnspan=7 ,stick=W)
	Label(v2, text=" Futuro", fg="gray6",font=("Loma",12)).grid(row=1,column=1,stick=W)
	Label(v2, text=" Ejercicio", fg="gray6",font=("Loma",12)).grid(row=2,column=1,stick=W)
	Label(v2, text=" Call", fg="gray6",font=("Loma",12)).grid(row=2,column=2,stick=W)
	Label(v2, text=" Put", fg="gray6",font=("Loma",12)).grid(row=2,column=3,stick=W)
	Label(v2, text=" Estrategia", fg="gray6",font=("Loma",12)).grid(row=6,column=2,stick=W)
	l=Label(v2, text=" Estrategia", fg="gray6",font=("Loma",12));l.grid(row=1,column=6,stick=W)

	f1=Entry(v2, validate="key", validatecommand=(validatecommand, "%S"));f1 .grid(row=1,column=2)
	e=Entry(v2, validate="key", validatecommand=(validatecommand, "%S"));e .grid(row=3,column=1)
	c=Entry(v2, validate="key", validatecommand=(validatecommand, "%S"));c .grid(row=3,column=2)
	p=Entry(v2, validate="key", validatecommand=(validatecommand, "%S"));p .grid(row=3,column=3)

	rr1 = Text(v2,width=6,height=5,bg= "khaki1");rr1.insert(INSERT,"Ejercicio\n");rr1.grid(column=1,row=5,stick=W+E)
	rr2 = Text(v2,width=6,height=5,bg= "khaki1");rr2.insert(INSERT,"Call\n");rr2.grid(column=2,row=5,stick=W+E)
	rr3 = Text(v2,width=6,height=5,bg= "khaki1");rr3.insert(INSERT,"Put\n");rr3.grid(column=3,row=5,stick=W+E)
	rr4 = Text(v2,width=21,height=15,bg= "khaki1");rr4.insert(INSERT,"Combinacion\n");rr4.grid(column=6,row=2,rowspan=7,stick=W+E)
	rr5 = Text(v2,width=21,height=15,bg= "khaki1");rr5.insert(INSERT,"Criterio\n");rr5.grid(column=7,row=2,rowspan=7,stick=W+E)

	cb1=ttk.Combobox(v2, state="readonly")
	cb1.grid(row=6,column=1)
	cb1["values"]=lestra
	df = pd.DataFrame(columns=("Ejercicio","Call","Prima"))
	

	def agregar():
		global nn1
		nn1=nn1+1
		df.loc[nn1] = [float(e.get()),float(c.get()),float(p.get())]
		rr1.insert(INSERT,str(e.get())+"\n")
		rr2.insert(INSERT,str(c.get())+"\n")
		rr3.insert(INSERT,str(p.get())+"\n")

		
	def com1():
		global nlista; global pr1; global pr2; global pr3; global ej1;global ej2;global ej3
		cr1=str(cr.get())
		if cr1=="1":
			crrr="F.C.I"
		elif cr1=="2":
			crrr="Max. ganancia"
		elif cr1=="3":
			crrr="Max. Perdida"
		elif cr1=="4":
			crrr="Beneficio/Perdida"

		rr4 = Text(v2,width=21,height=15,bg= "khaki1");rr4.insert(INSERT,"Combinacion\n");rr4.grid(column=6,row=2,rowspan=7,stick=W+E)
		rr5 = Text(v2,width=21,height=15,bg= "khaki1");rr5.insert(INSERT,crrr+"\n");rr5.grid(column=7,row=2,rowspan=7,stick=W+E)

		for i in df.index:
			nlista=cb1.get()
			pr1=df.loc[i].iloc[1]
			pr2=df.loc[i].iloc[2]
			pr3=0
			ej1=df.loc[i].iloc[0]
			ej2=df.loc[i].iloc[0]
			ej3=float(f1.get())
			resultado()
			l.config(text=nlista)
			rr4.insert(INSERT,str(df.loc[i].iloc[0])+"\n")
			
			if cr1=="1":
				rr5.insert(INSERT,str(ivin)+"\n")
			elif cr1=="2":
				rr5.insert(INSERT,str(Maxben)+"\n")
			elif cr1=="3":
				rr5.insert(INSERT,str(Maxper)+"\n")
			elif cr1=="4":
				rr5.insert(INSERT,str(b_p)+"\n")


	def com2():
		global nlista; global pr1; global pr2; global pr3; global ej1;global ej2;global ej3
		cr1=str(cr.get())
		jp=cb1.current()
		if cr1=="1":
			crrr="F.C.I"
		elif cr1=="2":
			crrr="Max. ganancia"
		elif cr1=="3":
			crrr="Max. Perdida"
		elif cr1=="4":
			crrr="Beneficio/Perdida"

		rr4 = Text(v2,width=21,height=15,bg= "khaki1");rr4.insert(INSERT,"Combinacion\n");rr4.grid(column=6,row=2,rowspan=7,stick=W+E)
		rr5 = Text(v2,width=21,height=15,bg= "khaki1");rr5.insert(INSERT,crrr+"\n");rr5.grid(column=7,row=2,rowspan=7,stick=W+E)

		for i in df.index:
			for e in df.index:
				ej1=df.loc[i].iloc[0]
				ej2=df.loc[e].iloc[0]

				if ej1< ej2:
					nlista=cb1.get()

					if jp<=11:

						pr1=df.loc[e].iloc[1]
						pr2=df.loc[i].iloc[2]
						pr3=0
						ej1=df.loc[e].iloc[0]
						ej2=df.loc[i].iloc[0]
						ej3=0
					else:
						if jp==12 or jp==13 or jp==14 or 15:

							pr1=df.loc[i].iloc[1]
							pr2=df.loc[e].iloc[1]
							pr3=0
							ej1=df.loc[i].iloc[0]
							ej2=df.loc[e].iloc[0]
							ej3=0
						else:
							pr1=df.loc[i].iloc[2]
							pr2=df.loc[e].iloc[2]
							pr3=0
							ej1=df.loc[i].iloc[0]
							ej2=df.loc[e].iloc[0]
							ej3=0

					resultado()
					l.config(text=nlista)
					rr4.insert(INSERT,str(df.loc[i].iloc[0])+"-"+str(df.loc[e].iloc[0])+"\n")
					
					if cr1=="1":
						rr5.insert(INSERT,str(ivin)+"\n")
					elif cr1=="2":
						rr5.insert(INSERT,str(Maxben)+"\n")
					elif cr1=="3":
						rr5.insert(INSERT,str(Maxper)+"\n")
					elif cr1=="4":
						rr5.insert(INSERT,str(b_p)+"\n")




	def com3():
		global nlista; global pr1; global pr2; global pr3; global ej1;global ej2;global ej3
		cr1=str(cr.get())
		jp=cb1.current()
		if cr1=="1":
			crrr="F.C.I"
		elif cr1=="2":
			crrr="Max. ganancia"
		elif cr1=="3":
			crrr="Max. Perdida"
		elif cr1=="4":
			crrr="Beneficio/Perdida"

		rr4 = Text(v2,width=21,height=15,bg= "khaki1");rr4.insert(INSERT,"Combinacion\n");rr4.grid(column=6,row=2,rowspan=7,stick=W+E)
		rr5 = Text(v2,width=21,height=15,bg= "khaki1");rr5.insert(INSERT,crrr+"\n");rr5.grid(column=7,row=2,rowspan=7,stick=W+E)

		for i in df.index:
			for e in df.index:
				for a in df.index:
					ej1=df.loc[i].iloc[0]
					ej2=df.loc[e].iloc[0]
					ej3=df.loc[a].iloc[0]
					prom= (ej1+ej2)/2

					if prom==ej3 and ej1<ej3:
						nlista=cb1.get()

						if jp==16 or jp== 17:
						
							pr1=df.loc[i].iloc[1]
							pr2=df.loc[e].iloc[1]
							pr3=df.loc[a].iloc[1]
							ej1=df.loc[i].iloc[0]
							ej2=df.loc[e].iloc[0]
							ej3=df.loc[a].iloc[0]
						else:
							pr1=df.loc[i].iloc[2]
							pr2=df.loc[e].iloc[2]
							pr3=df.loc[a].iloc[2]
							ej1=df.loc[i].iloc[0]
							ej2=df.loc[e].iloc[0]
							ej3=df.loc[a].iloc[0]
						
						resultado()
						l.config(text=nlista)
						rr4.insert(INSERT,str(df.loc[i].iloc[0])+"-"+str(df.loc[a].iloc[0])+"-"+str(df.loc[e].iloc[0])+"\n")
						
						if cr1=="1":
							rr5.insert(INSERT,str(ivin)+"\n")
						elif cr1=="2":
							rr5.insert(INSERT,str(Maxben)+"\n")
						elif cr1=="3":
							rr5.insert(INSERT,str(Maxper)+"\n")
						elif cr1=="4":
							rr5.insert(INSERT,str(b_p)+"\n")


	def ress():
		jp=cb1.current()

		if jp<=7:
			com1()
		elif jp>=16 and jp<=19:
			com3()
		else :
			com2()
		





	Button(v2, text="Agregar",font=("Loma",15),bg= "thistle1",fg="black",command=agregar).grid(column=1, row=4,columnspan=4, stick=W+E)
	Button(v2, text="Resultado",font=("Loma",15),bg= "thistle1",fg="black",command=ress).grid(column=1, row=8,columnspan=4,stick=W+E)
	cr = IntVar()
	ra1=Radiobutton(v2, text='F.C.I',value=1, variable=cr,font=("Loma",12));ra1.grid(column=1, row=7,stick=W)
	ra2=Radiobutton(v2, text='Max.Beneficio',value=2, variable=cr,font=("Loma",12));ra2.grid(column=2, row=7,stick=W)
	ra2=Radiobutton(v2, text='Max.Perdida',value=3, variable=cr,font=("Loma",12));ra2.grid(column=3, row=7,stick=W)
	ra2=Radiobutton(v2, text='Beneficio/Perdida',value=4, variable=cr,font=("Loma",12));ra2.grid(column=3, row=6,stick=W)









raiz= Tk()

raiz.title("Estrategias especualtivas con opciones y otros activos")
raiz.resizable(0,0)


def sintetica():

	l11.select()
	l12.grid_forget()

	l21.select()
	l22.grid_forget()
	l21.config(text="put")

	l31.select()
	l33.grid_forget()
	p3.grid_forget()
	
	l34.config(text="Futuro:")
	l31.config(text="Futuro")
	l35.grid_forget()
	l31.grid(column=1, row=9,stick=W)
	text1.config(text="")
	l34.grid(row=9,column=6,stick=W)
	e3.grid(row=9,column=7)

	l42.grid_forget()
	l41.select()

def combinada():

	
	l12.grid_forget()

	
	l22.grid_forget()
	l21.config(text="put")


	l31.grid_forget()
	l33.grid_forget()
	l34.grid_forget()
	l35.grid_forget()
	e3.grid_forget()
	p3.grid_forget()
	l42.grid(column=3, row=11,columnspan=2,stick=W)
	l11.select();l21.select()

def spread():
	l12.grid(column=2, row=7,stick=W)
	l21.config(text="")

	
	l22.grid_forget()
	l21.config(text="")

	l31.grid_forget()
	l33.grid_forget()
	l34.grid_forget()
	l35.grid_forget()
	text1.config(text="")
	e3.grid_forget()
	p3.grid_forget()
	l42.grid:grid_forget()

	l11.deselect();l12.deselect();l21.select()

def ratio():
	l12.grid(column=2, row=7,stick=W)
	l21.config(text="");	l21.select()

	l31.grid_forget(); l22.grid_forget()
	l33.grid_forget()
	l34.grid_forget()
	l35.grid_forget()
	text1.config(text="")
	e3.grid_forget()
	p3.grid_forget()
	l11.deselect();l12.deselect();l21.select()
	
	l42.grid_forget()
	l41.select()

def opcion3():
	VAR1=str(CPF1.get())
	VAR2=str(CPF2.get())
	VAR3=str(tip_est.get())
	
	if VAR1=="1"  and VAR3 =="3":
		l31.grid(column=1, row=9,stick=W)
		l31.config(text="CallDoble");
		l31.select()
		text1.config(text="Emedia se toma a partir de E1 Y E2 POR DEFAULT");

		text1.grid(column=2, row=9,stick=W,columnspan=4)
		l34.grid(column=6, row=9,stick=W)
		l34.config(text="Prima Em")
		e3.grid(column=7, row=9,stick=W)	

		l21.config(text="CALL")
	elif VAR1=="2" and VAR3 =="3":
		l31.grid(column=1, row=9,stick=W)
		l31.config(text="PutDoble");
		l31.select()
		text1.config(text="Emedia se toma a partir de E1 Y E2 POR DEFAULT");
		text1.grid(column=2, row=9,stick=W,columnspan=5)
		e3.grid(column=7, row=9,stick=W)	
		
		l21.config(text="PUT")
	
	if VAR1=="1" and VAR3=="4":
		l21.config(text="CALL")
		
	elif VAR1=="2" and (VAR3=="4" or VAR3=="3") :
		l21.config(text="PUT")
	if VAR1=="1" and VAR3=="2":
		l22.select()
		
	


def actualizar():
	sc=str(tip_est.get())
	global pr1; global pr2; global pr3; global ej1; global ej2; global ej3
	
	if sc=="1":
		pr1=str(p1.get());pr2=str(p2.get());ej1=str(e1.get());ej2=str(e2.get());ej3=str(e3.get())
		
		if pr1=="" or pr2==""or ej1=="" or ej2=="" or ej3=="":
			messagebox.showinfo(message="POR FAVOR INGRESAR TODOS LOS DATOS", title="DATOS INSUFICIENTES")
		elif ej1 != ej2:
			messagebox.showinfo(message="EL PRECIO DE EJERCICIO DE AMBAS OPCIONES DEBEN SER IGUALES", title="DATOS ERRONEOS")
		else:
			est.delete(0, END)
			est.insert(0,*lsinteticas)
			pr1=float(p1.get());pr2=float(p2.get());ej1=float(e1.get());ej2=float(e2.get());ej3=float(e3.get())

	elif sc=="2":
		pr1=str(p1.get());pr2=str(p2.get());ej1=str(e1.get());ej2=str(e2.get());ind1=str(indi.get())
		if pr1=="" or pr2==""or ej1=="" or ej2=="":
			messagebox.showinfo(message="POR FAVOR INGRESAR TODOS LOS DATOS", title="DATOS INSUFICIENTES")
		

		else:
			if ind1=="1":
				if ej1<=ej2  :
					messagebox.showinfo(message="El precio de ejercicio de la CALL debe ser mayor que la PUT", title="DATOS ERRONEOS")
				else:
					est.delete(0, END)
					est.insert(0,lcombinadas[4])
					est.insert(1,lcombinadas[5])
			elif ind1=="2":
				if ej1==ej2:
					est.delete(0, END)
					est.insert(0,lcombinadas[0]);est.insert(1,lcombinadas[1])
				elif ej1<=ej2  :
					messagebox.showinfo(message="El precio de ejercicio de la CALL debe ser mayor que la PUT", title="DATOS ERRONEOS")
				else:
					est.delete(0, END)
					est.insert(2,lcombinadas[2]);est.insert(3,lcombinadas[3])	

			pr1=float(p1.get());pr2=float(p2.get());ej1=float(e1.get());ej2=float(e2.get())	
				
	elif sc=="3":
		pr1=str(p1.get());pr2=str(p2.get());ej1=str(e1.get());ej2=str(e2.get());ind1=str(indi.get());pr3=str(e3.get())
		if pr1=="" or pr2==""or ej1=="" or ej2=="" or pr3=="":
			messagebox.showinfo(message="POR FAVOR INGRESAR TODOS LOS DATOS", title="DATOS INSUFICIENTES")
		elif ej1 == ej2:
			messagebox.showinfo(message="EL PRECIO DE EJERCICIO DE AMBAS OPCIONES NO DEBEN SER IGUALES", title="DATOS ERRONEOS")
		elif ej1 > ej2:
				messagebox.showinfo(message="Por favor porner primero el Precio de \n ejercicio menor en primer lugar", title="DATOS ERRONEOS")
		else:
			
			if ind1=="1":
				if str(CPF1.get())=="1":
					est.delete(0, END)
					est.insert(0,lspread[0])
					est.insert(1,lspread[2])
				else:
					est.delete(0, END)
					est.insert(2,lspread[1])
					est.insert(3,lspread[3])
			elif ind1=="2":
				if str(CPF1.get())=="1":
					est.delete(0, END)
					est.insert(0,lspread[4])
					est.insert(1,lspread[5])
				else:
					est.delete(0, END)
					est.insert(2,lspread[6])
					est.insert(3,lspread[7])
			
			pr1=float(p1.get());pr2=float(p2.get());ej1=float(e1.get());ej2=float(e2.get());pr3=float(e3.get());ej3=(ej2+ej1)/2

	elif sc=="4":
			pr1=str(p1.get());pr2=str(p2.get());ej1=str(e1.get());ej2=str(e2.get())
			if pr1=="" or pr2==""or ej1=="" or ej2=="" or pr3=="":
				messagebox.showinfo(message="POR FAVOR INGRESAR TODOS LOS DATOS", title="DATOS INSUFICIENTES")
			elif ej1 == ej2:
				messagebox.showinfo(message="EL PRECIO DE EJERCICIO DE AMBAS OPCIONES NO DEBEN SER IGUALES", title="DATOS ERRONEOS")
			elif ej1 > ej2:
				messagebox.showinfo(message="Por favor porner primero el Precio de \n ejercicio menor en primer lugar", title="DATOS ERRONEOS")
			else:
				est.delete(0, END)
				if str(CPF1.get())=="1":
					est.delete(0, END)
					est.insert(0,lratio[0])
					est.insert(1,lratio[1])
				else:
					est.delete(0, END)
					est.insert(2,lratio[2])
					est.insert(3,lratio[3])
			
				pr2=float(p2.get());pr1=float(p1.get());ej2=float(e2.get());ej1=float(e1.get())


				

			

titulo= Label(raiz, text="ESTRATEGIAS ESPECULATIVAS CON OPCIONES Y OTROS ACTIVOS",justify="center", fg="red4",bg="gold2",font=("Loma",15))
titulo.grid(row=1,column=1,columnspan=13,stick=W+E)
Label(raiz,bg="light goldenrod", text=" La siguiente aplicación está diseñada para que a partir de una serie de datos de entrada, el usuario construya el \ntipo de estrategia especulativa que desea.Una vez completados los datos solicitados, la herramienta \npermite verla gráfica de la estrategia seleccionada, el cuadro de utilidades en función del spot, puntos de equilibrio,\n máxima pérdida, máxima ganancia\n\n ",  fg="gray6",font=("Loma",12)).grid(row=2,column=1,columnspan=13,stick=W+E)
#izquierda
Label(raiz, text=" Datos",  justify="center",fg="gray6",font=("Loma",15)).grid(row=3,column=1,columnspan=7)

Label(raiz, text=" 1) Seleccione el tipo de estrategia", fg="gray6",font=("Loma",15)).grid(row=4,column=1,columnspan=7,stick=W)
tip_est = IntVar()
Radiobutton(raiz, text='Sintetica',value=1, variable=tip_est,font=("Loma",12),command=sintetica).grid(column=1,columnspan=2, row=5,stick=W)
Radiobutton(raiz, text='Combinada',value=2, variable=tip_est,font=("Loma",12),command=combinada).grid(column=3,columnspan=2, row=5,stick=W)
Radiobutton(raiz, text='Spreads-Diferenciales',value=3, variable=tip_est,font=("Loma",12),command=spread).grid(column=5,columnspan=2, row=5,stick=W)
Radiobutton(raiz, text='Ratios',value=4, variable=tip_est,font=("Loma",12),command=ratio).grid(column=7,columnspan=2, row=5,stick=W)

Label(raiz, text=" 2)Completa los Datos", fg="gray6",font=("Loma",15)).grid(row=6,column=1,columnspan=7,stick=W)
def is_valid_char(char):
    return char in "0123456789."
validatecommand = raiz.register(is_valid_char)
CPF1 = IntVar()
l11=Radiobutton(raiz, text='Call',value=1, variable=CPF1,font=("Loma",12),command=opcion3); l11.grid(column=1, row=7,stick=W)
l12=Radiobutton(raiz, text='Put',value=2, variable=CPF1,font=("Loma",12),command=opcion3);l12.grid(column=2, row=7,stick=W)
Label(raiz, text=" Prima:", fg="gray6",font=("Loma",12)).grid(row=7,column=4,stick=W)
p1= Entry(raiz, validate="key", validatecommand=(validatecommand, "%S")); p1.grid(row=7,column=5,)


Label(raiz, text=" Ejercicio:", fg="gray6",font=("Loma",12)).grid(row=7,column=6,stick=W)
e1=Entry(raiz, validate="key", validatecommand=(validatecommand, "%S"));e1.grid(row=7,column=7)

CPF2 = IntVar()
l21=Radiobutton(raiz, text='CALL',value=1, variable=CPF2,font=("Loma",12),command=opcion3);l21.grid(column=1, row=8,stick=W)
l22=Radiobutton(raiz, text='PUT',value=2, variable=CPF2,font=("Loma",12),command=opcion3);l22.grid(column=2, row=8,stick=W)
Label(raiz, text=" Prima:", fg="gray6",font=("Loma",12)).grid(row=8,column=4,stick=W)
p2=Entry(raiz, validate="key", validatecommand=(validatecommand, "%S"));p2 .grid(row=8,column=5)
Label(raiz, text=" Ejercicio:", fg="gray6",font=("Loma",12)).grid(row=8,column=6,stick=W)
e2=Entry(raiz, validate="key", validatecommand=(validatecommand, "%S"));e2.grid(row=8,column=7)

CPF3 = IntVar()
l31=Radiobutton(raiz, text='CALL',value=1, variable=CPF3,font=("Loma",12));l31.grid(column=1, row=9,stick=W)
text1=Label(raiz,text=""); text1.grid(column=2, row=9,stick=W)	
l33=Radiobutton(raiz, text='FUTURO',value=3, variable=CPF3,font=("Loma",12));l33.grid(column=3, row=9,stick=W)
l35=Label(raiz, text=" Prima:", fg="gray6",font=("Loma",12));l35.grid(row=9,column=4,stick=W)
p3=Entry(raiz, validate="key", validatecommand=(validatecommand, "%S"));p3.grid(row=9,column=5)
l34=Label(raiz, text=" Ejercio o Futuro",fg="gray6",font=("Loma",12));l34.grid(row=9,column=6,stick=W)
e3=Entry(raiz, validate="key", validatecommand=(validatecommand, "%S"));e3.grid(row=9,column=7)

Label(raiz, text=" 3) Tipo de indicador", fg="gray6",font=("Loma",15)).grid(row=10,column=1,columnspan=7,stick=W)
indi = IntVar()
l41=Radiobutton(raiz, text='Tendencia',value=1, variable=indi,font=("Loma",12));l41.grid(column=1, row=11,columnspan=2,stick=W)
l42=Radiobutton(raiz, text='Volatilidad',value=2, variable=indi,font=("Loma",12));l42.grid(column=3, row=11,columnspan=2,stick=W)


Button(raiz, text="Actualizar",font=("Loma",15),bg= "thistle1",fg="black",command=actualizar).grid(column=1, row=12,columnspan=7,stick=W+E)


Label(raiz, text=" Posibles estrategias", justify="center",fg="gray6",font=("Loma",15)).grid(row=13,column=1,columnspan=7,stick=W+E)
est=Listbox(raiz,bg="cornsilk2");est.grid(row=14,column=1,columnspan=7,rowspan=8,stick=W+E+N+S)
def res():
	global nlista
	nlista= str(est.get(est.curselection()))
	resultado()

def actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t):
	d1.config(text=nlista); d2.config( text=comb) ; d3.config(text=estr)
	d8.config( text=d8t); d9.config(text=d9t); d10.config(text=d10t); d11.config(text=d11t)
	d12.config(text=d12t); d13.config(text=d13t); d14.config(text=d14t); d15.config(text=d15t)
	d16.config(text=d16t);d17.config(text=d17t) ;d18.config(text=d18t);d19.config(text=d19t)
	d20.config(text=d20t);d21.config(text=d21t);d22.config(text=d22t);d23.config(text=d23t)
	d24.config(text=d24t);d25.config( text=d25t);d28.config( text=d28t)
	d29.config( text=d29t);d26.config(text=d26t)
def resultado():
    global SPOT ;global act1 ;global act2 ; global act3 ;global act4 ;global act5 ;global ejex;global ivin; global Maxben;
    global Maxper; global b_p; global tend; global vol

    if nlista == "Call sintético comprado":
    	d1.config( text=nlista)

    	comb="Formado por: fututo comprado (Valor: "+str(ej3)+") \n y una Put comprada con precio de ejercicio de "+ str(ej1)
    	estr="Estrategia de tendencia alcista y volatilidad indiferente"
    	PG1= ej1-pr2-ej3
    	PG2=-pr2-ej3

    	ivin= ej1+-ej3 - pr2;     Maxben="Ilimitada";      Maxper=f"{PG1:.2f}"
    	b_p="N/A"       ; tend= "Alcista";        vol="Indiferente"  
    	EQ1=0; EQ2=0 

    	if ej1==(pr2+ej3)and ivin<0:
    		EQ1="desde 0 a "+str(ej1)
    		EQ2= "N/A"
    	elif ej1<(pr2+ej3)and ivin<0:
    		EQ1= "N/A"
    		EQ2=pr2+ej3
    	else: 
    		EQ1= "N/A"
    		EQ2= "N/A"

    	d8t="S < E" ; d9t="E - P -F" ; d10t=f"{PG1:.2f}"; d11t=EQ1
    	d12t="S >= E" ; d13t="S - F - P" ; d14t="S + ("f"{PG2:.2f}" + ")"; d15t=EQ2
    	d16t="" ; d17t="" ; d18t=""; d19t=""
    	d20t="" ; d21t="" ; d22t=""; d23t=""
    	d24t="Maxima perdida: "+f"{PG1:.2f}" ; d25t="Maxima ganancia= ilimitada"
    	d28t="Flujo de caja inicial: "+f"{ivin:.2f}"	
    	d29t="Beneficio/perdida: No aplica"

    	if -PG1<pr1:
    		d26t="La Long Call sintetico es mas favorable que la Lang Call"
    	else:
    	    d26t="La Long Call es mas favorable que la Lang Call sintentico"
    	
    	actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)
	    
    	ej4 = (ej1*1.5); SPOT=[0,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
    	for i in SPOT:
    		pyg=option(3,pr2,i,ej2) ;act1.append(pyg)
    	for i in SPOT:
    		pyg=futuro(1,ej3,i)  ;act2.append(pyg)
    	for i in act1:
    		act5.append(act1[nind]+act2[nind]) ;nind=nind+1
    	for i in SPOT: 
    		ejex.append(0)
    elif nlista == "Call sintético vendido":
        	d1.config( text=nlista)
        	comb="Formado: fututo vendido (Valor "+str(ej3) + ") \n y una Put vendido con ejercicio de: "+str(ej1)
        	estr="Estrategia de tendencia bajista y volatilidad indiferente"
        	PG1= -ej1+pr2+ej3
        	PG2=+pr2+ej3
        	ivin= -ej1+ ej3 + pr2;  Maxben=f"{PG1:.2f}";      Maxper="Ilimitada"
        	b_p="N/A"       ; tend= "Bajista";        vol="Indiferente"  
        	if ej1==(pr2+ej3)and ivin<0:
        		EQ1="desde 0 a "+str(ej1)
        		EQ2= "N/A"
        	elif ej1<(pr2+ej3)and ivin<0:
        		EQ1= "N/A"
        		EQ2=pr2+ej3
        	else: 
        		EQ1= "N/A"
        		EQ2= "N/A"

        	d8t="S < E" ; d9t="F + P - E" ; d10t=f"{PG1:.2f}"; d11t=EQ1
        	d12t="S >= E" ; d13t="F + P - S" ; d14t="-S + ("f"{PG2:.2f}" + ")"; d15t=EQ2
        	d16t="" ; d17t="" ; d18t=""; d19t=""
        	d20t="" ; d21t="" ; d22t=""; d23t=""
        	d24t="Maxima perdida: Ilimitada" ; d25t="Maxima ganancia: "+f"{PG1:.2f}"
        	d28t="Flujo de caja inicial: "+f"{ivin:.2f}"
        	d29t="Beneficio/perdida: no aplica"

        	if PG1>pr1:
        		d26t="La Short Call sintetico es mas favorable que la Short Call"
        	else:
        	   d26t="La Short Call es mas favorable que la Short Call sintentico"
        	actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        	ej4 = (ej1*1.5); SPOT=[0,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        	for i in SPOT:
        		pyg=option(4,pr2,i,ej2)
        		act1.append(pyg)
        	for i in SPOT:
        		pyg=futuro(2,ej3,i)
        		act2.append(pyg)
        	for i in act1:
        		act5.append(act1[nind]+act2[nind])
        		nind=nind+1
        	for i in SPOT:
        		ejex.append(0)

    elif nlista == "Put sintético comprado":
    	d1.config( text=nlista)
    	
    	PG2= ej3-ej1-pr1
    	PG1=ej3-pr1
    	ivin= ej3 - pr1 -ej1; Maxben=PG1;      Maxper=PG2
    	b_p=Maxben/-Maxper if (Maxben>0 and Maxper<0) else "N/A"      ; tend= "Bajista";        vol="Indiferente"  
    	if ej1==(-pr1+ej3)and ivin<0:
    		EQ2="desde "+str(ej1)+ " hasta infinito"
    		EQ1= "N/A"
    	elif ej3>(-pr1+ej1)and ivin<0:
    		EQ2= "N/A"
    		EQ1=-pr1+ej3
    	else: 
    		EQ1= "N/A"
    		EQ2= "N/A"

    	comb="Formado por: Fututo vendido (Valor "+str(ej3)+")\n y una Call comprada con ejercio de "+str(ej1)
    	estr="Estrategia de tendencia bajista y volatilidad indiferente"

    	d8t="S < E" ; d9t="F - S - C" ; d10t="-S + ("f"{PG1:.2f}"+")"; d11t=EQ1
    	d12t="S >= E" ; d13t="F - E - C" ; d14t=f"{PG2:.2f}" ; d15t=EQ2
    	d16t="" ; d17t="" ; d18t=""; d19t=""
    	d20t="" ; d21t="" ; d22t=""; d23t=""
    	d24t="Maxima perdida: "+f"{PG2:.2f}" ; d25t="Maxima ganancia: "+f"{PG1:.2f}"
    	d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
    	d29t="Beneficio/perdida: "+str(b_p)

    	if PG2<pr2:
    		d26t="La Long Put sintetico es mas favorable que la Long Put"
    	else:
    	    d26t="La Long Put es mas favorable que la Long Put sintentico"
    	actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

    	ej4 = (ej1*1.5); SPOT=[0,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
    	for i in SPOT:
    		pyg=option(1,pr1,i,ej2)
    		act1.append(pyg)
    	for i in SPOT:
    		pyg=futuro(2,ej3,i)
    		act2.append(pyg)
    	for i in act1:
    		act5.append(act1[nind]+act2[nind])
    		nind=nind+1
    	for i in SPOT:
    		ejex.append(0)
    elif nlista == "Put sintético vendido":

    	d1.config( text=nlista)

    	PG2= -ej3+ej1+pr1
    	PG1=-ej3+pr1
    	ivin= -ej3 + pr1 + ej1; Maxben=PG2    ;  Maxper=PG1
    	b_p=Maxben/-Maxper if (Maxben>0 and Maxper<0) else "N/A"      ; tend= "Alcista";        vol="Indiferente"  
    	if ej1==(-pr1+ej3)and ivin>0:
    		EQ2="desde "+str(ej1)+ " hasta infinito"
    		EQ1= "N/A"
    	elif ej1>(-pr1+ej3) and ivin>0:
    		EQ2= "N/A"
    		EQ1=-pr1+ej3
    	else: 
    		EQ1= "N/A"
    		EQ2= "N/A"

    	comb="Formado por: fututo Comprado (Valor "+str(ej3)+")\n y  una Call Vendido con Ejercicio de "+str(ej1)
    	estr="Estrategia de tendencia alcista y volatilidad indiferente" 
    	d8t="S < E" ; d9t="- F + S +  C"; d10t="S + ("f"{PG1:.2f}"+")"; d11t= EQ1
    	d12t="S >= E" ; d13t="-F + E + C" ; d14t=f"{PG2:.2f}"  ; d15t=EQ2
    	d16t="" ; d17t="" ; d18t=""; d19t=""
    	d20t="" ; d21t="" ; d22t=""; d23t=""
    	d24t="Maxima perdida: "+f"{PG1:.2f}" ; d25t="Maxima ganancia: "+f"{PG2:.2f}"

    	d28t="Flujo de caja inicial: "+f"{ivin:.2f}"
    	d29t="Beneficio/perdida: "+str(b_p)

    	if PG2>pr2:
    		d26t="La Short Put sintetico es mas favorable que la ShortPut"
    	else:
    	    d26t="La Short Put es mas favorable que la Short Put sintentico"
    	actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

    	ej4 = (ej1*1.5); SPOT=[0,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
    	for i in SPOT:
    		pyg=option(2,pr1,i,ej1)
    		act1.append(pyg)
    	for i in SPOT:
    		pyg=futuro(1,ej3,i)
    		act2.append(pyg)
    	for i in act1:
    		act5.append(act1[nind]+act2[nind])
    		nind=nind+1
    	for i in SPOT:
    		ejex.append(0)

    elif nlista == "Futuro sintético comprado":
    	d1.config( text=nlista); 
    	
    	PG2= pr2-ej1-pr1
    	PG1=pr2-ej1-pr1
    	ivin= -pr1+pr2 ; Maxben="Ilimitada";      Maxper=f"{PG1:.2f}"
    	b_p="N/A"      ; tend= "Alcista";        vol="Indiferente"  
    	
    	if pr1<pr2:
    		EQ2="N/A"
    		EQ1= ej1-(pr2-pr1)
    	else:
    		EQ1="N/A"
    		EQ2= ej1+(pr1-pr2)
    	
    	comb="Formado por un Call Comprado + Put Vendido con ejercicio de "+str(ej1)
    	estr="Estrategia de tendencia alcista y volatilidad indiferente" 
    	d8t="S < E" ; d9t="S + P -E - C"; d10t="S + ("f"{PG1:.2f}"+")"; d11t= EQ1
    	d12t="S >= E" ; d13t="S + P - E -C" ; d14t="S + ("+f"{PG2:.2f}" +")"; d15t=EQ2
    	d16t="" ; d17t="" ; d18t=""; d19t=""
    	d20t="" ; d21t="" ; d22t=""; d23t=""
    	d24t="Maxima perdida : "+f"{PG1:.2f}" ; d25t="Maxima ganancia: Ilimitada"
    	
    	d28t="Flujo de caja inicial: "+f"{ivin:.2f}"
    	d29t="Beneficio/perdida: no aplica"
    	

    	if -PG2<ej3:
    		d26t="La Long Futuro sintetico es mas favorable que la Long Futuro"
    	else:
    	    d26t="La Long Futuro es mas favorable que la Long Futuro sintentico"
    	actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

    	ej4 = (ej1*1.5); SPOT=[0,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
    	for i in SPOT:
    		pyg=option(1,pr1,i,ej1)
    		act1.append(pyg)
    	for i in SPOT:
    		pyg=option(4,pr2,i,ej2)
    		act2.append(pyg)
    	for i in act1:
    		act5.append(act1[nind]+act2[nind])
    		nind=nind+1
    	for i in SPOT:
    		ejex.append(0)
    elif nlista == "Futuro sintético vendido":
    	
    	PG2= -pr2+ej1+pr1
    	PG1=-pr2+ej1+pr1
    	ivin= pr1 - pr2; Maxben=f"{PG1:.2f}";      Maxper="Ilimitada"
    	b_p="N/A"      ; tend= "Bajista";        vol="Indiferente"  
    	
    	if pr1<pr2:
    		EQ2="N/A"
    		EQ1= ej1-(pr2-pr1)
    	else:
    		EQ1="N/A"
    		EQ2= ej1+(pr1-pr2)
    	comb="Formado por un Call Vendida + Put Comprada con ejercico de "+str(ej1)
    	estr="Estrategia de tendencia bajista y volatilidad indiferente" 
    	d8t="S < E" ; d9t="-S - P +E + C"; d10t="-S + ("f"{PG1:.2f}"+")"; d11t= EQ1
    	d12t="S >= E" ; d13t="-S - P + E + C" ; d14t="-S + ("+f"{PG2:.2f}"+")" ; d15t=EQ2
    	d16t="" ; d17t="" ; d18t=""; d19t=""
    	d20t="" ; d21t="" ; d22t=""; d23t=""
    	d24t="Maxima perdida= Ilimitada" ; d25t="Maxima ganancia: "+f"{PG1:.2f}"

    	
    	d28t="Flujo de caja inicial: "+f"{ivin:.2f}"
    	d29t="Beneficio/perdida: no aplica"

    	if PG2>ej3:
    		d26t="La Long Futuro sintetico es mas favorable que la Long Futuro"
    	else:
    	    d26t="La Long Futuro es mas favorable que la Long Futuro sintentico"
    	actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

    	ej4 = (ej1*1.5); SPOT=[0,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
    	for i in SPOT:
    		pyg=option(2,pr1,i,ej1)
    		act1.append(pyg)
    	for i in SPOT:
    		pyg=option(3,pr2,i,ej2)
    		act2.append(pyg)
    	for i in act1:
    		act5.append(act1[nind]+act2[nind])
    		nind=nind+1
    	for i in SPOT:
    		ejex.append(0)
    elif nlista == "Cono comprado":

        d1.config( text=nlista);

        PG2= -pr1-pr2+ej1
        PG1=-pr2-pr1 - ej1
        ivin= -pr1 -pr2;  Maxben="Ilimitada";      Maxper=-pr1-pr2
        b_p="N/A"      ; tend= "Indiferente";        vol="Alta"  
        

        comb="Formado por un Long Call + Long Put con Ejercicio de "+str(ej1)
        estr="Estrategia de tendencia indiferente y Alta volatilidad" 
        d8t="S < E" ; d9t="E - S -P - C"; d10t="-S + ("f"{PG2:.2f}"+")"; d11t= PG2
        d12t="S >= E" ; d13t="S - E - C - P" ; d14t="S + ("f"{PG1:.2f}"+")"; d15t=-PG1
        d16t="" ; d17t="" ; d18t=""; d19t=""
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej1*2); SPOT=[0,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(1,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(3,pr2,i,ej2)
            act2.append(pyg)
        for i in act1:
            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Cono vendido":
        d1.config( text=nlista);

        PG2= +pr1+pr2-ej1
        PG1=+pr2+pr1 + ej1
        ivin= +pr1 +pr2;  Maxben=pr1+pr2;      Maxper="ilimitada"
        b_p="N/A"      ; tend= "Indiferente";        vol="Baja"  
        

        comb="Formado por un Short Call + Shor Put con Ejercicio de "+str(ej1)
        estr="Estrategia de tendencia indiferente y Baja volatilidad"

        d8t="S < E" ; d9t="-E + S +P + C"; d10t="S + ("f"{PG2:.2f}"+")"; d11t= -PG2
        d12t="S >= E" ; d13t="-S + E + C + P" ; d14t="-S + ("f"{PG1:.2f}"+")"; d15t= PG1
        d16t="" ; d17t="" ; d18t=""; d19t=""
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej1*2); SPOT=[0,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(2,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(4,pr2,i,ej2)
            act2.append(pyg)
        for i in act1:
            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Cuna comprada":
        d1.config( text=nlista);

        PG2= ej2-pr2-pr1
        PG1=-ej1-pr2-pr1
        ivin= -pr1 -pr2;  Maxben="Ilimitada";      Maxper=-pr1-pr2
        b_p="N/A"      ; tend= "Indiferente";        vol="Alta"  
        

        comb="Formado por un Long  Call con P.ejercicio de: "+str(ej1) +"\n y una Long Put con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia indiferente y Alta volatilidad"

        d8t="S < E1" ; d9t="E1 - S - P -C"; d10t="- S + ("f"{PG2:.2f}"+")"; d11t= PG2
        d12t="E1<= S <= E2" ; d13t="-P - C" ; d14t= f"{Maxper:.2f}"; d15t= "N/A"
        d16t="S>E2" ; d17t="S - E2 -P - C" ; d18t="S  "f"{PG1:.2f}" ; d19t= -PG1
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej2,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(3,pr2,i,ej2)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(1,pr1,i,ej1)
            act2.append(pyg)
        for i in act1:
            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Cuna vendida":
        d1.config( text=nlista);
        

        PG2= -ej2+ pr2+ pr1
        PG1=+ej1+pr2+pr1
        ivin= +pr1 +pr2;  Maxper="Ilimitada";      Maxben=+pr1+pr2
        b_p="N/A"      ; tend= "Indiferente";        vol="Baja"  
        

        comb="Formado por un Short  Call con P.ejercicio de: "+str(ej1) +"\n y una Short Put con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia indiferente y Baja volatilidad"

        d8t="S < E1" ; d9t="-E1 + S + P +C"; d10t=" S + ("f"{PG2:.2f}"+")"; d11t= -PG2
        d12t="E1<= S <= E2" ; d13t="+P + C" ; d14t= f"{Maxben:.2f}"; d15t= "N/A"
        d16t="S>E2" ; d17t="-S + E2 +P + C" ; d18t="-S  + "f"{PG1:.2f}" ; d19t= PG1
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej2,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(4,pr2,i,ej2)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(2,pr1,i,ej1)
            act2.append(pyg)
        for i in act1:
            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)

    elif nlista == "Tunel bajista":
        d1.config( text=nlista);
        

        PG2= ej2-pr2+pr1
        PG1=ej1-pr2+pr1
        ivin= +pr1 -pr2;  Maxper="Ilimitada";      Maxben=PG2
        b_p="N/A"      ; tend= "Bajista";        vol="Indiferente"  
        if pr1==pr2:
            EQ1="N/A"; EQ2="Desde "+str(ej2)+" hasta "+str(ej1); EQ3="N/A"
        elif pr1<pr2:
            EQ1=PG2; EQ2="N/A"; EQ3="N/A"
        else:
            EQ1="N/A"; EQ2="N/A"; EQ3=PG1

        comb="Formado por un Short  Call con P.ejercicio de: "+str(ej1) +"\n y una Long Put con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia bajista y volatilidad indiferente"

        d8t="S < E1" ; d9t="E1 - S- P + C"; d10t=" S + ("f"{PG2:.2f}"+")"; d11t= EQ1
        d12t="E1<= S <= E2" ; d13t="-P + C" ; d14t= f"{ivin:.2f}"; d15t= EQ2
        d16t="S>E2" ; d17t="-S + E2 + C - P" ; d18t="-S  + "f"{PG1:.2f}" ; d19t= EQ3
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej2,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(3,pr2,i,ej2)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(2,pr1,i,ej1)
            act2.append(pyg)
        for i in act1:
            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Tunel alcista":
        d1.config( text=nlista);
        

        PG2= -ej2+pr2-pr1
        PG1=-ej1+pr2-pr1
        ivin= -pr1 +pr2;  Maxben="Ilimitada";      Maxper=PG2
        b_p="N/A"      ; tend= "Alcista";        vol="Indiferente"  
        if pr1==pr2:
            EQ1="N/A"; EQ2="Desde "+str(ej2)+" hasta "+str(ej1); EQ3="N/A"
        elif pr1<pr2:
            EQ1=-PG2; EQ2="N/A"; EQ3="N/A"
        else:
            EQ1="N/A"; EQ2="N/A"; EQ3=-PG1

        comb="Formado por un Long Call con P.ejercicio de: "+str(ej1) +"\n y una Short Put con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia Alcista y volatilidad indiferente"

        d8t="S < E1" ; d9t="-E1 + S + P - C"; d10t=" S  ("f"{PG2:.2f}"+")"; d11t= EQ1
        d12t="E1<= S <= E2" ; d13t="+P - C" ; d14t= f"{ivin:.2f}"; d15t= EQ2
        d16t="S>E2" ; d17t="+S - E2 - C + P" ; d18t="S  "f"{PG1:.2f}" ; d19t= EQ3
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej2,ej1,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(4,pr2,i,ej2)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(1,pr1,i,ej1)
            act2.append(pyg)
        for i in act1:
            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)

    elif nlista == "Bull Call":
        d1.config( text=nlista);
        

        PG2= -ej1-pr1+pr2
        PG1=-pr1+pr2-ej1+ej2
        ivin= -pr1+pr2;  Maxben=PG1;      Maxper=ivin
        b_p=Maxben/-Maxper if (Maxben>0 and Maxper<0) else "N/A"       ; tend= "Alcista";        vol="Indiferente"  
        if pr1==pr2:
            EQ1="Desde 0 hasta "+str(ej1); EQ2="N/A"; EQ3="N/A"
        elif pr1<pr2:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"
        elif PG1>0:
            EQ1="N/A"; EQ2=str(PG2); EQ3="N/A"
        elif PG1==0:
            EQ1="N/A"; EQ2=str(PG2); EQ3="Desde "+str(ej12)+" Hasta infinito"
        else:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"

        comb="Formado por un Long Call con P.ejercicio de: "+str(ej1) +"\n y una Short Call con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia Alcista y volatilidad indiferente"

        d8t="S < E1" ; d9t="-C1 + C2"; d10t=str(ivin); d11t= EQ1
        d12t="E1<= S <= E2" ; d13t="S - E1 -C1 + C2" ; d14t="S "f"{PG2:.2f}"; d15t= EQ2
        d16t="S>E2" ; d17t="-E1 - C1 - C2 + E2" ; d18t=f"{PG2:.2f}" ; d19t= EQ3
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej1,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(1,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(2,pr2,i,ej2)
            act2.append(pyg)
        for i in act1:
            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Bear Call":
        d1.config( text=nlista);
        

        PG2= ej1+pr1-pr2
        PG1=pr1-pr2+ej1-ej2
        ivin= +pr1-pr2;  Maxper=PG1;      Maxben=ivin
        b_p=Maxben/-Maxper if (Maxben>0 and Maxper<0) else "N/A"      ; tend= "Bajista";        vol="Indiferente"  
        if pr1==pr2:
            EQ1="Desde 0 hasta "+str(ej1); EQ2="N/A"; EQ3="N/A"
        elif pr1<pr2:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"
        elif PG1<0:
            EQ1="N/A"; EQ2=str(PG2); EQ3="N/A"
        elif PG1==0:
            EQ1="N/A"; EQ2="N/A"; EQ3="Desde "+str(ej12)+" Hasta infinito"
        else:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"

        comb="Formado por un Short Call con P.ejercicio de: "+str(ej1) +"\n y una Long Call con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia Bajista y volatilidad indiferente"

        d8t="S < E1" ; d9t="+C1 - C2"; d10t=str(ivin); d11t= EQ1
        d12t="E1<= S <= E2" ; d13t="-S + E1 +C1 - C2" ; d14t="-S +"f"{PG2:.2f}"; d15t= EQ2
        d16t="S>E2" ; d17t="E1 + C1 - C2 - E2" ; d18t=f"{PG2:.2f}" ; d19t= EQ3
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej1,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(2,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(1,pr2,i,ej2)
            act2.append(pyg)
        for i in act1:
            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Bear Put":
        d1.config( text=nlista);
        

        PG2= ej2-pr2+pr1-ej1
        PG1=ej2-pr2 +pr1
        ivin= -pr2 + pr1;  Maxper=ivin;      Maxben=PG2
        b_p=Maxben/-Maxper if (Maxben>0 and Maxper<0) else "N/A"      ; tend= "Bajista";        vol="Indiferente"  
        if pr1==pr2:
            EQ3="Desde "+str(ej2)+" Hasta infinito"; EQ2="N/A"; EQ1="N/A"
        elif pr1>pr2:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"
        elif PG2>0:
            EQ1="N/A"; EQ2=str(PG1); EQ3="N/A"
        elif PG1==0:
            EQ3="N/A"; EQ2="N/A"; EQ1="Desde 0 hasta "+str(ej1)
        else:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"

        comb="Formado por un Short PUT con P.ejercicio de: "+str(ej1) +"\n y una Long PUT con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia Bajista y volatilidad indiferente"

        d8t="S < E1" ; d9t="E2 - P2 + P1 -E1"; d10t=str(PG2); d11t= EQ1
        d12t="E1<= S <= E2" ; d13t="E2 - S - P2 + P1" ; d14t="-S +"f"{PG1:.2f}"; d15t= EQ2
        d16t="S>E2" ; d17t="-P2 + P1" ; d18t=f"{ivin:.2f}" ; d19t= EQ3
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej1,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(4,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(3,pr2,i,ej2)
            act2.append(pyg)
        for i in act1:
            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)

    elif nlista == "Bull PUT":
        d1.config( text=nlista);
        

        PG2= -ej2+pr2-pr1+ej1
        PG1=-ej2+pr2 -pr1
        ivin= pr2 - pr1;  Maxben=ivin;      Maxper=PG2
        b_p=Maxben/-Maxper if (Maxben>0 and Maxper<0) else "N/A"      ; tend= "Alcista";        vol="Indiferente"  
        if pr1==pr2:
            EQ3="Desde "+str(ej2)+" Hasta infinito"; EQ2="N/A"; EQ1="N/A"
        elif pr1>pr2:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"
        elif PG2<0:
            EQ1="N/A"; EQ2=str(PG1); EQ3="N/A"
        elif PG1==0:
            EQ3="N/A"; EQ2="N/A"; EQ1="Desde 0 hasta "+str(ej1)
        else:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"

        comb="Formado por un Long PUT con P.ejercicio de: "+str(ej1) +"\n y una Short PUT con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia Alcista y volatilidad indiferente"

        d8t="S < E1" ; d9t="-E2 + P2 - P1 +E1"; d10t=str(PG2); d11t= EQ1
        d12t="E1<= S <= E2" ; d13t="-E2 + S + P2 - P1" ; d14t="S "f"{PG1:.2f}"; d15t= EQ2
        d16t="S>E2" ; d17t="+P2 - P1" ; d18t=f"{ivin:.2f}" ; d19t= EQ3
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej1,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(3,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(4,pr2,i,ej2)
            act2.append(pyg)
        for i in act1:
            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Mariposa CALL Comprada":
        d1.config( text=nlista);
        

        PG2= -pr1-pr2+(2*pr3) - ej1
        PG1=-pr1-pr2+(2*pr3) - ej1 + (2*ej3)
        ivin= -pr1-pr2+(2*pr3);  Maxben=PG1-ej3;      Maxper=ivin
        b_p=Maxben/-Maxper if (Maxben>0 and Maxper<0) else "N/A"      ; tend= "Indiferente";        vol="Baja"  
        if ivin==0:
            EQ1="Desde 0 hasta "+str(ej1); EQ2="N/A";EQ3="N/A"; EQ4=" Desde "+str(ej2)+ "hasta infinito"
        elif ivin>0:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"
        elif -PG2<0:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"
        elif Maxben>=0:
            EQ3=str(PG1); EQ2=str(-PG2); EQ1="N/A"; EQ4="N/A"
        else:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"

        comb="Formado por un Long CALL con P.ejercicio de: "+str(ej1) +"\n  Dos Short Call con Ejercicio de "+str(ej3)+"\n  una Long Call con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia indiferente y volatilidad baja"

        d8t="S < E1" ; d9t="-C1 -C2 +2CM"; d10t=str(ivin); d11t= EQ1
        d12t="E1<= S <= EM" ; d13t="-C1 -C2 +2CM\n -E1 +S" ; d14t="S "f"{PG2:.2f}"; d15t= EQ2
        d16t="EM<= S <= E2" ; d17t="-C1 -C2 +2CM \n o-E1 +2EM -S" ;d18t= "-S +"f"{PG1:.2f}" ; d19t= EQ3
        d20t="S>E2" ; d21t="-C1 -C2 +2CM" ; d22t=str(ivin); d23t=EQ4
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej1,ej3,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(1,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(1,pr2,i,ej2)
            act2.append(pyg)
        for i in SPOT:
            pyg=2*(option(2,pr3,i,ej3))
            act3.append(pyg)
        for i in act1:

            act5.append(act1[nind]+act2[nind]+act3[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Mariposa Call Vendida":
        d1.config( text=nlista);
        

        PG2= +pr1+pr2-(2*pr3) + ej1
        PG1=pr1+pr2-(2*pr3) + ej1 - (2*ej3)
        ivin= +pr1+pr2-(2*pr3);  Maxper=PG1+ej3;      Maxben=ivin
        b_p=Maxben/-Maxper if (Maxben>0 and Maxper<0) else "N/A"      ; tend= "Indiferente";        vol="Alta"  
        if ivin==0:
            EQ1="Desde 0 hasta "+str(ej1); EQ2="N/A";EQ3="N/A"; EQ4=" Desde "+str(ej2)+ "hasta infinito"
        elif ivin<0:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"
        elif PG2<0:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"
        elif Maxben>=0:
            EQ3=str(-PG1); EQ2=str(PG2); EQ1="N/A"; EQ4="N/A"
        else:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"

        comb="Formado por un Shor CALL con P.ejercicio de: "+str(ej1) +"\n  Dos Long Call con Ejercicio de "+str(ej3)+"\n  una Short Call con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia indiferente y volatilidad alta"

        d8t="S < E1" ; d9t="C1 +C2 -2CM"; d10t=str(ivin); d11t= EQ1
        d12t="E1<= S <= EM" ; d13t="+C1 +C2 -2CM\n +E1 -S" ; d14t="-S +"f"{PG2:.2f}"; d15t= EQ2
        d16t="EM<= S <= E2" ; d17t="C1 +C2 -2CM \nE1 -2EM +S" ;d18t= "S "f"{PG1:.2f}" ; d19t= EQ3
        d20t="S>E2" ; d21t="+C1 +C2 -2CM" ; d22t=str(ivin); d23t=EQ4
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej1,ej3,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(2,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(2,pr2,i,ej2)
            act2.append(pyg)
        for i in SPOT:
            pyg=2*(option(1,pr3,i,ej3))
            act3.append(pyg)
        for i in act1:

            act5.append(act1[nind]+act2[nind]+act3[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Mariposa Put Comprada":
        d1.config( text=nlista);
        

        PG2= -pr1-pr2+(2*pr3) + ej2 -(2*ej3) 
        PG1=-pr1-pr2+(2*pr3) + ej2 
        ivin= -pr1-pr2+(2*pr3);  Maxben=PG1-ej3;      Maxper=ivin
        b_p=Maxben/-Maxper if (Maxben>0 and Maxper<0) else "N/A"      ; tend= "Indiferente";        vol="Baja"  
        if ivin==0:
            EQ1="Desde 0 hasta "+str(ej1); EQ2="N/A";EQ3="N/A"; EQ4=" Desde "+str(ej2)+ "hasta infinito"
        elif ivin>0:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"
        elif -PG2<0:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"
        elif Maxben>=0:
            EQ3=str(PG1); EQ2=str(-PG2); EQ1="N/A"; EQ4="N/A"
        else:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"

        comb="Formado por un Long Put con P.ejercicio de: "+str(ej1) +"\n  Dos Short Put con Ejercicio de "+str(ej3)+"\n  una Long Put con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia indiferente y volatilidad baja"

        d8t="S < E1" ; d9t="-P1 -P2 +2PM"; d10t=str(ivin); d11t= EQ1
        d12t="E1<= S <= EM" ; d13t="-P1 -P2 +2PM\n E2 -2EM +S" ; d14t="S "f"{PG2:.2f}"; d15t= EQ2
        d16t="EM<= S <= E2" ; d17t="-P1 -P2 +2PM\nE2-S" ;d18t= "-S +"f"{PG1:.2f}" ; d19t= EQ3
        d20t="S>E2" ; d21t="-P1 -P2 +2PM" ; d22t=str(ivin); d23t=EQ4
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej1,ej3,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(3,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(3,pr2,i,ej2)
            act2.append(pyg)
        for i in SPOT:
            pyg=2*(option(4,pr3,i,ej3))
            act3.append(pyg)
        for i in act1:

            act5.append(act1[nind]+act2[nind]+act3[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Mariposa Put Vendida":
        d1.config( text=nlista);


        PG2= pr1+pr2-(2*pr3) - ej2 +(2*ej3)
        PG1=pr1+pr2-(2*pr3) - ej2 
        ivin= pr1+pr2-(2*pr3);  Maxper=PG1+ej3;      Maxben=ivin
        b_p=Maxben/-Maxper if (Maxben>0 and Maxper<0) else "N/A"      ; tend= "Indiferente";        vol="Alta"  
        if ivin==0:
            EQ1="Desde 0 hasta "+str(ej1); EQ2="N/A";EQ3="N/A"; EQ4=" Desde "+str(ej2)+ "hasta infinito"
        elif Maxper>0:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"
        elif PG2<0:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"
        elif Maxben>0:
            EQ3=str(-PG1); EQ2=str(PG2); EQ1="N/A"; EQ4="N/A"
        else:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"; EQ4="N/A"

        comb="Formado por un Short Put con P.ejercicio de: "+str(ej1) +"\n  Dos Long Put con Ejercicio de "+str(ej3)+"\n  una Short Put con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia indiferente y volatilidad Alta"

        d8t="S < E1" ; d9t="P1 +P2 -2PM"; d10t=str(ivin); d11t= EQ1
        d12t="E1<= S <= EM" ; d13t="+P1 +P2 -2PM\n -E2 +2EM -S" ; d14t="-S +"f"{PG2:.2f}"; d15t= EQ2
        d16t="EM<= S <= E2" ; d17t="+P1 +P2 -2PM\n-E2+S" ;d18t= "S "f"{PG1:.2f}" ; d19t= EQ3
        d20t="S>E2" ; d21t="P1 P2 -2PM" ; d22t=str(ivin); d23t=EQ4
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej1,ej3,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(4,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(4,pr2,i,ej2)
            act2.append(pyg)
        for i in SPOT:
            pyg=2*(option(3,pr3,i,ej3))
            act3.append(pyg)
        for i in act1:

            act5.append(act1[nind]+act2[nind]+act3[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Ratio Call Spread":
        d1.config( text=nlista);


        PG2= -pr1+(2*pr2)-ej1
        PG1=-pr1+(2*pr2)-ej1 + (2* ej2)
        ivin= -pr1+(2*pr2);  Maxper="Ilimitada";      Maxben=PG2+ej2
        b_p="N/A"      ; tend= "Bajista";        vol="Baja"  
        if ivin==0:
            EQ1="Desde 0 hasta "+str(ej1); EQ2="N/A"; EQ3=str(ej2+Maxben)
        elif Maxben<=0:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"
        elif ivin>0:
            EQ1="N/A"; EQ2="N/A"; EQ3=str(ej2+Maxben)
        elif ivin<0:
            EQ3=str(PG1); EQ2=str(-PG2); EQ1="N/A";
        

        comb="Formado por un Lon Call con P.ejercicio de: "+str(ej1) +"\n  Dos Short Call  con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia Bajista y volatilidad Baja"

        d8t="S < E1" ; d9t="-C1 + 2C2"; d10t=str(ivin); d11t= EQ1
        d12t="E1<= S <= E2" ; d13t="-C1 + 2C2 -E1 + S " ; d14t="S "f"{PG2:.2f}"; d15t= EQ2
        d16t=" S > E2" ; d17t="-C1 + 2C2 -E1 +2E2 -S" ;d18t= "-S +"f"{PG1:.2f}" ; d19t= EQ3
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej1,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(1,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=2*option(2,pr2,i,ej2)
            act2.append(pyg)
        
        for i in act1:

            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Ratio Call back Spread":
        d1.config( text=nlista);


        PG2= pr1-(2*pr2)+ej1
        PG1=pr1-(2*pr2)+ej1 - (2* ej2)
        ivin= pr1-(2*pr2);  Maxben="Ilimitada";      Maxper=PG2-ej2
        b_p="N/A"      ; tend= "Alcista";        vol="Alta"  
        if ivin==0:
            EQ1="Desde 0 hasta "+str(ej1); EQ2="N/A"; EQ3=str(ej2-Maxper)
        elif Maxper>=0:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"
        elif ivin<0:
            EQ1="N/A"; EQ2="N/A"; EQ3=str(ej2-Maxper)
        elif ivin>0:
            EQ3=str(-PG1); EQ2=str(PG2); EQ1="N/A";
        

        comb="Formado por un Lon Call con P.ejercicio de: "+str(ej1) +"\n  Dos Short Call  con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia Alcista y volatilidad Alta"

        d8t="S < E1" ; d9t="C1 - 2C2"; d10t=str(ivin); d11t= EQ1
        d12t="E1<= S <= E2" ; d13t="C1 -2C2 +E1 - S " ; d14t="-S + "f"{PG2:.2f}"; d15t= EQ2
        d16t=" S > E2" ; d17t="C1 -2C2 +E1 -2E2 +S" ;d18t= "S "f"{PG1:.2f}" ; d19t= EQ3
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej1,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=option(2,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=2*option(1,pr2,i,ej2)
            act2.append(pyg)
        
        for i in act1:

            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Ratio Put Back Spread":
        d1.config( text=nlista);


        PG2= (-2*pr1)+pr2-ej2 + (2*ej1)
        PG1=(-2*pr1)+pr2 - ej2
        ivin= (-2*pr1)+pr2;  Maxben=PG2;      Maxper=-ej1+PG2
        b_p="N/A"      ; tend= "Bajista";        vol="Alta"  
        if ivin==0:
            EQ1=str(PG2); EQ2="N/A"; EQ3="Desde "+str(ej1)+" hasta infinito"
        elif Maxper>=0:
            EQ1="N/A"; EQ2="N/A"; EQ3="N/A"
        elif ivin<0:
            EQ1=str(PG2); EQ2="N/A"; EQ3="N/A"
        elif ivin>0:
            EQ3=str(-PG1); EQ2=str(PG2); EQ1="N/A";
        

        comb="Formado por Dos Long Put con P.ejercicio de: "+str(ej1) +"\n un Short Put  con Ejercicio de "+str(ej2)
        estr="Estrategia de tendencia Bajista y volatilidad Alta"

        d8t="S < E1" ; d9t="-2P1 +P2 -E2 +2E1 -S"; d10t="-S + "f"{PG2:.2f}"; d11t= EQ1
        d12t="E1<= S <= E2" ; d13t="-2P1 +P2 -E2 + S" ; d14t="S "f"{PG2:.2f}"; d15t= EQ2
        d16t=" S > E2" ; d17t="-2P1 +P2" ;d18t= str(ivin); d19t= EQ3
        d20t="" ; d21t="" ; d22t=""; d23t=""
        d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)

        
        d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
        d29t="Beneficio/perdida: "+str(b_p)
        d26t=""

        actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

        ej4 = (ej2*2); SPOT=[0,ej1,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
        for i in SPOT:
            pyg=2*option(3,pr1,i,ej1)
            act1.append(pyg)
        for i in SPOT:
            pyg=option(4,pr2,i,ej2)
            act2.append(pyg)
        
        for i in act1:

            act5.append(act1[nind]+act2[nind])
            nind=nind+1
        for i in SPOT:
            ejex.append(0)
    elif nlista == "Ratio Put Spread":
	    d1.config( text=nlista);


	    PG2= (2*pr1)-pr2+ej2 - (2*ej1)
	    PG1=(2*pr1)-pr2 + ej2
	    ivin= (2*pr1)-pr2;  Maxper=PG2;      Maxben=ej1+PG2
	    b_p="N/A"      ; tend= "Alcista";        vol="Baja"  
	    if ivin==0:
	        EQ1=str(-PG2); EQ2="N/A"; EQ3="Desde "+str(ej1)+" hasta infinito"
	    elif Maxben<=0:
	        EQ1="N/A"; EQ2="N/A"; EQ3="N/A"
	    elif ivin>0:
	        EQ1=str(-PG2); EQ2="N/A"; EQ3="N/A"
	    elif ivin<0:
	        EQ3=str(PG1); EQ2=str(-PG2); EQ1="N/A";


	    comb="Formado por Dos Short Put con P.ejercicio de: "+str(ej1) +"\n un Long Put  con Ejercicio de "+str(ej2)
	    estr="Estrategia de tendencia Alcista y volatilidad Baja"

	    d8t="S < E1" ; d9t="2P1 -P2 +E2 -2E1 +S"; d10t="S "f"{PG2:.2f}"; d11t= EQ1
	    d12t="E1<= S <= E2" ; d13t="2P1 -P2 +E2 - S" ; d14t="-S +"f"{PG2:.2f}"; d15t= EQ2
	    d16t=" S > E2" ; d17t="2P1 -P2" ;d18t= str(ivin); d19t= EQ3
	    d20t="" ; d21t="" ; d22t=""; d23t=""
	    d24t="Maxima perdida: " +str(Maxper); d25t="Maxima ganancia: "+str(Maxben)


	    d28t="El flujo de caja inicial: "+f"{ivin:.2f}"
	    d29t="Beneficio/perdida: "+str(b_p)
	    d26t=""

	    actualizar2(comb,estr,d8t,d9t,d10t,d11t,d12t,d13t,d14t,d15t,d16t,d17t,d18t,d19t,d20t,d21t,d22t,d23t,d24t,d25t,d28t,d29t,d26t)

	    ej4 = (ej2*2); SPOT=[0,ej1,ej2,ej4]; act1=[]; act2=[]; act3=[]; act4=[]; act5=[]; nind=0; ejex=[]
	    for i in SPOT:
	        pyg=2*option(4,pr1,i,ej1)
	        act1.append(pyg)
	    for i in SPOT:
	        pyg=option(3,pr2,i,ej2)
	        act2.append(pyg)

	    for i in act1:

	        act5.append(act1[nind]+act2[nind])
	        nind=nind+1
	    for i in SPOT:
	        ejex.append(0)

            
       
                

    




Button(raiz, text="Ver resultado",font=("Loma",15),command=res,bg= "thistle1",fg="black").grid(column=1, row=22,columnspan=5,stick=W+E)
color1="khaki1"
color2="khaki2"
 
Label(raiz, text="°                                                      Resultado                                                      °",justify="center", fg="red4",bg="Chocolate1",font=("Loma",15)).grid(row=3,column=8,columnspan=6,stick=W+E)
Label(raiz,text="",bg=color1).grid(row=4,column=8,columnspan=6,rowspan=19,stick=W+E+S+N)
d1=Label(raiz, text="",justify="center", fg="red4",bg="gold2",font=("Loma",15));d1.grid(row=4,column=8,columnspan=6,stick=W+E)
d2=Label(raiz, text="",bg=color1, fg="gray3",font=("Loma",15));d2.grid(row=5,column=9,columnspan=4,stick=W+E)
d3=Label(raiz, text="" ,bg=color1, fg="gray3",font=("Loma",15));d3.grid(row=6,column=9,columnspan=4,stick=W+E)


Label(raiz, text="SPOT",font=("Loma",15),bg=color2).grid(row=8,column=9,stick=W+E)
Label(raiz, text="Funcion p/g",font=("Loma",15),bg=color2).grid(row=8,column=10,stick=W+E)
Label(raiz, text="P/G",font=("Loma",15),bg=color2).grid(row=8,column=11,stick=W+E)
Label(raiz, text="PUNTO EQULIBRIO",font=("Loma",15),bg=color2).grid(row=8,column=12,stick=W+E)

d8=Label(raiz, text="",font=("Loma",12),bg=color1);d8.grid(row=9,column=9,stick=W)
d9=Label(raiz, text="",font=("Loma",12),bg=color1);d9.grid(row=9,column=10)
d10=Label(raiz, text="",font=("Loma",12),bg=color1);d10.grid(row=9,column=11)
d11=Label(raiz, text="",font=("Loma",12),bg=color1);d11.grid(row=9,column=12)

d12=Label(raiz, text="",font=("Loma",12),bg=color1);d12.grid(row=10,column=9,stick=W)
d13=Label(raiz, text="",font=("Loma",12),bg=color1);d13.grid(row=10,column=10)
d14=Label(raiz, text="",font=("Loma",12),bg=color1);d14.grid(row=10,column=11)
d15=Label(raiz, text="",font=("Loma",12),bg=color1);d15.grid(row=10,column=12)

d16=Label(raiz, text="",font=("Loma",12),bg=color1);d16.grid(row=11,column=9,stick=W)
d17=Label(raiz, text="",font=("Loma",12),bg=color1);d17.grid(row=11,column=10)
d18=Label(raiz, text="",font=("Loma",12),bg=color1);d18.grid(row=11,column=11)
d19=Label(raiz, text="",font=("Loma",12),bg=color1);d19.grid(row=11,column=12)

d20=Label(raiz, text="",font=("Loma",12),bg=color1);d20.grid(row=12,column=9,stick=W)
d21=Label(raiz, text="",font=("Loma",12),bg=color1);d21.grid(row=12,column=10)
d22=Label(raiz, text="",font=("Loma",12),bg=color1);d22.grid(row=12,column=11)
d23=Label(raiz, text="",font=("Loma",12),bg=color1);d23.grid(row=12,column=12)



d24=Label(raiz, text="", bg=color1,fg="gray3",font=("Loma",15));d24.grid(row=14,column=9,columnspan=4,stick=W)
d25=Label(raiz, text="",bg=color1 ,fg="gray3",font=("Loma",15));d25.grid(row=15,column=9,columnspan=4,stick=W)
d28=Label(raiz, text="",bg=color1 ,fg="gray3",font=("Loma",15));d28.grid(row=16,column=9,columnspan=4,stick=W)
d29=Label(raiz, text="",bg=color1 ,fg="gray3",font=("Loma",15));d29.grid(row=17,column=9,columnspan=4,stick=W)


d26= Label(raiz, text="",bg=color1 ,fg="gray3",font=("Loma",15));d26.grid(row=18,column=9,columnspan=4,stick=W)


d27= Button(raiz, text="Ver grafica",font=("Loma",15),bg= "thistle1",fg="black",command=grafica);d27.grid(column=8, row=22,columnspan=6,stick=W+E)
def iniciarArchivo():
    archivo = open("datos.txt","a")
    nlista+"$"+str(tend)+"$"+str(vol)+"$"+str(ivin)+"$"+str(Maxben)+"$"+str(Maxper)+"$"+str(b_p)
    archivo.write(nlista+"$"+str(tend)+"$"+str(vol)+"$"+str(ivin)+"$"+str(Maxben)+"$"+str(Maxper)+"$"+str(b_p)+"\n")
    archivo.close()
def cargar():
    archivo = open("datos.txt","r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea = linea[:-1]
            listag.append(linea)
            linea = archivo.readline()
    archivo.close()



listag=[]
n=0
df = pd.DataFrame(columns=("pr1","pr2","pr3","ej1","ej2","ej3"))

def guardar():
	global n
	n=n+1
	listag.append(nlista+"$"+str(tend)+"$"+str(vol)+"$"+str(ivin)+"$"+str(Maxben)+"$"+str(Maxper)+"$"+str(b_p))
	df.loc[n] = [pr1,pr2,pr3,ej1,ej2,ej3]
	


	messagebox.showinfo("Guardado","Los ha sido guardado")
	consultar()
cb=ttk.Combobox(raiz, state="readonly")
cb["values"]=["1","2"]

cb.grid(column=6,row=23)
r1 = Text(raiz,width=27,height=10);r2=Text(raiz,width=15,height=10);r3=Text(raiz,width=15,height=10);r4= Text(raiz,width=15,height=10);r5=Text(raiz,width=15,height=10);r6=Text(raiz,width=10,height=10);r7=Text(raiz,width=20,height=10);r8=Text(raiz,width=5,height=10)
r1.insert(INSERT,"Estrategia\n"); r2.insert(INSERT,"Tendencia\n") ; r3.insert(INSERT,"Volatilidad\n"); r4.insert(INSERT,"FC Inicial\n")
r5.insert(INSERT,"Max.Ganancia\n"); r6.insert(INSERT,"Max.Perdida\n"); r7.insert(INSERT,"Beneficio/Perdida\n"); r8.insert(INSERT,"Numero\n")
r1.grid(column=7,row=24,stick=W+E) ; r2.grid(column=8,row=24,stick=W+E)  ;r3.grid(column=9,row=24,stick=W+E);r8.grid(column=6,row=24,stick=W+E)
r4.grid(column=10,row=24,stick=W+E); r5.grid(column=11,row=24,stick=W+E); r6.grid(column=12,row=24,stick=W+E) ;r7.grid(column=13,row=24,stick=W+E)
rr = Text(raiz,width=10,height=11,bg= "khaki1")
rr.insert(INSERT,"                     ......               \n                  .:||||||||:.            \n                 /            \           \n                (   o      o   )          \n      --@@@@----------:  :----------@@@@--\n          DEINER FABIAN IGLESIAS BLANCO\n          DORIS ADRIANA CHAVARRO CRUZ\n         JERSON DAVID PEREZ CONTRERAS\n                DESARROLLADORES\n      ------------------------------------")
rr.grid(column=1,columnspan=5,row=24,stick=W+E)
def consultar():
    r1 = Text(raiz,width=27,height=10);r2=Text(raiz,width=15,height=10);r3=Text(raiz,width=15,height=10);r4= Text(raiz,width=15,height=10);r5=Text(raiz,width=15,height=10);r6=Text(raiz,width=10,height=10);r7=Text(raiz,width=20,height=10);r8=Text(raiz,width=5,height=10)
    r1.insert(INSERT,"Estrategia\n"); r2.insert(INSERT,"Tendencia\n") ; r3.insert(INSERT,"Volatilidad\n"); r4.insert(INSERT,"FC Inicial\n")
    r5.insert(INSERT,"Max.Ganancia\n"); r6.insert(INSERT,"Max.Perdida\n"); r7.insert(INSERT,"Beneficio/Perdida\n"); r8.insert(INSERT,"Numero\n")
    valores = []
    nn=0
    print(ivin)
   
    for elemento in listag:
    	
	    arreglo = elemento.split("$")
	    nn=nn+1
	    valores.append(nn)

	    r1.insert(INSERT,arreglo[0]+"\n"); r2.insert(INSERT,arreglo[1]+"\n") ; r3.insert(INSERT,arreglo[2]+"\n"); r4.insert(INSERT,arreglo[3]+"\n")
	    r5.insert(INSERT,arreglo[4]+"\n"); r6.insert(INSERT,arreglo[5]+"\n"); r7.insert(INSERT,arreglo[6]+"\n"); r8.insert(INSERT,"N°"+str(nn)+"\n")
    cb["values"]=valores      
    r1.grid(column=7,row=24,stick=W+E) ; r2.grid(column=8,row=24,stick=W+E)  ;r3.grid(column=9,row=24,stick=W+E);r8.grid(column=6,row=24,stick=W+E)
    r4.grid(column=10,row=24,stick=W+E); r5.grid(column=11,row=24,stick=W+E); r6.grid(column=12,row=24,stick=W+E) ;r7.grid(column=13,row=24,stick=W+E)
def volver():
	if str(cb.get())=="":
		messagebox.showinfo(message="Seleccione una estratefia guardada", title="DATOS INSUFICIENTES")
	else:
		nnn=int(cb.get())-1
		pp=nnn+1
		global nlista; global pr1; global pr2; global pr3; global ej1; global ej2; global ej3; global b_P
		arreglo = listag[nnn].split("$")
		nlista=arreglo[0]
		pr1=df.loc[pp].iloc[0]
		pr2=df.loc[pp].iloc[1]
		pr3=df.loc[pp].iloc[2]
		ej1=df.loc[pp].iloc[3]
		ej2=df.loc[pp].iloc[4]
		ej3=df.loc[pp].iloc[5]
		resultado()





Button(raiz, text="Guardar estrategia",font=("Loma",15),bg= "thistle1",fg="black",command=guardar).grid(column=8, row=23,columnspan=6,stick=W+E)
Button(raiz, text="Volver a ver",font=("Loma",15),bg= "thistle1",fg="black",command=volver).grid(column=7, row=23,stick=W+E)
Button(raiz, text="Simulador Mejor Estrategia",font=("Loma",15),bg= "thistle1",fg="black",command=ventana2).grid(column=1, columnspan=5,row=23,stick=W+E)
Label(raiz, text="Selecionar el Numero de \nla estrategia guardada",bg=color1 ,fg="gray3",font=("Loma",15)).grid(row=22,column=6,columnspan=2,stick=W)




raiz.mainloop()
