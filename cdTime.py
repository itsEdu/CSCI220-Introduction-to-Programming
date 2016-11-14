# Name: Eduardo R Abreu
# cdTime.py
#
# Problem: This program will output the total time of a CD.
#
# Certification of Authenticity:  
# I certify that this lab is entirely my own work.

def cdTime():
    #Variables and constants.
    SEC_TO_MIN = 60
    MIN_TO_HOUR = 60
    totalMinutes = 0
    totalSeconds = 0
    calcMin = 0
    remSeconds = 0
    cdNumber = 0
    trackNumber = 0
    
    #States what the program does.
    print("This program outputs the total audio time in a cd.")

    #Asks for the amount of CDs.
    cdCount = eval(input("How many CDs are there? "))
    print()
    
    #Loop for amount of CDs.
    for i in range(cdCount):
        
        #Print number of CD.
        cdNumber = i + 1
        print("CD#: " + str(cdNumber))
        
        #Ask user for amount of tracks in one CD.
        trackCount = eval(input("Tracks in this CD? "))
        print()
        
        #Loop to total the minutes and seconds of each CD.
        for j in range(trackCount):

            #Print number of track.
            trackNumber = j + 1
            print("Track number " + str(trackNumber) + ":")
            
            #Get the minutes and seconds of the track.
            trackMin = eval(input("How many minutes in this track? "))
            trackSec = eval(input("How many seconds in this track? "))
            print()

            #Math for total minutes of CD.
            trackTotalMin = calcMin + trackMin
            trackTotalSec = remSeconds + trackSec

            #Math for the seconds of CD.
            remSeconds = trackTotalSec % SEC_TO_MIN
            calcMin = trackTotalMin + trackTotalSec // SEC_TO_MIN

        
        #Print total time of the CD.
        print("CD number " + str(cdNumber) + ":")
        print("Total time: " + str(calcMin) + " minutes", end = " ")
        print(" " + str(remSeconds) + " seconds")
        print()
              
        #Adds to the total minutes and seconds of the CDs.
        totalMinutes += calcMin
        totalSeconds += remSeconds

    #Math for the total of all CDs.
    hours = totalMinutes // MIN_TO_HOUR
    totalMinutes = totalMinutes % SEC_TO_MIN
    totalSeconds = totalSeconds % SEC_TO_MIN

    #Displays total time of all CDs.
    print("Total time of CDs: " + str(hours) +" hours", end = " ")
    print(str(totalMinutes) +" minutes " + str(totalSeconds), end = " ")
    print("seconds")
    
cdTime()
    
