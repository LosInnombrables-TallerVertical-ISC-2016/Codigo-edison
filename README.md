# Codigo-edison
Code an scripts for the Edison boards.

##_Overview_

In this repository is where the scripts that are used by the Edison boards are stored. Those scripts are used to control the sensors and receive information from them, send that information to the Edison board, and from there make the necesary changes in the database.

We have 3 scripts:

**lcd.py**
In the screen on the entrance, the emptiest area is displayed, also the amount of free spaces in each area.
It also recommends an area where you should park.

**area-type-1.py** 
Used for areas with one entrance that can be used as an exit.
It gets the maximum capacity and number of free spaces of a type 1 area specified by a user from the database.
It also detects when a vehicle enters or gets out of this area, and it adds or substracts to the number of free spaces, it updates the database.

**area-type-2.py** 
Used for areas with one entrance and one exit.
It gets the maximum capacity and number of free spaces of a type 2 area from the database.
It also detects when a vehicle enters or gets out of this area, and it adds or substracts to the number of free spaces, it updates the database.

##Scripts decription:

###Common variables

This are the variables that all the scripts have in common, they are necesary for the connections with the database and to make the scripts work:

* **areaName:** This is the variable that has the name of the area to administrate, and there should be an area named like this in the database. 

* **server:** This variable contains the address of the server.

####

####

####


![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
