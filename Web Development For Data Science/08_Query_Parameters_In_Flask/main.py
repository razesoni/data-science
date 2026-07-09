from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get("name", default="unamed")
    lang = request.args.get("lang")
    print(name, lang)
    return render_template("index.html", name=name, lang=lang)  

app.run(debug=True)