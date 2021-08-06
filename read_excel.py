import pandas

from pprint import pprint

import collections


excel_data_df = pandas.read_excel(
    'wine2.xlsx', na_values=' ', keep_default_na=False)

drinks = excel_data_df.to_dict('records')

list_of_drinks = collections.defaultdict(list)

for drink  in drinks:
	list_of_drinks[drink['Категория']].append(drink)

for category in sorted(list_of_drinks):
	print('\t', category)
	for drink in list_of_drinks[category]:
		print(drink)
pprint(list_of_drinks)
