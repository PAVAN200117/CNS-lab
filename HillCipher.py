import numpy as np
 
def getSize(key):
    if(len(key)==4):
        return 2
    elif(len(key)==9):
        return 3
        
def getReshapedKey(key, size): 
    if(size == 2):
        return key.reshape(2,2)
    elif(size == 3):
        return key.reshape(3,3)
        
def encryption(pt, key):
     # loop to append extra characters
    while(len(pt)%size!=0):
        pt+="x"
    pt = np.array([(ord(a)-97) for a in pt])
    #splits the array into equal parts
    ptm = np.array_split(pt,len(pt)/size)
    ct = ""
    for a in ptm:
        a = a.reshape(size,1)
        encr = np.dot(keym,a)%26
        for a in np.nditer(encr):
            ct+=chr(a+97)
    
    return ct
    
def decryption(ct, key):
    adj = np.linalg.inv(keym)
    det = round(np.linalg.det(keym))
    adj = adj*det  # inverse*det = adjacent matrix
 
    #np.where() to add all the negative numbers 
    np.where(adj<0,adj+26,adj)
 
    # loop to find the inverse which is used to multiply with matrix
    x = 1
    while((det*x)%26!=1):
        x+=1
 
    final = (x*adj)%26 #final is the inverse matrix of the key
    enc = np.array([(ord(a)-97) for a in ct])
    encm = np.array_split(enc,len(enc)/size) #spliting it into equal sizes
    decrypt = ""
    for a in encm:
        a = a.reshape(size,1)
        decr = np.round_(np.dot(final,a))
        decr = decr.astype(int)
        decr = decr%26
        for a in np.nditer(decr):
            decrypt+=chr(a+97)
    
    return decrypt
    
 
pt = input("Enter the plain text ")
key = input("Enter the key ")
 
pt = pt.lower()
key = key.lower()
key = np.array([(ord(b)-48) for b in key]) #converting alphabets to ascii values
size = getSize(key)
keym = getReshapedKey(key, size)
 
cipher = encryption(pt, keym)
print("\nEncrypted text is: ", cipher)
 
decryptedText = decryption(cipher, keym)
print("\nDecrypted text is: ", decryptedText)
