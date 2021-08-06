import pandas


from pprint import pprint


excel_data_df = pandas.read_excel(
    'wine2.xlsx', na_values=' ', keep_default_na=False)

data = excel_data_df.to_dict('records')

categories = set(excel_data_df['Категория'].tolist())

list_of_drinks = {}
for category in categories:
	list_of_drinks[category] = [drink for drink in data if drink['Категория'] == category]



pprint(list_of_drinks)
