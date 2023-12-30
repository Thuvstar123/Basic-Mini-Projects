import subprocess
import sys
from time import time

subprocess.check_call([sys.executable,"-m","pip","install","PysImpleGUI"])

import PySimpleGUI as sg

def create_window():
    sg.theme("Black")
    layout=[[sg.Push(),sg.Image("cross.png",key="CLOSE", enable_events=True)],
            [sg.VPush()],
            [sg.Text("0.0",key="OUTPUT",font="Young 50")],
            [sg.Button("Start",button_color="DarkGrey",font="Young",border_width=0,key="START",visible=True),sg.Button("Lap",button_color="DarkGrey",border_width=0,key="LAP",visible=True)],
            [sg.Button("Reset",key="RESET",button_color="DarkGrey",font="Young",border_width=0,visible=False)],
            [sg.Column([[]],key="LAPS")],
            [sg.VPush()]
        ]
    return sg.Window("Stopwatch",layout,size=(400,400),no_titlebar=True,element_justification="Center",font="Young")

window=create_window()
start_time=0
active=False
lap_number=0

while True:
    event,value=window.read(timeout=10)

    if event==sg.WIN_CLOSED:
        break
    elif event=="CLOSE":
        window.close()
    if event=="START":
        if active:
            window["OUTPUT"].update(elapsed_time)
            active=False
            window["RESET"].update(visible=True)
            window["START"].update(visible=False)
            window["LAP"].update(visible=False)
        else:
            window["RESET"].update(visible=False)
            start_time=time()
            active=True
            window["START"].update("Stop")
    if active:
        elapsed_time=round(time()-start_time,1)
        window["OUTPUT"].update(elapsed_time)
    if event=="RESET":
        window.close()
        window=create_window()
    if event=="LAP":
        lap_number+=1
        lap="Lap "+str(lap_number)
        window.extend_layout(window["LAPS"],[[sg.Text(lap),sg.VSeparator(),sg.Text(elapsed_time)]])
