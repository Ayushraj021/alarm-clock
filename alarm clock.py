from tkinter.ttk import *
from tkinter import *
from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread

from PIL import ImageTk, Image

#color
bg_color = '#ffffff'
col1 = 'black'
col2 = 'blue'


#window
window = Tk()
window.title("")
window.geometry('300x150')
window.config(bg=bg_color)

#frame up

frame_line = Frame(window, width=400, height=2, bg=col1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg=bg_color)
frame_body.grid(row=1, column=0)

#configuring frame body

img = Image.open('image.png')
img.resize((100,100))
img = ImageTk.PhotoImage(img)

app_image =Label(frame_body, height=100, image=img, bg= bg_color)
app_image.place(x=10, y=10)

name = Label(frame_body, text= 'Alarm', height=1, font=('Ivy 18 bold'), bg=bg_color)
name.place(x=125, y=10)

hours = Label(frame_body, text= 'Hours', height=1, font=('Ivy 10 bold'), fg=col2, bg= bg_color)
hours.place(x=127, y=40)
c_hours = Combobox(frame_body, width=2, font=('arial 15'))
c_hours['values']= ("00","01","02","03","04","05","06","07","08","09","10","11","12", "13","14","15","16","17","18","19","20","21","22","23")
c_hours.current(0)
c_hours.place(x=130, y=58)


minutes = Label(frame_body, text= 'Mins', height=1, font=('Ivy 10 bold'), fg=col2, bg= bg_color)
minutes.place(x=177, y=40)
c_minutes = Combobox(frame_body, width=2, font=('arial 15'))
c_minutes['values']= ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_minutes.current(0)
c_minutes.place(x=180, y=58)



seconds = Label(frame_body, text= 'Secs', height=1, font=('Ivy 10 bold'), fg=col2, bg= bg_color)
seconds.place(x=227, y=40)
c_seconds = Combobox(frame_body, width=2, font=('arial 15'))
c_seconds['values']= ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_seconds.current(0)
c_seconds.place(x=230, y=58)


def activate_alarm():
    t = Thread(target=alarm)
    t.start()


def deactivate_alarm():
    print('Alarm Deactivated:', selected.get())
    mixer.music.stop()



selected = IntVar()

rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text="Activate", bg=bg_color, command= activate_alarm, variable=selected)
rad1.place(x=125, y=95)




def sound_alarm():
    mixer.music.load('music.wav')
    mixer.music.play()
    selected.set(0)
    
rad2 = Radiobutton(frame_body, font=('arial 10 bold'), value=2, text="Deactivate", bg=bg_color, command= deactivate_alarm, variable=selected)
rad2.place(x=200, y=95)
    
def alarm():
    while True:
        control =1
        print(control)
        
        
        alarm_hour=c_hours.get()
        alarm_minute=c_minutes.get()
        alarm_second=c_seconds.get()
        
        
        
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
