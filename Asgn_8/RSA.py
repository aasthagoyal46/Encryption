#Binary Juggler functions
#Convert integer to binary
def int2bin(integer):
        binString=''
        while integer > 0:
                mod = integer % 2
                binString = str(mod)+binString
                integer //= 2

        while len(binString)%8 !=0:
                binString = '0' + binString
        return binString

#Convert binary to integer
def bin2int(binary):
        return int(binary,2)

#Convert string to binary
def msg2bin(message):
        return ''.join(['{0:08b}'.format(ord(x)) for x in message])

#Convert binary to string
def bin2msg(binary):
        return ''.join(chr(int(binary[(i*8):(i*8 + 8)],2)) for i in range(len(binary)//8))

#Convert string to integer
def msg2int(message):
        return bin2int(msg2bin(message))

#Convert integer to String
def int2msg(integer):
        return bin2msg(int2bin(integer))

#Function to calculate fast power
def fastPower(g, x, p):
	result = 1
	while x > 0:
		if x%2 == 1:
			result = result*g %p 
		g = g**2 %p
		x //= 2
	return result

# Defining initial values of s1, s2, t1 and t2
s1 = 1
s2 = 0
t1 = 0
t2 = 1
e=1
phi=1
d=0

#Multiplicative Inverse Calculator
def mulInverse(r1, r2, s1, s2, t1, t2):
	global e
	global phi
	global d

	q=r1//r2
	r=r1%r2
	s=s1-q*s2
	t=t1-q*t2
	# Iterate till remainder is not 0
	if(r>0):
		mulInverse(r2, r, s2, s, t2, t)
	else:
		# print('GCD ', e*s2+phi*t2)
		if e*s2+phi*t2 == 1:
			d = s2%phi	# As phi*t2 %phi(equals 0), so e*s2 %phi = 1
			# print("D: ", d)
	return d

#Function to read file
def rsa():
	global e
	global phi
	file = open('input.txt', 'r')
	p = int(file.readline()) #Read the value of p
	q = int(file.readline()) #Read the value of q
	e = int(file.readline()) #Read the value of e
	message = input("Enter your message: ") #Read user message

	N = p*q #Calculating the value of N
	phi = (p-1)*(q-1) #Calculating the value of phi
	d = mulInverse(e, phi, s1, s2, t1, t2) #Calculating multiplicative inverse of e mod phi
	
	crypt = rsa_encrypt(message, e, N) # Calculate encrypted message
	print("Encrypted: ", crypt) # Print Encrypted message
	decrypt = rsa_decrypt(crypt, d, N) # Decrypt Encrypted message

def rsa_encrypt(m, e, N):
	#Take a list to store encrypted message blocks
	crypt = []
	# Break the message in blocks of 10 and loop over each block
	i=0
	while i < len(m):	
		if(i+10 <= len(m)):
			message_block = msg2int(m[i:i+10])
		else:
			# Last block can be less than 10 chars
			message_block = msg2int(m[i:len(m)])
		i+=10
		c = fastPower(message_block, e , N)
		#Add encrypted message to crypt list
		crypt.append(c)
	return crypt	

def rsa_decrypt(crypt, d, N):
	# Variable to store decrypted message
	message = ''
	# Iterate over the list of cryted messages
	for c in crypt:
		m = fastPower(c,d,N)
		# Cobvert decrypted message to string an append to variable
		message += int2msg(m)
	print(message)

rsa()
