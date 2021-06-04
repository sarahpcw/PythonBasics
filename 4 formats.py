##More Printing
#
#x = 'John'
##print (x)
##print (x)
##print (x)
##print (x, end=" ")
##print (x, end=" ")
##print (x, end=" ")
##print ( x)
##print( x)
#
#### =============================================================================
##print (x)
##print ('\n') 
##print ( x)
#print (x,  'smith')
#print (x, '\t', 'smith')
#print (x, '\t',  'smith' )
##
##
##print ( "----")
## #left justification to create columns ( try .rjust() in your own time )
a ='apple'
p ='pear'
w ='watermelon'
b ='pomegranate'
print (a , "\t\t", p) 
print (w , "\t\t", b) 
## print ( "----")

lengtha = len(a)
lengthp = len(p)
lengthw = len(w)
lengthb = len(b)

longest = 0
if longest < lengtha :
     longest = lengtha
if longest < lengthp :
     longest = lengthp
if longest < lengthw :
     longest = lengthw
if longest < lengthb :
     longest = lengthb
print (longest)

print  ( w.ljust(longest),  a.ljust(longest) ) 
print  ( b.ljust(longest),  p.ljust(longest) ) 

print  ( w.rjust(longest),  a.ljust(longest) ) 
print  ( b.rjust(longest),  p.ljust(longest) ) 
## =============================================================================
#
##
#print ( "----")
# % is used to format variables when printing
# the % symbol means: ignore the % and ignore the s see the %s and understand it as a place holder for a string variable 
# %s for strings
#$ %f for floating point variables , i.e.  #3.2f  will print 3 number with 2 decimals etc

###### %s for string variables
name = 'John'
print (name, p)
print ('Your name is %s' % (name ))
print ('your name is', name)
#
#print ( "----")
movie = 'The Wolf of Wall Street'
print(movie)
print ('You chose the movie %s' % (movie))
print ( 'Hi %s, you chose  the movie %s' % (name, movie))
print ( 'Hi', name,', you chose the movie', movie)
##
## print variable using placeholders and formatting codes 
## % indicates to print a formatted value in the place of the placeholder
## s for string variable and use f for floating point numbers and d for int
###### %f  for numbers
print ( "----")
t = int ( 7 ) 
t = t*7.2567
print ( 'Hi %s, for the movie %s, the price is $%.2f ' % (name, movie, t))
print ( 'Hi', name, ', for the movie',movie,', the price is $',t)

#print ( "----")
Ticketprice = 6.50
t = 2
print ( 'The ticket price:'.ljust(25), '$%5.2f' % ( Ticketprice) )
print ( 'The total ticket price:'.ljust(25), '$%5.2f' % (Ticketprice*t))       
#print ( 'The ticket price:'.ljust(25), '$%d' % ( Ticketprice) )
#print ( 'The number of tickets:'.ljust(25), ' %d' % ( t) )
print ( 'The number of tickets:'.ljust(25), ' %2.f' % ( t) )
#       

# HOMEWORK =============================================================================
# # Display :
# # The ticket price for ___  adults , ___ children and ___ pensioners will be ___
# =============================================================================
