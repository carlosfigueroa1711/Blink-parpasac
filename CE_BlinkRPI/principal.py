from Tkinter import *
import GUI

ventana=Tk()
ventana.title("Prueba GUI")
ventana.geometry=("300x300")
accion=1
actual=GUI.GUI(accion, ventana)
