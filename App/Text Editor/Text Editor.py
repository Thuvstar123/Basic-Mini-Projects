import sys
import subprocess

subprocess.check_call([sys.executable,"-m","pip","install","PySimpleGUI"])

import PySimpleGUI as sg
from pathlib import Path as pa

def create_window():
    global formula_symbols, forsym_events

    sg.theme("DarkBrown6")

    menu_layout=[
            ["File",["Open","Save","Close"]],
            ["Tools",["Word Count","Find"]],
            ["Add",formula_symbols],
            ["Help",["Library Info","Video Reference","Info"]]
        ]

    layout=[
            [sg.Menu(menu_layout)],
            [sg.Text("Untitled.txt",key="FILE_NAME")],
            [sg.Multiline("Enter here...",expand_x=True,expand_y=True,no_scrollbar=True,key="TEXTBOX",text_color="Black")]
        ]
    return sg.Window("Text Editor",layout,size=(440,440))

def save():
    try:
        file_path=sg.popup_get_file("Save as",no_window=True,save_as=True)
        file=pa(file_path)
        file.write_text(value["TEXTBOX"])
        window["FILE_NAME"].update(file_path.split("/")[-1])
    except PermissionError:
        pass

formula_symbols=[
            "calculus",["∫","dy/dx"],
            "operations",["+","-","×","÷"]
        ]
formsym_events=formula_symbols[1]+formula_symbols[3]

window=create_window()


while True:
    event,value=window.read()

    match event:
        case sg.WIN_CLOSED:
            break

#This section refers to the "Tools" section of the menu
        case "Word Count":
            text=value["TEXTBOX"]
            if text.count(" ")>0:
                sg.Popup("Words:",(len(text)-len(text.replace(" ","")))+1,"\nCharacters (with spaces):",len(text),"\nCharacters (Without Spaces)",len(text.replace(" ","")))
            else:
                sg.Popup("Words:",1,"\nCharacters (with spaces):",len(text),"\nCharacters (Without Spaces)",len(text))
        case "Find":
            text=value["TEXTBOX"]
            found=text.find(sg.PopupGetText("Find word:"))
            if found>0:
                sg.PopupNoTitlebar("The word is located on the "+str(found+1)+"th character")
            else:
                sg.PopupNoTitlebar("There are no such words/characters in the text")

#This section refers to the "Help" section of the menu
        case "Library Info":
            sg.PopupNoTitlebar("Library name: PySimpleGUI")
        case "Video Reference":
            sg.PopupNoTitlebar("Video name:Creating 10 Apps in Python [ with PySimpleGui ]\nVideo Link:https://www.youtube.com/watch?v=kQ8DGP9p2LY")
        case "Info":
            sg.PopupNoTitlebar("This is a mini project made my Thuv, very simple and not entirely practical. The purpose of this project was simply to learn and gain experience with python.")

#This section refers to the "File" section of the menu
        case "Open":
            try:
                file_path=sg.popup_get_file("Open",no_window=True)
                file=pa(file_path)
                window["TEXTBOX"].update(file.read_text())
                window["FILE_NAME"].update(file_path.split("/")[-1])
            except PermissionError:
                pass
        case "Save":
            save()
        case "Close":
            save_confirm=sg.popup_yes_no("Do you want to save your file?")
            if save_confirm=="No":
                window.close()
                window=create_window()
            else:
                save()
                window.close()
                window=create_window()

#This section refers to the "Add" section of the menu
    if event in formsym_events:
        text=value["TEXTBOX"]
        window["TEXTBOX"].update(text+event)
    else:
        pass