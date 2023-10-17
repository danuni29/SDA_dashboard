from flask import Flask, request, render_template
import requests
import os

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

def menucrawling_func():
    URL = "https://sobi.chonbuk.ac.kr/function/ajax.get.rest.data.php"
    # URL = 'https://sobi.chonbuk.ac.kr/menu/week_menu.php'
    data = {"code": "mobile1"}

    res = requests.post(URL, data=data)
    res.encoding = "UTF-8"

    return res.text


@app.route("/menu/<day>")
# def menu_func(day):
#
#     if day == 'monday':
#         menu_data = menucrawling_func('monday')
#     elif day == 'tuesday':
#         menu_data = menucrawling_func('tuesday')
#     return render_template("menu.html", menu_data=menu_data, current_day = day)

def menu_func():
    menu_data = menucrawling_func()
    return render_template("menu.html", menu_data=menu_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

app.run(host="0.0.0.0", debug=True)
