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


# Define a custom theme with orange and navy blue colors
custom_theme = {'BACKGROUND': '#003366',
                'TEXT': '#FFA500',
                'INPUT': '#FFA500',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#FFA500',
                'BUTTON': ('white', '#FFA500'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

sg.theme_add_new('CustomTheme', custom_theme)
sg.theme('CustomTheme')

layout = [
    [sg.Text('CSU Clocker Simple GUI-Input Hours', font=('Helvetica', 16), justification='center')],
    [sg.Button('Setup Login', key='-SETUP-')],
    [sg.Text('Set Delay (Minutes) below')],
    [sg.InputText('0', key='-DELAY-', size=(10, 1))],
    [sg.Button('Clock Hours Enter Hours Below (-hrs #)', key='-RUN-')],
    [sg.Button('Clock Hours without Saved Password (No Delay)', key='-PROMPT-')],
    [sg.InputText('-hrs 4', key='-COMMAND-', size=(30, 1))],
]

window = sg.Window('CSU Clocker', layout, element_justification='center', icon='CSU.ico', resizable=True)

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

