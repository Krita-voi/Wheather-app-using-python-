import tkinter as tk
import requests
import time

key = "0aa1ca9dfd5b4cd7ba031329240808"

def getWeather(event=None):
    city = textfiled.get()
    try:
        response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={key}&q={city}')
        data = response.json()
        
        # Extracting data
        condition = data['current']['condition']['text']
        temperature = data['current']['temp_c']
        pressure = data['current']['pressure_mb']
        humidity = data['current']['humidity']
        wind = data['current']['wind_kph']
        sunrise = time.strftime("%I:%M:%S %p", time.gmtime(data['location']['localtime_epoch']))
        
        # Preparing output text
        final_info = f"{condition}\n{temperature}°C"
        final_data = f"\nWind Pressure: {pressure} mb\nHumidity: {humidity}%\nWind: {wind} kph\nSunrise: {sunrise}"
        
        # Displaying the result
        label1.config(text=final_info)
        label2.config(text=final_data)
    except Exception as e:
        label1.config(text="Error fetching weather data")
        label2.config(text=str(e))

# Setting up the GUI
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("Poppins", 15, "bold")
t = ("Poppins", 35, "bold")

textfiled = tk.Entry(canvas, font=t)
textfiled.pack(pady=20)
textfiled.focus()
textfiled.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()