# For this script you will make use of for-loops and while-loops



# Using a for-loop print every number from 1-10 in ascending order
def ascending():
    for i in range(10):
        print(i+1)

# Using a while-loop print every number from 1-10 in descending order
def descending():
    i=10
    while(i>0):
        print(i)
        i-=1

# Using nested for-loops, print a basic multiplication table for number 1-10
def multiplcationTable():
    for i in range(11):
        for j in range(11):
            if(i==0):
                print(j, end = '\t')
            elif(j==0):
                print(i, end = '\t')
            else:
                print(i*j, end = '\t')
        print()

ascending()
descending()
multiplcationTable()
