import PySimpleGUI as sg
import os


#install pre-reqs
os.system('apt-get install jq')
latestRAW = os.system("curl -s http://127.0.0.1:5000/latest | \jq '.'")

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Red Meter Serial #: xxxxx')],
            [sg.Text(latestRAW)],
            [sg.Text('Cartridge Name:'), sg.InputText(), sg.Button('Enter')],
            [sg.Text('RUN Mass Configuration [Saved/NotSaved]'), sg.Button('Configure Mass')],
            [sg.Text('Temperature and Pressure'), sg.Button('Run Temp/Press')],
            [sg.Button('Mass Calibration')],
            [sg.Button('Exit')] ]

cartName = sg.InputText()

# Create the Window
window = sg.Window('Red Meters Test Suite', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event is None or event == 'Exit':   # if user closes window or clicks 'Exit'
        break
    print('You entered ', values[0])




window.close()
