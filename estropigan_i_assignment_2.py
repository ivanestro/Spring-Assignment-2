"""Assignment 2."""

__author__ = "Ivan Estropigan"
__version__ = "1.0.0"
__credits__ = "COMP-1327 Dev Team, w3school, peps.python.org, "

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
test_tuple = ('MB', "AB", "SK", "BC")
dictionary = {'nickle': 0.05,
              'dime': 0.10,
              'quarter': 0.25}
store_set = {2, 4, 6, 8, 10, 12, 14 ,16, 18 ,20}
store_new_set = {5, 10, 15, 20}


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
""" Check if they have a valid driver's license.

Args:
CURRENT_MANITOBA_DRIVERS_LICENS = True
convert the type from str to boolean
type should return as boolean

Returns: 
Do you have Drivers License? [True] or [False] 
If True has license: True type:  <class 'bool'>
If False: Invalid Drivers License.
"""

# Print current year of 2025 and type
print(f"this year: {current_year}", "type: ", type(current_year))

""" Store current year, print it to the system and get the datatype

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

""" Calculate and print without using print(f"")

Args:
GST = 0.05 Constant name and fixed number manitoba's tax
PST 0.07 Constant name and a fixed number for manitoba's tax
vehicle_cost = 100000 The cost of vehicle can change regarding the assignment
final_vehicle_cost_with_tax = (0.05 + 0.07) * (vehicle_cost) + vehicle_cost

Returns: Purchase price:  100000.0 Provincial Tax: 0.07 Federal Tax: 0.05 Total: 112000.0
"""

# Calculate and add format With print(f""":,.2f)
print(f"Purchase Price: ${vehicle_cost:,.2f}",
      f"Provincial Tax: ${PST:,.2f}",
      f"Federal Tax: ${GST:,.2f}",
      f"Total: ${final_vehicle_cost_with_tax:,.2f}")

""" Calculate and print using print(f"") to format the $ and decimal points

Args:
GST = 0.05 Constant name and fixed number manitoba's tax
PST 0.07 Constant name and a fixed number for manitoba's tax
vehicle_cost = 100000 The cost of vehicle can change regarding the assignment
final_vehicle_cost_with_tax = (0.05 + 0.07) * (vehicle_cost) + vehicle_cost

Returns: Purchase Price: $100,000.00 Provincial Tax: $0.07 Federal Tax: $0.05 Total: $112,000.00
"""

## LISTS

# Checking if list type list
print(type(list))

""" To check if the list I have created is a type of list and print(type(list))

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


## TUPLES

# Checking if it is a tuple
print(type(test_tuple))
""" Creating test_tuple and checking if it is a tuple data type
Args:
test_tuple = ('MB', 'AB', 'SK', 'BC')

Returns: <class 'tuple'>
"""

# printing contents of tuple
print(test_tuple)
""" Printing the tuples variable contents
Args:
test_tuple = ('MB', 'AB', 'SK', 'BC')

Returns: ('MB', 'AB', 'SK', 'BC')
"""

## DICTIONARY

# Checking if it is a dictionary
print(type(dictionary))
""" Checking to see if it is a type referring to dictionary.
Args:
dictionary = {'nickle': 0.05,
              'dime': 0.10,
              'quarter': 0.25}

Returns: <class 'dict'>
"""

# Modifying dictionary list by update
dictionary.update({'nickle': 5, 'dime':10, 'quarter': 25})
print(dictionary)
""" Updating the list to their desired values this will help less clutter of code.
Args:
dictionary.update({'nickle': 5, 'dime':10, 'quarter': 25})

Returns: dictionary.update({'nickle': 5, 'dime':10, 'quarter': 25})
"""

# Adding two items to dictionary
dictionary['Loonie'] = 100
dictionary['Toonie'] = 200
print(dictionary)
""" Adding two items loonie and toonie, setting values and printing it
Args:
dictionary['Loonie'] = 100
dictionary['Toonie'] = 200

Returns: {'nickle': 5, 'dime': 0.1, 'quarter': 0.25, 'Loonie': 100, 'Toonie': 200}
"""

## SETS

# Making sure type is: set
print(type(store_set))
""" printing what type is set
Args:
store_set = {2, 4, 6, 8, 10, 12, 14 ,16, 18 ,20} 

Returns: <class 'set'>
"""

# Verifying the contents of set
print(store_set)
""" printing the contents inside of the set
Args:
store_set = {2, 4, 6, 8, 10, 12, 14 ,16, 18 ,20} 

Returns: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
"""

# Added new set only multiple of 5's
print(store_new_set)
""" printing the new set of multiples of 5's
Args:
new_set = {5, 10, 15, 20}

Returns: {10, 20, 5, 15}
"""

# Combine both two sets
union = store_new_set.union(store_set)
print(union)
""" combining two sets and printing both sets in one line

Args:
union = store_new_set.union(store_set)

Returns: {2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20}
"""

# Both set have in common
both_set = store_set.intersection(store_new_set)
print(both_set)
""" Comparing both sets to see which ones are the same value if so print 

Args:
both_set = store_set.intersection(store_new_set)

Returns: {10, 20}
"""

# unique values of 2
both_set = store_set.difference(store_new_set)
print(both_set)
""" Compare both sets containing all elements and are different from the element by 2

Args:
both_set = store_set.difference(store_new_set)

Returns: {2, 4, 6, 8, 12, 14, 16, 18}
"""

# unique values of 5
both_set = store_new_set.difference(store_set)
print(both_set)
""" Compare both sets containing all elements and are different from the element by 5

Args:
both_set = store_new_set.difference(store_set)

Returns: {5, 15}
"""