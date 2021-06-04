# lesson 1
for i in range( 0, 4, 1):  # Loop forward  from 0 to 3  , INcrement by 1 
    print (  i)
    # count = count + 1
print ("xxxxxx")

for value in range( 4, 11, 2 ):  # Loop forward  from 0 to 3  , INcrement by 1 
    print ( " hello world " , value)
    # i +=1
print ("xxxxxx")

for i in range( 3 ):      # the increment value 1 is omitted, and it defaults to 1
    print ( i  )
print ("xxxxxx")

for i in range( 3,6):  # Loop forward  from 0 to 3  , INcrement by 1 
    print ( " hello world " , i)
    # i +=1
print ("xxxxxx")
#
for i in range( 5 ):      # the start value 0 is omitted, and it defaults to 0
    print ( i  )
print ("xxxxxx")
#
#
for i in range( 50, -1, -1):      
    print ( i  )
print ("xxxxxx")
#
N = int(input("please enter a number between 0 and 20"))
count = 0 
for count in range (0, N, 1) :
    print ( 'The square of ', count, 'is ',  (count * count))




count = 0
while count < N :
     print ( 'The square of ', count, 'is ',  (count * count))
     count += 1



for i in range( 3):        # the increment value 1 is omitted, AND the start value 0 is omitted start defaults to 0
    try:
        print ( ' before divide' )
        number = 1/(3-i-1)
        print ( ' after divide' )
        # CODE
    except:
        print ( 'exception' , i, ( 3-i-1) )
    print ( i )
print ("xxxxxx")


movies = [  'bambi', 'rambo II', 'schrek' ]
print ( len(movies))
print ( len( movies[1]) )
movies.append('cinderella')
print ( movies)

for count in range (0, len( movies ) , 1) :
    print ( movies[count])




 
 

## lesson 2 , 2 examples: 
#for i in range( 0 , 3, 1 ): 
#    print ( i  )
#print ("xxxxxx")
#
#for i in range( 1 , 4, 1 ): 
#    print ( i  )
#print ("xxxxxx")
#
## lesson 3
#for i in range( 2,-1,-1):   # Loop backwords from 2 to 0 , DEcrement by 1
#    print ( i  )
#print ("xxxxxx")
#
#for i in range( 3,0,-1): # Loop backwords from 3 to 1 , decrement by 1
#    print ( i  )
#print ("xxxxxx")
#
#
