print ( 'Hello world ')

#String Variables '\t' (tab)
name = "John"
surname = "Smith's Bookshop" 
print (name , surname)
print (name + surname)  # concatenate
print (name + '  ' + surname)  # concatenate
print (name + "\t\t\t" + surname)
print (name + '\n' + surname)
name=10
#
#
##More Printing
x = 'John'
print (x)
print (x)
print (x)
print (x, end=" ")
print (x, end=" ")
print (x, end=" ")
print (x)
print (x)
print (x, end=": ")
print (x, end="---")
print (x)
#
strVar = 'apple'
print (strVar[0])  
print (strVar[1])  
print (strVar[2])  
print (strVar[3])  
print (strVar[4])    
#         01234567890          
strVar = 'Hello World!'
print (strVar  )        # Prints complete string
print (strVar[0])       # Prints first character of the string
print (strVar[2:8])     # Prints characters starting from 
print (strVar[2:] )     # Prints string starting from 3rd character
print (strVar * 3)      # Prints string   times
print (strVar + "TEST") # Prints concatenated string
print (strVar[-1:]) 
print (strVar[-5:])  # Prints last five string
print (strVar[-5:-1]) 
print (strVar[-5:-2])    
#
#
name = 'John' 
print (name, type(name))
name = 10
print (name, type(name))
#### collect input from end-user
name = input ( 'What is your name ' )
print (name, type(name))
#moviename = "The Terminator 2"


# get user input
moviename = input ( 'Which movie would you like to see? ')
adults     = input ('How many adults? ')
children   = int( input ('How many children tickets would you like to buy? '))
pensioners = int (input ('How many pensioner tickets would you like to buy? '))
adults     = int(adults)
tp = 10 

print ('Movie name:', moviename)
print ('Ticket price:' , tp)
print ('Adults:', adults)
print ('Children:',children)
print ('Pensioners:', pensioners)

totalPrice = tp*adults + (tp/2*children ) + (tp/3*pensioners)
print ('Total Price', totalPrice)

### cast string input to numbers
adults = int ( adults )
children = int ( children )
pensioners = int (pensioners)
# calculations
price = 10
totalprice = ( int(adults) * price ) 
totalprice = totalprice + ( int(children) * price / 2 )
totalprice = totalprice  + ( int( pensioners) * price * 0.3) 
#### give output of results to the end user
print ("")
print (name)
print ("You have ordered:")
print ("Movie:", moviename)
print ("Number of adult tickets:", adults)
print ("Number of children tickets:", children)
print ("Number of pensioners tickets:", pensioners)
print ("Please pay:", totalprice )