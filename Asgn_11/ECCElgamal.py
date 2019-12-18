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

def int2msg(integer):
	return bin2msg(int2bin(integer))

def bin2msg(binary):
    return ''.join(chr(int(binary[(i*8):(i*8 + 8)],2)) for i in range(len(binary)//8))

def int2bin(integer):
    binString=''
    while integer > 0:
            mod = integer % 2
            binString = str(mod)+binString
            integer //= 2

    while len(binString)%8 !=0:
            binString = '0' + binString
    return binString


#Function to read file
def read_file():
	global p
	file = open('ECCElGamalinput.txt', 'r')
	A = int(file.readline()) #Read the value of A
	B = int(file.readline()) #Read the value of B
	p = int(file.readline()) #Read the value of p
	G = file.readline() #Read the value of G
	C1 = file.readline() #Read the value of C1
	C2 = file.readline() #Read the value of C2
	a = int(file.readline()) #Read the value of a

	# Convert point G and X in array of integers
	G = list(map(int, G.split(", ")))
	C1 = list(map(int, C1.split(", ")))
	C2 = list(map(int, C2.split(", ")))

	# Calculate a.C1
	aC1 = multiply(a, C1, A, B)
	aC1 = [aC1[0], -aC1[1]]

	M = add(C2, aC1, A, B)

	# Print the Decrypted message
	print(int2msg(M[0]))

read_file()
