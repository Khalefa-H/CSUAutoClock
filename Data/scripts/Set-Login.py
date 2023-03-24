from cryptography.fernet import Fernet
import os
import re
import time
from dotenv import load_dotenv
from getpass import getpass
import sys
#Changes the Directory so that the file is saved where the data is 
os.chdir(os.path.dirname(sys.argv[0]))
#Genrating key
print("Generating new key in current dirrectory (Please keep your key.txt file somewhere safe)")
i=0
while(i<2):
    print("...")
    time.sleep(1)
    i= i+1
key= Fernet.generate_key()
open(".\key.txt","wb").write(key)
load_dotenv()

f=Fernet(open('key.txt',encoding='ascii').read())

print("Enter username")
Username=bytes((input()),'ascii')
Password=bytes(getpass(prompt='Enter Swan password \n'),"ascii")
file0=open(".\\.env","wb")
#file0.write(b'#Creds \n')
file0.write(bytes('\nUname=',"ascii"))
file0.write(f.encrypt(Username))
file0.write(bytes('\nPw=',"ascii"))
file0.write(f.encrypt(Password))
