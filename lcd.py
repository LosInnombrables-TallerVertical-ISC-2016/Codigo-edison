
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


#Crete the lcd object
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setColor(255,255,255)
lcdDisplay.setCursor(0, 0)
lcdDisplay.write("hola")
lcdDisplay.setCursor(1, 7)
lcdDisplay.write(str(disponibles) + "/"+ str(capacidad))




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
        lcdDisplay.write("Lugares: "+str(disponibles))
        time.sleep(0.5)


    

# Delete the button object
del button

# Delete the button object
del button2

del ledPin
