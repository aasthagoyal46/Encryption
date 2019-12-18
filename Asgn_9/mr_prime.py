import random
#Binary Juggler functions
#Convert binary to integer
def bin2int(binary):
        return int(binary,2)

#Convert string to binary
def msg2bin(message):
        return ''.join(['{0:08b}'.format(ord(x)) for x in message])

#Convert string to integer
def msg2int(message):
        return bin2int(msg2bin(message))

#Function to calculate fast power
def fastPower(g, x, p):
	result = 1
	while x > 0:
		if x%2 == 1:
			result = result*g %p 
		g = g**2 %p
		x //= 2
	return result

#Function to calculate gcd of 2 numbers
def gcd(a,b):
    if a<b:
        gcd(b,a)
    q = a//b
    r = a % b
    if r == 0:
    	return b
    else:
        return gcd(b,r)

#Function to read file
def prime():
	# Generate a number randomly
	p = generateP()
	# Check if it is prime, if not regenerate
	while(check(p)!=True):
		print("Checked: ", p)
		p = generateP()
	print("Generated prime: ", p)
	return p

def generateP():
	# Start and end with 1 to reduce time complexity wasted on number divisible by 2 or starting with 0
	prime = '1'
	# Take 510 random 0s and 1s
	for i in range(510):
		prime += str(random.randint(0,1))
	prime += '1'
	return bin2int(prime)

def check(p):
	# Check if number is even return false
	if(p%2 == 0):
		return False
	
	# Check primality by taking 100 values of a
	for a in range(2,102):
		flag = 0
		# Check that GCD of number is equal to 1
		if(gcd(a, p) != 1):
			return False
		k = 0
		q = p-1
		# Get the value of k and q
		while(q%2 == 0):
			k += 1
			q = q//2
		# Set a = a^q(mod(N))
		a = fastPower(a, q, p)
		# if a not 1 or -1
		if (a != 1 and a != p-1):
			# loop till k-1 to check if a is 1 or -1
			for _ in range(k):
				a = fastPower(a,2,p)
				if (a == p-1):
					flag = 1
					break
			if flag == 0:
				return False
	return True

prime()
