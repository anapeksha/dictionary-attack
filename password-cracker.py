import hashlib
import os
import sys

sha1hash = input("Enter the hash to be cracked: \n>")

file = open(os.path.join(sys.path[0],"wordlist/common_passwords.txt"), "r", encoding = 'utf-8')

COMMON_PASSWORDS = file.read()


for guess in COMMON_PASSWORDS.split('\n'):
    hashed = hashlib.sha256(bytes(guess, 'utf-8')).hexdigest()
    if hashed == sha1hash:
        print("Password is :", str(guess))
        quit()
    else:
        print(str(guess),"does not match! Trying next....")

print("Password not in database!!")


