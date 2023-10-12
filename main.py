from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def first_page():
    return render_template("index.html")



@app.route("/about")
def about_func():
    return render_template("about.html")


@app.route("/timetable")
def timetable_func():
    return render_template("timetable.html")



@app.route("/menu")
def menu_func():
    return render_template("menu.html")


app.run(host="0.0.0.0", debug=True)