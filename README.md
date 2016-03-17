# Codigo-edison
Code an scripts for the Edison boards.

##_Overview_

In this repository is where the scripts that are used by the Edison boards are stored. Those scripts are used to control the sensors and receive information from them, send that information to the Edison board, and from there make the necesary changes in the database.

We have 3 scripts:

**lcd.py**
In the screen on the entrance, the emptiest area is displayed, also the amount of free spaces in each area.
It also recommends an area where you should park.

**area-type-1.py** 
Used for areas with one entrance and one exit.
It gets the maximum capacity and number of free spaces of a type 2 area from the database.
It also detects when a vehicle enters or gets out of this area, and it adds or substracts to the number of free spaces, it updates the database.

**area-type-2.py**
Used for areas with one entrance that can be used as an exit.
It gets the maximum capacity and number of free spaces of a type 1 area specified by a user from the database.
It also detects when a vehicle enters or gets out of this area, and it adds or substracts to the number of free spaces, it updates the database.

##Scripts decription:

###Common variables

This are the variables that all the scripts have in common, they are necesary for the connections with the database and to make the scripts work:

* **areaName:** This is the variable that has the name of the area to administrate, and there should be an area named like this in the database. 

* **server:** This variable contains the address of the server.

####lcd.py functions

```select_best(resultSorted):``` receives a list of lists, this lists contain the areas sorted by priority.

sorted_by_priority(jsonResult): receives a json object from the server and sorts the areas by priority. If two areas have the same priority, it adds the to a bucket in the same position.

```show_general(lcd, welcomeMessage, jsonResult, stop_event):``` this function was made to run in an independent thread, receives lcd as an object that controls the lcd screen, the welcomeMessage is a string that is showed to the user on screen, jsonResult is a json object that is received from the server, it contains all the areas and stop_event is a threading event that should be passed unsetted also it is in charge of stopping the function.
This function shows general information on the lcd screen when the lcd screen is not in use.

```show_best(lcd, jsonResult):``` receives an lcd object, jsonResult is a json object. This function is supposed to show on screen the best area to park in.

####area-type-1.py: it has four sensors, that are used to simulate one entrance and one exit.

This are the parameters corresponding to the buttons:
```python
# Create the button object using GPIO pin 2
button = mraa.Gpio(2)
# Create the buzzer object using GPIO pin 3
button2 = mraa.Gpio(3)
button.dir(mraa.DIR_IN)
button2.dir(mraa.DIR_IN)
# Create the button object using GPIO pin 6
button3 = mraa.Gpio(6)
# Create the buzzer object using GPIO pin 7
button4 = mraa.Gpio(7)
button3.dir(mraa.DIR_IN)
button4.dir(mraa.DIR_IN)
```

####area-type-2.py: it has two sensors, that are used to simulate ane entrance that can be used as an exit.
```
# Create the button object using GPIO pin 2
button = mraa.Gpio(2)
# Create the buzzer object using GPIO pin 3
button2 = mraa.Gpio(3)
```

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
