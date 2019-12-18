import random
import mysql.connector
import hashlib

# string of characters to be used in salt and pepper generation
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

# function to generate a random string of variable length
def randomString(length):
    # loop till the length and join one of the random chars in every iteration
    return ''.join(random.choice(chars) for i in range(length))

# function to connect to database
def connectToDb():
    # using mysql connector to connect to my database
    conn = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='applied_encryption')
    return conn

# function to close the connection with db
def closeConnection(conn):
    conn.close()

# function to check whether the password is correct for a user
def checkPassword(conn, userid, newpass):
    cursor = conn.cursor()

    # Query to get the salt and password corresponding to a user
    query = ("SELECT salt, password FROM Users where userid = %s")
    # Parameters to be passed in that query
    values = (userid, )

    cursor.execute(query, values)

    for (salt, password) in cursor:
    	# Call verification function on entered password
        if(verify(newpass, salt, password)):
        	print("Authenticated")
        else:
        	print("Invalid User id or Password")

    cursor.close()

# Function to add a user
def addUser(conn, userid, password):
    cursor = conn.cursor()

    # Generate a random salt to be saved in databse
    salt = randomString(64)
    # Generate a random pepper that is not stored anywhere.
    # Here we have taken the pepper of length one for simplicity
    pepper = randomString(1)
    # Generate hashed password to be saved in database
    dbpass = encrypt(password, salt, pepper)

    # Query to insert a new row in the database
    query = "INSERT INTO Users (userid, salt, password) VALUES (%s, %s, %s)"
    # Parameter for the insert query
    values = (userid, salt, dbpass)

    cursor.execute(query, values)

    conn.commit()
    cursor.close()

# Function to generate the hashed password using sha256
def encrypt(password, salt, pepper):
	# Use hashlib library to generate hash
	# Concatenate password with salt and pepper to make it difficult to crack
    h = hashlib.sha256((salt+password+pepper).encode())
    return h.hexdigest()

# Function to verify if the entered password is same as the saved password
def verify(password, salt, dbpass):
	# Brute force to generate pepper
	for char in chars:
		# For every pepper, check if hash matches the saved password hash
	    if(dbpass == encrypt(password, salt, char)):
	        return True;
	return False;

conn = connectToDb();

# addUser(conn, "aastha", "password")
checkPassword(conn, "aastha", "password")

closeConnection(conn)
