# Ceasar Cipher
"""
Before writing the code, you should plan out the algorithm for encryption as follows:

    1. Take three arguments: the message, the cipherKey, and the alphabet.

    2. Initialize variables.

    3. Use a for loop to traverse each letter in the message.

    4. For a specific letter, find the position.

    5. For a specific letter
        5.1 Determine the new position given the cipher key.

        5.2 If current letter is IN the alphabet, append the new letter to the encrypted message.

        5.3 If current letter is not in the alphabet, append the current letter.

    6. Return the encrypted message after exhausting all the letters in the message.
"""
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getDoubleAlphabet(alphabet):
    return alphabet+alphabet

def getMessage():
    stringToEncrypt = input("Input your message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = int(input("Please enter a key (from 1 - 25): "))

    if shiftAmount <1 or shiftAmount > 25 :
        shiftAmount = 0
        
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    alphabet = alphabet.upper()
    #print(alphabet)
    #print(uppercaseMessage)
    for c in uppercaseMessage:
        position = alphabet.find(c)
        newPosition = position + int(cipherKey)
        #print(c, "at pos", position, "newpos ", newPosition)
        if c in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + c
        
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    return encryptMessage(message, -int(cipherKey), alphabet)

msg = getMessage()
cipher = getCipherKey()

encryptMsg = encryptMessage(msg, cipher, getDoubleAlphabet(ALPHABET))

print(encryptMsg)

print(decryptMessage(encryptMsg, cipher, getDoubleAlphabet(ALPHABET)))
