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
areaName = "Area 1"

#Direccion del servidor
server='http://10.43.14.124:3000/api'

r = urllib.urlopen(server)

#Leyendo query a server.
jsonStr = r.read()

#Convirtiendo en un objeto JSON
jsonResult = json.loads(jsonStr);

#Numero de areas
size = len(jsonResult)

#Buscar objeto del area a administrar
for i in (0, size - 1):
    print(jsonResult[i])
    if(jsonResult[i]["name"] == areaName):
        area = jsonResult[i]

#Espacios ocupados
occupied = area['generalCapacity'] - area['generalAvailable']
#Capacidad del area
capacity = area['generalCapacity']
overload = 0

# Create the button object using GPIO pin 2
button = mraa.Gpio(2)
# Create the buzzer object using GPIO pin 3
button2 = mraa.Gpio(3)

button.dir(mraa.DIR_IN)
button2.dir(mraa.DIR_IN)

#Inicializar led
ledPin = mraa.Gpio(5)
ledPin.dir(mraa.DIR_OUT)
ledPin.write(1)

#Crete the lcd object
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setColor(0,0,0)
entra=False
sale=False
lcdDisplay.setCursor(0, 0)
lcdDisplay.write(str(area["name"]))
lcdDisplay.setCursor(1, 7)
lcdDisplay.write(str(occupied) + "/"+ str(capacity))

#Color blanco para la pantalla
if(occupied == capacity):
    r = 204
    g = 6
    b = 5
else:
    r = 205
    g = 205
    b = 205
lcdDisplay.setColor(r,g,b)

# Read the input and print, waiting one second between readings
while 1:
    if(entra):
        if(button2.read()!=0):
            lcdDisplay.setCursor(1, 0)
            lcdDisplay.write("                ")
            lcdDisplay.setCursor(1, 0)

            if(occupied + 1 <= capacity):
                occupied = occupied + 1
                subprocess.check_call(['curl', '-X', 'PUT', '-H', "Cache-Control: no-cache",
                    '-H', "Content-Type: application/x-www-form-urlencoded", '-d', "name=Area 1&generalAvailable=-1", server])
            else:
                overload = overload + 1

            lcdDisplay.write(str(occupied))
            lcdDisplay.setCursor(1, 7)
            lcdDisplay.write(str(capacity))

            lcdDisplay.setCursor(1, 9)
            lcdDisplay.write(str(overload))

            print("Boton 2 presionado, entro")
            ledPin.write(0)
            entra=False
            sale=False
            time.sleep(0.5)
            lcdDisplay.setCursor(0, 0)
            lcdDisplay.write("                ")
            #subprocess.check_call('curl -X PUT -H "Cache-Control: no-cache" -H "Content-Type: application/x-www-form-urlencoded" -d "name=Area 1&generalAvailable=-1" '+server)
    else:
        if(button2.read() != 0):
            sale=True
            ledPin.write(1)
            print("Boton 2 presionado")
            time.sleep(0.5)


    if(sale):
        if(button.read()!=0):
            lcdDisplay.setCursor(1, 0)
            lcdDisplay.write("                ")
            lcdDisplay.setCursor(1, 0)

            if(occupied - 1 >= 0):
                if(overload == 0):
                    occupied = occupied - 1
                    subprocess.check_call(['curl', '-X', 'PUT', '-H', "Cache-Control: no-cache",
                        '-H', "Content-Type: application/x-www-form-urlencoded", '-d', "name=Area 1&generalAvailable=1", server])
                else:
                    overload = overload - 1

            lcdDisplay.write(str(occupied))
            lcdDisplay.setCursor(1, 7)
            lcdDisplay.write(str(capacity))

            lcdDisplay.setCursor(1, 9)
            lcdDisplay.write(str(overload))

            print("Boton 1 presionado, salio")
            ledPin.write(0)
            entra=False
            sale=False
            time.sleep(0.5)
    else:
        if(button.read() != 0):
            entra=True
            ledPin.write(1)
            print("Boton 1 presionado")
            lcdDisplay.setCursor(0, 0)
            lcdDisplay.write("                ")
            if(occupied<capacity ):
                lcdDisplay.setCursor(0, 0)
                lcdDisplay.write("Est-1")
            else:
                lcdDisplay.setCursor(0, 0)
                lcdDisplay.write("Est-2")

            time.sleep(0.5)

    if(occupied == capacity):
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
