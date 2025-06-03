"""Assignment 2."""

__author__ = "Ivan Estropigan"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Dev Team"

## SIMPLE DATA TYPES

# Variables
NAME = 'Ivan'
CURRENT_DRIVERS_LICENSE = True
current_year = 2025
GST = 0.05
PST = 0.07
vehicle_cost = 100000.00
final_vehicle_cost_with_tax = (0.05 + 0.07) * (vehicle_cost) + vehicle_cost
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = ['A', 'B', 'C']
combine_list = list + new_list


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

# Increase the current year by 1 and type
current_year += 1
print(f"next year: {current_year}", "type: ", type(current_year))

""" To store current year and increase by 1

Args:
current_year = 2025 variable
type(current_year) = int

Returns: 
next year: 2026 type: <class 'int'>
"""

# Calculate and add Without print(f"")
print("Purchase price: ", (vehicle_cost),
      "Provincial Tax:", PST, 
      "Federal Tax:", GST, 
      "Total:", (final_vehicle_cost_with_tax))

""" To calculate and print without using print(f"") how much is the gst and total vehicle cost.

Args:
GST = 0.05
PST 0.07
vehicle_cost = 100000
final_vehicle_cost_with_tax = (0.05 + 0.07) * (vehicle_cost) + vehicle_cost

Returns: Purchase price:  100000.0 Provincial Tax: 0.07 Federal Tax: 0.05 Total: 112000.0
"""

# Calculate and add format With print(f""":,.2f)
print(f"Purchase Price: ${vehicle_cost:,.2f}",
      f"Provincial Tax: ${PST:,.2f}",
      f"Federal Tax: ${GST:,.2f}",
      f"Total: ${final_vehicle_cost_with_tax:,.2f}")

""" To calculate and print using print(f"") to format the $ and decimal points

Args:
GST = 0.05
PST 0.07
vehicle_cost = 100000
final_vehicle_cost_with_tax = (0.05 + 0.07) * (vehicle_cost) + vehicle_cost

Returns: Purchase Price: $100,000.00 Provincial Tax: $0.07 Federal Tax: $0.05 Total: $112,000.00
"""

# Checking if list type list
print(type(list))

""" To check if the list I have created is a type of list

Args:
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Returns: <class 'list'>
"""

# Adding my first name
list.insert(5, 'Ivan')
print(list)

""" To add my first name in between 5 and 6 without re-defining.
Args:
list.insert(5, 'Ivan')

Returns: [1, 2 ,3, 4, 5, 'Ivan", 6, 7, 8, 9, 10]
"""

# Remove number 9 to the list
list.remove(9)
print(list)
""" To remove number 9 in the list and print to check
Args:
list.remove(9)

Returns: [1, 2 ,3, 4, 5, 'Ivan", 6, 7, 8, 10]
"""

# Combine both list and print
print(combine_list)
""" Combining both list and new list and print
Args:
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = ['A', 'B', 'C']

Returns: [1, 2 ,3, 4, 5, 6, 7, 8, 10, 'A', 'B', 'C']
"""