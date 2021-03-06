import argparse
import collections
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path",
                        help='paste path to file', default='wine_example.xlsx')
    return parser.parse_args()


def read_excel(path_to_excel):
    excel_data_df = pandas.read_excel(
        path_to_excel, na_values=' ', keep_default_na=False)
    return excel_data_df.to_dict('records')


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    path_to_excel = parse_arguments().path
    drinks = read_excel(path_to_excel)

    drinks_by_category = collections.defaultdict(list)

    for drink in drinks:
        drinks_by_category[drink['Категория']].append(drink)

    drinks_by_category = collections.OrderedDict(
        sorted(drinks_by_category.items()))

    rendered_page = template.render(
        winery_age=datetime.now().year - 1920,
        drinks_by_category=drinks_by_category,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
