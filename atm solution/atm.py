# allowed papers: 100, 50, 10, 5, and rest of request
balance = 500


def withdraw(balance, request):
    amount = request
    print "Current balance = " + str(balance)
    if request > balance:
        print "Can't give you all this money !!"
    elif request > 0:
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
        return balance - amount
    else:
        print "More than zero plz!"

    return balance


balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)
