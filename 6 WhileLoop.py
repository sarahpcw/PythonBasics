# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:58:00 2020

Task 
Read an integer N 
Constraints: 0 <= N <= 20

For all integers <= N, print n squared n * n

#Declare a list :  
#Ctrl + Fn + F11 or Fn + B or Fn + Ctrl + B on certain Lenovo laptops.


"""
# why: to repeat 

count = 0

print ( "hello world ", count)
count = count + 1  

print ( "hello world ", count) 
count = count + 1

print ( "hello world ", count) 
count = count + 1

print ( '---')
    #start value # control variable -- must have an initial value
count = 0 # start value
while count <= 50 :   #stop 
    print ("hello world ", count) 
    count = count + 1   # count += 1  # increment or step
print ("after the Loop " , count)

count = 50 
while count > 0 :
    print (count)
    count = count - 1   # count -= 1
print ('after the loop', count )
#
repeat = 'yes'
while repeat != 'no' : 
    # sell movie tickets
    repeat = input ('Repeat? yes/no ') 
print ('after the loop', repeat )    
#
if adults > 0 and pensioners  > 0 :
#
    
pw     = '123'
userpw = ''
count  = 0
## ask for a password, increment counter
while userpw != '123' and count < 3:
    userpw = input ( 'What is the password? ' )
    count  = count + 1 
    # you code here
    
if userpw != '123':
    print ( 'You are blocked' )
else: 
    print ( 'Correct, you may continue ' )


print 

pw     = '123'
userpw = ''
count  = 0

while count < 3 and userpw != pw :
   if count == 2 and userpw != pw :
        print ('You have 3 tries, this is your last chance')
   print ( 'You have tried ', count, 'times' )
   userpw = input ( 'what is the password ' )
   count  = count + 1 
    
if userpw != '123':
    print ( 'You are blocked' )
else: 
    print ( 'Correct, you may continue ' )
#    
    

"""   
ask the enduser for the password.
if he gets it wrong, then ask again, 
but not more than 3 times
"""


#
#N = input ("please enter a number between 0 and 20 " )
#N = int (N)
#
#count = 0
#while count  <= N : 
#    answer = count * count 
#    print ( count, 'count squared', answer )
#    count = count + 1
#
#print ( ' loop stopped ', count)
#
#
#
#    
#
##
##print ( ' loop stopped ', count)
#for count  in range (0,6, 3): #start stop step
#    print ( count )

