import random
import os
import sys
from cryptography.fernet import Fernet

if len(sys.argv) > 1:
    if sys.argv[1] == "add":
        if not os.path.exists("tmp.txt"):
            tmp = open("tmp.txt","x")
        else:
            tmp = open("tmp.txt","a")
        sn = input("Enter site name: ")
        ps = ""
        chars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()"
        for i in range(0,20):
            ps = ps + chars[random.randint(0,71)]
        new_entry = sn + ": " + ps
        tmp.write(new_entry+"\n")

    elif sys.argv[1] == "help":

        print("--------------------Welcome to Passgen-----------------")
        print("Recommended to run in a empty folder")
        print("Commands:-")
        print("help - Show help")
        print("add - Add or create password file(saved as tmp.txt)")
        print("encrypt - Creates encrypted file(saved as entmp.txt) for password file(tmp.txt) with key(saved as enkey.key)")
        print("decrypt - Creates a decryted file(saved as tmp.txt) for entmp.txt with enkey.key")
        print("delete - Removes password file(saved as tmp.txt)")
        print("-------------------------------------------------------")

    elif sys.argv[1] == "encrypt":
        key = Fernet.generate_key()
        with open('enkey.key', 'wb') as keys:
            keys.write(key)
        with open('enkey.key', 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        try:
            with open('entmp.txt', 'rb') as file:
                psf = file.read()
        except:
            print("File not found!")
            exit()
        enf = fernet.encrypt(psf)
        
        with open('entmp.txt', 'wb') as enw:
            enw.write(enf)

    elif sys.argv[1] == "decrypt":
        with open('enkey.key', 'rb') as key:
            keys = key.read()
        fernet = Fernet(keys)
        with open('entmp.txt', 'rb') as enc:
            encr = enc.read()
        decr = fernet.decrypt(encr)
        with open('tmp.txt', 'wb') as decf:
            decf.write(decr)

    elif sys.argv[1] == "delete":
        if os.path.exists("tmp.txt"):
            os.remove("tmp.txt")
        else:
            print("File not found!")
        

    
    else:
        print("--------------------Welcome to Passgen-----------------")
        print("Recomended to run in a empty folder")
        print("Commands:-")
        print("help - Show help")
        print("add - Add or create password file(saved as tmp.txt)")
        print("encrypt - Creates encrypted file(saved as entmp.txt) for password file(tmp.txt) with key(saved as enkey.key)")
        print("decrypt - Creates a decryted file(saved as tmp.txt) for entmp.txt with enkey.key")
        print("delete - Removes password file(saved as tmp.txt)")
        print("-------------------------------------------------------")
else:
        print("--------------------Welcome to Passgen-----------------")
        print("Recomended to run in a empty folder")
        print("Commands:-")
        print("help - Show help")
        print("add - Add or create password file(saved as tmp.txt)")
        print("encrypt - Creates encrypted file(saved as entmp.txt) for password file(tmp.txt) with key(saved as enkey.key)")
        print("decrypt - Creates a decryted file(saved as tmp.txt) for entmp.txt with enkey.key")
        
        print("delete - Removes password file(saved as tmp.txt)")
        print("-------------------------------------------------------")