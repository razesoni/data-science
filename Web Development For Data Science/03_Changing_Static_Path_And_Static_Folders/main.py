from flask import Flask, render_template

app = Flask(__name__, static_folder='assets', static_url_path='/files')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def hello_about():
    return render_template("about.html")

app.run(debug=True)