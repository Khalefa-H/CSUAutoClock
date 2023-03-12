# Auto Clockin (NO input Rejection Make sure you enter the right password please)
#------------------------------------------------------#
from datetime import date
import datetime
import configparser
import sys
import time
import os
import argparse
import configparser
from getpass import getpass 

import logging
logging.getLogger("urllib3").setLevel(logging.ERROR)
#Selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#---------------------------------------------------------------#
#DEBUG FLAG
DEBUG_MODE = False
#import chromedriver_autoinstaller


DEFAULT_HOURS = 4

#parsers
 #ini
config = configparser.ConfigParser()

config.read('clocker.ini')

  #--arguments
parser = argparse.ArgumentParser(description='CSUautoclockin')
parser.add_argument('-u', '--username', help="CSU Username", required=False ,default=config['User']['Username'])
parser.add_argument('-p', '--prompt', help="Turn on Password from ini file set to 'y' to enable   ", required=False)
parser.add_argument('-hrs', '--hours', type=float, help="Hours to clock if not set the Hours will be four", required=False, default=DEFAULT_HOURS)
args = vars(parser.parse_args())

USERNAME = args['username']
#Password Check you can insert your password below in the Password first variable below if loop (UNSAFE)
if(args['prompt'] == 'y'):
   #remove config
   PASSWORD = config['User']['Password']
else:
   PASSWORD =  getpass('Enter Password:')
   
#getpass.getpass(prompt='CSU Password: ', stream=None)
HOURS_TO_CLOCK = args['hours']
#Headless-MODE
chrome_options = Options()
#chrome_options.binary_location=(".\chrome-win")
#Headless mode

chrome_options.add_argument('--window-size=1920,1080')
if(DEBUG_MODE==False):
 chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--disable-sofware-rasterizer")

#Current CSU Portal Values
CLOCKOUT="#TL_RPTD_TIME_PUNCH_TYPE\$0 > option:nth-child(4)"
MEAL    ="#TL_RPTD_TIME_PUNCH_TYPE\$0 > option:nth-child(3)"
CLOCKIN ="#TL_RPTD_TIME_PUNCH_TYPE\$0 > option:nth-child(2)"

if HOURS_TO_CLOCK < DEFAULT_HOURS:
    print(f"[NOTE] Hours less than {DEFAULT_HOURS} unsupported")
    print(f"[NOTE] Using {DEFAULT_HOURS} hours")
if PASSWORD == "":
    print("Be sure to set your password.\n")
    sys.exit(1)
# ( variables with CAPITAL LETTERS  are a global variables.)

#=================================================================================================#
#=================================================================================================#

# CODE BELOW -----------------------------------------Don't Change unless you know what you are doing

#=================================================================================================#
#=================================================================================================#

# Global Variables:

MINUTES = HOURS_TO_CLOCK * 60
PROGRAM_TIME = (MINUTES*60)-1
SECONDS = int(MINUTES*60)
#CHROMEDRIVER options=chrome_options
REFRESH=[]
# REFRESH INTERVAL (SECS) 
REFRESH_TIME=300
#DRIVER
DRIVER = webdriver.Chrome(options=chrome_options)
WAIT = WebDriverWait(DRIVER, 25)
MINI_WAIT = WebDriverWait(DRIVER, 5)

#=================================================================================================#
# Functions, each step gets its own function:

def goToCSUClock():
    
    DRIVER.get("https://hcm-sso.onehcm.usg.edu/")
    
    return True


# Selecting CSU:
def selectCSU():
    # Selects CSU's icon 
    CSU_option = WAIT.until(EC.element_to_be_clickable((By.XPATH,
                                                       "//*[@id='http_fsauth_clayton_edu_adfs_services_trust']/div/div/a/img")))
    CSU_option.click()
    #return checkExistence(element_to_find="Username", method_to_find="name", purpose="Selecting CSU")
#&S

