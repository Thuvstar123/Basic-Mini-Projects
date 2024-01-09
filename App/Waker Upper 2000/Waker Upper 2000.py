import sys
import subprocess

subprocess.check_call([sys.executable,"-m","pip","install","PySimpleGUI"])
subprocess.check_call([sys.executable,"-m","pip","install","opencv-python"])
subprocess.check_call([sys.executable,"-m","pip","install","pygame"])

import PySimpleGUI as sg
import cv2
import pygame
import time
from pygame import mixer
mixer.init()

number_people=0

layout=[
        [sg.Image(key="IMAGE")],
        [sg.Text(f"Eyes are closed",key="TEXT",expand_x=True,justification="c")]
    ]

window=sg.Window("Face Detector",layout)

#This section will refer to the camera settings
video=cv2.VideoCapture(0)
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    event,value=window.read(timeout=0)

    if event==sg.WIN_CLOSED:
        break
    _,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes=eye_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=7,minSize=(20,20))

    #boxed heads
    for (x,y,h,w) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(128,0,128),2)

    #image update
    imgbytes=cv2.imencode(".png",frame)[1].tobytes()
    window["IMAGE"].update(data=imgbytes)

    #text update
    number_people=str(len(eyes))
    match number_people:
        case "2":
            window["TEXT"].update("Awake")
            try:
                song.stop()
            except pygame.error and NameError:
                pass
        case "1":
            window["TEXT"].update("Almost asleep")
            if mixer.get_busy()==False:
                song=mixer.Sound("C:/Users/suguu/Documents/Apps/Coding/Python/Learning/App/Waker Upper 2000/snore-mimimimimimi.mp3")
                song.play()
            else:
                mixer.unpause()
        case "0":
            window["TEXT"].update("Asleep")
            if mixer.get_busy()==False:
                song=mixer.Sound("C:/Users/suguu/Documents/Apps/Coding/Python/Learning/App/Waker Upper 2000/wake_up.mp3")
                song.play()
            else:
                mixer.unpause()

#This project is a mixture of PySimpleGUI, OpenCV and PyGame. All of such modules may have copyrights, so do not use the following for business purposes, unless given the permission.
