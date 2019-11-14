# Defining initial values of s1, s2, t1 and t2
s1 = 1
s2 = 0
t1 = 0
t2 = 1
g=1
m=1

#Function to read the input file
def readFile():
	global g
	global m
	file = open('input.txt', 'r')
	m = int(file.readline())
	g = int(file.readline())
	
	# Calling gcd function
	exEucledean(g, m, s1, s2, t1, t2)
	file.close()

def exEucledean(r1, r2, s1, s2, t1, t2):
	global g
	global m
	
	q=r1//r2
	r=r1%r2
	s=s1-q*s2
	t=t1-q*t2
	# Iterate till remainder is not 0
	if(r>0):
		exEucledean(r2, r, s2, s, t2, t)
	else:
		#print('GCD ', a*s2+b*t2)
		if g*s2+m*t2 == 1:
			inv = s2%m
			print('Multiplicative Inverse ', inv)
			print(inv*g %m)

readFile()