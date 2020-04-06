#!/usr/bin/python3

from tkinter import *
import time
from urllib import request
import json

def GetClima():
    apikey = "1bf90c1dc3e17f0405996dd6a0e8c0cf"
    url = "http://api.openweathermap.org/data/2.5/weather?q=Curico&appid=" + apikey + ""
    meteo = request.urlopen(url)
    # meteo= meteo.read().decode('utf-8')
    diccio = json.load(meteo)
    temp = diccio["main"]["temp"]
    ciudad = diccio["name"]
    print(ciudad)
    print(temp)
    temp=temp-273.15
    return temp

def num(digito, pos):
        y=pos*150
        S1=(y+10,20,Vert)
        S2=(y+10,130,Vert)
        S3=(y+120,20,Vert)
        S4=(y+120,130,Vert)
        S5=(y+25,5,Hor)
        S6=(y+25,115,Hor)
        S7=(y+25,225,Hor)
        PS=(y+70,70,Punt)
        PI=(y+70,180,Punt)
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
            image = canvas.create_image(ind[0], ind[1], anchor=NW, image=ind[2])
        return

temp= str(GetClima())+" °C"

root = Tk()
Hor = PhotoImage(file="Dig.png")
Vert = PhotoImage(file="DigVer.png")
Punt= PhotoImage(file="Punto.png")
Clima = PhotoImage(file="clima.png")

canvas = Canvas(root, bd=0,bg="black", width=1200, height=500)
canvas.pack() # this makes it visible
canvas2 = Canvas(canvas, highlightthickness=0,bg="green", width=180, height=180)

def tiempo(test):
    Line1=(-90, -30)
    Line2=(-90,-200)
    Desp=(200,180)
    TI={"chubasco": (Line1), "tormenta":(Line1[0]-Desp[0],Line1[1]), "nublado":(Line1[0]-Desp[0]*2,Line1[1]),
        "nieve": (Line2), "soleado":(Line2[0]-Desp[0],Line2[1]),"lluvia":(Line2[0]-Desp[0]*2,Line2[1])   }
    return TI[test]

def Ren():
    canvas.delete(ALL)
    hora = time.strftime('%H:%M:%S')
    canvas.create_window(700, 400, window=canvas2)
    canvas.create_text(1000, 450, fill="white", font=('arial',40, "bold"), text=temp)
    icon=tiempo("tormenta")
    canvas2.create_image(icon[0],icon[1], anchor=NW, image=Clima)
    for x in range(len(hora)):
        num(hora[x],x)
    canvas.after(200, Ren)

Ren()



root.mainloop(  )

