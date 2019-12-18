# For this script I want you to prompt for user input, and put that information to use

# First you will prompt the user for their favorite number
favNum = input("What's your favourite number? ")

# Python interprets all user input as STRINGs, meaning if you want to do any math with input numbers,
# you will need to first convert that input into a number using either "int()" like we did in class,
# or by using "float()" which does the same thing, but also preserves decimal values if necessary
favNum = int(favNum)
# Next you will need to use a conditional statement (if statement) to identify if
# the user input is odd or even
if(favNum%2==0):
    print(favNum, 'is even')
else:
    print(favNum, 'is odd')

# Finally, print a message telling the user which (odd or even) their favorite number is

