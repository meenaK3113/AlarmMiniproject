import datetime
from playsound import playsound
ah=int(input("Enter alarm hour:"))
amin=int(input("Enter minutes:"))
al=input("Is it am/pm??")
if al=="pm":
    ah+=12
while(1):
    if ah==datetime.datetime.now().hour and amin==datetime.datetime.now().minute:
        print("Alarmingg!!!")
        playsound("C:/Users/balaj/Downloads/Halena.mp3")
        break
