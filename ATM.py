class ATM:
    def __init__(self, cardnumber, pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber

    def cashWithDrawl(self):
        print("Enter card number: ", self.cardnumber)

    def balanceEnquiry(self):
        print("Enter pin number: ", self.pinnumber)

card = ATM("1234567890123456", "1234")
card.cashWithDrawl()
card.balanceEnquiry()

##class ATM:
##    def __init__(self, cardnumber, pin):
##        self.cardnumber = cardnumber
##        self.pin = pin
##
##    def 
