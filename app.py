from flask import Flask, render_template
Amare Walters Lyte

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("template.html")

if __name__ == "__main__":

    app.run(debug=True)
