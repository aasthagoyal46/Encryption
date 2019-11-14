lowers = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Read from file, check if binary or nor and print mesage accordingly
def binReadWrite():
	message = readFile()
	if(checkBinary(message)):
		# Converting to alphabet if message binary
		print(binToAlpha(message))
	else:
		# Converting to binary if message alphabet
		print(alphaToBin(message))

# Function to read the message from file	
def readFile():
	file = open('input.txt', 'r')
	text = file.readline()
	# Print the input text read from input file
	print(text)
	file.close()
	return text

# Fuction to check if the text is binary
def checkBinary(text):
	# Loop all characters in input text and return true if they are 0, 1 or spaces
	for char in list(text)[:-1]:
		if(char!='1' and char!='0' and char!=' '):
			# Return false if char other than 0, 1 and  space
			return False
	return True

# Function to convert binary to decimal
def binToDec(binary):
	dec=0
	for i in range(0,len(binary)):
		dec+=int(binary[i])*(2**(len(binary)-i-1))
	return dec

# Function to convert binary message to Alphabet
def binToAlpha(message):
	print('Converting Binary to Alphabet')
	i=0
	text=''
	# Used while loop to increment i by different amounts
	while(i<len(message)):
		if(message[i]!=' '):
			# Space = 0b00100000
			if(message[i:i+8]=='sb00100000'):
				text+=' '
			elif(message[i:i+3]=='010'):
				text+=caps[binToDec(message[i+3:i+8])-1]
			elif(message[i:i+3]=='011'):
				text+=lowers[binToDec(message[i+3:i+8])-1]
			i+=8
		else:
			i+=1
	return text

# Function to convert alphabet message to binary
def alphaToBin(message):
	print('Convert Alphabet to Binary')
	binary=''
	for letter in message:
		if(letter in caps):
			binary += '010'
			# Find the position of letter in caps, replace 0b from bin() and left pad with 0s
			binary += (bin(caps.find(letter)+1).replace("0b",'')).zfill(5)
		elif(letter in lowers):
			binary += '011'
			# Find the position of letter in lowers, replace 0b from bin() and left pad with 0s
			binary += (bin(lowers.find(letter)+1).replace("0b",'')).zfill(5)
		elif(letter == ' '):
			binary += '00100000'
		binary += ' '
	return(binary)

#Call function
binReadWrite()