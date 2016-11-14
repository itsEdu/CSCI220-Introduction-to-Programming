# Name: Eduardo R Abreu
# mean.py
#
# Problem: This program will calculate the mean, outputint the
# RMS Average and the Harmonic Mean. The user will input numbers. The
# Program will output the RMS average and the Harmonic Mean.
#
# Certification of Authenticity:  
# I certify that this lab is entirely my own work.

import math

def main():
    #Variables
    #Declared a list where the numbers will be stored
    sumNumbers = []

    #States what the program does
    print("This program finds the RMS Average and", end = " ")
    print("the Harmonic Mean of a list of numbers.\n")

    #Get the amount of times the loop will loop
    rangeOfLoop = eval(input("Length of the list of numbers: "))

    #Loop the adding of the numbers to the list
    for i in range(rangeOfLoop):
        
        #Input the numbers to be sumed into the list
        sumNumbers.append(eval(input("Give me a number: ")))

    #Using the math library take the square root of:
    #The sum of all integers in the list squared divided by
    #The amount of numbers in the list
    rmsAverage = math.sqrt(sum(i**2 for i in sumNumbers)/ rangeOfLoop)

    #Divide the amount of numbers in the list by
    #The sum of the ratios with denominators being each number in
    #The list of numbers
    harmonicMean = rangeOfLoop / sum(1 / i for i in sumNumbers)

    #Output the RMS Average and the Harmonic Mean
    print("\nThe RMS Average is: " + str(rmsAverage))
    print("The Harmonic Mean is: " + str(harmonicMean))
    
main()