# This function logs us in once we are at the CSU login Page:
def loginCSU():
     
    CSU_login_username = DRIVER.find_element(By.ID,"userNameInput")
    CSU_login_password = DRIVER.find_element(By.ID,"passwordInput")

    CSU_login_username.send_keys(USERNAME+"@student.clayton.edu")
    CSU_login_password.send_keys(PASSWORD)

    submit_button = DRIVER.find_element(By.ID,"submitButton")
    submit_button.click()

    staff = WAIT.until(EC.element_to_be_clickable((By.XPATH,
                                               "//*[@id='DuoAdfsAdapter']")))
    staff.click()
    # YOU HAVE TO SWITCH iframes IN Selenium ! 
   
    WAIT.until(EC.frame_to_be_available_and_switch_to_it((By.ID,"duo_iframe")))

    pushb = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                               "#auth_methods > fieldset > div.row-label.push-label > button")))
    pushb.click()
    
    #waiting for duo
    print ('Waiting for duo......')
    #Claytonstate Web portal
    #DRIVER.get("https://hcm-sso.onehcm.usg.edus/")
    
    #Code below will 
    timebox = WAIT.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='win0divPTNUI_LAND_REC_GROUPLET$5']")))
    timebox.click()
  
    print("On CSU WEB PORTAL loggining status .....")
def clockHoursIn():
 elapsed = 1
 try:
    Go(CLOCKIN)
 except (NoSuchElementException, TimeoutException):
    Go(CLOCKIN)
    #loop below is a messy timer that loops until the seconds elasped are larger than the PROGRAM TIME
 print("Waiting for end of shift.....")
 while elapsed < PROGRAM_TIME:
 
    #print("...")
    for i in range(SECONDS):
     #print(i)
     #lets 1sec pass
     time.sleep(1)
     #+
     elapsed = elapsed + 1
        # If i greater than zero and leaves no remainder  i/x then refresh page 
     if(i>0):
      
      if(i%REFRESH_TIME == 0):
       # adding to Refresh occurance list
       REFRESH.append(i)
       #Refresh page
       DRIVER.refresh()
       print('...')
    #print(elapsed)
    if elapsed == PROGRAM_TIME:
    
        break
# This function clocks us out:
def clockHoursOut(x):
 if(x=='FULL'):
  try:
    Go(CLOCKOUT)
  except (NoSuchElementException, TimeoutException):
    Go(CLOCKOUT)
  else:
    DRIVER.get("https://selfservice.hprod.onehcm.usg.edu/psc/hprodsssso/HCMSS/HRMS/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL?")
    
    

def Clockselector(x):
    #Prototype Clock Selector
    
    if(True):
        Selection=x
        # Direct-To-Time-Page
    DRIVER.get("https://selfservice.hprod.onehcm.usg.edu/psc/hprodsssso/HCMSS/HRMS/c/TL_EMPLOYEE_FL.TL_RPT_TIME_FLU.GBL?Action=U&EMPLJOB=0")
    #Find Dropdown
    DRIVER.find_element(By.CSS_SELECTOR, "#TL_RPTD_TIME_PUNCH_TYPE\$0").click()
    #OPEN Dropdown
    #Find Desire clock state Selection=x
    DRIVER.find_element(By.CSS_SELECTOR, Selection ).click()
    #Select Clock State 
    DRIVER.find_element(By.CSS_SELECTOR, "#TL_WEB_CLOCK_WK_TL_SAVE_PB").click()
    print("Done")


#Controller
def Go(x):
 goToCSUClock()
 selectCSU()
 loginCSU()
 #Clockselector(x)
# The script running:

print('\nClocking {0} hours...\n'.format(HOURS_TO_CLOCK))
'''
'''
#Script Runtime
#INFO
print(datetime.datetime.now())
if(DEBUG_MODE):
 print(PROGRAM_TIME)
#Running
clockHoursIn()
Clockselector(CLOCKOUT)
time.sleep(2)

