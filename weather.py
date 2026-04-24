import tkinter as tk
import requests


API_KEY = "63a460a3171b36fe7944756affd7f485"
root = tk.Tk()
root.title("Weather App")
root.geometry("400x500")
root.configure(bg="#0f172a")

def get_weather():
    city = entry.get()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        data = requests.get(url).json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        condition = data["weather"][0]["main"]

        temp_label.config(text=f"{temp}°C")
        desc_label.config(text=condition)
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind: {wind} m/s")

    except:
        temp_label.config(text="Error")
        desc_label.config(text="Invalid City")

# 🔷 Title
tk.Label(root, text="Weather App",
         font=("Segoe UI", 20, "bold"),
         bg="#0f172a", fg="white").pack(pady=10)

# 🔷 Search Box
entry = tk.Entry(root, font=("Segoe UI", 12),
                 bg="#1e293b", fg="white", bd=0)
entry.pack(padx=20, pady=10, fill="x", ipady=8)

# 🔷 Button
tk.Button(root, text="Get Weather",
          bg="#3b82f6", fg="white",
          font=("Segoe UI", 12),
          bd=0, command=get_weather).pack(pady=10)

# 🔷 Weather Card
card = tk.Frame(root, bg="#1e293b", bd=0)
card.pack(padx=20, pady=20, fill="both", expand=True)

# Temperature
temp_label = tk.Label(card, text="--°C",
                      font=("Segoe UI", 40, "bold"),
                      bg="#1e293b", fg="#22c55e")
temp_label.pack(pady=10)

# Condition
desc_label = tk.Label(card, text="Condition",
                      font=("Segoe UI", 16),
                      bg="#1e293b", fg="white")
desc_label.pack(pady=5)

# Humidity
humidity_label = tk.Label(card, text="Humidity: --",
                          font=("Segoe UI", 12),
                          bg="#1e293b", fg="#38bdf8")
humidity_label.pack(pady=5)

# Wind Speed
wind_label = tk.Label(card, text="Wind: --",
                      font=("Segoe UI", 12),
                      bg="#1e293b", fg="#facc15")
wind_label.pack(pady=5)

root.mainloop()