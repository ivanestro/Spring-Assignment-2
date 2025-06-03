"""Assignment 2."""

__author__ = "Ivan Estropigan"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Dev Team"

## SIMPLE DATA TYPES

# Variables
NAME = 'Ivan'
CURRENT_DRIVERS_LICENSE = True
current_year = 2025


# Print name and datatype
print("name: ", NAME, "type: ", type(NAME))

"""Printing the name and data type 
Args:

    parameter-name (type): 

Returns: name: Ivan type: <class 'str'> 
"""

# Checking a valid license, and convert to Boolean
CURRENT_DRIVERS_LICENSE = input("Do you have Drivers License? [True] or [False] ")
if CURRENT_DRIVERS_LICENSE == 'True':
    CURRENT_DRIVERS_LICENSE = True

elif CURRENT_DRIVERS_LICENSE == 'False':
    CURRENT_DRIVERS_LICENSE = False

else:
    print("Invalid")

if CURRENT_DRIVERS_LICENSE:
    print(f"has license: {CURRENT_DRIVERS_LICENSE}", "type: ", type(CURRENT_DRIVERS_LICENSE))

else: 
    print("")
""" The purpose of this code is to check whether they have valid or invalid Driver's License.

Args:
CURRENT_MANITOBA_DRIVERS_LICENS = True
convert the type from str to boolean
type should return as boolean

Returns: 
Do you have Drivers License? [True] or [False] 
If True: has license: {MANITOBA_DRIVERS_LICENSE} type: <class 'str'>
If False: Invalid Drivers License.
"""

# Print current year of 2025 and type
print(f"this year: {current_year}", "type: ", type(current_year))

""" To store current year, print it to the system and get the type of the year

Args:
current_year = 2025 variable
type(current_year) = int

Returns: 
this year: 2025 type: <class 'int'> 
"""

#Increase the current year by 1 and type
current_year += 1
print(f"next year: {current_year}", "type: ", type(current_year))

""" To store current year and increase by 1

Args:
current_year = 2025 variable
type(current_year) = int

Returns: 
next year: 2026 type: <class 'int'>
"""
