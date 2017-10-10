def parseFile(file):
    average = 0
    classAverage = 0
    weight = 0
    grade = 0
    count = 0
    
    for line in file:
        lineSplit = line.split()
        numbersList = lineSplit[2:]
        for i in range(0, len(numbersList), 2):
            weight = int(numbersList[i])
            grade = int(numbersList[i + 1])
            average += weight * grade
        average = average / 100
        print("{0} {1}\'s average: {2:.1f}".format(lineSplit[0], lineSplit[1], average))

        count += 1
        classAverage += average
    classAverage = classAverage / count
    print()
    print("Class average: {0:.1f}".format(classAverage))

def main():
    infile = input("What is the name of the file containing the grade data? ")
    file = open(infile, "r")
    parseFile(file)

main()
