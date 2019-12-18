# For this script you will read lines from "input.txt"
# If we refer to lines 1,2,3, and 4 as a,b,c, and d respectively
# then you will calculate and print (a*b) + (c*d)


def readFile():
    file = open("input.txt","r")
    a = int(file.readline())
    b = int(file.readline())
    c = int(file.readline())
    d = int(file.readline())
    file.close()
    print('Values of a,b,c and d are: ', a,b,c,d)
    print('Outcome(a*b + c*d): ',a*b + c*d)

readFile()
