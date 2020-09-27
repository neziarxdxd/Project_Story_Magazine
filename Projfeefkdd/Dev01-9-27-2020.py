money =0.0
maintaining =0.0
target = 0
day =0
gold = 0
loans=0
real_estate=0


def buyRealEstate():
    global money, real_estate
    if money>=4000000:
        money=money-4_000_000
        real_estate+=1
        print("Congratulations, you just bought one unit of real estate. You have ", money," left in your bank.")
        gameMenu()
      else:
        print("Sorry you do not have enough money, you must have more than 4000000 in  your bank to avail this option")
        gameMenu()
def loanRealEstate():
    pass
def sellRealEstate():
    pass
def investGold():
    pass
def sellGold():
    pass
def endTheDay():
    pass
def endDayTen():
    pass

def gameMenu():
    global day, maintaining, target,money
    day+=1
    print("Day",day)
    print("Bank Savings: ",money)
    print("Maintaining Balance: ",maintaining)
    print("Target Amount: ",target)
    print("")
    print(''''
    STATUS
===========================
GOLD: {gold}
REAL ESTATE: {real_estate}
LOAN ESTATE: {loans}

===========================

    '''.format(gold=gold,real_estate=real_estate,loans=loans))
    print("What would you like to do?")
    print(" 1. Buy real estate")
    print(" 2. Loan real estate")
    print(" 3. Sell real estate")
    print(" 4. Invest in gold")
    print(" 5. Sell gold")
    print(" 6. End the day")
    print(" 7. End the day x10")
    choice = input("Enter the number of your choice: ")
    if choice not in ["1","2","3","4","5","6","7"]:
        print("Invalid Choices")
        gameMenu()
    else:
        if choice == "1": buyRealEstate()
        if choice == "2": loanRealEstate()
        if choice == "3": sellRealEstate()
        if choice == "4": investGold()
        if choice == "5": sellGold()
        if choice == "6": endTheDay()
        if choice == "7": endDayTen()
        
            
    


def getTargetMoney():
    global target
    global money
	
    target= float(input("How much is your target amount (>=starting amount)? "))
    if target < money:
        print("Invalid, the amount is less than your starting amount", money)
        getTargetMoney()
    else:
        print ("Succesfully get Target Money")
        gameMenu()
      


def getMaintainingMoney():
    global money
    global maintaining
    maintaining =float(input("How much is the maintaining balance(Choose from 100,000 to your {}): ".format(money)))
    if (maintaining < 100000):
        print("Invalid, the amount is less than 100000")
        getMaintainingMoney()
    elif (maintaining >=money):
        print("Invalid, the amount is greater than your starting amount", money)
        getMaintainingMoney()
    else:    	
        print("Successfully Maintain Money")  
        getTargetMoney()
          

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
