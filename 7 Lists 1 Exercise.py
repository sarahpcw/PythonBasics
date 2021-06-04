# -*- coding: utf-8 -*-
"""
list: l = ['','','']
tuple: cannot change t = ('','','')
Set : unordered , unique values
set() method is used to convert any 
of the iterable to sequence of iterable elements with dintinct elements, commonly called Set

"""

name = 'john'
i = 0 
count = 0



days = ['mon','tue', 'wed','thu', 'fri', 'sat','sun']
print ( days[0])
print ( days )



daysset = set(days)

print (daysset) # removes thursday but scrambles the order

# use list functios to correct the list to show all the days of the week

