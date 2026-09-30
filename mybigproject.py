import requests
import tkinter as tk
from tkinter import messagebox


def search():
    city = city_entry.get()

    #сссылка апи 
    url = 'https://geocoding-api.open-meteo.com/v1/search'
    params = {
        'name': city,
        'count': 3,
        'language': 'ru',
    }
    #

    respone =  requests.get(url, params=params, timeout=5)
    data = respone.json()
    result = data['results'][0]

  
    # вывод ответа
    messagebox.showinfo(
    "Search result",
        f"Город: {result['name']}\n"
        f"Страна: {result['country']}\n"
)


window = tk.Tk()
window.title("Weather Tracking App")
window.geometry("400x400")


# Приветственный текст

label = tk.Label(
    window,
    text="Enter the city",
    font=("Arial", 20),
    fg="black",
)
label.pack()

# Кнопка
button = tk.Button(
    window,
    text="Search",
    command=search
)
button.pack()

# Поле ввода
city_entry = tk.Entry(window)
city_entry.pack()




window.mainloop()
