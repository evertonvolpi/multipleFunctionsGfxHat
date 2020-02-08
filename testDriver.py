# -------------------- T E S T    D R I V E R --------------------
# This program exhibits all the programs inside volp0009Library in 
# a simple menu and then proceeds the respective tests.

from gfxhat import lcd, backlight
import volp0009Library

# -------------------------------- L A B   4 --------------------------------
# Function tested: 'calculateAreaOfCircle'
# Objective: calculate the area of a circle given its radius.
def callCalculateAreaOfCircle():
    print("This program calculates the area of a circle given its radius.")
    r = float(input("Please inform the radius of the circle > "))
    result = volp0009Library.calculateAreaOfCircle(r)
    print("The area of a circle of radius '{}' is equal to {}." .format(r,result))


# Function tested: 'calculateMpg'
# Objective: calculate the MPG-Miles Per Gallon of a car.
def callCalculateMpg():
    print("This program calculates the MPG-Miles Per Gallon of a car.")
    miles = float(input("Please inform how many miles you have driven > "))
    gallons = float(input("Please inform how many gallons you have used > "))
    mpg = volp0009Library.calculateMpg(miles,gallons)
    print("The MGP of a car that consumed {} gallons in {} miles is equal to {}" .format(gallons,miles,mpg))

# Function tested: 'convertFahrenheitToCelcius'
# Objective: convert the temperature value from Fahrenheit to Celcius.
def callConvertFahrenheitToCelcius():
    print("This program makes the temperature conversion from Fahrenheit to Celcius.")
    fahrenheit = float(input("Please inform the temperature in Fahrenheit > "))
    celcius = volp0009Library.convertFahrenheitToCelcius(fahrenheit)
    print("{} Fahrenheit is equal to {} Celcius." .format(fahrenheit,celcius))

# Function tested: 'calculateDistanceBetweenPoints'
# Objective: calculate the distance between two points given their coordinates.
def callCalculateDistanceBetweenPoints():
    print("This program calculates the distance between two points given their coordinates")
    x1 = float(input("Please inform the position of point A in the X axis > "))
    y1 = float(input("Please inform the position of point A in the Y axis > "))
    x2 = float(input("Please inform the position of point B in the X axis > "))
    y2 = float(input("Please inform the position of point B in the Y axis > "))
    distance = volp0009Library.calculateDistanceBetweenPoints(x1,x2,y1,y2)
    print("The distance between point A({}x, {}y) and point B({}x, {}y) is equal to {}." .format(x1,y1,x2,y2,distance))

    
# -------------------------------- L A B   5 --------------------------------
# Function tested: 'verticalLine'
# Objective: creates a vertical line across the screen of the GFX HAT given the value of x axis.
def callVerticalLine ():
    x = int(input("Please inform a value between 0 and 127 for the line's position in axis x > "))
    if (x>0 and x<127):
        volp0009Library.verticalLine(x)
    else:
        print("Invalid value.")
        callVerticalLine()


# Function tested: 'horizontalLine'
# Objective: creates a horizontal line across the screen of the GFX HAT given the value of y axis.
def callHorizontalLine ():
    y = int(input("Please inform a value between 0 and 63 for the line's position in axis y > "))
    if (y>0 and y<63):
        volp0009Library.horizontalLine(y)
    else:
        print("Invalid value.")
        callHorizontalLine()


# ------- S T A I R C A S E -------
# Functions tested: 'stairsRightDown', 'stairsRightUp', 'stairsLeftDown', 'stairsLeftUp' 
# Objective: create a staircase in the screen of the GFX HAT given the point of start in axis
# 'x' and 'y', the 'weight' and 'height' of the steps. One program each direction.
# ---To the RIGHT and DOWN:
def callStairsRightDown():
    x = xAxisValue()
    y = yAxisValue()
    weight = weightValue()
    height = heightValue()
    volp0009Library.stairsRightDown(x,y,weight,height)

# ---To the RIGHT and UP:
def callStairsRightUp():
    x = xAxisValue()
    y = yAxisValue()
    weight = weightValue()
    height = heightValue()
    volp0009Library.stairsRightUp(x,y,weight,height)

# ---To the LEFT and DOWN:
def callStairsLeftDown():
    x = xAxisValue()
    y = yAxisValue()
    weight = weightValue()
    height = heightValue()
    volp0009Library.stairsLeftDown(x,y,weight,height)

# ---To the LEFT and UP:
def callStairsLeftUp():
    x = xAxisValue()
    y = yAxisValue()
    weight = weightValue()
    height = heightValue()
    volp0009Library.stairsLeftUp(x,y,weight,height)

# --- I N P U T S ---
def xAxisValue():
    x = int(input("Enter a value between 0 and 127 for axis x > "))
    if (x<0 or x>127):
        print("Invalid value.")
        xAxisValue()
    else: return(x)

def yAxisValue():
    y = int(input("Enter a value between 0 and 63 for axis y > "))
    if (y<0 or y>63):
        print("Invalid value.")
        yAxisValue()
    else: return(y)

def weightValue():
    w = int(input("Enter a value for the weight of the step > "))
    if (w<0 or w>127):
        print("Weight must be a value between 0 and 127.")
        weightValue()
    else: return(w)

