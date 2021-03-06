class ATM:

    def __init__(self, balance, bank_name):
        self.withdaws_list = []
        self.balance = balance
        self.bank_name = bank_name


    # allowed papers: 100, 50, 10, 5, and rest of request
    def withdraw(self, request):
        print "Welcome to " + self.bank_name
        print "Current balance = " + str(self.balance)
        print "=================================="

        if request > self.balance:
            print "Can't give you all this money !!"
        elif request <= 0:
            print "More than zero plz!"
        else:
            self.process_request(request)


    def process_request(self, request):
        self.withdaws_list.append(request)
        self.balance -= request
        while request > 0:
            if request >= 100:
                print "give 100"
                request -= 100
            elif request >= 50:
                print "give 50"
                request -= 50
            elif request >= 10:
                print "give 10"
                request -= 10
            elif request >= 5:
                print "give 5"
                request -= 5
            else:
                print "give " + str(request)
                request -= request


    def show_withdrawals(self):
        print "****** Your withdrawals ******"
        for withdrawal in self.withdaws_list:
            print str(withdrawal)
        print "******************************"

balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(55)
atm1.withdraw(99)
atm1.withdraw(800)
atm1.show_withdrawals()

atm2.withdraw(100)
atm2.withdraw(2000)
atm2.show_withdrawals()
