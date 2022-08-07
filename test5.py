from tkinter import *
import requests
import tkinter as tk


def get_weather(mainWindow):
    city = textField.get()
    API_KEY = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=06c921750b9a82d8f5d1294e1586276f"

    response = requests.get(API_KEY).json()
    city = response['name']
    country = response['sys']['country']
    temp_kelvin = response['main']['temp']
    temp_celsius = (temp_kelvin - 272.15)
    temp_fahrenheit = (temp_celsius * 9 / 5 + 32)
    icon = response['weather'][0]['icon']
    weather = response['weather'][0]['main']
    final1 = (city)
    final2 = (country)
    textField.config(text=final1)
    place_label.config(text=final2)


mainWindow = tk.Tk()
mainWindow.title('Weather Report')
mainWindow.geometry("400x400")

textField = StringVar()
textField = tk.Entry(mainWindow, textvariable=textField)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', get_weather)

place_label = Label(mainWindow, text='', font=('Verdana', 20))
img = PhotoImage(file="")
Image = Label(mainWindow, image=img)
Image.pack()
place_label.pack()

temp_label = Label(mainWindow, text='')
temp_label.pack()

weather_label = Label(mainWindow, text='')
weather_label.pack()

mainWindow.mainloop()
