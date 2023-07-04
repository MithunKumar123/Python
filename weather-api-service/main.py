from flask import Flask as fl, render_template
import pandas as p

app = fl(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def details(station, date):
    file_name = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    content = p.read_csv(file_name, skiprows=20, parse_dates=["    DATE"])
    temperature = content.loc[content["    DATE"] == date]["   TG"].squeeze() /10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


if __name__ == "__main__":
    app.run(debug=True)