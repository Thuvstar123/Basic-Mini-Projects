import sys
import subprocess

subprocess.check_call([sys.executable,"-m","pip","install","PySimpleGUI"])

import PySimpleGUI as sg

def window_content(theme):
    sg.set_options(font="Franklin 14",button_element_size=(6,3))
    button_size=(6,3)
    sg.theme(theme)

    layout=[[sg.Text("", expand_x=True, right_click_menu=theme_menu, key="TEXT", justification="Right",pad=(10,20))],
            [sg.Button("Clear", expand_x=True),sg.Button("Clear All", expand_x=True),sg.Button("Enter", expand_x=True),sg.Button("ans", expand_x=True)],
            [sg.Button(1, size=button_size),sg.Button(2, size=button_size),sg.Button(3, size=button_size),sg.Button("+", size=button_size)],
            [sg.Button(4, size=button_size),sg.Button(5, size=button_size),sg.Button(6, size=button_size),sg.Button("-", size=button_size)],
            [sg.Button(7, size=button_size),sg.Button(8, size=button_size),sg.Button(9, size=button_size),sg.Button("*", size=button_size)],
            [sg.Button(0, expand_x=True),sg.Button(".", size=button_size), sg.Button("/", size=button_size)]

        ]
    return sg.Window("Calculator",layout)


theme_menu=["menu", ["DarkGreen4","DarkBrown6","DarkBlack1","random"]]
window=window_content("dark")

cnum=[]
num_string=""
alloper=[]
ans=0

while True:
    event,value=window.read()

    match event:
        case sg.WIN_CLOSED:
            break
        case "Enter":
            try:
                full_oper="".join(alloper)
                ans=eval(full_oper)
                window["TEXT"].update(ans)
                alloper=[]
                full_oper=[]
            except (SyntaxError, NameError):
                window["TEXT"].update("There is an input error")
        case "Clear All":
            cnum=[]
            alloper=[]
            num_string="".join(alloper)
            window["TEXT"].update(num_string)
        case "Clear":
            cnum=cnum[:-1]
            alloper=alloper[:-1]
            num_string="".join(alloper)
            window["TEXT"].update(num_string)


    if event in theme_menu[1]:
        window.close()
        window=window_content(event)
    if event in ["1","2","3","4","5","6","7","8","9","0",".","ans"]:
        cnum.append(event)
        alloper.append(event)
        num_string="".join(alloper)
        window["TEXT"].update(num_string)
    if event in ["+","-","/","*"]:
        alloper.append(event)




