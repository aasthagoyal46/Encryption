caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers = caps.lower()

# Read text from input file
def OTP():
	#Open input file
    file = open('input.txt','r')
    #Read Key from file
    key = file.readline()
    #Get a list of key values
    key = key.split()
    #Read input text
    inputText = file.readline()
    print("Input text: ", inputText)
    #Close input file
    file.close()
    if(isEnglish(inputText)):
    	#Encrypt and write in encryption.txt
    	file = open('encryption.txt','w')
    	file.write(encrypt(inputText, key))
    else:
    	#Decrypt and write in decryption.txt
    	file = open('decryption.txt','w')
    	file.write(decrypt(inputText, key))
    file.close()
  
# Load a list of valid words in english  
def loadDictionary():
	#Open dictionary file
    dictionary = open('dictionary.txt','r')
    
    #Read the list of words 
    wordList = (dictionary.read().split('\n'))[:-1]

    #Close dictionary file
    dictionary.close()
    return wordList

# Remove special characters from the message
def removeSpecials(message):
    # Make letters variable containing A-Z, a-z, space, \t and \n
    letters = caps + ' \t\n'

    lettersOnly = ''
    for symbol in message:
    # Keep the charachters that are in letters variable
        if symbol in letters:
            lettersOnly = lettersOnly + symbol
    # Return the modified, letters-only message
    return lettersOnly

# Calculate the perectage of english words to total blocks of letters
def wordRatio(message):
    WORDS = loadDictionary()
    
    # Convert the message to all caps and remove the special characters
    message = message.upper()
    message = removeSpecials(message)
    
    # Record all groups of letters separated by spaces
    possibleWords = message.split()
    
    # If there are no possible words, then we can end this function and return 0
    if possibleWords == []:
        return 0.0

    # Count possibleWords that are found in the dictionary and save it in the variable matches
    matches = 0
    for word in possibleWords:
        if word in WORDS:
            matches = matches + 1
            
    # Return a ratio of actual words to possible words
    return float(matches) / len(possibleWords)

def isEnglish(message):
    if wordRatio(message) >= 0.3:
        return True
    else:
        return False

def decrypt(message, key):
	letters = list(message)
	text = ''
	#Maintain a key Index separately
	keyIndex=0
	for i in range(0,len(letters)):
		letter = letters[i] 
		if letter in lowers:
			num = lowers.index(letter)
			num = num-int(key[keyIndex])
			num = num%26
			letter = lowers[num]
			#Increment key index if letter in lower or caps
			keyIndex+=1
		elif letter in caps:
			num = caps.index(letter)
			num = num-int(key[keyIndex])
			num = num%26
			letter = caps[num]
			#Increment key index if letter in lower or caps
			keyIndex+=1
		# Build the new text with moved letters
		text = text+letter
	print(text)
	return text

def encrypt(message, key):
	letters = list(message)
	text = ''
	#Maintain a key Index separately
	keyIndex=0
	for i in range(0,len(letters)):
		letter = letters[i] 
		if letter in lowers:
			num = lowers.index(letter)
			num = num+int(key[keyIndex])
			num = num%26
			letter = lowers[num]
			#Increment key index if letter in lower or caps
			keyIndex+=1
		elif letter in caps:
			num = caps.index(letter)
			num = num+int(key[keyIndex])
			num = num%26
			letter = caps[num]
			#Increment key index if letter in lower or caps
			keyIndex+=1
		# Build the new text with moved letters
		text = text+letter
	print(text)
	return text

OTP()