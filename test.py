import re
import requests
import sqlite3

url = 'https://www.baidu.com'
html = requests.get(url)
print(html.content)
