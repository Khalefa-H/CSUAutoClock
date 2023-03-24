import subprocess
import tkinter as tk

def run_command():
    command = powershell_input.get()
    subprocess.call(["powershell.exe", "-Command","Start-Process powershell 'python .\clocker.py "+command+"'"])
def Setup():
    subprocess.call(["Powershell.exe","-Command","Start-Process powershell 'python .\Set-Login.py'"])
def chpw():
    subprocess.call(["Powershell.exe","-Command","Start-Process powershell 'python .\changepw.py'"])
root = tk.Tk()
root.title("CSU Clocker Simple GUI-Input Hours")

# Create input box for PowerShell command
powershell_input = tk.Entry(root, width=10)


# Create button to run command
run_button = tk.Button(root, text="Clock Hours (Enter Below)", command=run_command)
run_button1 = tk.Button(root, text="Setup", command=Setup)
run_button2 = tk.Button(root, text="Update Password", command=chpw)
run_button1.pack(pady=0)
run_button2.pack(pady=0)
run_button.pack(pady=10)
powershell_input.pack()
root.mainloop()

