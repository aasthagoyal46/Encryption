# Defining initial values of s1, s2, t1 and t2
s1 = 1
s2 = 0
t1 = 0
t2 = 1
a=1
b=1

#Function to read the input file
def readFile():
	global a
	global b
	file = open('input.txt', 'r')
	m = int(file.readline())
	g = int(file.readline())
	print(r1, ' ', r2)

	# Calling gcd function
	if(r1>=r2):
		a=r1
		b=r2
	else:
		a=r2
		b=r1
	extendedEucledean(g, m, s1, s2, t1, t2)
	file.close()

def extendedEucledean(r1, r2, s1, s2, t1, t2):
	global a
	global b
	
	q=r1//r2
	r=r1%r2
	s=s1-q*s2
	t=t1-q*t2
	print(q, ' ', r, ' ', s, ' ', t)
	# Iterate till remainder is not 0
	if(r>0):
		extendedEucledean(r2, r, s2, s, t2, t)
	else:
		print('u: ', s2, ' v:', t2)
		#print('GCD: ', a*s2+b*t2)

readFile()