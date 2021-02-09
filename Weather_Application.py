from tkinter import *
'''import tkinter as tk'''
import requests
from tkinter import messagebox as mb
import time

# Gui Window

window = Tk()
window.geometry('1050x450')
window.title("Weather Application")
window.configure(bg='yellow')

# Clock
# reference to https://bytes.com/topic/python/answers/629499-dynamically-displaying-time-using-tkinter-label

time1 = ''
clock = Label(window, font=('times', 20, 'bold'), bg='white')
clock.grid(row=3, column=3)


def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)

# logo

# Tried to package The Image with the code didn't work hence code is commented out


'''logo = tk.PhotoImage(file="motion.gif")

w = tk.Label(window, compound=tk.CENTER, image=logo).grid(row=0, column=0)'''

# Tried to get the gif to work but unfortunately i couldn't
# reference to Aashiq

'''frame_count = 50
frames =[PhotoImage(file='wow.gif', format= 'gif -index %i' %(i)) for i in range(frame_count)]

def backing(ind):
    frame = frames[ind]
    ind += 1
    gif_label = Label(frame)
    gif_label.grid(row=1, column=1)

    if ind == frame_count:
        ind = 0
    gif_label.configure(image=frames)
    window.after(100, backing, ind)

window.after(0, backing, 0)'''


# Clear button Function


def clr():
    ety.delete("0", END)


# Exit button function


def ext():
    window.destroy()

# Weather api + functions + Labels


def weather_app():
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        weather_key = '1f6496372caf01e9613a33fbf08f51f8'
        params1 = {'appid': weather_key, 'q': ety.get(), 'units': 'Metric'}
        response = requests.get(url, params=params1)
        weather = response.json()
        print(response)

        lbl_weather_name = Label(window, bg='white')
        lbl_weather_name.config(font=("Courier", 20))
        lbl_weather_name['text'] = weather['name']
        lbl_weather_name.grid(row=5, column=3)

        lbl_weather_tmp = Label(window, bg='white', text=weather['main']['temp'])
        lbl_weather_tmp.config(font=("Courier", 20))
        lbl_weather_tmp.grid(row=7, column=3)

        lbl_weather_min_tmp = Label(window, bg='white', text=weather['main']['temp_min'])
        lbl_weather_min_tmp.config(font=("Courier", 20))
        lbl_weather_min_tmp.grid(row=9, column=3)

        lbl_weather_max_tmp = Label(window, bg='white', text=weather['main']['temp_max'])
        lbl_weather_max_tmp.config(font=("Courier", 20))
        lbl_weather_max_tmp.grid(row=11, column=3)

        lbl_weather_wnd = Label(window, bg='white', text=weather['wind']['speed'])
        lbl_weather_wnd.config(font=("Courier", 20))
        lbl_weather_wnd.grid(row=13, column=3)

        lbl_weather_humidity = Label(window, bg='white', text=weather['main']['humidity'])
        lbl_weather_humidity.config(font=("Courier", 20))
        lbl_weather_humidity.grid(row=15, column=3)

        lbl_weather_wnd = Label(window, bg='white', text=weather['weather'][0]['description'])
        lbl_weather_wnd.config(font=("Courier", 20))
        lbl_weather_wnd.grid(row=17, column=3)

    except Exception:
        mb.showerror("Error", "Please Enter a valid Entry")


# Used empty labels to space out my labels
# Struggled using place to mae things much easier i used grid instead

lbl_space_1 = Label(window, bg='yellow').grid(row=1, column=4)
lbl_space_2 = Label(window, bg='yellow').grid(row=2, column=4)
lbl_space_3 = Label(window, bg='yellow').grid(row=6, column=4)
lbl_space_4 = Label(window, bg='yellow').grid(row=8, column=4)
lbl_space_5 = Label(window, bg='yellow').grid(row=10, column=4)
lbl_space_6 = Label(window, bg='yellow').grid(row=12, column=4)
lbl_space_7 = Label(window, bg='yellow').grid(row=14, column=4)
lbl_space_8 = Label(window, bg='yellow').grid(row=16, column=4)

# labels for the corresponding texts

lbl_time = Label(window, bg='white', text="ZA Local Time:")
lbl_time.config(font=("Courier", 20))
lbl_time.grid(row=3, column=1)

lbl_title = Label(window, bg='white', text="Weather Application")
lbl_title.configure(foreground='dark blue')
lbl_title.config(font=("Courier", 40, 'bold'))
lbl_title.grid(row=0, column=3)

lbl_name = Label(window, bg='white', text="Name Of City: ")
lbl_name.config(font=("Courier", 20))
lbl_name.grid(row=5, column=1)

lbl_tmp = Label(window, bg='white', text="Temperature: ")
lbl_tmp.config(font=("Courier", 20))
lbl_tmp.grid(row=7, column=1)

lbl_min_tmp = Label(window, bg='white', text="Minimum Temperature: ")
lbl_min_tmp.config(font=("Courier", 20))
lbl_min_tmp.grid(row=9, column=1)

lbl_max_tmp = Label(window, bg='white', text="Maximum Temperature: ")
lbl_max_tmp.config(font=("Courier", 20))
lbl_max_tmp.grid(row=11, column=1)

lbl_wnd_speed = Label(window, bg='white', text="Wind Speed: ")
lbl_wnd_speed.config(font=("Courier", 20))
lbl_wnd_speed.grid(row=13, column=1)

lbl_humidity = Label(window, bg='white', text="Humidity: ")
lbl_humidity.config(font=("Courier", 20))
lbl_humidity.grid(row=15, column=1)

lbl_cloud_coverage = Label(window, bg='white', text="Cloud Coverage: ")
lbl_cloud_coverage.config(font=("Courier", 20))
lbl_cloud_coverage.grid(row=17, column=1)

# Entry box

ety = Entry(window, textvariable=1)
ety.grid(row=3, column=5, padx=5, pady=10, ipady=3)

# Buttons

btn_generate = Button(window, text="Generate", activebackground='yellow', command=weather_app).grid(row=3, column=6)

btn_clr = Button(window, text="Clear", activebackground='yellow', command=clr).grid(row=3, column=7)

btn_ext = Button(window, text="Exit", activebackground='yellow', command=ext).grid(row=3, column=8)

tick()
window.mainloop()
