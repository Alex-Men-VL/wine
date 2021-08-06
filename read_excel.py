import pandas

from pprint import pprint

import collections


excel_data_df = pandas.read_excel(
    'wine2.xlsx', na_values=' ', keep_default_na=False)

drinks = excel_data_df.to_dict('records')

categories = set(excel_data_df['Категория'].tolist())

# list_of_drinks = {}
# for category in categories:
# 	list_of_drinks[category] = [drink for drink in drinks if drink['Категория'] == category]

list_of_drinks = collections.defaultdict(list)

for drink  in drinks:
	list_of_drinks[drink['Категория']].append(drink)

pprint(list_of_drinks)
