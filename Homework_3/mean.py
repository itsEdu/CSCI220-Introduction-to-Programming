'''
Name: Eduardo Abreu
Problem: Write a Python program designed to output the
         RMS (root-mean-square) Average and the Harmonic Mean.
'''
import math

def parseRawLst(rawLst):
    lst = rawLst.split(",")
    newLst = []
    for numString in lst:
        newLst.append(int(numString))

    return newLst

def calcMean(lst):
    mean = 0
    for num in lst:
        mean += num
    mean = mean / len(lst)
    
    return mean

def calcRmsAverage(lst):
    mean = 0
    for num in lst:
        mean += num**2
    mean = mean / len(lst)
    rms = math.sqrt(mean)

    return rms

def calcHarmonicMean(lst):
    harmonicMean = 0
    for num in lst:
        harmonicMean += 1 / num
    harmonicMean = len(lst) / harmonicMean

    return harmonicMean

def main():
    lst = ""
    mean = 0
    rmsAverage = 0
    harmonicMean = 0
    
    rawLst = input("Please enter a list of numbers seperated by commas:\n")
    lst = parseRawLst(rawLst)
    mean = calcMean(lst)
    rmsAverage = calcRmsAverage(lst)
    harmonicMean = calcHarmonicMean(lst)

    print("\nMean: " + str(mean))
    print("RMS Average: " + str(rmsAverage))
    print("Harmonic Mean: " + str(harmonicMean))

main()
