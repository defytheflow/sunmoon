import json

from flask import Flask, render_template, request, redirect, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    RESULT = "LOL"

    if request.method == "POST":  
        location = request.values["location"]
        datetime = request.values["datetime"]
        location = json.loads(location)
        datetime = json.loads(datetime)
        print(location)
        print(datetime)
        return jsonify(RESULT)

    else:
        return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    print("Has been redirected.")
    return jsonify("LOL")


if __name__ == "__main__":
    app.run(debug=True)