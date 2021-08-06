from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from datetime import datetime

import pandas


env = Environment(
    loader=FileSystemLoader('.'),  
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

excel_data_df = pandas.read_excel('wine.xlsx')

wines = excel_data_df.to_dict('records')

rendered_page = template.render(
    winery_age = datetime.now().year - 1920,
	wines = wines,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
