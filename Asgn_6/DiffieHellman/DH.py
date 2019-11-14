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
	file = open('input.txt', 'r')
	p = int(file.readline()) #prime number
	g = int(file.readline()) #number who's inverse modulo is to be found
	b = int(file.readline())
	A = int(file.readline())
	cipher = file.readline()
	
	# Calculate shared key as A**b %p
	key = fastPower(A, b, p)
	
	# Find the secret message
	plain = diffieHelman(cipher, int2bin(key))
	print(plain)

	file.close()

#Decrypt a cipher text using the shared key
def diffieHelman(cipher, key):
	#print(cipher)
	#print(key)
	plain=''
	for i in range(len(cipher)):
		if cipher[i]==key[i]:
			plain+='0'
		else:
			plain+='1'
	#print(plain)
	#Return the plain text
	return ''.join(chr(int(plain[(i*8):(i*8 + 8)],2)) for i in range(len(plain)//8))

readFile()