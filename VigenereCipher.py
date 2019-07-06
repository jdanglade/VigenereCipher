#Vigenere Cipher Implementation

def keyGen(strInput, key):
    key = list(key)
    if len(strInput) == len(key):
        return(key)
    else:
        for i in range(len(strInput) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encryptStr(strInput, key):
    cipher_text = []
    for i in range(len(strInput)):
        x = (ord(strInput[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def decryptStr(strInput, key):
    orig_text = []
    for i in range(len(strInput)):
        x = (ord(strInput[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)

def vigCipher():
    strInput = input("Please enter a word to encrypt ").upper()
    strInput = strInput.replace(" ", "")
    keyword = input("Please enter a keyword for the encryption ").upper()
    keyword = keyword.replace(" ", "")
    key = keyGen(strInput, keyword)
    cipher_text = encryptStr(strInput,key)
    print("Cipher Text :", cipher_text)
    print("Decrypted Text :",  decryptStr(cipher_text, key))

vigCipher()

