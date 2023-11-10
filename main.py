from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

app.static_folder = 'static'

@app.route("/")
def first_page():
    return render_template("index.html")



@app.route("/about")
def about_func():
    return render_template("about.html")


@app.route("/timetable")
def timetable_func():
    return render_template("timetable.html")

def menucrawling_func(mobile):
    URL = "https://sobi.chonbuk.ac.kr/function/ajax.get.rest.data.php"
    data = {"code": f"{mobile}"}

    res = requests.post(URL, data=data)
    res.encoding = "UTF-8"

    return res.text

@app.route("/menu/<string:mobile>")
def menu_func(mobile):
    menu_data = menucrawling_func(mobile)
    return render_template("menu.html", menu_data = menu_data, mobile=mobile )



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

app.run(host="0.0.0.0", debug=True)
