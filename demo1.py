from tkinter.ttk import *
from tkinter import *
from pygame import mixer
from datetime import datetime
from time import sleep

#window
window = Tk()
window.title("")
window.geometry('300x150')

def sound_alarm():
    mixer.music.load('music.wav')
    mixer.music.play()
    
def alarm():
    while True:
        control =1
        print(control)
        
        
        alarm_hour='11'
        alarm_minute='20'
        alarm_second='00'
        
        
        
        now = datetime.now()
        
        
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S") 
        
        
        if control == 1:
            if alarm_hour == hour:
                if alarm_minute == minute:
                    if alarm_second == second:
                        alarm()             
        sleep(1)


mixer.init()
sound_alarm()

window.mainloop()

