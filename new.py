import time
import pyupm_buzzer as upmBuzzer
import pyupm_grove as grove
import mraa
import pyupm_i2clcd as lcd
import sys
import random

import json
import urllib.request
from pip._vendor.requests.packages.urllib3.connectionpool import xrange
from setuptools.command.build_ext import if_dl
from builtins import int
url='http://10.43.14.124:3000/api'
r = urllib.request.urlopen(url)

contador=0
palabra= str(r.read())

for y in xrange(3, palabra.__len__()):
        if(palabra[y]=="{"):
            contador=contador+1;

arreglo = ['']*contador
contador=-1
escribe=False
for x in xrange(3, palabra.__len__()):
    if (palabra[x]=="{"):
        contador=contador+1
        escribe=True
    
    if (escribe):
        arreglo[contador]=arreglo[contador]+palabra[x]
    
    if (palabra[x]=="}"):
        escribe=False        

print(arreglo[0])
print(arreglo[1])
pal=arreglo[0]
ls=json.loads(pal)
print (ls['name'])






pal=arreglo[0]
ls=json.loads(pal)
counter = ls['generalAvailable']
pal=arreglo[0]
ls=json.loads(pal)
counter2 = ls['generalAvailable']
# Create the button object using GPIO pin 0
button = mraa.Gpio(2)
button2 = mraa.Gpio(3)
# Create the buzzer object using GPIO pin 5

button.dir(mraa.DIR_IN)
button2.dir(mraa.DIR_IN)

ledPin = mraa.Gpio(5)
ledPin.dir(mraa.DIR_OUT)
ledPin.write(1)


#Crete the lcd object 
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setColor(0,0,0)
entra=False
sale=False
lcdDisplay.setCursor(0, 0)
lcdDisplay.write("Hello world!!")
lcdDisplay.setCursor(1, 7)
lcdDisplay.write(str(counter2))
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
lcdDisplay.setColor(r,g,b)
# Read the input and print, waiting one second between readings
while 1:
    
    
        
    if(entra):
        if(button2.read()!=0):
            lcdDisplay.setCursor(1, 0)
            lcdDisplay.write("                ")
            lcdDisplay.setCursor(1, 0)
            counter = counter + 1
            lcdDisplay.write(str(counter))
            lcdDisplay.setCursor(1, 7)
            lcdDisplay.write(str(counter2))
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            lcdDisplay.setColor(r,g,b)
            print("Boton 2 presionado, entro")
            ledPin.write(0)
            entra=False
            sale=False
            time.sleep(0.5)
            lcdDisplay.setCursor(0, 0)
            lcdDisplay.write("                ")
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
            counter = counter - 1
            lcdDisplay.write(str(counter))
            lcdDisplay.setCursor(1, 7)
            lcdDisplay.write(str(counter2))
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            lcdDisplay.setColor(r,g,b)
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
            if(counter<counter2):
                lcdDisplay.setCursor(0, 0)
                lcdDisplay.write("Est-1")
            else:
                lcdDisplay.setCursor(0, 0)
                lcdDisplay.write("Est-2")  
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            lcdDisplay.setColor(r,g,b)
            time.sleep(0.5)
    

# Delete the buzzer object


# Delete the button object
del button

# Delete the button object
del button2

del ledPin
