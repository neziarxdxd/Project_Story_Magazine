money =0.0
maintaining =0.0
target = 0
day =1
gold = 0
loans=0
real_estate=0

# TODO: the end of the day


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
    global money, real_estate
    if money<2000000:
        print("Oopss, you do not have enough money. This option requires the player to have money more than 2,000,000")
        gameMenu()
    elif real_estate==0:
        print("Oopss! This option is not applicable to you anymorer because you are already paying loaned real estate.")
        gameMenu()
    else:        
        money=money - 2000000
        real_estate=+1
        print("Congratulations! You just loaned a  real estate. You have ", money, " left in your bank.")
        gameMenu()

        
def sellRealEstate():
    if estate<1:
        print("Sorry you cannot choose this action. You do not have at least one unit of real estate to sell.")
        gameMenu()
    else:
        global money, real_estate
        real_estate= real_estate-1
        money= money + 2000000
        print("Congratulations, you just sell one unit of real estate for 2,000,000.")
        print("You have ", money, " left in your bank.")
        gameMenu()
    
def investGold():
    global money, gold
    if money >= 400000:
        buy_gold=int(input("How many gold bar would you like to buy? "))
        gold+=buy_gold
        goldprice=buy_gold*100_000
        money= money- goldprice
        print("Congratulations! You just bought ", goldowned, "gold bar/s for ", goldprice, ". You have ", money, " left in your bank")
        gameMenu()
    else:
        print("Oops, you cannot avail this choice. You must have at least 400,000 in your bank")
        gameMenu()

        
def sellGold():
    global gold, money
    print("You have ", gold," gold bar/s owned. ")
    goldsell=int(input("How many gold bar/s would you like to sell?"))
    if goldsell<=gold:
        goldprice=goldsell*75_000
        print("Congratulations! You just sold ", goldsell, " for ", goldprice)
        money= money+goldprice
        gameMenu()
        print("You have ", money," left in your bank.")
    else:
        print("Sorry, you cannot avail this choice. You do not have this much number of gold  bar owned.")
        gameMenu()
def endTheDay():
    day+=1
    
def endDayTen():
    pass

def gameMenu():
    global day, maintaining, target,money
    
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
