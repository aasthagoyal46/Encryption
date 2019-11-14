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

#Function to read file
def flt():
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
	# Fermats little theorem a^(p-1) mod(p) = 1 checked 98 times.
	# If it is true for all values then assume it is prime.
	for a in range(2,100):
		if fastPower(a, p-1, p) != 1:
			return False;
	return True;

flt()
