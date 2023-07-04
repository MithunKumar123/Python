import streamlit as sl
import requests as req

api_key = "1NsFccmShiwdB34nqzfXwvbUvGA7Wydwf4RoM8de"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = req.get(url)
data = response.json()


title = data["title"]
image_url = data["url"]
description = data["explanation"]

image_filePath = "img1.png"
response_from_image_url = req.get(image_url)
with open("img1.png", "wb") as image:
    image.write(response_from_image_url.content)

sl.title(title)
sl.image("img1.png")
sl.write(description)

