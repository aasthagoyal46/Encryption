#Function to convert integer to binary string
def int2bin(num):
    binString = ''
    
    while num > 0:
        mod = num % 2
        binString = str(mod)+binString
        num //= 2

    return binString

#Function to calculate fast power
def fastPower(g, x, p):
	result = 1
	while x > 0:
		if x%2 == 1:
			result = result*g %p 
		g = g**2 %p
		x //= 2
	return result

#Function to read file
def readFile():
	file = open('alice.txt', 'r')
	p = int(file.readline()) #prime number
	g = int(file.readline()) 
	a = int(file.readline())
	C1 = int(file.readline())
	C2 = int(file.readline())

	file.close()
	alice(p, g, a, C1, C2)

def alice(p, g, a, C1, C2):
	M = C2 * (fastPower(fastPower(C1, a, p), p-2, p)) % p
	print(M)

readFile()