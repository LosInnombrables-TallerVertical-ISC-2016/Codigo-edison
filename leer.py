import json
import urllib
#import urllib.request
import setuptools.command.build_ext 


url='http://10.43.14.124:3000/api'
r = urllib.request.urlopen(url)

data =json.loads('{"_id":"56e84d461a12721263023879","name":"Area 1","generalCapacity":20,"handicapCapacity":5,"generalAvailable":20,"handicapAvailable":5,"__v":0}')
contador=0
print(data['name'])
palabra= str(r.read())

for y in range(3, palabra.__len__()):
        if(palabra[y]=="{"):
            contador=contador+1;

arreglo = ['']*contador
contador=-1
escribe=False
for x in range(3, palabra.__len__()):
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
print (data)
