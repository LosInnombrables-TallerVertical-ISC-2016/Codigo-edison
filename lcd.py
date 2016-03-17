
import time
import pyupm_buzzer as upmBuzzer
import pyupm_grove as grove
import mraa
import pyupm_i2clcd as lcd
import sys
import random

import threading
import json
import urllib
import subprocess

#Area que administra
areaName = "LCD"
#Direccion del servidor
server='http://10.43.14.124:3000/api'
#Mensaje bienvenida
welcomeMessage = "Bienvenido al Tec de Monterrey"
#Leyendo query a server.
r = urllib.urlopen(server)
jsonStr = r.read()


def select_best(resultSorted):
    result = resultSorted[0][0]
    i = 0
    for i in (0, len(resultSorted) - 1):
        j = 0
        while(j < len(resultSorted[i])):
            if(resultSorted[i][j]["generalAvailable"] > result["generalAvailable"]):
                result = resultSorted[i][j]
            j = j + 1
        if(result["generalAvailable"] > 0):
            return result
    return None

def sort_by_priority(jsonResult):
    resultSorted = list()
    size = len(jsonResult)
    i = 0
    while( i <  size):
        resultSorted.append(list())
        i = i + 1
    i = 0
    while( i < size):
        j = jsonResult[i]["priority"] - 1
        resultSorted[j].append(jsonResult[i])
        i = i + 1
    i = 0
    while(i < size):
        if(len(resultSorted[i]) == 0):
            resultSorted.remove(resultSorted[i])
            size = size - 1
            i = i - 1
        i = i + 1
    return resultSorted

def show_general(lcd, welcomeMessage, jsonResult, stop_event):
    #Limpiando LCD
    lcdDisplay.setCursor(0, 0)
    lcdDisplay.write("                ")
    lcdDisplay.setCursor(1, 0)
    lcdDisplay.write("                ")
    #Numero de lugares disponibles
    disponibles=0
    #Numero de lugares del estacionamiento
    capacidad=0
    #Numero de areas
    size = len(jsonResult)
    i = 0
    while(i < size):
        #Suma losespacios disponibles de cada area
        disponibles=disponibles+jsonResult[i]['generalAvailable']
        capacidad=capacidad+(jsonResult[i]['generalCapacity'])
        i = i + 1

    lcd.setCursor(1, 6)
    lcd.write(str(capacidad - disponibles) + "/" + str(capacidad))
    pos = 0;
    while(not stop_event.is_set()):
        #Mensaje de bienvenida
        lcdDisplay.setCursor(0, 0)
        lcdDisplay.write(welcomeMessage[0 + pos: 16  + pos])
        pos = pos + 1
        if(len(welcomeMessage) < pos + 16):
            pos = 0;
        time.sleep(0.5)

def show_best(lcd, jsonResult):
    #Limpiando LCD
    lcdDisplay.setCursor(0, 0)
    lcdDisplay.write("                ")
    lcdDisplay.setCursor(1, 0)
    lcdDisplay.write("                ")
    lcdDisplay.setCursor(0, 0)
    if(jsonResult != None):
        lcdDisplay.write("Vaya a "+ str(result["name"]))
        lcdDisplay.setCursor(1, 0)
        lcdDisplay.write("Lugares: "+str(result["generalAvailable"]))
    else:
        lcdDisplay.write("No hay lugares")
        lcdDisplay.setCursor(1, 0)
        lcdDisplay.write("disponibles")
    time.sleep(3)


#Convirtiendo en un objeto JSON
jsonResult = json.loads(jsonStr)


# Create the button object using GPIO pin 2
button = mraa.Gpio(2)
button.dir(mraa.DIR_IN)

#Crete the lcd object
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setColor(255,255,255)
lcdDisplay.setCursor(0, 0)
lcdDisplay.write(welcomeMessage)

sort_by_priority(jsonResult)

#   thread.start_new_thread(show_general, (lcdDisplay, welcomeMessage, jsonResult))
t1_stop = threading.Event()
t1 = threading.Thread(target=show_general, args=(lcdDisplay, welcomeMessage, jsonResult, t1_stop))
t1.start()
# Le la entrada de un boton
while 1:
    if(button.read()!=0):
        t1_stop.set()
        r = urllib.urlopen(server)
        #Leyendo query a server.
        jsonStr = r.read()
        #Convirtiendo en un objeto JSON
        jsonResult = json.loads(jsonStr)
        resultSorted = sort_by_priority(jsonResult)
        result = select_best(resultSorted)
        show_best(lcdDisplay, result)
        t1_stop = threading.Event()
        t1 = threading.Thread(target=show_general, args=(lcdDisplay, welcomeMessage, jsonResult, t1_stop))
        t1.start()

# Delete the button object
del button

# Delete the button object
del button2

del ledPin
