# CSUAutoClock
 A Simple Script to Clock OneUSG User to Clock user in and out using pyhton and selium
It logs in then starts the Duo push for aproval (It tries twice if you it times out) then clocks you in then waits on the Web portal until the end of the shift by refreshing the page for the duration then clocking out at the end 
<h1>SETUP</h1><br/>
<p>Windows<p/><br/>
<li>1.Install Python3 w/ pip
<li>2.Install requirements with "pip install -r requirements.txt"
<li>3.Run with arguments  example "python3 .\clocker.py" or create a powershell .ps1 file


<h2>usage: clocker.py [-h] [-u USERNAME] [-p PROMPT] [-hrs HOURS]<h2/>

#CSUautoclockin

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        CSU Username (everything before the @)
  -p PROMPT, --prompt PROMPT
                        Disable Password prompt for automation (add password
                        directly into the code)
  -hrs HOURS, --hours HOURS
                        Hours to clock if not set the Hours will be set to 4
 <br/> <br/>Some issues: 

This version will not tell you if you got the wrong login if it stops outputting during login this is most likely why

No date and time logging  into a file yet 
