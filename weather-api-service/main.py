from flask import Flask as fl, render_template
import pandas as p

app = fl(__name__)

stations = p.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


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

@app.route("/api/v1/<station>")
def station_details(station):
    file_name = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    content = p.read_csv(file_name, skiprows=20, parse_dates=["    DATE"])
    result = content.to_dict(orient="records")
    return result

if __name__ == "__main__":
    app.run(debug=True)