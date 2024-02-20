import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=cadf0a7dad87df5446c4061b589ffe7a"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(((json_data['main']['temp'] - 272.15)*1.8)+32)
    min_temp = int(((json_data['main']['temp_min'] - 272.15)*1.8)+32)
    max_tmep = int(((json_data['main']['temp_max'] - 272.15)*1.8)+32)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 18000))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 18000))

    final_info = condition + "\n" + str(temp) + " degrees fahrenheit"
    final_data = "\n" + "Max Temp: " + str(max_tmep) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.configure(bg='cyan')

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()


canvas.mainloop()