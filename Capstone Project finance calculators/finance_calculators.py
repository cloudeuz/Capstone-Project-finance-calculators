#import math to use math functions
# user input chooses investment or bond
import math
choice = input(""" Choose either 'investment' or 'bond' from the menu below to proceed :

investment - to calculate amount of interest you'll earn on your investment
bond - to calculate amount you'll have to pay on a home loan

enter choice  here: """ )

# if user choice == investment ask more details store in variables to be used later
# then user input chooses simple or compound interest
# each option works out given interest with stored details and prints out total interest
if choice.lower() == "investment":
    money = float(input("Enter how much money are you depositing: "))
    rate = float(input("Enter your  interest rate %"))
    year = float(input("Enter years you plan on investing for: "))
    interest = input("Would you like 'simple' or 'compound' interest:  ")


    if interest == "simple":
        rate_fix = rate/100
        total = money*(1 + rate_fix*year)
        print(f"your total simple interest is ${total}")

    elif interest == "compound":
        rate_fix = rate / 100
        total = money*math.pow((1+rate_fix),year)
        print(f"your total compound interest is ${total}")

# if user choice == bond ask more details store in variables to be used later
# then monthly payment is worked out and printed
elif choice.lower() == "bond":
    value = float(input("Enter present value of your house. "))
    rate = float(input("Enter interest rate. "))
    month = float(input("Enter number of months you plan to take to repay the bond. "))
    rate_fix = rate / 100 / 12
    repay = (rate_fix*value)/(1 -(1-rate_fix)**month)
    print(f"Your monthly payment is ${repay}")