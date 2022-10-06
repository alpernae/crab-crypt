#!/usr/bin/env python3

import time
import os
from cryptography.fernet import Fernet

#FIND FILES

files = []

for file in os.listdir():
	if file == "creeper.py" or file == "secret.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print("Generating decryption key!")
time.sleep(2)
print("Decryption key generated!")
time.sleep(2)
print("You LUCKY! All your files in safe this time ;) ")

# Decrypt Files

with open("secret.key", "rb") as key:
	decrypt = key.read() 

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	
	contents_decrypted = Fernet(decrypt).decrypt(contents)
	with open(file,"wb") as thefile:
		thefile.write(contents_decrypted)
