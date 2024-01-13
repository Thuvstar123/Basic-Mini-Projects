import sys
import subprocess

subprocess.check_call([sys.executable,'-m','pip','install','PySimpleGUI'])

import PySimpleGUI as sg
import time

#These procedures undergo background processes that will initiate the saving of URLs.
#weblist: Net URL count
#websave: Current URL count

def appendation(url):
    '''''''''''''''''''''''
    Simply appends text documents. Since the format is preferred to be sent
    in a website1,website2 format, the format is preset this way. If the
    file has nothing in it, seperation witha  comma cannot be used, so
    validation is put in place.
    '''''''''''''''''''''''
    global weblist,websave,weblist_content,websave_content

    close_file()

    weblist=open("Weblist.txt","a")
    if len(weblist_content)!=0:
        weblist.write(","+url)
    else:
        weblist.write(url)
    websave=open("Websave.txt","a")
    if len(websave_content)!=0:
        websave.write(","+url)
    else:
        websave.write(url)

    close_file()

def read_content():
    '''''''''''''''''''''''
    Reads what the file contains.
    Since the websave file is going to be deleted often, a verification is
    done to see if the file still exists. If not, a new file is created and
    the function calls itself again.
    '''''''''''''''''''''''
    global weblist,websave,weblist_content,websave_content,url_list_tot,url_save_tot

    weblist=open("Weblist.txt","r")
    weblist_content=weblist.read()
    try:
        websave=open("Websave.txt","r")
        websave_content=websave.read()
    except FileNotFoundError:
        websave=open("Websave.txt","w")
        websave.close()
        read_content()
    url_list_tot=len(weblist_content.split(","))-1
    url_save_tot=len(websave_content.split(","))-1

def close_file():
    '''''''''''''''''''''''
    Closes BOTH files if opened.
    '''''''''''''''''''''''
    global weblist,websave

    websave.close()
    weblist.close()

def websave_create():
    '''''''''''''''''''''''
    If it is a new set of urls, the file is emptied so that the later set of
    URLs can be svaed onto the file, like RAM, whilst the weblist does not get
    recreated, like ROM.
    '''''''''''''''''''''''
    websave=open("Websave.txt","w")
    websave.write("")
    websave.close()

def repeat_check():
    '''''''''''''''''''''''
    Checks to see if the URL that has been input is already reported by
    comparing it to the weblist file, containing all of the sites.
    '''''''''''''''''''''''
    global url_input,weblist_content

    if url_input in weblist_content.split(","):
        return "Reported"
    else:
        return

try:
    read_content()
except FileNotFoundError:
    weblist=open("Weblist.txt","w")
    websave=open("Websave.txt","w")
    close_file()
    read_content()

#This section refers to the window processes.

sg.theme("DarkBrown6")
layout=[[sg.Push(),sg.Image("cross.png",key="CLOSE",enable_events=True)],
        [sg.Text("Website Reporter",key="TEXT",expand_x=True),sg.Text("Update",key="LIST_TOTAL",expand_x=True,visible=False)],
        [sg.Input("Enter URL",key="INPUT",expand_x=True)],
        [sg.Button("Enter",expand_x=True),sg.Button("New day",expand_x=True)],
        [sg.Text("Already Reported",key="REPORTED",visible=False)]
        ]

window=sg.Window("Website Reporter",layout,no_titlebar=True,size=(400,300),grab_anywhere=True)

while True:
    event,value=window.read()

    if event==sg.WIN_CLOSED:
        break
    elif event=="CLOSE":
        sg.popup("Net URL count:"+str(url_list_tot)+"\nCurrent URL count:"+str(url_save_tot))
        time.sleep(1)
        window.close()

    if event=="Enter":
        if value["INPUT"]!="STOP":
            window["TEXT"].update("URL: "+value["INPUT"])
            url_input=str(value["INPUT"])
            if repeat_check()!="Reported":
                window["REPORTED"].update(visible=False)
                appendation(url_input)
                close_file()
                read_content()
            else:
                window["REPORTED"].update(visible=True)
        else:
            break

    if event=="New day":
        websave_create()
        read_content()

close_file()
