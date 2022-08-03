from flask import Flask, render_template
from datetime import date

current_year = date.today().year

app = Flask(__name__)

print(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", year=current_year)


if __name__ == "__main__":
    app.run(debug=True)