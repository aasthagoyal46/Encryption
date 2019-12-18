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

#Function to read file
def read_file():
	global p
	file = open('input.txt', 'r')
	A = int(file.readline()) #Read the value of A
	B = int(file.readline()) #Read the value of B
	p = int(file.readline()) #Read the value of p
	P = file.readline() #Read the value of P
	x = file.readline() #Read the value of P

	# Convert point P in array of integers
	P = list(map(int, P.split(", ")))
	if(',' in x):
		# Convert point Q in array of integers
		Q = list(map(int, x.split(", ")))
		# Call add function if Q in input
		R = add(P, Q, A, B)
		
	else:
		a = int(x)
		# Call add function if Q not in input
		R = multiply(a, P, A, B)
	print("Point: ", R)
	check(R[0], R[1], A, B)


# P+Q function
def add(P, Q, A, B):
	global g
	global p

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

def multiply(a, P, A, B):
	R = fastPower(P, a, A, B)
	return R

def check(x3, y3, A, B):
	if((y3**2 %p) == (((x3**3 %p) + A*x3 + B)) %p):
		print(True)
	else:
		print(False)

read_file()
