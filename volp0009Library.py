import math
import time
import random
from gfxhat import lcd, backlight

# -------------------------------- L A B   4 --------------------------------
#This function calculates the area of a circle from its radius.
# The user will inform: 'radius'.
def calculateAreaOfCircle(radius):
    area = round((math.pi * radius ** 2), 2)
    return(area)


#This function calculates the MPG (Miles Per Gallon) of a car.
# The user will inform: 'miles' driven and 'gallons' consumed.
def calculateMpg(miles,gallons):
    mpg = round((miles / gallons),2)
    return(mpg)


# This function makes the temperature conversion from Fahrenheit to Celcius.
# The user will inform: temperature in 'fahrenheit'.
def convertFahrenheitToCelcius(fahrenheit):
    celcius = round(((fahrenheit - 32) * 5 / 9), 2)
    return(celcius)


# This program calculates the distance between two points given their coordinates.
# The user will inform: Point A in axis 'x1' and 'y1; point B in axis 'x2' and 'y2'.
def calculateDistanceBetweenPoints(x1,x2,y1,y2):
    distance = round(math.sqrt(((x2 - x1)**2)+((y2 - y1)**2)),2)
    return(distance)

# -------------------------------- L A B   5 --------------------------------
# This program creates a vertical line across the screen of the GFX HAT.
# The user will inform: Value of axis 'x'.
def verticalLine (x):
    for y in range(0,63):
        lcd.set_pixel(x,y,1)
        lcd.show()


# This program creates a horizontal line across the screen of the GFX HAT.
# The user will inform: Value of axis 'y'.
def horizontalLine (y):
    for x in range(0,127):
        lcd.set_pixel(x,y,1)
        lcd.show()


# These programs create a staircase in the screen of the GFX HAT. One program each direction.
# The user will inform: Point of start in axis 'x' and 'y', the 'weight' and the 'height' of the steps.
# To the RIGHT and DOWN:
def stairsRightDown(x,y,weight,height):
    while (x<=127):
        for a in range(x,x+weight):
            if(a>=127): break
            elif (y>=63): break
            lcd.set_pixel(a,y,1)
            lcd.show()
        for b in range(y,y+height):
            if (b>=63): break
            elif (x+weight>=127): break
            lcd.set_pixel(x+weight,b,1)
            lcd.show()
        x+=weight 
        y+=height

# To the RIGHT and UP:
def stairsRightUp(x,y,weight,height):
    while (x<=127):
        for a in range(x,x+weight):
            if(a>=127): break
            elif (y<=0): break
            lcd.set_pixel(a,y,1)
            lcd.show()
        for b in reversed(range(y-height,y)):
            if (b<=0): break
            elif (x+weight>=127): break
            lcd.set_pixel(x+weight,b,1)
            lcd.show()
        x+=weight 
        y-=height

# To the LEFT and DOWN:
def stairsLeftDown(x,y,weight,height):
    while (x>0):
        for a in reversed(range(x-weight,x)):
            if(a<=0): break
            elif (y>=63): break
            lcd.set_pixel(a,y,1)
            lcd.show()
        for b in range(y,y+height):
            if (b>=63): break
            elif (x-weight<=0): break
            lcd.set_pixel(x-weight,b,1)
            lcd.show()
        x-=weight 
        y+=height

# To the LEFT and UP:
def stairsLeftUp(x,y,weight,height):
    while (x>0):
        for a in reversed(range(x-weight,x)):
            if(a<=0): break
            elif (y<=0): break
            lcd.set_pixel(a,y,1)
            lcd.show()
        for b in reversed(range(y-height,y)):
            if (b<=0): break
            elif (x-weight<=0): break
            lcd.set_pixel(x-weight,b,1)
            lcd.show()
        x-=weight 
        y-=height


# This program shows a random pixel on the screen of the GFX HAT for a period of time.
# The user will inform: how many time ('secs') the random pixel will be shown.
def randomPixelSleep (secs):
    x = random.randrange(127)
    y = random.randrange(63)
    lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(secs)
    lcd.clear()
    lcd.show()


# This program turn off the backlight on the GFX HAT's screen.
# The user will inform: -
def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()

# This program clean the information displayed on the GFX HAT's screen.
# The user will inform: -
def clearLCD():
    lcd.clear()
    lcd.show()