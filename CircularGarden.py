# Author: Princess Sofia H. Macala
# Date: September 19, 2026

# ======================================================================================================================
# PROJECT TITLE: Circular Garden Information Calculator
# ======================================================================================================================

# Description: This program helps determine the information about a circular garden based on the radius entered by the user


# This allows us to use the math library so we can use math functions like math.sqrt, math.pow, etc.
import math

# ======================================================================================================================
# INPUT STAGE: Get information for the problem
# ======================================================================================================================

# Gets the Radius of the garden.
GardenRadius = float(input("Enter Garden radius in meters: "))

# ======================================================================================================================
# PROCESS STAGE: Calculate for the complete information of the circular garden
# ======================================================================================================================

# Calculates for the area of the circular garden.
Area = math.pi*math.pow(GardenRadius, GardenRadius)

# Calculates for the circumference of the circular garden.
Circumference = 2*math.pi*GardenRadius

# Calculates for the square root of the area of the circular garden.
SquareRoot = math.sqrt(Area)

# Rounds down the area to the nearest whole number.
AreaDown = math.floor(Area)

# Rounds up the area to the nearest whole number.
AreaUp = math.ceil(Area)

# ======================================================================================================================
# OUTPUT STAGE: Display the results.
# ======================================================================================================================

# Display the area of the garden
print(f"Area of Garden is: {Area:.2f}")

# Display the circumference of the garden
print(f"Circumference of Garden is: {Circumference:.2f}")

# Display the square root of the garden
print(f"Square root of Garden is: {SquareRoot:.2f}")

# Rounds down the area to the nearest whole number.
print(f"Area rounded down: {AreaDown:.2f}")

# Rounds up the area to the nearest whole number.
print(f"Area rounded up: {AreaUp:.2f}")