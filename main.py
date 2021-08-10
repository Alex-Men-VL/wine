import argparse
import collections
import os
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def dir_path(path):
    if os.path.exists(path):
        return path
    else:
        raise FileNotFoundError(path)


env = Environment(
    loader=FileSystemLoader('.'),  
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

parser = argparse.ArgumentParser()
parser.add_argument("--path", type=dir_path,
                    help='paste path to file', default='wine3.xlsx')
args = parser.parse_args()

excel_data_df = pandas.read_excel(
    args.path, na_values=' ', keep_default_na=False)
drinks = excel_data_df.to_dict('records')

drinks_by_category = collections.defaultdict(list)

for drink in drinks:
	drinks_by_category[drink['Категория']].append(drink)

drinks_by_category = collections.OrderedDict(
    sorted(drinks_by_category.items()))


rendered_page = template.render(
    winery_age=datetime.now().year - 1920,
   	list_of_drinks=drinks_by_category,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
