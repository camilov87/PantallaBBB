#!/usr/bin/env python3

from tkinter import *
import time
from urllib import request
import json

class Getclima:
    def __init__(self):
        self.api= "1bf90c1dc3e17f0405996dd6a0e8c0cf"
        self.url= "http://api.openweathermap.org/data/2.5/weather?q=Curico&appid=" + self.api + ""
    def getwebdata(self):
        meteo = request.urlopen(self.url)
        meteo = meteo.read().decode('utf-8')
        diccio = json.loads(meteo)
        return diccio
    def gettemp(self,dic):
        self.temp=dic["main"]["temp"]
        return self.temp
    def getciudad(self,dic):
        ciudad = dic["name"]
        return ciudad
    def getestado(self,dic):
        estado= dic["weather"][0]["main"]
        return estado

def GetClima():
    apikey = "1bf90c1dc3e17f0405996dd6a0e8c0cf"
    url = "http://api.openweathermap.org/data/2.5/weather?q=Curico&appid=" + apikey + ""
    meteo = request.urlopen(url)
    meteo= meteo.read().decode('utf-8')
    diccio = json.loads(meteo)
    temp = diccio["main"]["temp"]
    ciudad = diccio["name"]
    print(ciudad)
    print(temp)
    temp=temp-273.15
    return temp

def num(digito, pos):
        y=pos*90
        S1=(y+10,15,Vert)
        S2=(y+10,80,Vert)
        S3=(y+80,15,Vert)
        S4=(y+80,80,Vert)
        S5=(y+20,5,Hor)
        S6=(y+20,70,Hor)
        S7=(y+20,140,Hor)
        PS=(y+40,30,Punt)
        PI=(y+40,120,Punt)
        numeros= {
            "1":(S3,S4),
            "2":(S2,S3,S5,S6,S7),
            "3":(S3,S4,S5,S6,S7),
            "4":(S1,S3,S4,S6),
            "5":(S1,S4,S5,S6,S7),
            "6":(S1,S2,S4,S5,S6,S7),
            "7":(S3,S4,S5),
            "8":(S1,S2,S3,S4,S5,S6,S7),
            "9":(S1,S3,S4,S5,S6),
            "0":(S1,S2,S3,S4,S5,S7),
            ":":(PS,PI)
        }
        for ind in numeros[digito]:
            ihora.creaimg(ind[0], ind[1],ind[2])
        return

def tiempo(test):
    Line1=(-90, -30)
    Line2=(-90,-200)
    Desp=(200,180)
    TI={"chubasco": (Line1), "tormenta":(Line1[0]-Desp[0],Line1[1]), "Clouds":(Line1[0]-Desp[0]*2,Line1[1]),
        "nieve": (Line2), "Clear":(Line2[0]-Desp[0],Line2[1]),"Rain":(Line2[0]-Desp[0]*2,Line2[1])   }
    return TI[test]

class subcanvas:
    def __init__(self, bigcanvas,xpos,ypos,ancho,alto):
        self.bigcanvas=bigcanvas
        self.xpos=xpos
        self.ypos=ypos
        self.subcuadro=Canvas(bigcanvas,highlightthickness=0,bg="black",width=ancho, height=alto)
    def abrevent(self):
        self.bigcanvas.create_window(self.xpos, self.ypos, window=self.subcuadro)
    def creaimg(self, fotox, fotoy,imagen):
        self.subcuadro.create_image(fotox,fotoy, anchor=NW, image=imagen)
    def delimg(self):
        self.subcuadro.delete(ALL)


root = Tk()
Hor = PhotoImage(file="Dig.png")
Vert = PhotoImage(file="DigVer.png")
Punt= PhotoImage(file="Punto.png")
Clima = PhotoImage(file="clima.png")

wi=800
hi=600
clima= Getclima()
dicDato= clima.getwebdata()
ciudad= clima.getciudad(dicDato)
temp= int(clima.gettemp(dicDato)-273.15)
temp= str(temp)+" °C"

canvas = Canvas(root, bd=0,bg="black", width=wi, height=hi)
canvas.pack() # this makes it visible
#canvas2 = Canvas(canvas, highlightthickness=0,bg="green", width=180, height=180)
IClima= subcanvas(canvas,wi*0.5,hi*0.6,180,200)
ihora=subcanvas(canvas,402,102,wi,200)
icon=tiempo(clima.getestado(dicDato))


def Ren():
    ihora.delimg()
    hora = time.strftime('%H:%M:%S')
    #canvas.create_window(700, 400, window=canvas2)  #Crea canvas para icono2
    ihora.abrevent()
    IClima.abrevent()
    canvas.create_text(wi * 0.80, hi * 0.55, fill="white", font=('arial', 50, "bold"), text=ciudad)
    canvas.create_text(wi*0.80, hi*0.65, fill="white", font=('arial',50, "bold"), text=temp)
    IClima.creaimg(icon[0],icon[1],Clima)
    #canvas2.create_image(icon[0],icon[1], anchor=NW, image=Clima) #
    for x in range(len(hora)):
        num(hora[x],x)
    canvas.after(200, Ren)

Ren()



root.mainloop(  )
