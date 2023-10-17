import requests
import openpyxl
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['제목','채널명','조회수','좋아요'])

raw = requests.get('https://tv.naver.com/r')
html = BeautifulSoup(raw.text, 'html.parser')
container = html.select('div_inner')
for con in container:
    t = con.select_one('dt.title').text.strip()
    sheet.append([t])

wb.save('naver_tv.xlsx')