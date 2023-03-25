# CSUAutoClock

<h1>SETUP Windows</h1><br/>

<li>1. install Python "winget install python" or get python3 from the MSstore
<li>2. Use python pip to install requirements "pip install -r "Wherever you put the application"\requirements.txt "
<li>3.Run gui.exe or Run the GUI with "python.exe .\Data\Scripts\clocker.py" NOTE: Run Setup login First (You can leave password empty if you plan to use the prompted version)

usage: clocker.py [-h] [--Config | --no-Config]
                  [-u | --username | --no-username]
                  [-p | --prompt | --no-prompt] [-hrs HOURS]

CSUautoclockin

options:
  -h, --help            show this help message and exit<br/>
  --Config, --no-Config<br/>
                        Not needed but overrides other arugments in favor of
                        save creds<br/>
  -u, --username, --no-username<br/>
                        CSU Username(everything before the @) (default: N/A)<br/>
  -p, --prompt, --no-prompt<br/>
                        Disable Password prompt for automation (add password
                        directly into the code)<br/>
  -hrs HOURS, --hours HOURS<br/>
                        Hours to clock if not set the Hours will be 4<br/>


No date and time logging  into a file yet 

<h1>Additional Files<h1>
<li>Set-Login.* : Will create a new Encryption key then allow you to enter A new Login 
<li>Changepw.* : Will Allow you to Change the password without reseting everything else 
<li>Key.txt : Holds your encryption key (!KEEP THIS FILE SAFE & REPLACE WHEN YOU WANT TO RUN THE PROGRAM!)
