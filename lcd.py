
import time
import pyupm_buzzer as upmBuzzer
import pyupm_grove as grove
import mraa
import pyupm_i2clcd as lcd
import sys
import random

import json
import urllib
import subprocess

#Area que administra
areaName = "LCD"

#Direccion del servidor
server='http://10.43.14.124:3000/api'

r = urllib.urlopen(server)

#Leyendo query a server.
jsonStr = r.read()

#Convirtiendo en un objeto JSON
jsonResult = json.loads(jsonStr);

#Numero de areas
size = len(jsonResult)

#Numero de lugares disponibles
disponibles=0

#Numero de lugares del estacionamiento
capacidad=0

#Buscar objeto del area a administrar
for i in (0, size - 1):
    #Suma losespacios disponibles de cada area
    disponibles=disponibles+jsonResult[i]['generalAvailable']
    capacidad=capacidad+(jsonResult[i]['generalCapacity'])
    print(jsonResult[i])


overload = 0

# Create the button object using GPIO pin 2
button = mraa.Gpio(2)
button.dir(mraa.DIR_IN)


#Inicializar led
ledPin = mraa.Gpio(5)
ledPin.dir(mraa.DIR_OUT)
ledPin.write(1)

#Crete the lcd object
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setColor(255,255,255)
lcdDisplay.setCursor(0, 0)
lcdDisplay.write(str(area["name"]))
lcdDisplay.setCursor(1, 7)
lcdDisplay.write(str(disponibles) + "/"+ str(capacidad))
entra=False
sale=False

#Color blanco para la pantalla y rojo si el estacionamiento esta lleno
if(disponible == 0):
    r = 204
    g = 6
    b = 5
else:
    r = 205
    g = 205
    b = 205
lcdDisplay.setColor(r,g,b)

# Le la entrada de un boton
while 1:

    if(button.read()!=0):
        r = urllib.urlopen(server)
        #Leyendo query a server.
        jsonStr = r.read()
        #Convirtiendo en un objeto JSON
        jsonResult = json.loads(jsonStr);
        #Numero de lugares disponibles
        disponibles=0
        #Numero de lugares del estacionamiento
        capacidad=0
        #Buscar objeto del area a administrar
        for i in (0, size - 1):
            #Suma losespacios disponibles de cada area
            disponibles=disponibles+jsonResult[i]['generalAvailable']
            capacidad=capacidad+(jsonResult[i]['generalCapacity'])

        lcdDisplay.setCursor(0, 0)
        lcdDisplay.write("                ")
        lcdDisplay.setCursor(1, 0)
        lcdDisplay.write("                ")
        lcdDisplay.setCursor(0, 0)
        lcdDisplay.write("Best: "+"YOLO")
        lcdDisplay.setCursor(1, 0)
        lcdDisplay.write("Lugares: "+disponibles)
        time.sleep(0.5)


    #Pinta de color blando la pantalla si hay lugares disponibles y de rojo si estan ocupados
    if(dsiponibles == 0):
        r = 204
        g = 6
        b = 5
    else:
        r = 205
        g = 205
        b = 205

    lcdDisplay.setColor(r,g,b)

# Delete the button object
del button

# Delete the button object
del button2

del ledPin
