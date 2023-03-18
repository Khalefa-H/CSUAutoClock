# CSUAutoClock
 A Simple Script to Clock OneUSG User to Clock user in and out using pyhton and selium
It logs in then starts the Duo push for aproval (It tries twice if you it times out) then clocks you in then waits on the Web portal until the end of the shift by refreshing the page for the duration then clocking out at the end 
<h1>SETUP Windows</h1><br/>

<li>1.Run First-Time-Setup.ps1
<li>2.Read and go though process
<li>3.Run with arguments  example "python3 .\clocker.py" or Start-Program.ps1 (ps1 file does no take arguments)

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
<li>Set-Login.* : Will create a new Encryption key then allow you to enter A new Login <br/>
<li>Changepw.* : Will Allow you to Change the password without reseting everything else <br/>
