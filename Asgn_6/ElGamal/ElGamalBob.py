#Function to read file
def readFile():
	file = open('ElGamalInput.txt', 'r')
	p = int(file.readline()) #prime number
	g = int(file.readline()) 
	A = int(file.readline())
	a = int(file.readline())

	file.close()
	bob(p, g, A, a)


def writeFile(p, g, a, C1, C2):
	f = open("alice.txt", "w")
	f.write(str(p)+'\n')
	f.write(str(g)+'\n')
	f.write(str(a)+'\n')
	f.write(str(C1)+'\n')
	f.write(str(C2)+'\n')
	f.close()

def bob(p, g, A, a):
	r = 9
	M = 37

	C1 = g**r
	C2 = M * (A**r)

	writeFile(p, g, a, C1, C2)

readFile()