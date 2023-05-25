import subprocess
import PySimpleGUI as sg
import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))


def run_command():
    command = values['-COMMAND-']
    timer = values['-DELAY-']
    subprocess.call(["powershell.exe", "-Command",
                     f"sleep ({timer}*60) ; Start-Process powershell 'python .\data\scripts\clocker.py {command}'"])


def Setup():
    subprocess.call(["Powershell.exe", "-Command", "Start-Process powershell 'python .\data\scripts\Set-Login.py'"])


def chpw():
    subprocess.call(["Powershell.exe", "-Command", "Start-Process powershell 'python .\data\scripts\changepw.py'"])


def prompt():
    command = values['-COMMAND-']
    timer = values['-DELAY-']
    subprocess.call(["powershell.exe", "-Command",
                     f"sleep {timer}; Start-Process powershell 'python .\data\scripts\clocker.py {command} -p'"])


sg.theme('DefaultNoMoreNagging')

layout = [
    [sg.Text('CSU Clocker Simple GUI-Input Hours')],
    [sg.Button('Setup Login', key='-SETUP-')],
    [sg.Text('Set Delay (Minutes) below')],
    [sg.InputText('0', key='-DELAY-', size=(10, 1))],
    [sg.Button('Clock Hours Enter Hours Below (-hrs #)', key='-RUN-')],
    [sg.Button('Clock Hours without Saved Password (No Delay)', key='-PROMPT-')],
    [sg.InputText('-hrs 4', key='-COMMAND-', size=(30, 1))],
]

window = sg.Window('CSU Clocker', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-RUN-':
        run_command()
    elif event == '-SETUP-':
        Setup()
    elif event == '-PROMPT-':
        prompt()

window.close()

