# -*- coding: cp1252 -*-
#Si se pone este códig dentro de una función,
#solo es necesario ingresar el argumento necesario para que el
#menú se cambie directamente en la GUI, la red neuronal debe
#enviar la información directamete como un argumento.

from Tkinter import *
ventana=Tk()
ventana.title("Prueba GUI")
ventana.geometry=("300x300")


def GUI(Accion, ventana):
   ventana=ventana
   LED=Button(ventana,bg='green',width=5)
   LED.grid(row=1,column=1)
   Regresar=Button(ventana,bg='red',width=5)
   Regresar.grid(row=1,column=2)
   OPC1=Button(ventana,bg='yellow',width=5)
   OPC1.grid(row=2,column=1)
   OPC2=Button(ventana,bg='Blue',width=5)
   OPC2.grid(row=2,column=2)
   OPC3=Button(ventana,bg='purple',width=5)
   OPC3.grid(row=3,column=1)
   OPC4=Button(ventana,bg='orange',width=5)
   OPC4.grid(row=3,column=2)
   ventana.update()
   actualidad=0
   return actualidad
   
