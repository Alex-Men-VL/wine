import collections
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),  
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

excel_data_df = pandas.read_excel(
    'wine3.xlsx', na_values=' ', keep_default_na=False)
drinks = excel_data_df.to_dict('records')

list_of_drinks = collections.defaultdict(list)

for drink in drinks:
	list_of_drinks[drink['Категория']].append(drink)

sorted_list_of_drinks = collections.OrderedDict(sorted(list_of_drinks.items()))


rendered_page = template.render(
    winery_age = datetime.now().year - 1920,
   	list_of_drinks=sorted_list_of_drinks,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
