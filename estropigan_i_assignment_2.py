"""Assignment 2."""

__author__ = "Ivan Estropigan"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Dev Team"

## SIMPLE DATA TYPES

# Variables 
NAME = 'Ivan'
MANITOBA_DRIVERS_LICENSE = False

# Print name and datatype
print("name: ", NAME, "type:", type(NAME))

# 
MANITOBA_DRIVERS_LICENSE = input("Do you have Drivers License? [True] or [False] ")
if MANITOBA_DRIVERS_LICENSE == 'True':
    print("has license: {MANITOBA_DRIVERS_LICENSE}", "type: ", type(MANITOBA_DRIVERS_LICENSE))

elif MANITOBA_DRIVERS_LICENSE == 'False':
    print("Invalid Drivers License.")
