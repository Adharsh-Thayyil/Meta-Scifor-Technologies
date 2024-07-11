import tkinter as tk

import requests

window = tk.Tk()
window.title("Quote Generator")

label = tk.Label(window, text = "", wraplength = 400)
label.pack()

def fetch_Quote():
  url = "https://official-joke-api.appspot.com/random_joke"
  response = requests.get(url)
  json = response.json()
  setup = json["setup"]
  punchline = json["punchline"]
  label.config(text = f"{setup} \n\n {punchline}")

button = tk.Button(window, text ="Click", bg = "yellow", command = fetch_Quote)

button.pack()

window.mainloop()