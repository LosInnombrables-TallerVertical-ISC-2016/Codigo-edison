# Codigo-edison
Code an scripts for the Edison boards.

In this repository is where the scripts that are used by the Edison boards are stored. Those scripts are used to control the sensors and receive information from them, send that information to the Edison board, and from there make the necesary changes in the databases.

We have 2 scripts:

lcd.py
In the screen on the entrance, the emptiest area is displayed, also the amount of free spaces in each area.
It also recommends an area where you should park.

InserttNameHere.py 
It detects which is the current area and gets the maximum capacity and number of free spaces of that area from the databases.
It also detects when a vehicle enters or gets out of the current area, and it adds or substracts to the number of free spaces, it updates the databases.

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
