from flask import Flask as fl, render_template
import pandas as p

app = fl(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def details(station, date):
    temperature = 23
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


if __name__ == "__main__":
    app.run(debug=True)