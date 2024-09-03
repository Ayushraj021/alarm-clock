# importing tkinter 
from tkinter.ttk import *
from tkinter import *

# importing pillow
from PIL import Image, ImageTk
from matplotlib import image
from matplotlib.pyplot import text

from pygame import mixer
import time
from datetime import datetime

from time import sleep
from threading import Thread

# colors

co0 = "#f0f3f5"  # Black
co1 = "#feffff"  # White
co2 = "#d6872d"  # Gold
co3 = "#fc766d"  # Red
co4 = "#403d3d"  # Black
co5 = "#4a88e8"  # Blue

# creating the window

window = Tk()
window.title("")
window.geometry('350x150')
window.configure(background=co1)
window.resizable(width=FALSE, height=FALSE)

# dividing the window into 2 frames
frame_logo = Frame(window, width=400, height=10, bg=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0)

frame_body = Frame(window, width=400, height=290, bg=co1)
frame_body.grid(row=1, column=0, pady=1, padx=0)

# configuring the logo frame
l_line = Label(frame_logo, width=400, height=1, bg=co2, anchor=NW, font=('Ivy 1'))
l_line.place(x=0, y=0)

# configuring the body frame

image = Image.open('image.png')
image = image.resize((100, 100))
image = ImageTk.PhotoImage(image)

l_image = Label(frame_body, height=100, image=image, compound=LEFT, padx=10, anchor=NW, font=('Ivy 16 bold'), bg=co1, fg=co3)
l_image.place(x=10, y=10)

l_name = Label(frame_body, text='Alarm', height=1, anchor=NE, font=('Ivy 10'), bg=co1, fg=co4)
l_name.place(x=105, y=10)

# creating combo boxes

l_hour = Label(frame_body, text='Hours', height=1, anchor=NW, font=('arial 7'), bg=co1, fg=co4)
l_hour.place(x=127, y=40)
c_hour = Combobox(frame_body, width=2, font=('Ivy 15'))
c_hour['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.place(x=130, y=58)

l_minute = Label(frame_body, text='Minutes', height=1, anchor=NW, font=('arial 7'), bg=co1, fg=co4)
l_minute.place(x=177, y=40)
c_minute = Combobox(frame_body, width=2, font=('Ivy 15'))
c_minute['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28",
                     "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_minute.current(0)
c_minute.place(x=180, y=58)

l_seconds = Label(frame_body, text='Seconds', height=1, anchor=NW, font=('arial 7'), bg=co1, fg=co4)
l_seconds.place(x=227, y=40)
c_seconds = Combobox(frame_body, width=2, font=('Ivy 15'))
c_seconds['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28",
                      "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_seconds.current(0)
c_seconds.place(x=230, y=58)

l_period = Label(frame_body, text='Period', height=1, anchor=NW, font=('arial 7'), bg=co1, fg=co4)
l_period.place(x=277, y=40)
c_period = Combobox(frame_body, width=3, font=('Ivy 15'))
c_period['value'] = ("AM", "PM")
c_period.current(0)
c_period.place(x=280, y=58)

def activate_alarm():
    if selected.get() == 1:
        print('Activate: ', selected.get())
    else:
        # create thread
        t1 = Thread(target=alarm)   
        # start the thread
        t1.start()

def deactivate_alarm():
    print('Alarm deactivated: ', selected.get())
    mixer.music.stop()

selected = IntVar()

radio = Radiobutton(frame_body, command=activate_alarm, text='Activate', value=1, variable=selected, font=('Arial 8'), bg=co1, fg=co4)
radio.place(x=125, y=95)

def play_alarm():
    mixer.music.load('music.wav')
    mixer.music.play()
    selected.set(0)
    
    radio = Radiobutton(frame_body, command=deactivate_alarm, text='Deactivate', value=1, variable=selected, font=('Arial 8'), bg=co1, fg=co4)
    radio.place(x=187, y=95)

def alarm():
    while True:
        control = selected.get()
        alarm_hour = c_hour.get()
        alarm_minute = c_minute.get()
        alarm_second = c_seconds.get()
        alarm_period = c_period.get().upper()
        
        # getting the current time
        current_time = datetime.now()

        hour = current_time.strftime("%I")
        minute = current_time.strftime("%M")
        second = current_time.strftime("%S")
        period = current_time.strftime("%p")
        
        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_second == second:
                            print("Time to take a break")
                            play_alarm()
                            activate_alarm()

        sleep(1)

t1 = Thread(target=alarm)   

# start the thread
t1.start()
mixer.init()

window.mainloop()
