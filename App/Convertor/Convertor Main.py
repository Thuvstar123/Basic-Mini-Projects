import subprocess
import sys

subprocess.check_call([sys.executable,"-m","pip","install","PySimpleGUI"])

import PySimpleGUI as sg

sg.theme("DarkGreen6")

layout=[
    [sg.Spin(["Km to Miles","Years to Hours"],key="Spinner"),sg.Input(key="inputt")],
    [sg.Button("Enter", key="Input1")],
    [sg.Text("Output",key="Toldya")]
]

window=sg.Window("Convertor",layout)

while True:
    event,value=window.read()

    if event==sg.WIN_CLOSED:
        break
    if event=="Input1":
        if value["inputt"].isnumeric()==False:
            print("Input must be numeric")
        else:
            match value["Spinner"]:
                case "Km to Miles":
                    #outputs the value on the text of the window
                    miles=int(value["inputt"])*0.621371
                    outputm=f"In {value['inputt']}km, there are {miles}miles."
                    window["Toldya"].update(outputm)
                case other:
                    #outputs the value on the text of the window
                    hours=int(value["inputt"])*24*365
                    outputh=f"In {value['inputt']} years, there are {hours} hours."
                    window["Toldya"].update(outputh)

