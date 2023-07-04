from flask import Flask as fl, render_template
import pandas as p

app = fl(__name__)


@app.route("/")
def home():
    return render_template("translator-home.html")


@app.route("/api/v1/<words>")
def details(words):
    definition = words.upper()
    return {
        "word": words,
        "definition": definition
    }


if __name__ == "__main__":
    app.run(debug=True)