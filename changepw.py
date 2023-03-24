import base64
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv
from getpass import getpass

load_dotenv()

f=Fernet(open('key.txt',encoding='ascii').read())

Username= os.getenv("Uname")

Password=bytes(getpass(prompt='Enter New Swan password \n'),"ascii")

file0=open(".\\.env","wb")
#file0.write(b'#Creds \n')
file0.write(bytes('\nUname=',"ascii"))
file0.write(f.encrypt(Username))
file0.write(bytes('\nPw=',"ascii"))
file0.write(f.encrypt(Password))
