money =0.0
maintaining =0.0

def getMaintainingMoney():
    global money
    global maintaining
    maintaining =float(input("How much is the maintaining balance(Choose from 100,000 to your {}): ".format(money)))
    if (maintaining < 100000):
        print("Invalid, the amount is less than 100000")
    elif (maintaining >=money):
        print("Invalid, the amount is greater than your starting amount", money)
    else:
        print("Successfully Maintain Money")

def getMoney():
    global money
    money= float(input("How much would you like to start with (Choose from  100,000 to 10,000,000)? "))
    if money > 10000000:
        print("Oops! Sorry that's too much!")
        getMoney()
    elif money < 100000:
        print("Oops! That's too little!")
        getMoney()
    else:
        print("Successfully Start Money")
        getMaintainingMoney()
getMoney()