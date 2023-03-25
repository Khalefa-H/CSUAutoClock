import subprocess
import tkinter as tk
import os 
import sys

os.chdir(os.path.dirname(sys.argv[0]))

def run_command():
    command = powershell_input.get()
    timer=delay.get()
    subprocess.call(["powershell.exe", "-Command","sleep ("+timer+"*60) ; Start-Process powershell 'python .\data\scripts\clocker.py "+command+"'"])
def Setup():
    subprocess.call(["Powershell.exe","-Command","Start-Process powershell 'python .\data\scripts\Set-Login.py'"])
def chpw():
    subprocess.call(["Powershell.exe","-Command","Start-Process powershell 'python .\data\scripts\changepw.py'"])
def prompt():
    command = powershell_input.get()
    timer=delay.get()
    subprocess.call(["powershell.exe", "-Command","sleep "+timer+"; Start-Process powershell 'python .\data\scripts\clocker.py "+command+" -p  '"])    
root = tk.Tk()
root.title("CSU Clocker Simple GUI-Input Hours")

# Create input box for PowerShell command
powershell_input = tk.Entry(root, width=10)
delay = tk.Entry(root, width=3)
#add defaults
delay.insert(0, "0")
powershell_input.insert(0, "-hrs 4")
# Create button to run command
delaylabel = tk.Button(root, text="Set Delay(Minutes) below ")

run_button = tk.Button(root, text="Clock Hours Enter Hours Below (-hrs #) ", command=run_command)
run_button1 = tk.Button(root, text="Setup Login", command=Setup)
run_button3 = tk.Button(root, text="Clock Hours without Saved Password(No Delay)", command=prompt)

run_button1.pack(pady=10)

delaylabel.pack()
delay.pack()
run_button3.pack(pady=5)
run_button.pack(pady=10)

powershell_input.pack()
root.mainloop()

