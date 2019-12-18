# Defining initial values for global variables
s1 = 1
s2 = 0
t1 = 0
t2 = 1
inv = 0
g = 1
p = 1

# Function to calculate multiplicative inverse - Used from previous assignments
def mulInverse(r1, r2, s1, s2, t1, t2):
	global inv
	global g
	global p

	q=r1//r2
	r=r1%r2
	s=s1-q*s2
	t=t1-q*t2
	# Iterate till remainder is not 0
	if(r>0):
		mulInverse(r2, r, s2, s, t2, t)
	else:
		#print('GCD ', g*s2+m*t2)
		if g*s2+p*t2 == 1:
			inv = s2%p	# As m*t2 %m(equals 0), so g*s2 %m = 1
			# print("D: ", d)
	return inv


#Function to calculate fast power - Used from previous assignments
def fastPower(P, x, A, B):
	Q = P
	R = [0, 0]
	while x > 0:
		if x%2 == 1:
			R = add(R, Q, A, B) 
		Q = add(Q, Q, A, B)
		x //= 2
	return R

# P+Q function
def add(P, Q, A, B):
	global g
	global p

	# Special case added for fast power to work
	if(P == [0, 0]):
		return Q

	# Tangent Case
	if(P==Q):
		g = 2*P[1]
		# Calculate slope of tangent
		m = (3*(P[0]**2 %p) + A)* mulInverse(g, p, s1, s2, t1, t2)
	else:
		g = Q[0]-P[0]
		# Calculate slope of line given 2 points
		m = (Q[1]-P[1])*mulInverse(g, p, s1, s2, t1, t2)
	# print("Slope: ", m)

	# Calculte Points
	x3 = ((m**2 % p) - P[0] - Q[0]) %p
	y3 = (m*(P[0]- x3) - P[1]) %p

	return [x3, y3]

# Multiply function
def multiply(a, P, A, B):
	# Use fast power to multiply
	R = fastPower(P, a, A, B)
	return R

# Function to check if point is valid or not
def check(x3, y3, A, B):
	global p
	if((y3**2 %p) == (((x3**3 %p) + A*x3 + B)) %p):
		print(True)
	else:
		print(False)

def xorbit(binary, key):
    ciphertext = ''
    for i in range(len(binary)): # run through the entire binary message
        # xor with corresponding place in the key.
        # the key position is mod the key length in case the message is somehow
        # longer than they key.
        ciphertext = ciphertext + str(int(binary[i])^int(key[i%len(key)]))
    return ciphertext

# Binary Jugler: Convert integer to binary
def int2bin(integer):
        binString=''
        while integer > 0:
                mod = integer % 2
                binString = str(mod)+binString
                integer //= 2

        while len(binString)%8 !=0:
                binString = '0' + binString
        return binString

# From binary Jugler: Convert binary to characters
def bin2msg(binary):
        return ''.join(chr(int(binary[(i*8):(i*8 + 8)],2)) for i in range(len(binary)//8))

#Function to read file
def read_file():
	global p
	file = open('ECCDHinput.txt', 'r')
	A = int(file.readline()) #Read the value of A
	B = int(file.readline()) #Read the value of B
	p = int(file.readline()) #Read the value of p
	G = file.readline() #Read the value of G
	X = file.readline() #Read the value of Alice's Shared key
	b = int(file.readline()) #Read the value of Bob's secret b
	C = file.readline() #Read the value of Ciper Text

	# Convert point G and X in array of integers
	G = list(map(int, G.split(", ")))
	X = list(map(int, X.split(", ")))

	# Calculate shared secret key
	K = multiply(b, X, A, B)

	# xor message with secret to calculate message
	message = xorbit(C, int2bin(K[0]))

	# Print the Decrypted message
	print(bin2msg(message))

read_file()
