### -*- coding: cp1252 -*-
##
import serial
ser=serial.Serial()
ser.BAUDRATES=9600
ser.port='COM4'

try:
    ser.open()
    print("puerto abierto")
    ser.flush()

except:
    ser.close()
##
from Tkinter import *
from pygame import mixer
import bluetooth
import struct
import collections
import numpy as np
import Red_eventos
import Red_Clases
import peak
import scipy
import scipy.signal
import pandas as pd
from scipy.signal import butter,lfilter
import traceback
from MindwaveDataPoints import RawDataPoint
import matplotlib.pyplot as plt
import time

from MindwaveDataPointReader import MindwaveDataPointReader
import textwrap

ventana = Tk()
ventana.geometry=("683x768+0+0")
#ventana.geometry("WxH±X±Y")
##w: Ancho de la ventana en pixeles
##h: Alto de la ventana en pixeles
##x: Posicion en el eje X
##y: Posicion en el eje Y

ventana.title("CE-BLINK")
#ventana.iconbitmap("form.ico") #Cambiar el icono
mixer.init()
mixer.music.load('Bienvenida.mp3')
mixer.music.play()

#B1=Button(ventana,text="Conectando",bg='gray',height=300, width=300)
#B1.grid(row=1,column=1)
#ventana.update_idletasks()
#################
# Boton de inicio de sistema
mindwaveDataPointReader = MindwaveDataPointReader()

def inicio():
        intentos=0
        global mindwaveDataPointReader
        mindwaveDataPointReader.start()
        while (not(mindwaveDataPointReader.isConnected())):
                mixer.music.load('Conectando.mp3')
                mixer.music.play()
                intentos=intentos+1
                mindwaveDataPointReader.start()
                if (intentos>3):
                        mixer.music.load('Reinicia.mp3')
                        mixer.music.play()
                        return 0
                        break
        if (mindwaveDataPointReader.isConnected()):
                return 1


##################

def iniciar():
        mixer.music.load('piano.mp3')
        mixer.music.play()
        Led=Button(ventana,bg='white',font="Helvetica 16 bold",height = 10,width=26)
        Led.grid(row=1, column=1)
        Regresar=Button(ventana,bg='gray',font="Helvetica 16 bold",height = 10,width=26)
        Regresar.grid(row=1, column=2)
        OPC1=Button(ventana,text="Responder",font="Helvetica 16 bold",bg='yellow',height = 10,width=26)   
        OPC1.grid(row=2, column=1)
        OPC2=Button(ventana,text="Preguntar",font="Helvetica 16 bold",bg='purple',height = 10,width=26)
        OPC2.grid(row=2, column=2)
        OPC3=Button(ventana,text="Controlar",font="Helvetica 16 bold",bg='red',height = 10,width=26)
        OPC3.grid(row=3, column=1)
        OPC4=Button(ventana,text="Jugar",font="Helvetica 16 bold",bg='blue',height = 10,width=26)
        OPC4.grid(row=3, column=2)
        #plt.figure(1)
        d=0
        fm=1022
        paso=511
        vector=[]
        evento=list()
        menu1=1  #Principal
        menu2=0  #responder
        menu3=0  #Pedir preguntar
        menu4=0
        menu5=0
        menu6=0
        menu7=0
        menu8=0
        menu9=0
        menu10=0
        menu11=0
        menu12=0
        menu13=0
        c_m1=0
        c_m2=0
        c_m3=0
        c_m4=0
        c_m5=0
        c_m6=0
        c_m7=0
        c_m8=0
        c_m9=0
        c_m10=0
        c_m11=0
        c_m12=0
        c_m13=0
        luz=0
        vent=0
        acceso=0
        timbre=0
        bandera_musica=0
        bandera_ROCK=0
        bandera_BALADA=0
        bandera_PODCAST=0
        bandera_SOLOMUSICA=0
        Vjuego=0
        Con_level=1
        Ok=0
        av=1
        global mindwaveDataPointReader
        while(mindwaveDataPointReader.isConnected()):
