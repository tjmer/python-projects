# Get teh loan details

money_owed = float(input("How much money do you owe, in dollars?: "))  #$50,000
apr = float(input("What is the annual percentage rate?: ")) #3%
payment = float(input("What will your monthly payment be, in dollars?: ")) #1,000
months = int(input("How many months do you want to see the results for?: ")) #24

# divide apr by 100 to make it a decimal, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
    # Add in interest
    interest_paid = money_owed * monthly_rate
    money_owed += interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break

        # Make payment
    money_owed -= payment

        # Print the results after this month

    print("Paid", payment, "of which", interest_paid, "was interest", end=' ')
    print("Now I owe", money_owed)