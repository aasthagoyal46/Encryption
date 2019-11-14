caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers = caps.lower()

# Read cipher text from input file
def readCipher():
	#Open input file
    encryptedFile = open('input.txt','r')
    #Read input cipher text
    inputText = encryptedFile.read()
    print("Cipher text: ", inputText)
    #Close input file
    encryptedFile.close()
    return inputText
  
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


def decrypt():
	message = readCipher()
	letters = list(message)
	
	# A flag variable to see if we found a solution of not
	flag = False

	#Brute force all 25 keys - 1 to 25
	for key in range(1,26):
		text = ''
		#Move the letters in text by the amount of key
		for letter in letters:
			if letter in lowers:
				num = lowers.index(letter)
				num = num+key
				num = num%26
				letter = lowers[num]
			elif letter in caps:
				num = caps.index(letter)
				num = num+key
				num = num%26
				letter = caps[num]
			# Build the new text with moved letters
			text = text+letter
		# Check if the text is in English
		if(isEnglish(text)):
			# Print all the possible plaint text
			print(text)
			# Set flag as true
			flag = True

	if(flag!=True):
			print("Can't find a solution with confidence: 0.3")

decrypt()
