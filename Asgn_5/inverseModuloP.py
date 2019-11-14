def readFile():
	file = open('input.txt', 'r')
	p = int(file.readline()) #prime number
	g = int(file.readline()) #number who's inverse modulo is to be found
	#print(p, ' ', g)

        # Calling a function to calculate the inverse modulus
        # Passing p-2 to calculate g**(p-2) %p
	inverse = calcInverse(g, p-2, p)
	print(inverse)

	file.close()
	
# Function to calculate inverse modulus
def calcInverse(g, x, p):
        #Flag to check if first cycle or not
	count = 0
	inverse = 1
	#loop till we get 0
	while (x/2>0):
                # For 2**0, take g%p 
		if(count==0):
			g = g%p
		else:
			g = g**2 % p
		if(x%2==1):     # Multiply in inverse only if remainder 1
			inverse*=g
			inverse%=p
		#print('2^', count, ' ', x%2, ' ', g, ' ', inverse)
		# Update x for next iteration
		x//=2
		count+=1
		
	return inverse
readFile()
