import os
passwd = "2007"
replace = False 
def formula(key):
    fkey=0
    list = [int(d) for d in str(key)]
    print(list)
    for i in range(len(list)):
        if i != (len(list) -1):
            fkey += list[i]
        else:
            fkey *= list[i] 
    final_key = fkey * ((-1)**list[2])
    return final_key;
def upperlimiter(ul): #ul = Key to be upper limited
    while ul > 126:   #When a key crosses 126, it subtracts the difference and adds it to 32
        ul = 33 + (ul-126)                                   
    return ul;

def lowerlimiter(ll): #ll = Key to be lower limited
    while ll < 33:
        ll = 126 - (33 - ll)
    return ll;        

def limiter(lim): #To choose which limiter should be used
    if lim > 126:
        lim = upperlimiter(lim)
    elif lim < 33:
        lim = lowerlimiter(lim)
    elif lim > 33 and lim < 127:
        lim = lim 
    return lim;
            
def encrypt(loc,key):
    try:
        f = open(loc,"r")
    except (FileNotFoundError):
        print("File can't be opened or doesn't exist")
    info = f.readlines()
    # print(info)
    f.close()
    #Encryptor
    '''1)Basically a 4 number key is used with the formula (+,+,*)
       2)Our range is from 32 to 126, inclusive
       3)Adding or subtracting will be decided by whether the third digit is odd(-) or even(+)
        '''
    #Final key for encyption   
    ekey = formula(key) 
    output = []
    for i in info:
        temp_output=""
        for j in i:
            if j != "\n" and ord(j) != 32:
                original = ord(j)
                encrypted = limiter(original + ekey)
                #print(ekey, encrypted)
                temp_output += chr(encrypted)
            elif j== "\n":
                temp_output += "\n"
            elif ord(j) == 32:
                temp_output += j
        output.extend(temp_output)
                
    # print(output)
    desktop = os.path.expanduser("~/Desktop")
    if replace == False: 
        out_loc = desktop + "\\encrypted.txt"
    elif replace == True: 
        out_loc = loc
    ff = open(out_loc,"w")
    ff.writelines(output)
    ff.close()
    

def decrypt(loc,key):
    try:
        f = open(loc,"r")
    except (FileNotFoundError):
        print("File can't be opened or doesn't exist")
    info = f.readlines()
    # print(info)
    f.close()
    #Decryptor
    #Final key for decyption   
    ekey = -(formula(key)) 
    output = []
    for i in info:
        temp_output=""
        for j in i:
            if j != "\n" and ord(j) != 32:
                original = ord(j)
                encrypted = limiter(original + ekey)
                #print(ekey, encrypted)
                temp_output += chr(encrypted)
            elif j== "\n":
                temp_output += "\n"
            elif ord(j) == 32:
                temp_output += j
        output.extend(temp_output)
    # print(output)
    desktop = os.path.expanduser("~/Desktop")
    if replace == False: 
        out_loc = desktop + "\\decrypted.txt"
    elif replace == True: 
        out_loc = loc
    ff = open(out_loc,"w")
    ff.writelines(output)
    ff.close()
    

            
    
if __name__ == "__main__":
    v = str(input("Enter password: "))
    if v == passwd:
        location = str(input("Enter location of file: "))
        key = int(input("Enter you file key(4 Digit, no 0's): "))
        method = str(input("Would you like to encrypt the file or decrypt it?(E/D): "))
        new = str(input("Would you like to replace the file or make a new file(Created on Desktop)?(R/N): "))
        if new == "R" or new == "r":
            replace = True
        if method == "E" or method =="e":
            if["0" not in str(key)]:
                encrypt(location,key)
        if method == "D" or method == "d":
            if["0" not in str(key)]:
                decrypt(location,key)
        
        

    
