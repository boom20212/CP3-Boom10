from tkinter import*
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
        temp_fahrenheit = (temp_celsius * 9/5 + 32)
        icon = response['weather'][0]['icon']
        weather = response['weather'][0]['main']
        data = (city, country, temp_celsius, temp_fahrenheit, icon, weather)
        return data


def search():
    city = textField.get()
    weather = get_weather(city)
    place_label['text'] = '{}, {}'.format(weather[0], weather[1])
    temp_label['text'] = '{:.0F}°C, {:.0F}°F'.format(weather[2], weather[3])
    img["file"] = 'weather_icon\{}.png'.format(weather[4])


mainWindow = Tk()
mainWindow.title('Weather Report')
mainWindow.geometry("400x400")


textField = StringVar()
textField = tk.Entry(mainWindow, textvariable=textField)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', get_weather)


search_button = Button(mainWindow, text='Done', command=search)
search_button.pack()

label = Label(mainWindow, text='Enter City Name \n Ex: Bangkok', font=('verdana', 10,))
label.pack()

temp_label = Label(mainWindow, text='', font=('verdana', 10))
temp_label.pack()


place_label = Label(mainWindow, text='', font=('Verdana', 20))
img = PhotoImage(file="")
Image = Label(mainWindow, image=img)
Image.pack()
place_label.pack()

mainWindow.mainloop()