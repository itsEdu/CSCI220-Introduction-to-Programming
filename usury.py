# Name: Eduardo R Abreu
# usury.py
#
# Problem: This program will give the user information on the loan he/she is taking out.
#          It will give information on the monthly payments.
#          The input will be the data from the user.
#          The output will be the calculated data from the program.
#
# Certification of Authenticity:  
# I certify that this lab is entirely my own work.

def main():
    #Tell the user what the program is about.
    print("Hi, I can help you figure out how much interest you will be paying on your loan.")

    #Get loan amount from user.
    principal = eval(input("\nLoan amount: "))

    #Get the number of months of the loan.
    months = eval(input("Number of months: "))

    #Get the interest.
    interest = eval(input("Interest rate: "))

    #Make all the calculations.
    rate = interest / 1200
    numeratorCalculation = (principal*(rate*(pow(1+rate,months))))
    denominatorCalculation = (pow(1+rate,months)-1)
    monthlyPayment = numeratorCalculation / denominatorCalculation
    
    totalAmountPaid = months * monthlyPayment
    totalInterestPaid = totalAmountPaid - principal

    #Output the information the user wants.
    print("\nThe total amount you will pay is: " + str(totalAmountPaid))
    print("The total amount of interest is: " + str(totalInterestPaid))
    print("Your monthly payment will be: " + str(monthlyPayment))
    
main()

    
    
