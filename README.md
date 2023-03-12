# CSUAutoClock
 A Simple Script to Clock OneUSG User to Clock user in and out using pyhton and selium



usage: clocker.py [-h] [-u USERNAME] [-p PROMPT] [-hrs HOURS]

CSUautoclockin

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        CSU Username (everything before the @)
  -p PROMPT, --prompt PROMPT
                        Disable Password prompt for automation (add password
                        directly into the code)
  -hrs HOURS, --hours HOURS
                        Hours to clock if not set the Hours will be set to 4
 <br/>Some issues: 

This version will not tell you if you got the wrong login if it stops outputting during login this is most likely why

No date and time logging  into a file yet 
