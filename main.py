from flask import Flask, request, render_template
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

app = Flask(__name__)

app.static_folder = 'static'

@app.route("/")
def first_page():
    return render_template("index.html")



@app.route("/about")
def about_func():
    return render_template("about.html")

@app.route("/project")
def project_func():
    return render_template("project.html")


@app.route("/timetable")
def timetable_func():
    # excel_data = read_googlesheet_func()
    # return render_template("timetable.html", excel_data=excel_data)
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

def read_googlesheet_func():
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/spreadsheets'
    ]
    json_file_path = os.path.join('static', 'smartdigitalagriculture-0ee0176ef713.json')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_path, scope)
    # json_file_name = 'C:\code\SDA_dashboard\static\smartdigitalagriculture-0ee0176ef713.json'
    # credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)

    gc = gspread.authorize(credentials)


    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1-BG2vFjbDNZOYK1gyquhL9QIsvPEEmBp9ImOEnDapZQ/edit#gid=1946315011'
    doc = gc.open_by_url(spreadsheet_url)

    worksheet = doc.worksheet('시간표_2023F')

    range_list = worksheet.range('A1:N31')

    values = []
    for cell in range_list:
        values.append(cell.value)

    cell_data = worksheet.acell('B1').value
    print(cell_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

app.run(host="0.0.0.0", debug=True)
