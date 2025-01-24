"""
This code is to
Convert normal text into a an encrypted text
Using the encryption code called caesar cipher
"""

# Data
alp = 'abcdefghijklmnopqrstuvwxyz'
cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
tempString = ""
encrypt = ""
decrypt = ""


# Receive the text from the user
# Receive the key from the user
userTxt = input("\nEnter your text : ")

userKey = input("Enter the key : ")

if userKey.isdigit() == True:
    userKey = int(userKey)

    # Encryption of the Caesar Cipher

    for i in userTxt:

        if i in alp:

            index = alp.find(i) + userKey

            if index >= 26:

                while index >= 26:
                    index = index - 26
                character = alp[index]
                tempString += character
                encrypt += character

            else:
                index = alp.find(i) + userKey
                character = alp[index]
                tempString += character
                encrypt += character

        elif i in cap:
            index = cap.find(i) + userKey

            if index >= 26:

                while index >= 26:
                    index = index - 26
                character = cap[index]
                tempString += character
                encrypt += character

            else:
                index = cap.find(i) + userKey
                character = cap[index]
                tempString += character
                encrypt += character

        else:
            tempString += i
            encrypt += i

    # Decryption of the caesar cipher

    for i in tempString:

        if i in alp:

            position = alp.find(i) - userKey

            if position <= 0:

                while position < 0:
                    position = position + 26
                newpos = alp[position]
                decrypt += newpos
            else:
                position = alp.find(i) - userKey
                newpos = alp[position]
                decrypt += newpos

        elif i in cap:
            position = cap.find(i) - userKey

            if position < 0:

                while position < 0:
                    position = position + 26
                newpos = cap[position]
                decrypt += newpos

            else:
                index = cap.find(i) + userKey
                character = cap[position]
                tempString += character
                decrypt += character

        else:
            decrypt += i

    # Printing the encryption
    print("\n---------Encryption------------")
    print(encrypt)

    # Printing the decryption
    print("\n---------Decryption------------")
    print(decrypt)

else:
    print("\nOh so you are here for the every method of decryption possible. ")
    print("In the Caesar Cipher there are 26 possible encryption for each alphabet available. ")

    # Data
    userKey = 1

    print()

    while userKey < 26:
        for i in userTxt:

            if i in alp:

                if alp.find(i) + userKey < 0:
                    position = alp.find(i) - userKey + 26
                    newpos = alp[position]
                    decrypt += newpos
                else:
                    position = alp.find(i) - userKey
                    newpos = alp[position]
                    decrypt += newpos

            elif i in cap:

                if cap.find(i) + userKey < 0:
                    position = cap.find(i) - userKey + 26
                    newpos = cap[position]
                    decrypt += newpos
                else:
                    position = cap.find(i) - userKey
                    newpos = cap[position]
                    decrypt += newpos

            else:
                decrypt += i

        print("Key : {}, {}".format(userKey, decrypt))
        decrypt = ""
        userKey += 1