def heightValue():
    h = int(input("Enter a value for the height of the step > "))
    if (h<0 or h>63):
        print("Height must be a value between 0 and 63.")
        heightValue()
    else: return(h)
# ------ * * * ------

# Function tested: 'randomPixelSleep'
# Objective: shows a random pixel on the screen of the GFX HAT for a given period of time.
def callRandomPixelSleep():
    s = int(input("Please inform for how long you want to see the random pixel (in secs) > "))
    volp0009Library.randomPixelSleep(s)
    
# Function tested: 'clearBacklight'
# Objective: turn off the backlight of the GFX HAT's screen.
def callClearBacklight():
    volp0009Library.clearBacklight()

# Function tested: 'clearLCD'
# Objective: clear the information displayed on the GFX HAT's screen.
def callClearLCD():
    volp0009Library.clearLCD()


# -------------------------------- M A I N    M E N U --------------------------------
def menu():
    choice = input("""
        *** M A I N   M E N U ***
        Enter the number of your choice:
            1. LAB 4
            2. LAB 5
            3. Turn ON GFX HAT's backlight
            4. Turn OFF GFX HAT's backlight
            5. Clear GFX HAT's LCD
            6. Exit
            > """)
    if (choice == "1"):
        lab4library()
    elif (choice == "2"):
        lab5library()
    elif (choice == "3"):
        backlightColor()
    elif (choice == "4"):
        callClearBacklight()
        menu()
    elif (choice == "5"):
        callClearLCD()
        menu()
    elif (choice == "6"):
        callClearBacklight()
        callClearLCD()
        print ("Goodbye!")
    else:
        print("Invalid option.")
        menu()

# --- S I D E    M E N U S ---
# --- Lab 4 Menu:
def lab4library():
    choice = input("""
        *** L A B   4 ***
        Which function do you wish to test? (enter the number)
            1. Calculate the area of a circumference
            2. Calculate MPG - Miles Per Gallon
            3. Convert Fahrenheit to Celcius
            4. Calculate distance between two points
            5. Back to MAIN MENU
            > """)
    if (choice == "1"):
        callCalculateAreaOfCircle()
        goBackLab4()
    elif (choice == "2"):
        callCalculateMpg()
        goBackLab4()
    elif (choice == "3"):
        callConvertFahrenheitToCelcius()
        goBackLab4()
    elif (choice == "4"):
        callCalculateDistanceBetweenPoints()
        goBackLab4()
    elif (choice == "5"):
        menu()
    else:
        print("Invalid option.")
        lab4library()

# --- Lab 5 Menu:
def lab5library():
    choice = input("""
        *** L A B   5 ***
        Which function do you wish to test? (enter the number)
            1. Vertical line on GFX HAT
            2. Horizontal line on GFX HAT
            3. Staircase on GFX HAT
            4. Random pixel for limited period of time on GFX HAT
            5. Clear GFX HAT's Backlight
            6. Back to MAIN MENU
            > """)
    if (choice == "1"):
        callVerticalLine()
        goBackLab5()
    elif (choice == "2"):
        callHorizontalLine()
        goBackLab5()
    elif (choice == "3"):
        stairsMenu()
    elif (choice == "4"):
        callRandomPixelSleep()
        lab5library()
    elif (choice == "5"):
        callClearBacklight()
        lab5library()
    elif (choice == "6"):
        menu()
    else:
        print("Invalid option.")
        lab5library()

# --- GFX HAT's Backlight Colour:
def backlightColor():
    choice = input("""
        *** B A C K L I G H T   C O L O U R ***
        Which color do you prefer for the backlight? (enter the number)
            1. red
            2. green
            3. blue
            4. white
            5. Back to MAIN MENU
            > """)
    if (choice == "1"):
        backlight.set_all(255,0,0)
        backlight.show()
        menu()
    elif (choice == "2"):
        backlight.set_all(0,255,0)
        backlight.show()
        menu()
    elif (choice == "3"):
        backlight.set_all(0,0,255)
        backlight.show()
        menu()
    elif (choice == "4"):
        backlight.set_all(255,255,255)
        backlight.show()
        menu()
    elif (choice == "5"):
        menu()
    else:
        print("Invalid option.")
        backlightColor()

# --- Stairs' functions inside menu:
def stairsMenu():
    choice = input("""
        *** S T A I R C A S E ***
        Which direction do you want to test? (enter the number)
            1. Right and down
            2. Right and up
            3. Left and down
            4. Left and up
            5. Back to LAB 5 MENU
            6. Back to MAIN MENU
            > """)
    if (choice == "1"):
        callStairsRightDown()
        goBackStairs()
    elif (choice == "2"):
        callStairsRightUp()
        goBackStairs()
    elif (choice == "3"):
        callStairsLeftDown()
        goBackStairs()
    elif (choice == "4"):
        callStairsLeftUp()
        goBackStairs()
    elif (choice == "5"):
        lab5library()
    elif (choice == "6"):
        menu()
    else:
        print("Invalid choice.")
        stairsMenu()

# --- Returns:
def goBackLab4():
    input("Press ENTER to return to the menu")
    lab4library()

def goBackLab5():
    input("Press ENTER to return to the menu")
    callClearLCD()
    lab5library()

def goBackStairs():
    input("Press ENTER to return to the menu")
    callClearLCD()
    stairsMenu()


menu()
# --- * * * ---