import datetime
import pandas
import collections
import argparse


def calculate_years_together():
    year_of_foundation = 1920
    current_year = datetime.datetime.now().year
    return current_year - year_of_foundation


def parse_file(path):
    excel_data_df = pandas.read_excel(path, usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'])

    renamed_data = excel_data_df.rename(columns={'Категория': 'category', 'Название': 'title', 'Сорт': 'grape_variety',
                                                 'Цена': 'price', 'Картинка': 'image', 'Акция': 'sale'}).fillna('')

    all_wines = renamed_data.to_dict(orient='record')

    wines = collections.defaultdict(list)

    for wine in all_wines:
        wines[wine['category']].append(wine)

    return wines.items()


def parse_args():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('filepath', help='Path to *.xlsx file with your data.')
    args = parser.parse_args()
    return args
