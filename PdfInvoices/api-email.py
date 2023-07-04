import requests as req
import send_email

api_key = "c4f1a1948cd44416987df1c1956f1ef2"

url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=c4f1a1948cd44416987df1c1956f1ef2"

data = req.get(url)

content = data.json()
body = ""

#print(content)

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] +2 * "\n"

body = body.encode("utf-8")
send_email.send_mail(message=body)