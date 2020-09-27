print("Welcome to Investmnt Game")
print("")
starting= float(input("How much would you like to start with (Choose from  100,000 to 10,000,000)? "))
if starting > 10000000:
  print("Oops! Sorry that's too much!")
elif starting < 100000:
  print("Oops! That's too little!")
else:
  maintaining =float(input("How much is the maintaining balance(Choose from 100,000 to your starting amount): "))
  if (maintaining < 100000):
    print("Invalid, the amount is less than 100000")
  elif (maintaining > starting):
    print("Invalid, the amount is greater than your starting amount", starting)
  else:
    target= float(input("How much is your target amount (>=starting amount)? "))
    if target < starting:
      print("Invalid, the amount is less than your starting amount", starting)
    else:
      print ("")

money = starting
estate = 0
day = 0
while money != target:
    day = day + 1
    print("Day ", day)
    print ("")
    print("Bank Savings: ", starting)
    print("Maintaning Balance: ", maintaining)
    print("Target Amount: ", target)
    print("")
    print("What would you like to do?")
    print(" 1. Buy real estate")
    print(" 2. Loan real estate")
    print(" 3. Sell real estate")
    print(" 4. Invest in gold")
    print(" 5. Sell gold")
    print(" 6. End the day")
    print(" 7. End the day x10")
    action=int(input("Enter the number of your choice: "))
    if action == 1:
      if starting>=4000000:
        money=starting - 4000000
        print("Congratulations, you just bought one unit of real estate. You have ", money," left in your bank.")
      else:
        print("Sorry you do not have enough money, you must have more than 4000000 in  your bank to avail this option")
    elif action==2:
      if starting<2000000:
        print("Oopss, you do not have enough money. This option requires the player to have money more than 2,000,000")
      elif estate!=0:
        print("Oopss! This option is not applicable to you anymorer because you are already paying loaned real estate.")
      else: 
        estate=0
        money=starting - 2000000
        estate=estate+1
        print("Congratulations! You just loaned a  real estate. You have ", money, " left in your bank.")
    elif action==3:
      if estate<1:
        print("Sorry you cannot choose this action. You do not have at least one unit of real estate to sell.")
      else:
        estate= estate-1
        money= starting + 2000000
        print("Congratulations, you just sell one unit of real estate for 2,000,000.")
        print("You have ", money, " left in your bank.")
    elif action==4:
      if money >= 400000:
        goldowned=int(input("How many gold bar would you like to buy? "))
        goldprice=goldowned*100000
        money= money- goldprice
        print("Congratulations! You just bought ", goldowned, "gold bar/s for ", goldprice, ". You have ", money, " left in your bank")
      else:
        print("Oops, you cannot avail this choice. You must have at least 400,000 in your bank")
    elif action==5 and goldowned>0:
      print("You have ", goldowned," gold bar/s owned. ")
      goldsell=int(input("How many gold bar/s would you like to sell?"))
      if goldsell<=goldowned:
        goldprice=goldsell*75000
        print("Congratulations! You just sold ", goldsell, " for ", goldprice)
        money= money+goldprice
        print("You have ", money," left in your bank.")
      else:
        print("Sorry, you cannot avail this choice. You do not have this much number of gold  bar owned.")
    elif action==6:
      print("You just ended the day.")
    else:
      print("Choose a number from choices above!")

print("Hello World")
