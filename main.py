from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from datetime import datetime

import pandas

from pprint import pprint

import collections


env = Environment(
    loader=FileSystemLoader('.'),  
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

excel_data_df = pandas.read_excel(
    'wine3.xlsx', na_values=' ', keep_default_na=False)
drinks = excel_data_df.to_dict('records')

# list_of_drinks = collections.defaultdict(list)
# for drink in drinks:
# 	list_of_drinks[drink['Категория']].append(drink)

categories = list(set(excel_data_df['Категория'].tolist()))
categories.sort()

list_of_drinks = {}
for category in categories:
	list_of_drinks[category] = [drink for drink in drinks if drink['Категория'] == category]

rendered_page = template.render(
    winery_age = datetime.now().year - 1920,
   	list_of_drinks=list_of_drinks,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
