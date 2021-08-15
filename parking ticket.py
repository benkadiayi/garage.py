class Parking_garage:
    def __init__(self):
        self.ticket = [1,1,1,1,1]
        self.parkingSpaces = [0,0,0,0,0]
        self.dict = {"currentTicket":"paid"}
        self.dict = False
    def takeTicket(self):
        print(f"there is {len(self.ticket)} spots. ")
        prompt = "Would you like to get a ticket? (yes/no)"
        answer = input(prompt)
        if answer == "yes":
            self.ticket.pop()
            self.parkingSpaces.pop()
            print(f"there is {len(self.ticket)} spots. ")
        if answer == "no":
            print("Thank you. have a nice day.")

    def payForParking(self):
        prompt = "You own 10$."
        prompt += "Type the amount (10) to pay."
        amount = input(prompt)
        if amount == "10":
            self.dict = True
    def leaveGarage(self):
        if self.dict == True:
            print('Thank you, have a nice day.')
            self.ticket.append(1)
            self.parkingSpaces.pop(0)
        



Parking_garage().takeTicket()
Parking_garage().takeTicket()
# Parking_garage().payForParking()
Parking_garage().leaveGarage()

