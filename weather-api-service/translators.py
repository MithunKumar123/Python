from flask import Flask as fl, render_template
import pandas as p

app = fl(__name__)


@app.route("/")
def home():
    return render_template("translator-home.html")


@app.route("/api/v1/<word>")
def details(word):
    file_name = "Dictonary/dictionary.csv"
    content = p.read_csv(file_name)
    definition = content.loc[content["word"] == word]["definition"].squeeze()
    return {
        "word": word,
        "definition": definition
    }


if __name__ == "__main__":
    app.run(debug=True)