caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def removeSpecials(message):
    #make a list of individual characters from message
    lettersOnly = ''
    for symbol in message:
        if symbol in caps:
            lettersOnly = lettersOnly+symbol
    # return the modified, letters-only message
    return lettersOnly

def vigenereEncrypt():
	message = input("What message would you like to encrypt? ")
	message = message.upper()
	key = input("What is your key? ")
	key = removeSpecials(key.upper())
	#print(message)
	#print(key)
	letters = list(message)
	keyLetters = list(key)
	text = ''
	#Loop to encrypt each letter
	for i in range (0,len(letters)):
		#print(i, ' ', letters[i], ' ', keyLetters[i%len(key)])
		#If the letter is in list of capitals, encode it
		letter = letters[i]
		if letter in list(caps):
			num = caps.index(letter)
			num = num+(caps.index(keyLetters[i%len(key)])+1)
			num = num%26
			letter = caps[num]
		text = text + letter
	#Printing cipher text
	print("Cipher Text: ", text)


vigenereEncrypt()
