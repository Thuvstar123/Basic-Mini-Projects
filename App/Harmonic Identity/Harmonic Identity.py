import sys
import subprocess

subprocess.check_call=([sys.executable,"-m","pip","install","PySimpleGUI"])
subprocess.check_call=([sys.executable,"-m","pip","install","numpy"])

import PySimpleGUI as sg
import numpy as np

layout=[[sg.Text("Enter the Identity:",justification="c")],
        [sg.Input("",size=(15,15),key="INPUT1"),sg.Text("cos(x)"),sg.Spin(["+","-"],size=(7,15),key="SPIN"),sg.Input("",size=(15,15),key="INPUT2"),sg.Text("sin(x)"),sg.Text("="),sg.Input("",size=(15,15),key="INPUT3")],
        [sg.Button("Enter",key="PROCESS")],
        [sg.Text("You are missing a parameter",visible=False,key="VALIDATION")],
        [sg.Text("\u03B1")]
    ]

window=sg.Window("Harmonic Identities Calculator",layout,element_justification="c")

while True:
    event,value=window.read()

    def validate():
        """""""""""""""""
        Returns true if the inputs have all been filled in. If not, returns false and validation text will
        detail to the user that a parameter is missing.
        """""""""""""""""
        if value["INPUT1"]=="" or value["INPUT2"]=="" or value["INPUT3"]=="":
            window["VALIDATION"].update(visible=True)
            return False
        else:
            window["VALIDATION"].update(visible=False)
            return True

    def harmonic():
        r=0
        alpha=0
        if sg.Popup("Press YES for Rsin(x+alpha). Press NO for Rcos(x+alpha)")=="Yes":
            alpha=np.arctan(int(value["INPUT2"]/int(value["INPUT1"])))


    if event==sg.WIN_CLOSED:
        break
    if event=="PROCESS":
        if validate()==True:
            harmonic()