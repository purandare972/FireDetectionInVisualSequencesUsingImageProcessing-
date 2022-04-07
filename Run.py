from ast import While
from email.mime import image
from tkinter import Image, PhotoImage
import cv2
import numpy as np
import playsound
import smtplib


Fire_Reported = 0
Alarm_Status = False


def play_audio():
    playsound.playsound("Alarm.mp3",True)

def send_email_function():

    recipientEmail = "gjoon1214@gmail.com"
    recipientEmail = recipientEmail.lower()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("gargipurandare14@gmail.com", 'gargigargi1427')
        server.sendmail('gargipuranadre14@gmail.com', recipientEmail, "Warning A Fire Accident has been reported on second floor at XYZ Company")
        print("sent to {}".format(recipientEmail))
        server.close()
    except Exception as e:
    	print(e)

video = cv2.VideoCapture("video4.mp4")
while True :

    ret, frame = video.read()
    frame = cv2.resize(frame,(1000,600))
    blur = cv2.GaussianBlur(frame,(15,15),0) 
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = [18,50,50]
    upper = [25,255,255]

    lower = np.array(lower,dtype='uint8')
    upper = np.array(upper,dtype='uint8')

    mask = cv2.inRange(hsv,lower,upper)

    output = cv2.bitwise_and(frame,hsv,mask=mask)

    size  = cv2.countNonZero(mask)

    if int(size) > 15000:
        print(" FIRE DETECTED!!! ")
        Fire_Reported = Fire_Reported +1
        
        if Fire_Reported >= 1:

            if Alarm_Status == False: 
                send_email_function()
                play_audio()
                Alarm_Status = True
            
        

    if ret == False:
        break

    cv2.imshow("Output",output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
video.release()