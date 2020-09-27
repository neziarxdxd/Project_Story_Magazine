money =0.0
maintaining =0.0
target = 0
day =0

def gameMenu():
	global day
	global target
	global money
	
	day = day+1 #added day
	if money>=target:
		print("You Win")
	else:
		


def getTargetMoney():
	global target
	global money
	
	target= float(input("How much is your target amount (>=starting amount)? "))
    if target < money:
      print("Invalid, the amount is less than your starting amount", starting)
      getTargetMoney()
    else:
      print ("Succesfully get Target Money")
      


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
