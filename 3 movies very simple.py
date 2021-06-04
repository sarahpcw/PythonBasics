# -*- coding: utf-8 -*-
"""

ask the end user which movie they would like to see?

How many adult tickets would they like to buy
How many children tickets would they like to buy
How many pensioners tickets would they like to buy

an adult ticket is 10 pounds
how much is the totalticketprice, 

Print the totalticketprice


"""
seats = 50
adults = c = p = 0

while seats >= 0:
    print ("available seats : " , seats)
    adults = int ( input( "How many adults want to buy a movie ticket? ")  ) # accepts the console input as string
    
    p = float ( input( "How many pensioners want to buy a movie ticket? ")  ) # accepts the console input as string
    
    c = float ( input( "How many children want to buy a movie ticket? ")  )  # accepts the console input as string
    
    price = 10.0
    ticketprice = ( adults * price) + ( c * price / 2  ) +  (  p * 0.3  ) 
    if seats -  (adults + p + c ) < 0:
        print ("moviehouse full")
    elif (adults + p + c ) > 10:
        print ("parties biggers than 10 not allowed")
    elif adults == 0 and p == 0 :
        print ("unaccompanied children not allowed")
    else:
        print ( "Ticket ordered: ",  adults, "Adults:", c, "Children:", p,  "Pensioners:" ) 
        print ( "Total Price:", ticketprice)
        seats = seats -  (adults + p + c )
      

print (seats)


