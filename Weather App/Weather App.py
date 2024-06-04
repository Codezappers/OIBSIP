import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

def get_weather(city):
    try:
        api_key = "e937f77c6818f211c691778d3d406fee"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "404":
            weather = data["main"]
            temp = weather["temp"]
            humidity = weather["humidity"]
            pressure = weather["pressure"]
            weather_desc = data["weather"][0]["description"]

            weather_data.set(f"Temperature: {temp}°C\nHumidity: {humidity}%\nPressure: {pressure} hPa\nDescription: {weather_desc.title()}")
        else:
            messagebox.showerror("Error", "Invalid city name")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

bg_image = "Weather App/tom-barrett-hgGplX3PFBg-unsplash(1).jpg"
bg_image = Image.open(bg_image)
bg_image = ImageTk.PhotoImage(bg_image)

bg_img_label = tk.Label(root, image=bg_image)
bg_img_label.place(x=0, y=0, relwidth=1, relheight=1)

weather_data = tk.StringVar()

city_label = tk.Label(root, text="Enter the city name:", font=("Helvetica", 16), bg="grey")
city_label.pack(pady=10, anchor="center" , expand=True)

city_entry = tk.Entry(root, font=("Helvetica", 18), bg="grey")
city_entry.pack(pady=10 , anchor="center" , expand=True)

weather_button = tk.Button(root, text="Check Weather", command=lambda: get_weather(city_entry.get()), font=("Helvetica", 14), bg="grey")
weather_button.pack(pady=10 , anchor="center", expand=True)

weather_label = tk.Label(root, textvariable=weather_data, font=("Helvetica", 14), bg="grey")
weather_label.pack(pady=10, anchor="center", expand=True)

root.mainloop()