##                try:
                if (av==1):
                        
                        #####
                        #Aqui va la comunicación serial
                        #####
                        if (menu1==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                Regresar.config(text="Inicio")
                                Vjuego=0
                                OPC1.config(text="Responder")
                                OPC2.config(text="Charlas \n"+"neccesidades\n"+ "entreteniminto\n")
                                OPC3.config(text="Jugar")
                                OPC4.config(text="Controlar")
                                ventana.update()
                                
                        if (menu2==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                #Menu de responder
                                Regresar.config(text="Menu principal")
                                OPC1.config(text="Si / No / Gracias / Muy bien")
                                OPC2.config(text="No entendi")
                                OPC3.config(text="Tengo un dolor")
                                OPC4.config(text="No tengo la respuesta")
                                c_m1=0
                                c_m2=1
                                c_m3=0
                                c_m4=0
                                c_m5=0
                                c_m6=0
                                c_m7=0
                                c_m8=0
                                c_m9=0
                                c_m10=0
                                c_m11=0
                                c_m12=0
                                c_m13=0
                                ventana.update()
                                
                        if (menu3==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                #Menu preguntar o pedir
                                Regresar.config(text="Menu principal")
                                OPC1.config(text="Necesidades")
                                OPC2.config(text="Televisión")
                                OPC3.config(text="Conversar")
                                OPC4.config(text="Musica")
                                c_m1=0
                                c_m2=0
                                c_m3=1
                                c_m4=0
                                c_m5=0
                                c_m6=0
                                c_m7=0
                                c_m8=0
                                c_m9=0
                                c_m10=0
                                c_m11=0
                                c_m12=0
                                c_m13=0
                                ventana.update()
                                
                        if (menu4==1):
                                #Menu jugar
                                if (Vjuego==0):
                                        tiempo=4
                                        ventana.title("CE-BLINK JUEGO INSTRUCCIONES")
                                        Led.config(text="Observa los numeros\n"+
                                                       "Y selecciona la opcion correcta\n"+
                                                       "dentro del menu principal",font="Helvetica 16 bold")

                                        ventana.update()
                                        time.sleep(4)
                                        Vjuego=1
                                        
                                        X_Juego=[]
                                        for i in range (0,4):
                                                import random
                                                dat=random.randint(0,20)
                                                while dat in X_Juego:
                                                        dat=random.randint(0,20)
                                                X_Juego.append(dat)
                                                
                                        
                                        print(X_Juego)
                                        X_d=str(X_Juego)
                                        Led.config(text=str(X_Juego))
                                        
                                        Con_level=1
                                        ventana.title("CE-BLINK JUEGO Nivel "+ str(Con_level))
                                        ventana.update()
                                        tiempo=4.0
                                        time.sleep(tiempo)
                                        
                                        t_vec=len(X_Juego)         #Tamaño del vector Se propone que incremente de tamaño el vector en algun nivel
                                        pos_correcto=random.randint(0,3)   #Se elige un numero del vector
                                        correcto=X_Juego[pos_correcto]     #Se elige la posicion del numero ganador
                                        print(correcto)
                                        print(pos_correcto)
##                                        print("Datos" + "Posicion")
                                        ventana.title("CE-BLINK JUEGO Pregunta ")

                                        modo=random.randint(1,2)
                                        
                                        Led.config(text="Cual es el numero de la posicion\n" + str(pos_correcto+1))
                                        ventana.update()
                                        organizar=random.randint(0,3)
                                        if (organizar==1):
                                                X_Juego.sort()
                                        elif (organizar==0):
                                                X_Juego.sort(reverse=True)
                                        elif (organizar==2):
                                                X_Juego.reverse()
                                        else:
                                                X_Juego=X_Juego
                                        Ok=0
                                        
                                elif ((Vjuego>0) and (Ok==1)):
                                        X_Juego=[]
                                        Ok=0
                                        for i in range (0,4):
                                                import random
                                                dat=random.randint(0,20)
                                                while dat in X_Juego:
                                                        dat=random.randint(0,20)
                                                X_Juego.append(dat)
                                        print(X_Juego)
                                        X_d=str(X_Juego)
                                        Led.config(text=str(X_Juego))
                                        
                                        Con_level=Con_level+1
                                        ventana.title("CE-BLINK JUEGO Nivel "+ str(Con_level))
                                        ventana.update()
                                        if (tiempo>0.3):
                                            tiempo=tiempo-0.25
                                        else:
                                            tiempo=0.2
                                        time.sleep(tiempo)
                                        
                                        t_vec=len(X_Juego)         #Tamaño del vector Se propone que incremente de tamaño el vector en algun nivel
                                        pos_correcto=random.randint(0,3)   #Se elige un numero del vector
                                        correcto=X_Juego[pos_correcto]     #Se elige la posicion del numero ganador
                                        print (correcto)
                                        print (pos_correcto)
##                                        print("Datos" + "Posicion")
                                        ventana.title("CE-BLINK JUEGO Pregunta ")

                                        modo=random.randint(1,2)
                                                
                                        Led.config(text="Cual es el numero de la posicion\n" + str(pos_correcto+1))
                                        ventana.update()
                                        organizar=random.randint(0,3)
                                        if (organizar==1):
                                                X_Juego.sort()
                                        elif (organizar==0):
                                                X_Juego.sort(reverse=True)
                                        elif (organizar==2):
                                                X_Juego.reverse()
                                        else:
                                                X_Juego=X_Juego
        
                                #print(X_Juego)
                                Regresar.config(text="Menu principal")
                                OPC1.config(text=str(X_Juego[0]))
                                OPC2.config(text=str(X_Juego[1]))
                                OPC3.config(text=str(X_Juego[2]))
                                OPC4.config(text=str(X_Juego[3]))
                                c_m1=0
                                c_m2=0
                                c_m3=0
                                c_m4=1
                                c_m5=0
                                c_m6=0
                                c_m7=0
                                c_m8=0
                                c_m9=0
                                c_m10=0
                                c_m11=0
                                c_m12=0
                                c_m13=0
                                ventana.update()
                                
                        if (menu5==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                #Menu controlar
                                Regresar.config(text="Menu principal")
                                OPC1.config(text="Luz")
                                OPC2.config(text="Ventilador")
                                OPC3.config(text="Entrada")
                                OPC4.config(text="Alarma")
                                c_m1=0
                                c_m2=0
                                c_m3=0
                                c_m4=0
                                c_m5=1
                                c_m6=0
                                c_m7=0
                                c_m8=0
                                c_m9=0
                                c_m10=0
                                c_m11=0
                                c_m12=0
                                c_m13=0
                                ventana.update()
                        if (menu6==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                Regresar.config(text="Menu Responder")
                                #sub menu responder (si,no,gracias,muy bien)
                                Regresar.config(text="Menu responder")
                                OPC1.config(text="Si")
                                OPC2.config(text="Gracias")
                                OPC3.config(text="No")
                                OPC4.config(text="Muy bien")
                                c_m1=0
                                c_m2=0
                                c_m3=0
                                c_m4=0
                                c_m5=0
                                c_m6=1
                                c_m7=0
                                c_m8=0
                                c_m9=0
                                c_m10=0
                                c_m11=0
                                c_m12=0
                                c_m13=0
                                ventana.update()
                                
                        if (menu7==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                #sub menu responder (dolor)
                                Regresar.config(text="Menu Responder")
                                OPC1.config(text="Cabeza")
                                OPC2.config(text="Estomago")
                                OPC3.config(text="Espalda")
                                OPC4.config(text="Otro")
                                c_m1=0
                                c_m2=0
                                c_m3=0
                                c_m4=0
                                c_m5=0
                                c_m6=0
                                c_m7=1
                                c_m8=0
                                c_m9=0
                                c_m10=0
                                c_m11=0
                                c_m12=0
                                c_m13=0
                                ventana.update()
                        if (menu8==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                #sub menu pedir (Necesidades)
                                Regresar.config(text="Menu Preguntar/pedir")
                                OPC1.config(text="Agua")
                                OPC2.config(text="Comida")
                                OPC3.config(text="Baño")
                                OPC4.config(text="Posicion")
                                c_m1=0
                                c_m2=0
                                c_m3=0
                                c_m4=0
                                c_m5=0
                                c_m6=0
                                c_m7=0
                                c_m8=1
                                c_m9=0
                                c_m10=0
                                c_m11=0
                                c_m12=0
                                c_m13=0
                                ventana.update()
                        if (menu9==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                #sub menu pedir (Television)
                                Regresar.config(text="Menu Charlas y mas")
                                OPC1.config(text="Cambiar canal")
                                OPC2.config(text="Volumen +")
                                OPC3.config(text="Volumen -")
                                OPC4.config(text="encender/apagar")
                                c_m1=0
                                c_m2=0
                                c_m3=0
                                c_m4=0
                                c_m5=0
                                c_m6=0
                                c_m7=0
                                c_m8=0
                                c_m9=1
                                c_m10=0
                                c_m11=0
                                c_m12=0
                                c_m13=0
                                ventana.update()
                                
                        if (menu10==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                #sub menu Cambiar canal ()
                                Regresar.config(text="Menu Television")
                                OPC1.config(text="Canal +")
                                OPC2.config(text="Canal -")
                                OPC3.config(text="")
                                OPC4.config(text="")
                                c_m1=0
                                c_m2=0
                                c_m3=0
                                c_m4=0
                                c_m5=0
                                c_m6=0
                                c_m7=0
                                c_m8=0
                                c_m9=0
                                c_m10=1
                                c_m11=0
                                c_m12=0
                                c_m13=0
                                ventana.update()
                        if (menu11==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                Regresar.config(text="Menu Television")
                                #sub menu television (Encender/ apagar)
                                OPC1.config(text="Encender")
                                OPC2.config(text="Apagar")
                                OPC3.config(text=" ")
                                OPC4.config(text=" ")
                                c_m1=0
                                c_m2=0
                                c_m3=0
                                c_m4=0
                                c_m5=0
                                c_m6=0
                                c_m7=0
                                c_m8=0
                                c_m9=0
                                c_m10=0
                                c_m11=1
                                c_m12=0
                                c_m13=0
                                ventana.update()
                        if (menu12==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                Regresar.config(text="Menu Preguntar/pedir")
                                #sub menu pedir (conversar)
                                OPC1.config(text="Presentarme")
                                OPC2.config(text="¿Como estas?")
                                OPC3.config(text="Cuentame algo")
                                OPC4.config(text="Todo estara bien")
                                c_m1=0
                                c_m2=0
                                c_m3=0
                                c_m4=0
                                c_m5=0
                                c_m6=0
                                c_m7=0
                                c_m8=0
                                c_m9=0
                                c_m10=0
                                c_m11=0
                                c_m12=1
                                c_m13=0
                                ventana.update()
                        if (menu13==1):
                                Led.config(text="")
                                ventana.title("CE-BLINK")
                                Regresar.config(text="Menu Preguntar/pedir")
                                #sub menu pedir (musica)
                                OPC1.config(text="Rock")
                                OPC2.config(text="Balada")
                                OPC3.config(text="Solo musica")
                                OPC4.config(text="Podacast")
                                c_m1=0
                                c_m2=0
                                c_m3=0
                                c_m4=0
                                c_m5=0
                                c_m6=0
                                c_m7=0
                                c_m8=0
                                c_m9=0
                                c_m10=0
                                c_m11=0
                                c_m12=0
                                c_m13=1
                                ventana.update()
                        c=0
                        #print("Si vamos bien")
                        plt.clf()
                        if (d==0):
                                
                                while (c<1022):
                                        #print(c)
                                        dataPoint = mindwaveDataPointReader.readNextDataPoint()
                                        if (dataPoint.__class__ is RawDataPoint):
                                                Num=str(dataPoint)
                                                vector.append(int(Num))
                                                c=c+1
                        else:
                                vector[0:(paso)]=vector[paso:fm]
                                c=0
                                while (c<510):
                                        dataPoint = mindwaveDataPointReader.readNextDataPoint()
                                        if (dataPoint.__class__ is RawDataPoint):
                                                Num=str(dataPoint)
                                                vector[paso+c]=int(Num)
                                                c=c+1
                        X=vector
                        plt.plot(X)
                        plt.pause(0.001)
                        Fk=[]
                        Fk.append(np.var(X))
                        Fk.append(np.mean(X))
                        #print (Fk)
                        ev=Red_eventos.red_eventos(Fk) ##Se debe verificar este algoritmo 
                        #print(ev)

                        if (ev[0]>ev[1]):
                                Led.config(bg='red')
                                ventana.update()
                                if (c==0):
                                        evento=X[0:fm]
                                        c=c+1
                                else:
                                        lon=len(evento)
                                        evento[lon:lon+paso]=X[paso+1:fm]
                                        c=c+1
                        else:
                                Led.config(bg='white')
                                ventana.update()
                                if c>1 and len(evento)>paso:
                                        c=0
                                        ###############################
                                        ###### Normalización de datos por puntuación estandar
                                        ###### Tomado del algoritmo Bag of Features
                                        X_1=evento
                                        mx=np.mean(X_1)
                                        stdx=np.std(X_1)
                                        X=[]
                                        for i in range (len(X_1)):
                                                X.append((X_1[i]-mx)/stdx)
                                        X=np.asarray(X)
                                        #print("ok")
                                        #############################
                                        ##### Fin de algoritmo de normalización
                                        #############################
                                        ##### Aplicación de un flitro Butterworth
                                        ##### Tomado de la experimentación de trabajo previo, modificaciones para detección de frecuencias bajas
                                        ##### Los parametros se pueden modificar
                                        fs=1023
                                        lowcut = 1
                                        highcut = 5
                                        nyq = 0.5 * fs
                                        low = lowcut / nyq
                                        high = highcut / nyq
                                        order= 1
                                        b, a = butter(order, [low, high], btype='band')
                                        X_fil = lfilter(b, a, X)
                                        ############################
                                        ##### Fin de aplicacion de filtro
                                        ###### Normalización de datos por puntuación estandar
                                        ###### Tomado del algoritmo Bag of Features
                                        X_p=X_fil/max(X_fil)
                                        X=[]
                                        for i in range (len(X_p)):
                                                if (X_p[i]>0.5):
                                                        X.append(X_p[i])
                                                else:
                                                        X.append(0)
                                        X=np.asarray(X)
                                        P_F=peak.indexes(X, thres=0.4, min_dist=100,thres_abs=False)  #detección de picos en la señal de evento

                                        try:
                                                dist1=P_F[2]-P_F[1]
                                        except:
                                                dist1=0
                                        try:
                                                dist2=P_F[3]-P_F[2]
                                        except:
                                                dist2=0
                                        try:
                                                dist3=P_F[4]-P_F[3]
                                        except:
                                                dist3=0
                                        try:
                                                dist4=P_F[5]-P_F[4]
                                        except:
                                                dist4=0
                                        energia = sum(X_p*X_p)
                                        picos=len(P_F)
                                        desviacion=np.std(X_p)
                                        varianza=np.var(X_p)

                                        Fk2=[dist1,dist2,dist3,dist4,energia,picos,desviacion,varianza]
                                        Clas=[]
                                        Clas= Red_Clases.red_Clases(Fk2)
                                        if ((Clas[0]>Clas[1]) and (Clas[0]>Clas[2]) and (Clas[0]>Clas[3]) and (Clas[0]>Clas[4]) and (Clas[0]>Clas[5])
                                            and (Clas[0]>Clas[6])):
                                                p=0
                                                print("Clase ruido")
      #########################################
                                        if ((Clas[1]>Clas[0]) and (Clas[1]>Clas[2]) and (Clas[1]>Clas[3]) and (Clas[1]>Clas[4]) and (Clas[1]>Clas[5])
                                            and (Clas[1]>Clas[6])):
                                                print("Clase 1")
                                                if (menu1==1):
                                                        menu1=0
                                                        menu2=1
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                if (c_m2==1):
                                                        menu1=0
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=1 #Si/no/gracias/muy bien
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                if (c_m6==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        
                                                        mixer.music.stop()
                                                        mixer.music.load('Si.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m3==1):
                                                        menu1=0
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=1 #Necesidades
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                if (c_m8==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.load('sed.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m4==1):
                                                        Ok=1
                                                        my_text = OPC1['text']
                                                        print(my_text)
                                                        print(correcto)
                                                        if (int(my_text)==(correcto)):
                                                                Vjuego=Vjuego+1
                                                                menu4=1
                                                                c_m4=1
                                                                Led.config(text="EXCELENTE")
                                                                ventana.update()
                                                                time.sleep(2)
                                                                
                                                        else:
                                                                Vjuego=0
                                                                Led.config(text="Vuelve a intentarlo\n GAME OVER")
                                                                ventana.update()
                                                                time.sleep(2)
                                                                menu1=1   #Principal
                                                                menu2=0
                                                                menu3=0
                                                                menu4=0
                                                                menu5=0
                                                                menu6=0
                                                                menu7=0
                                                                menu8=0
                                                                menu9=0
                                                                menu10=0
                                                                menu11=0
                                                                menu12=0
                                                                menu13=0
                                                                c_m1=0
                                                                c_m2=0
                                                                c_m3=0
                                                                c_m4=0
                                                                c_m5=0
                                                                c_m6=0
                                                                c_m7=0
                                                                c_m8=0
                                                                c_m9=0
                                                                c_m10=0
                                                                c_m11=0
                                                                c_m12=0
                                                                c_m13=0
                                                if (c_m5==1):
                                                        if (ser.isOpen()):
                                                                if (luz==0):
                                                                        luz=1
                                                                else:
                                                                        luz=0
                                                                a='@'+str(luz)
                                                                ser.write(a+'\r\n')
                                                                print(a)
                                                        
                                                                        
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m9==1):
                                                        menu1=0
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=1 #Canal de television 
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                if (c_m10==1):
                                                        print("Canal +")
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m7==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('Dolorcabeza.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m11==1):
                                                        print("Encender television")
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m12==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.load('Presentacion.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m13==1):
                                                        mixer.init()
                                                        mixer.music.load('Rock.mp3')
                                                        if (bandera_musica==0):
                                                                time.sleep(0.2)
                                                                mixer.music.play()
                                                                mixer.music.play()
                                                                print("Reproduciendo ROCK")
                                                                bandera_musica=1
                                                                bandera_ROCK=1
                                                                bandera_BALADA=0
                                                                bandera_PODCAST=0
                                                                bandera_SOLOMUSICA=0
                                                        
                                                        else:
                                                                if (bandera_ROCK==1):
                                                                        mixer.music.stop()
                                                                        print("Deteniendo ROCK")
                                                                        bandera_musica=0
                                                                        bandera_ROCK=0
                                                                else:
                                                                        time.sleep(0.2)
                                                                        mixer.music.play()
                                                                        mixer.music.play()
                                                                        print("Reproduciendo ROCK")
                                                                        bandera_musica=1
                                                                        bandera_ROCK=1
                                                                        bandera_BALADA=0
                                                                        bandera_PODCAST=0
                                                                        bandera_SOLOMUSICA=0  
                                                        
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                 ##############################################################                                       
                                        if ((Clas[2]>Clas[0]) and (Clas[2]>Clas[1]) and (Clas[2]>Clas[3]) and (Clas[2]>Clas[4]) and (Clas[2]>Clas[5])
                                            and (Clas[2]>Clas[6])):
                                                print("Clase 2")
                                                if (menu1==1):
                                                        menu1=0
                                                        menu2=0
                                                        menu3=1
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                if (c_m2==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('noentiendo.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m3==1):
                                                        menu1=0
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0 #Necesidades
                                                        menu9=1 #Television
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                if (c_m4==1):
                                                        Ok=1
                                                        my_text = OPC2['text']
                                                        print(my_text)
                                                        print(correcto)
                                                        if (int(my_text)==(correcto)):
                                                                Vjuego=Vjuego+1
                                                                menu4=1
                                                                c_m4=1
                                                                Led.config(text="EXCELENTE")
                                                                ventana.update()
                                                                time.sleep(2)
                                                                
                                                        else:
                                                                Vjuego=0
                                                                Led.config(text="Vuelve a intentarlo\n GAME OVER")
                                                                ventana.update()
                                                                time.sleep(2)
                                                                menu1=1   #Principal
                                                                menu2=0
                                                                menu3=0
                                                                menu4=0
                                                                menu5=0
                                                                menu6=0
                                                                menu7=0
                                                                menu8=0
                                                                menu9=0
                                                                menu10=0
                                                                menu11=0
                                                                menu12=0
                                                                menu13=0
                                                                c_m1=0
                                                                c_m2=0
                                                                c_m3=0
                                                                c_m4=0
                                                                c_m5=0
                                                                c_m6=0
                                                                c_m7=0
                                                                c_m8=0
                                                                c_m9=0
                                                                c_m10=0
                                                                c_m11=0
                                                                c_m12=0
                                                                c_m13=0
                                                if (c_m5==1):
                                                        if (ser.isOpen()):
                                                                if (vent==0):
                                                                        vent=1
                                                                else:
                                                                        vent=0
                                                                a='+'+str(vent)
                                                                ser.write(a+'\r\n')
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m6==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('Gracias.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m7==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('Estomago.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m8==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('hambre.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m9==1):
                                                        print("Subir volumen")
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m10==1):
                                                        print("Canal -")
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m11==1):
                                                        print("Apagar television")
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m12==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('Estado.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m13==1):
                                                        mixer.init()
                                                        mixer.music.load('BALADA.mp3')
                                                        if (bandera_musica==0):
                                                                time.sleep(0.2)
##                                                                mixer.music.play()
                                                                mixer.music.play()
                                                                print("Reproduciendo Balada")
                                                                bandera_musica=1
                                                                bandera_ROCK=0
                                                                bandera_BALADA=1
                                                                bandera_PODCAST=0
                                                                bandera_SOLOMUSICA=0
                                                        
                                                        else:
                                                                if (bandera_BALADA==1):
                                                                        mixer.music.stop()
                                                                        print("Deteniendo Balada")
                                                                        bandera_musica=0
                                                                        bandera_BALADA=0
                                                                else:
                                                                        time.sleep(0.2)
                                                                        mixer.music.play()
                                                                        print("Reproduciendo Balada")
                                                                        bandera_musica=1
                                                                        bandera_ROCK=0
                                                                        bandera_BALADA=1
                                                                        bandera_PODCAST=0
                                                                        bandera_SOLOMUSICA=0
##                                                        mixer.music.stop()
##                                                        mixer.music.load('BALADA.mp3')
##                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                        if ((Clas[3]>Clas[0]) and (Clas[3]>Clas[1]) and (Clas[3]>Clas[2]) and (Clas[3]>Clas[4]) and (Clas[3]>Clas[5])
                                            and (Clas[3]>Clas[6])):
                                                print("Clase 3")
                                                if (menu1==1):
                                                        menu1=0
                                                        menu2=0
                                                        menu3=0
                                                        menu4=1
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                if (c_m2==1):
                                                        menu1=0
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=1
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0##
                                                if (c_m3==1):
                                                        menu1=0
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0 #Necesidades
                                                        menu9=0 #Television
                                                        menu10=0
                                                        menu11=0
                                                        menu12=1 #Conversar 
                                                        menu13=0  #Musica
                                                if (c_m4==1):
                                                        Ok=1
                                                        my_text = OPC3['text']
                                                        print(my_text)
                                                        print(correcto)
                                                        if (int(my_text)==(correcto)):
                                                                Vjuego=Vjuego+1
                                                                menu4=1
                                                                c_m4=1
                                                                Led.config(text="EXCELENTE")
                                                                ventana.update()
                                                                time.sleep(2)
                                                                
                                                        else:
                                                                Vjuego=0
                                                                Led.config(text="Vuelve a intentarlo\n GAME OVER")
                                                                ventana.update()
                                                                time.sleep(2)
                                                                menu1=1   #Principal
                                                                menu2=0
                                                                menu3=0
                                                                menu4=0
                                                                menu5=0
                                                                menu6=0
                                                                menu7=0
                                                                menu8=0
                                                                menu9=0
                                                                menu10=0
                                                                menu11=0
                                                                menu12=0
                                                                menu13=0
                                                                c_m1=0
                                                                c_m2=0
                                                                c_m3=0
                                                                c_m4=0
                                                                c_m5=0
                                                                c_m6=0
                                                                c_m7=0
                                                                c_m8=0
                                                                c_m9=0
                                                                c_m10=0
                                                                c_m11=0
                                                                c_m12=0
                                                                c_m13=0
                                                if (c_m5==1):
                                                        if (ser.isOpen()):
                                                                if (acceso==0):
                                                                        acceso=1
                                                                else:
                                                                        acceso=0
                                                                a='*'+str(acceso)
                                                                ser.write(a+'\r\n')
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m6==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('no.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m7==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0

                                                        mixer.music.load('Espalda.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m8==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('Banio.mp3')
                                                        mixer.music.play()
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m9==1):
                                                        print("Bajar volumen")
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
##                                                if (c_m10==1):
##                                                        print("")
##                                                        menu1=1   #Principal
##                                                        menu2=0
##                                                        menu3=0
##                                                        menu4=0
##                                                        menu5=0
##                                                        menu6=0
##                                                        menu7=0
##                                                        menu8=0
##                                                        menu9=0
##                                                        menu10=0
##                                                        menu11=0
##                                                        menu12=0
##                                                        menu13=0
##                                                        c_m1=0
##                                                        c_m2=0
##                                                        c_m3=0
##                                                        c_m4=0
##                                                        c_m5=0
##                                                        c_m6=0
##                                                        c_m7=0
##                                                        c_m8=0
##                                                        c_m9=0
##                                                        c_m10=0
##                                                        c_m11=0
##                                                        c_m12=0
##                                                        c_m13=0
                                                ##if (c_m11=1):
                                                ##       print("Apagar television")
                                                        
                                                if (c_m12==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('Platicame.mp3')
                                                        mixer.music.play()
##                                                        bandera_ROCK=0
##                                                        bandera_BALADA=0
##                                                        bandera_PODCAST=0
##                                                        bandera_SOLOMUSICA=0
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m13==1):
                                                        mixer.init()
                                                        mixer.music.load('SoloMusica.mp3')
                                                        if (bandera_musica==0):
                                                                time.sleep(0.2)
                                                                mixer.music.play()
                                                                mixer.music.play()
                                                                print("Reproduciendo Solo musica")
                                                                bandera_musica=1
                                                                bandera_ROCK=0
                                                                bandera_BALADA=0
                                                                bandera_PODCAST=0
                                                                bandera_SOLOMUSICA=1
                                                        
                                                        else:
                                                                if (bandera_SOLOMUSICA==1):
                                                                        mixer.music.stop()
                                                                        print("Deteniendo Solo musica")
                                                                        bandera_musica=0
                                                                        bandera_SOLOMUSICA=0
                                                                else:
                                                                        time.sleep(0.2)
                                                                        mixer.music.play()
                                                                        print("Reproduciendo Solo musica")
                                                                        bandera_musica=1
                                                                        bandera_ROCK=0
                                                                        bandera_BALADA=0
                                                                        bandera_PODCAST=0
                                                                        bandera_SOLOMUSICA=1
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                  ###################################################
                                        if ((Clas[4]>Clas[0]) and (Clas[4]>Clas[1]) and (Clas[4]>Clas[2]) and (Clas[4]>Clas[5]) and (Clas[4]>Clas[5])
                                            and (Clas[4]>Clas[6])):
                                                print("Clase 4")
                                                if (menu1==1):
                                                        menu1=0
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=1
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                if (c_m2==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('Sin_respuesta.mp3')
                                                        mixer.music.play()
                                                        
##                                                        bandera_ROCK=0
##                                                        bandera_BALADA=0
##                                                        bandera_PODCAST=0
##                                                        bandera_SOLOMUSICA=0
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m3==1):
                                                        menu1=0
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0 #Necesidades
                                                        menu9=0 #Television
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0 #Conversar 
                                                        menu13=1 #Musica
                                                if (c_m4==1):
                                                        Ok=1
                                                        my_text = OPC4['text']
                                                        print(my_text)
                                                        print(correcto)
                                                        if (int(my_text)==(correcto)):
                                                                Vjuego=Vjuego+1
                                                                menu4=1
                                                                c_m4=1
                                                                Led.config(text="EXCELENTE")
                                                                ventana.update()
                                                                time.sleep(2)
                                                                
                                                        else:
                                                                Vjuego=0
                                                                Led.config(text="Vuelve a intentarlo\n GAME OVER")
                                                                ventana.update()
                                                                time.sleep(2)
                                                                menu1=1   #Principal
                                                                menu2=0
                                                                menu3=0
                                                                menu4=0
                                                                menu5=0
                                                                menu6=0
                                                                menu7=0
                                                                menu8=0
                                                                menu9=0
                                                                menu10=0
                                                                menu11=0
                                                                menu12=0
                                                                menu13=0
                                                                c_m1=0
                                                                c_m2=0
                                                                c_m3=0
                                                                c_m4=0
                                                                c_m5=0
                                                                c_m6=0
                                                                c_m7=0
                                                                c_m8=0
                                                                c_m9=0
                                                                c_m10=0
                                                                c_m11=0
                                                                c_m12=0
                                                                c_m13=0
                                                if (c_m5==1):
                                                        if (ser.isOpen()):
                                                                #Alarma
                                                                a='$'+str(1)
                                                                ser.write(a+'\r\n')
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m6==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('muybien.mp3')
                                                        mixer.music.play()
##                                                        bandera_ROCK=0
##                                                        bandera_BALADA=0
##                                                        bandera_PODCAST=0
##                                                        bandera_SOLOMUSICA=0
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m7==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('Dolor.mp3')
                                                        mixer.music.play()
##                                                        bandera_ROCK=0
##                                                        bandera_BALADA=0
##                                                        bandera_PODCAST=0
##                                                        bandera_SOLOMUSICA=0
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m8==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('movimiento.mp3')
                                                        mixer.music.play()
##                                                        bandera_ROCK=0
##                                                        bandera_BALADA=0
##                                                        bandera_PODCAST=0
##                                                        bandera_SOLOMUSICA=0
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m9==1):
                                                        #print("Encender / apagar")
                                                        menu1=0   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=1
                                                        menu12=0
                                                        menu13=0
##                                                        
##                                                if (c_m10==1):
##                                                        print("Comedia")
##                                                        menu1=1   #Principal
##                                                        menu2=0
##                                                        menu3=0
##                                                        menu4=0
##                                                        menu5=0
##                                                        menu6=0
##                                                        menu7=0
##                                                        menu8=0
##                                                        menu9=0
##                                                        menu10=0
##                                                        menu11=0
##                                                        menu12=0
##                                                        menu13=0
##                                                        c_m1=0
##                                                        c_m2=0
##                                                        c_m3=0
##                                                        c_m4=0
##                                                        c_m5=0
##                                                        c_m6=0
##                                                        c_m7=0
##                                                        c_m8=0
##                                                        c_m9=0
##                                                        c_m10=0
##                                                        c_m11=0
##                                                        c_m12=0
##                                                        c_m13=0
                                                ##if (c_m11=1):
                                                ##       print("Apagar television")
                                                        
                                                if (c_m12==1):
                                                        mixer.init()
                                                        bandera_musica=0
                                                        bandera_ROCK=0
                                                        bandera_BALADA=0
                                                        bandera_PODCAST=0
                                                        bandera_SOLOMUSICA=0
                                                        mixer.music.stop()
                                                        mixer.music.load('todo_bien.mp3')
                                                        mixer.music.play()
                                                        
##                                                        bandera_ROCK=0
##                                                        bandera_BALADA=0
##                                                        bandera_PODCAST=0
##                                                        bandera_SOLOMUSICA=0
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m13==1):
##                                                      mixer.init()
                                                        mixer.music.load('Podcast.mp3')
                                                        if (bandera_musica==0):
                                                                time.sleep(0.2)
                                                                mixer.music.play()
                                                                mixer.music.play()
                                                                print("Reproduciendo Podcast")
                                                                bandera_musica=1
                                                                bandera_ROCK=0
                                                                bandera_BALADA=0
                                                                bandera_PODCAST=1
                                                                bandera_SOLOMUSICA=0
                                                        
                                                        else:
                                                                if (bandera_PODCAST==1):
                                                                        mixer.music.stop()
                                                                        print("Deteniendo Podcast")
                                                                        bandera_musica=0
                                                                        bandera_PODCAST=0
                                                                else:
                                                                        time.sleep(0.2)
                                                                        mixer.music.play()
                                                                        print("Reproduciendo Podcast")
                                                                        bandera_musica=1
                                                                        bandera_ROCK=0
                                                                        bandera_BALADA=0
                                                                        bandera_PODCAST=1
                                                                        bandera_SOLOMUSICA=0
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                  #######################
                                        if ((Clas[5]>Clas[0]) and (Clas[5]>Clas[1]) and (Clas[5]>Clas[2]) and (Clas[5]>Clas[3]) and (Clas[5]>Clas[4])
                                            and (Clas[5]>Clas[6])):
                                                print("Clase 5")
                                                if (menu1==1):
                                                        
                                                        menu1=1
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        
                                                if (c_m2==1):
                                                        
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                        
                                                if (c_m3==1):
                                                        
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m4==1):
                                                       
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m5==1):
                                                       
                                                        menu1=1   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        c_m1=0
                                                        c_m2=0
                                                        c_m3=0
                                                        c_m4=0
                                                        c_m5=0
                                                        c_m6=0
                                                        c_m7=0
                                                        c_m8=0
                                                        c_m9=0
                                                        c_m10=0
                                                        c_m11=0
                                                        c_m12=0
                                                        c_m13=0
                                                if (c_m6==1):
                                                        
                                                        menu1=0   #Principal
                                                        menu2=1
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        
                                                if (c_m7==1):
                                                        
                                                        menu1=0   #Principal
                                                        menu2=1
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        
                                                if (c_m8==1):
                                                        
                                                        menu1=0   #Principal
                                                        menu2=0
                                                        menu3=1
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        
                                                if (c_m9==1):
                                                        
                                                        menu1=0   #Principal
                                                        menu2=0
                                                        menu3=1
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        
                                                if (c_m10==1):
                                                        
                                                        menu1=0   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=1
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        
                                                if (c_m11==1):
                                                        
                                                        menu1=0   #Principal
                                                        menu2=0
                                                        menu3=0
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=1
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        
                                                if (c_m12==1):
                                                        
                                                        menu1=0   #Principal
                                                        menu2=0
                                                        menu3=1
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        
                                                if (c_m13==1):
##                                                        print("Podcast")
##                                                        bandera_ROCK=0
##                                                        bandera_BALADA=0
##                                                        bandera_PODCAST=0
##                                                        bandera_SOLOMUSICA=0
                                                        menu1=0   #Principal
                                                        menu2=0
                                                        menu3=1
                                                        menu4=0
                                                        menu5=0
                                                        menu6=0
                                                        menu7=0
                                                        menu8=0
                                                        menu9=0
                                                        menu10=0
                                                        menu11=0
                                                        menu12=0
                                                        menu13=0
                                                        

                  ########################
                                        evento=list()
                        d=d+1

##                except:
                else:
                        break
        if(not(mindwaveDataPointReader.isConnected())):
                ventana.mainloop()
                


begin=inicio()
if (begin==0):
        
        mixer.music.load('Reinicia.mp3')
        mixer.music.play()
else:
        iniciar()

        
        
        

ventana.mainloop()



