# Write a class Train which has methods to book a ticket , get status(no of seats) and get fare information of trains running under Indians Railway 

class Train :
    def __init__(self , name , fare , seats):
        self.name = name
        self.fare = fare
        self.seats = seats 

    def getStatus(self):
        print("************************")    
        print(f"The name of the train is {self.name}")    
        print(f"The seats available in the train is {self.seats}")    
        print("***************************")   

    def fareInfo(self):
        print(f"The price of the ticket is :Rs {self.fare}")     

    def bookTicket(self):
        if(self.seats > 0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats-1

        else:
            print("Sorry this train is full ! kindly try in tatkal ")


        def cancelTicket(self , seatNO):
            pass   

intercity = Train("Intercity Express :12331" , 90 ,3 )
intercity.getStatus()
intercity.bookTicket() # we book 1 seats
intercity.bookTicket()  # we book 2nd seats 
intercity.getStatus()
intercity.bookTicket()  # we book 3 rd seat

intercity.bookTicket() # now no seats is left , try tatkal


